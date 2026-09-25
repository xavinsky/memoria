#!/usr/bin/env python3
"""Compile le contenu Markdown de content/ en www/data/content.js.

Le site reste un fichier statique qui s'ouvre en file:// : les données sont chargées par
<script src>, sous la forme `const SITE = {...}`, et non par fetch. Chaque section y porte son HTML
déjà rendu, avec les classes CSS de www/index.html.

Format des fichiers (arborescence, front matter, Markdown étendu, Syntaxes, Refs, Lexique) :
content/README.md.

Usage : python3 build/build.py
"""

import datetime
import html
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUTPUT = ROOT / "www" / "data" / "content.js"

DEFAULT_COLUMNS = {"Objectif": "col-objectif", "Syntaxe": "col-syntaxe", "Résultat": "col-resultat"}
# Colonnes affichées en police code : les crochets y sont du code, pas des liens
SYNTAX_CODE_COLUMNS = {"col-syntaxe", "col-formule"}
CALLOUTS = {"TIP": "tip", "NOTE": "tip", "WARNING": "warning", "CAUTION": "warning"}
CONTAINER_OPEN = re.compile(r"^(:{3,})\s*([\w-]+)\s*(.*?)\s*$")
CONTAINER_CLOSE = re.compile(r"^:{3,}\s*$")
FENCE = re.compile(r"^(`{3,}|~{3,})")
ATTRS = re.compile(r"\s*\{((?:\s*(?:#[\w-]+|\.[\w-]+|[\w-]+=[\w-]+))+)\s*\}$")
MODEL_TAG = re.compile(r"\[\[(N?P):(.+?)\]\]")
MD_LINK = re.compile(r"\[([^\]]+)\]\((#[\w-]+|https?://[^)\s]+)\)")


class BuildError(Exception):
    """Erreur de contenu : le build s'arrête et affiche le message."""


def esc(text):
    """Échappe un texte pour du HTML (attributs compris)."""
    return html.escape(text, quote=True)


def bold_code(text):
    """Texte brut → HTML où seul **gras** est interprété (code, cellules de Syntaxes)."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(text))


def slugify(text):
    """Minuscules sans accents, tout le reste en tirets : même calcul que slugify() de la page."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def split_front_matter(text, path):
    """Sépare le front matter YAML (entre deux lignes `---`) du corps."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        raise BuildError(f"{path}: front matter non fermé")
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


def parse_attrs(info):
    """`Titre {#id .classe clé=valeur}` → ("Titre", {"id":..., "class":[...], clé: valeur})."""
    attrs = {"class": []}
    m = ATTRS.search(info)
    if not m:
        return info, attrs
    for part in m.group(1).split():
        if part.startswith("#"):
            attrs["id"] = part[1:]
        elif part.startswith("."):
            attrs["class"].append(part[1:])
        else:
            key, value = part.split("=", 1)
            attrs[key] = value
    return info[:m.start()], attrs


def split_containers(text, path):
    """Découpe un corps Markdown en morceaux de Markdown simple et conteneurs :::nom ... :::."""
    root = {"children": []}
    stack = [root]
    chunk, fence = [], None

    def flush():
        if chunk:
            stack[-1]["children"].append({"md": "\n".join(chunk)})
            chunk.clear()

    for line in text.split("\n"):
        if fence:
            chunk.append(line)
            if line.strip().startswith(fence) and not line.strip()[len(fence):].strip():
                fence = None
            continue
        m = FENCE.match(line.strip())
        if m:
            fence = m.group(1)
            chunk.append(line)
            continue
        if CONTAINER_CLOSE.match(line):
            if len(stack) == 1:
                raise BuildError(f"{path}: `{line}` ferme un conteneur qui n'est pas ouvert")
            flush()
            stack.pop()
            continue
        m = CONTAINER_OPEN.match(line)
        if m:
            flush()
            args, attrs = parse_attrs(m.group(3))
            node = {"name": m.group(2), "args": args, "attrs": attrs, "children": []}
            stack[-1]["children"].append(node)
            stack.append(node)
            continue
        chunk.append(line)
    flush()
    if len(stack) > 1:
        raise BuildError(f"{path}: conteneur :::{stack[-1]['name']} non fermé")
    return root["children"]


def node_text(node):
    """Texte Markdown d'un conteneur, sans ses conteneurs enfants."""
    return "\n".join(c["md"] for c in node["children"] if "md" in c).strip()


def list_entries(node):
    """Puces `- ...` d'un conteneur (:::compare, :::cards), et le texte qui précède la première."""
    parts = re.split(r"^- ", node_text(node), flags=re.MULTILINE)
    return parts[0], [p.strip() for p in parts[1:]]


def id_attr(attrs):
    """Attribut HTML ` id="..."` d'après les attributs d'un conteneur, ou chaîne vide."""
    return f' id="{esc(attrs["id"])}"' if attrs.get("id") else ""


# ---------- Règles Markdown propres au site ----------

def math_inline(state, silent):
    """$...$ et $$...$$ : laissés tels quels (échappés) pour KaTeX, sans interprétation Markdown."""
    src, pos = state.src, state.pos
    if src[pos] != "$":
        return False
    delim = "$$" if src.startswith("$$", pos) else "$"
    end = src.find(delim, pos + len(delim))
    if end < 0 or end == pos + len(delim):
        return False
    if not silent:
        tok = state.push("math_inline", "", 0)
        tok.content = src[pos:end + len(delim)]
    state.pos = end + len(delim)
    return True


def model_tag(state, silent):
    """[[P:Classe|Nom convivial|id]] / [[NP:...]] : badge de modèle."""
    m = MODEL_TAG.match(state.src, state.pos)
    if not m:
        return False
    if not silent:
        kind = m.group(1)
        name, friendly, target = (m.group(2).replace("\\|", "|").split("|") + [None, None])[:3]
        cls = "model-tag model-tag-" + kind.lower()
        tooltip = f' data-tooltip="{esc(friendly)}"' if friendly else ""
        inner = f'{esc(name)}<span class="tag-suffix"> &#91;{kind}&#93;</span>'
        tok = state.push("html_inline", "", 0)
        if target:
            state.env.setdefault("links", []).append(target)
            tok.content = f'<a href="#{esc(target)}" class="{cls} model-tag-link"{tooltip}>{inner}</a>'
        else:
            tok.content = f'<span class="{cls}"{tooltip}>{inner}</span>'
    state.pos = m.end()
    return True


# Règles de rendu inline : signature imposée par markdown-it (renderer, tokens, idx, options, env)

def render_math(_self, tokens, idx, _options, _env):
    """Formule en ligne : texte source échappé, rendu ensuite par KaTeX."""
    return esc(tokens[idx].content)


def render_code_inline(_self, tokens, idx, _options, _env):
    """Code en ligne, où **gras** reste interprété."""
    return "<code>" + bold_code(tokens[idx].content) + "</code>"


def render_text(_self, tokens, idx, _options, _env):
    """Texte, avec les suffixes [P]/[NP] mis en forme."""
    return (esc(tokens[idx].content)
            .replace("[NP]", '<span class="tag-np">[NP]</span>')
            .replace("[P]", '<span class="tag-p">[P]</span>'))


def render_link_open(_self, tokens, idx, _options, env):
    """Ouverture de lien : relève les liens internes, ouvre les externes dans un nouvel onglet."""
    href = tokens[idx].attrGet("href") or ""
    external = bool(re.match(r"https?://", href))
    env.setdefault("open_links", []).append(external)
    if href.startswith("#"):
        env.setdefault("links", []).append(href[1:])
    extra = ' target="_blank" rel="noopener"' if external else ""
    return f'<a href="{esc(href)}"{extra}>'


def render_link_close(_self, _tokens, _idx, _options, env):
    """Fermeture de lien : ↗ après un lien externe, sauf dans les Refs."""
    external = env["open_links"].pop()
    return " ↗</a>" if external and not env.get("refs") else "</a>"


def make_parser():
    """Parseur CommonMark + tableaux + barré, avec les règles propres au site."""
    md = MarkdownIt("commonmark", {"html": True})
    md.enable(["table", "strikethrough"])
    md.inline.ruler.before("backticks", "math_inline", math_inline)
    md.inline.ruler.before("link", "model_tag", model_tag)
    md.add_render_rule("math_inline", render_math)
    md.add_render_rule("code_inline", render_code_inline)
    md.add_render_rule("text", render_text)
    md.add_render_rule("link_open", render_link_open)
    md.add_render_rule("link_close", render_link_close)
    return md


def close_index(tokens, i):
    """Index du token qui ferme le bloc ouvert en tokens[i]."""
    level, depth = tokens[i].level, 0
    for j in range(i, len(tokens)):
        if tokens[j].level == level:
            depth += tokens[j].nesting
            if depth == 0:
                return j
    raise BuildError("bloc non fermé")


class Renderer:
    """Rend le contenu en HTML et relève les liens internes et les ancres pour le contrôle final."""

    def __init__(self):
        self.md = make_parser()
        self.links = []    # (fichier source, id cible)
        self.anchors = []  # (fichier source, id posé dans le contenu)
        self.divider = False  # un `---` attend le bloc suivant
        self.containers = {"compare": self._compare, "category": self._category,
                           "derivation": self._derivation, "cards": self._cards}
        self.token_handlers = {
            "paragraph_open": self._tok_paragraph, "fence": self._tok_fence, "hr": self._tok_hr,
            "ordered_list_open": self._tok_ordered_list, "bullet_list_open": self._tok_bullet_list,
            "blockquote_open": self._tok_blockquote, "table_open": self._tok_table,
            "heading_open": self._tok_heading, "html_block": self._tok_html,
        }

    def inline(self, src, path, env=None):
        """Markdown inline (texte source) → HTML."""
        env = env if env is not None else {}
        out = self.md.renderInline(src, env)
        self.links += [(path, t) for t in env.get("links", [])]
        return out

    def inline_tokens(self, tok, path, env=None):
        """Token inline déjà parsé → HTML."""
        env = env if env is not None else {}
        out = self.md.renderer.renderInline(tok.children, self.md.options, env)
        self.links += [(path, t) for t in env.pop("links", [])]
        return out

    def _anchor(self, attrs, path):
        """Relève l'ancre {#id} d'un conteneur, pour le contrôle des doublons et des liens."""
        if attrs.get("id"):
            self.anchors.append((path, attrs["id"]))

    # ----- Cartes concept et Refs -----

    def card(self, body, path):
        """Corps d'une carte concept."""
        self.divider = False
        return self._nodes(split_containers(body, path), path)

    def refs(self, body, path):
        """Corps d'une section Refs : titres, lignes de liens, conteneurs :::cards."""
        self.divider = False
        return self._nodes(split_containers(body, path), path, refs=True)

    def _cls(self, base):
        """Classes d'un bloc, plus `with-divider` si un `---` le précède."""
        if self.divider:
            self.divider = False
            return base + " with-divider"
        return base

    def _block(self, tag, classes, inner, attrs=""):
        """Bloc de premier niveau d'une carte, avec le filet de séparation en attente éventuel."""
        return f'<{tag} class="{self._cls("concept-block " + classes)}"{attrs}>{inner}</{tag}>'

    def _nodes(self, nodes, path, refs=False):
        """Suite de morceaux Markdown et de conteneurs → HTML."""
        return "".join(self._md_blocks(n["md"], path, refs) if "md" in n else self._container(n, path)
                       for n in nodes)

    def _container(self, node, path):
        """Conteneur :::nom → HTML."""
        handler = self.containers.get(node["name"])
        if handler is None:
            raise BuildError(f"{path}: conteneur inconnu :::{node['name']}")
        self._anchor(node["attrs"], path)
        return handler(node, path)

    def _compare(self, node, path):
        """:::compare → cartes côte à côte, une par puce `- {rôle} **Libellé** : texte`."""
        before, items = list_entries(node)
        if before.strip():
            raise BuildError(f"{path}: :::compare doit contenir une liste `- **Libellé** : texte`")
        cards = []
        for item in items:
            m = re.match(r"(?:\{([\w-]+)\}\s+)?\*\*(.+?)\*\*\s*:\s*(.*)$", item, re.DOTALL)
            if not m:
                raise BuildError(f"{path}: élément de :::compare mal formé : {item[:60]}")
            role = f" role-{m.group(1)}" if m.group(1) else ""
            label, text = self.inline(m.group(2), path), self.inline(m.group(3), path)
            cards.append(f'<div class="compare-card{role}"><div class="compare-label">{label}</div>'
                         f'<div class="compare-text">{text}</div></div>')
        return self._block("div", "block-compare", "".join(cards))

    def _category(self, node, path):
        """:::category Libellé → badge + description."""
        desc = self.inline(node_text(node), path)
        inner = (f'<span class="category-badge">{esc(node["args"])}</span>'
                 f'<p class="category-desc">{desc}</p>')
        return self._block("div", "category-block", inner, id_attr(node["attrs"]))

    def _derivation(self, node, path):
        """::::derivation → étapes numérotées, chacune un conteneur :::step."""
        steps = [c for c in node["children"] if "name" in c]
        if any("md" in c and c["md"].strip() for c in node["children"]):
            raise BuildError(f"{path}: ::::derivation ne doit contenir que des :::step")
        start = int(node["attrs"].get("start", 0))
        out = []
        for i, step in enumerate(steps):
            if step["name"] != "step":
                raise BuildError(f"{path}: :::{step['name']} dans une dérivation (attendu :::step)")
            self._anchor(step["attrs"], path)
            num = step["attrs"].get("num", str(i + start))
            self.divider = False
            out.append(f'<div class="derivation-step"{id_attr(step["attrs"])}><div class="derivation-step-head">'
                       f'<span class="derivation-num">{esc(num)}</span>'
                       f'<span class="derivation-title">{self.inline(step["args"], path)}</span></div>'
                       f'<div class="derivation-step-body">{self._nodes(step["children"], path)}</div></div>')
        return self._block("div", "concept-derivation", "".join(out))

    def _cards(self, node, path):
        """:::cards (Refs) → grille de cartes, une par puce `- [Nom](url) : description`."""
        out = []
        for item in list_entries(node)[1]:
            m = re.match(r"\[(.+?)\]\((\S+?)\)\s*:\s*(.*)$", item, re.DOTALL)
            if not m:
                raise BuildError(f"{path}: élément de :::cards mal formé : {item[:60]}")
            out.append(f'<a class="datasrc-card" href="{esc(m.group(2))}" target="_blank" rel="noopener">'
                       f'<div class="datasrc-card-name">{esc(m.group(1))}</div>'
                       f'<p class="datasrc-card-desc">{esc(m.group(3))}</p></a>')
        return '<div class="datasrc-grid">' + "".join(out) + "</div>"

    # ----- Blocs Markdown : un traitement par type de token de premier niveau -----

    def _md_blocks(self, text, path, refs=False):
        """Morceau de Markdown simple → blocs du site."""
        tokens = self.md.parse(text)
        out, i = [], 0
        while i < len(tokens):
            handler = self.token_handlers.get(tokens[i].type)
            if handler is None:
                raise BuildError(f"{path}: élément Markdown non pris en charge ({tokens[i].type})")
            html_out, i = handler(tokens, i, path, refs)
            out.append(html_out)
        return "".join(out)

    def _tok_paragraph(self, tokens, i, path, _refs):
        """Paragraphe → bloc de texte, ou schéma s'il ne contient qu'une image."""
        inline = tokens[i + 1]
        kids = inline.children or []
        if len(kids) == 1 and kids[0].type == "image":
            return self._block("div", "block-diagram", self._diagram(kids[0], path)), i + 3
        return self._block("p", "block-text", self.inline_tokens(inline, path)), i + 3

    def _tok_fence(self, tokens, i, _path, _refs):
        """Bloc ``` → formule (math, latex) ou bloc de code."""
        info = tokens[i].info.strip().split(" ")[0]
        content = tokens[i].content.rstrip("\n")
        if info in ("math", "latex"):
            return self._block("div", "block-formula", esc("$$" + content + "$$")), i + 1
        return self._block("div", "block-code", f"<code>{bold_code(content)}</code>"), i + 1

    def _tok_hr(self, _tokens, i, _path, _refs):
        """`---` → filet de séparation sur le bloc suivant."""
        self.divider = True
        return "", i + 1

    def _tok_ordered_list(self, tokens, i, path, _refs):
        """Liste `1.` → étapes numérotées."""
        end = close_index(tokens, i)
        items = "".join(f'<li><div class="step-text">{it}</div></li>'
                        for it in self._list_items(tokens[i:end + 1], path))
        return self._block("ol", "concept-steps", items), end + 1

    def _tok_bullet_list(self, tokens, i, path, refs):
        """Liste à puces → liste, ou ligne de liens entre crochets dans les Refs."""
        end = close_index(tokens, i)
        items = self._list_items(tokens[i:end + 1], path, refs)
        if refs:
            return "<p>" + " ".join(f"[{it}]" for it in items) + "</p>", end + 1
        return self._block("ul", "", "".join(f"<li>{it}</li>" for it in items)), end + 1

    def _tok_blockquote(self, tokens, i, path, _refs):
        """Citation `> [!TIP]` / `> [!WARNING]` → encart."""
        end = close_index(tokens, i)
        inlines = [x for x in tokens[i:end] if x.type == "inline"]
        kids = inlines[0].children if inlines and inlines[0].children else []
        m = re.match(r"\[!(\w+)\]\s*", kids[0].content) if kids and kids[0].type == "text" else None
        if not m or m.group(1).upper() not in CALLOUTS:
            raise BuildError(f"{path}: citation sans [!TIP] ou [!WARNING]")
        kids[0].content = kids[0].content[m.end():]
        if not kids[0].content and len(kids) > 1 and kids[1].type == "softbreak":
            del kids[:2]
        body = "<br>".join(self.inline_tokens(x, path) for x in inlines)
        return self._block("div", "block-note " + CALLOUTS[m.group(1).upper()], body), end + 1

    def _tok_table(self, tokens, i, path, _refs):
        """Tableau → mini-tableau."""
        end = close_index(tokens, i)
        rows, row = [], []
        for tok in tokens[i:end + 1]:
            if tok.type == "tr_open":
                row = []
            elif tok.type == "tr_close":
                rows.append(row)
            elif tok.type == "inline":
                row.append(self.inline_tokens(tok, path))
        thead = "<tr>" + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr>"
        tbody = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:])
        table = f'<table class="concept-mini-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table>'
        return self._block("div", "block-table-wrap", table), end + 1

    def _tok_heading(self, tokens, i, path, refs):
        """Titre → sous-titre à puce dans les Refs, titre simple ailleurs."""
        text = self.inline_tokens(tokens[i + 1], path, {"refs": refs})
        if refs:
            dot = '<span class="dot" style="background:var(--accent)"></span>'
            return f'<h3 class="ref-subheading">{dot}{text}</h3>', i + 3
        tag = tokens[i].tag
        return f"<{tag}>{text}</{tag}>", i + 3

    def _tok_html(self, tokens, i, _path, _refs):
        """Bloc HTML brut, recopié tel quel."""
        return tokens[i].content, i + 1

    def _list_items(self, tokens, path, refs=False):
        """Contenu HTML de chaque élément d'une liste."""
        items, current = [], None
        for tok in tokens:
            if tok.type == "list_item_open":
                current = []
            elif tok.type == "list_item_close":
                items.append("<br>".join(current))
            elif tok.type == "inline" and current is not None:
                current.append(self.inline_tokens(tok, path, {"refs": refs}))
        return items

    def _diagram(self, img, path):
        """Contenu d'un schéma, inséré tel quel ; ses liens internes sont contrôlés."""
        target = (path.parent / img.attrGet("src")).resolve()
        if not target.is_file():
            raise BuildError(f"{path}: schéma introuvable {img.attrGet('src')}")
        content = target.read_text(encoding="utf-8").strip()
        self.links += [(path, h) for h in re.findall(r'href="#([^"]+)"', content)]
        return content

    # ----- Syntaxes -----

    def syntax(self, meta, body, path):
        """Section Syntaxes → tableau, une ligne par titre `## ...`."""
        columns = meta.get("columns") or DEFAULT_COLUMNS
        keys = sorted([*list(columns)[1:], "Incorrect"], key=len, reverse=True)
        key_re = re.compile(r"^(" + "|".join(re.escape(k) for k in keys) + r"):(.*)$")
        rows = re.split(r"^## +(.+)$", body, flags=re.MULTILINE)
        if rows[0].strip():
            raise BuildError(f"{path}: texte avant la première ligne `## ...`")
        body_html = "".join(self._syntax_row(first, syntax_fields(row, key_re, path, first), columns, path)
                            for first, row in zip(rows[1::2], rows[2::2]))
        thead = "<tr>" + "".join(f"<th>{esc(h)}</th>" for h in columns) + "</tr>"
        return f'<table class="syntax-table"><thead>{thead}</thead><tbody>{body_html}</tbody></table>'

    def _syntax_row(self, first, cells, columns, path):
        """Une ligne du tableau Syntaxes ; `Incorrect` s'affiche barré au-dessus de la 2e colonne."""
        headers = list(columns)
        missing = [h for h in headers[1:] if h not in cells]
        if missing:
            raise BuildError(f"{path}: ligne « {first} » sans {missing}")
        values = [first.strip()] + [cells[h] for h in headers[1:]]
        tds = []
        for idx, (label, cls) in enumerate(columns.items()):
            inner = ""
            if idx == 1 and "Incorrect" in cells:
                inner += f'<code class="broken-code">{bold_code(cells["Incorrect"])}</code>'
            inner += self._syntax_cell(values[idx], cls, path)
            tds.append(f'<td class="{cls}" data-label="{esc(label)}">{inner}</td>')
        return "<tr>" + "".join(tds) + "</tr>"

    def _syntax_cell(self, value, cls, path):
        """Contenu d'une cellule Syntaxes selon sa classe de colonne."""
        if isinstance(value, list):
            return "".join(syntax_segment(kind, text) for kind, text in value)
        if cls == "col-syntaxe":
            return f"<code>{bold_code(value)}</code>"
        if cls == "col-params":
            return "".join(f'<div class="param-line">{esc(line)}</div>' for line in value.split("\n"))
        if cls in SYNTAX_CODE_COLUMNS:
            return bold_code(value)
        return self._syntax_links(bold_code(value), path)

    def _syntax_links(self, text, path):
        """Liens [texte](#id) et [texte](https://...) des colonnes de texte de Syntaxes."""
        def link(m):
            label, href = m.group(1), html.unescape(m.group(2))
            if href.startswith("#"):
                self.links.append((path, href[1:]))
                return f'<a href="{esc(href)}">{label}</a>'
            return f'<a href="{esc(href)}" target="_blank" rel="noopener">{label} ↗</a>'
        return MD_LINK.sub(link, text)


def syntax_segment(kind, text):
    """Segment d'une cellule composée : ```table, label: ou bloc de code."""
    if kind == "table":
        return f'<div class="mini-table">{esc(text)}</div>'
    if kind == "label":
        return f'<div class="mini-label">{esc(text)}</div>'
    return f"<code>{bold_code(text)}</code>"


def read_fence(lines, i, where):
    """Bloc ``` qui commence en lines[i] → (info, contenu, index de la ligne suivante)."""
    marker = FENCE.match(lines[i]).group(1)
    j = i + 1
    while j < len(lines) and lines[j].strip() != marker:
        j += 1
    if j == len(lines):
        raise BuildError(f"{where} : bloc ``` non fermé")
    return lines[i][len(marker):].strip() or "text", "\n".join(lines[i + 1:j]), j + 1


def syntax_fields(text, key_re, path, first):
    """Lignes `Colonne: valeur` d'une ligne Syntaxes → {colonne: texte, ou liste de segments}."""
    where = f"{path}: « {first} »"
    cells, key = {}, None
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m = key_re.match(line)
        if m:
            key = m.group(1)
            if key in cells:
                raise BuildError(f"{where} : colonne {key} en double")
            cells[key] = m.group(2).strip() or []
            i += 1
        elif not line.strip():
            i += 1
        elif key is None or not isinstance(cells[key], list):
            raise BuildError(f"{where} : ligne hors colonne : {line[:60]}")
        elif FENCE.match(line):
            info, content, i = read_fence(lines, i, where)
            cells[key].append((info, content))
        elif line.startswith("label:"):
            cells[key].append(("label", line[6:].strip()))
            i += 1
        else:
            raise BuildError(f"{where} : ligne inattendue : {line[:60]}")
    return {k: collapse_segments(v) for k, v in cells.items()}


def collapse_segments(value):
    """Un seul bloc ``` sans info → texte simple ; aucun segment → texte vide."""
    if not isinstance(value, list):
        return value
    if len(value) == 1 and value[0][0] == "text":
        return value[0][1]
    return value or ""


# ---------- Assemblage ----------

class SubgroupOrder:  # pylint: disable=too-few-public-methods  # petit objet à état, une seule opération
    """Vérifie que les sections d'un même sous-groupe (et sous-sous-groupe) se suivent : le menu
    latéral ouvre une nouvelle boîte à chaque changement de valeur."""

    def __init__(self, group):
        self.group = group
        self.seen = set()
        self.last = (None, None)

    def check(self, meta, rel):
        """Enregistre la section suivante du groupe ; erreur si elle rouvre un sous-groupe fermé."""
        nav = (meta.get("subgroup"), meta.get("subsubgroup"))
        for level in (nav[:1], nav):
            if level[-1] and level != self.last[:len(level)] and level in self.seen:
                raise BuildError(f"{rel}: sous-groupe « {level[-1]} » non contigu dans {self.group}/")
            self.seen.add(level)
        self.last = nav


def render_section(meta, body, rel, renderer):
    """HTML d'une section selon son type (carte concept, syntax, refs)."""
    kind = meta.get("type")
    if kind == "syntax":
        return renderer.syntax(meta, body, rel)
    if kind == "refs":
        return '<div class="linklist">' + renderer.refs(body, rel) + "</div>"
    intro = f'<p class="concept-intro">{renderer.inline(meta["intro"], rel)}</p>' if meta.get("intro") else ""
    return '<div class="concept-body">' + intro + renderer.card(body, rel) + "</div>"


def load_group(page_key, group, renderer):
    """Sections d'un dossier de groupe, dans l'ordre des noms de fichiers."""
    order = SubgroupOrder(group)
    sections = []
    for path in sorted((CONTENT / page_key / group).glob("*.md")):
        meta, body = split_front_matter(path.read_text(encoding="utf-8"), path)
        rel = path.relative_to(ROOT)
        if "title" not in meta:
            raise BuildError(f"{rel}: `title` manquant dans le front matter")
        order.check(meta, rel)
        sections.append({
            "id": re.sub(r"^[a-z]?\d+-", "", path.stem), "page": page_key, "group": group,
            "subgroup": meta.get("subgroup"), "subsubgroup": meta.get("subsubgroup"),
            "title": meta["title"], "html": render_section(meta, body, rel, renderer), "source": str(rel),
        })
    return sections


def load_sections(site, renderer):
    """Sections de tous les onglets à groupes, dans l'ordre de site.yml."""
    sections = []
    for page in site["pages"]:
        if "groups" not in page:
            continue
        page_dir = CONTENT / page["key"]
        unknown = {p.name for p in page_dir.iterdir() if p.is_dir()} - set(page["groups"])
        if unknown:
            raise BuildError(f"{page_dir}: dossiers absents de site.yml : {sorted(unknown)}")
        for group in page["groups"]:
            sections += load_group(page["key"], group, renderer)
    return sections


def load_lexique(renderer):
    """Termes de content/lexique.md, un par titre `## Terme`, dans l'ordre du fichier."""
    path = CONTENT / "lexique.md"
    rel = path.relative_to(ROOT)
    parts = re.split(r"^## +(.+)$", path.read_text(encoding="utf-8"), flags=re.MULTILINE)
    return [{"t": term.strip(), "id": "lexterm-" + slugify(term.strip()),
             "html": renderer.inline(" ".join(body.split()), rel)}
            for term, body in zip(parts[1::2], parts[2::2])]


def check(site, sections, lexique, renderer):
    """Ids en double et liens internes vers une cible inexistante."""
    known = {p["key"]: "page" for p in site["pages"]}
    for sec in sections:
        if sec["id"] in known:
            raise BuildError(f"{sec['source']}: id `{sec['id']}` déjà utilisé")
        known[sec["id"]] = sec["source"]
    for src, anchor in renderer.anchors:
        if anchor in known and known[anchor] != str(src):
            raise BuildError(f"{src}: id `{anchor}` déjà utilisé ({known[anchor]})")
        known[anchor] = str(src)
    for entry in lexique:
        known[entry["id"]] = "lexique"
        known["lex-" + entry["t"][:1].lower()] = "lexique"
    broken = sorted({f"{src}: lien vers #{target} introuvable"
                     for src, target in renderer.links if target not in known})
    if broken:
        raise BuildError("\n".join(broken))


def last_updated():
    """Date du dernier commit touchant content/, sinon date du jour."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=format:%d/%m/%Y", "--", "content"],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        out = ""
    return out or datetime.datetime.now().astimezone().strftime("%d/%m/%Y")


def main():
    """Compile content/ et écrit www/data/content.js."""
    site = yaml.safe_load((CONTENT / "site.yml").read_text(encoding="utf-8"))
    renderer = Renderer()
    sections = load_sections(site, renderer)
    lexique = load_lexique(renderer)
    check(site, sections, lexique, renderer)
    for sec in sections:
        del sec["source"]
    data = {"title": site["title"], "updated": last_updated(), "pages": site["pages"],
            "sections": sections, "lexique": lexique}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("// Généré par build/build.py depuis content/ : ne pas éditer à la main.\n"
                      "const SITE = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    print(f"{OUTPUT.relative_to(ROOT)} : {len(sections)} sections, {len(lexique)} termes")


if __name__ == "__main__":
    try:
        main()
    except BuildError as err:
        sys.exit(f"Erreur de build :\n{err}")
