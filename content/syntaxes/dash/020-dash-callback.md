---
title: Dash — interactivité (callbacks) & multi-pages
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Callback : relier un composant d'entrée à une sortie
Syntaxe:
```code
**@callback**(
    Output("mon_graph", "figure"),
    Input("mon_dropdown", "value")
)
def update(valeur):
    filtered = df[df["country"] == valeur]
    return px.line(filtered, x="year", y="co2", title=f"CO2 — {valeur}")
```
Params: -
Explication: la fonction décorée se réexécute automatiquement à chaque changement de la valeur du composant Input, et met à jour le composant Output (ici la figure du graphique)

## Identifier les composants à relier
Syntaxe:
```
dcc.Dropdown(**id="mon_dropdown"**, options=[...])
dcc.Graph(**id="mon_graph"**)
```
Params: -
Explication: id= sert de clé pour cibler le composant depuis Output()/Input() dans un callback

## Construire dynamiquement les options d'un Dropdown
Syntaxe:
```
dcc.**Dropdown**(
    id="mon_dropdown",
    options=[{"label": c, "value": c} for c in df["country"].unique()],
    **value**="France"
)
```
Params:
```
options : liste de dicts {"label": texte affiché, "value": valeur envoyée au callback}
value= : valeur sélectionnée par défaut au chargement de l'app
```
Explication: pattern courant pour générer les choix à partir des valeurs réellement présentes dans le DataFrame, plutôt que de les écrire à la main

## Structurer une app multi-pages
Syntaxe:
```
dossier pages/ma_page.py :
dash.**register_page**(__name__)
layout = [...]  # pas de app.layout ici

app = Dash(use_pages=True)
app.layout = [dash.**page_container**]
```
Params: -
Explication: chaque fichier de pages/ devient une route automatiquement ; page_container affiche la page active dans le layout principal

## Menu de navigation entre les pages
Syntaxe: [dcc.**Link**(page["name"], href=page["relative_path"]) for page in dash.**page_registry**.values()]
Params: -
Explication: page_registry : dict rempli automatiquement par register_page() pour chaque page — dcc.Link crée un lien de navigation sans recharger toute l'app (contrairement à un <a> classique)
