# Écrire le contenu de MemorIA

Tout le contenu du site est ici, en Markdown. `python3 build/build.py` le compile en
`www/data/content.js`, que lit `www/index.html` ; ouvrir ensuite `www/index.html` pour vérifier
le rendu. Le build s'arrête avec un message explicite sur un lien interne cassé, un id en double,
un sous-groupe non contigu, un conteneur mal fermé ou un élément Markdown non pris en charge.

## Où ranger une notion

- **Syntaxes** : on cherche un bout de code à copier (appel de fonction, méthode, paramètre).
- **Carte concept** : on cherche à comprendre un mécanisme ou une dérivation. Selon le sujet :
  **Modélisation** (construire, entraîner, choisir un modèle), **Maths** (fondation mathématique
  ou probabiliste indépendante d'un algorithme), **Industrialisation** (ce qui entoure un modèle
  déjà entraîné : LLM, RAG, agents, MLOps, infrastructure).
- **Lexique** : un terme qui mérite une définition d'une ou deux phrases, avec un lien vers la
  section qui le détaille.

## Arborescence

```
content/
  site.yml                          onglets, et groupes de chaque onglet dans l'ordre du menu
  <onglet>/<groupe>/<NNN>-<id>.md   une section
  diagrams/<nom>.svg|html           schémas insérés dans les sections
  lexique.md                        glossaire
```

- **Onglet et groupe** : le dossier. Un nouveau groupe se déclare dans `site.yml` (clé = nom du
  dossier, valeur = libellé du menu) ; un dossier absent de `site.yml` fait échouer le build.
- **Ordre** : le préfixe numérique du nom de fichier. Les fichiers sont numérotés de 10 en 10 pour
  pouvoir en intercaler un (`015-...`).
- **Id** : le reste du nom de fichier. Il est unique sur tout le site, c'est la cible des liens
  `[texte](#id)` et l'ancre de l'URL. Renommer un fichier change son id : mettre à jour les liens
  (le build signale ceux qui cassent).

## Front matter

```yaml
---
title: Gradient Descent          # obligatoire : titre de la section et du menu
subgroup: Entraînement (fit)     # facultatif : boîte repliable dans le menu du groupe
subsubgroup: CNN                 # facultatif : boîte imbriquée dans le sous-groupe
intro: "Phrase d'accroche"       # facultatif (cartes concept) : paragraphe en tête
type: syntax                     # absent pour une carte concept ; syntax ou refs sinon
---
```

Les sections d'un même `subgroup` (et d'un même `subsubgroup`) doivent se suivre dans l'ordre des
fichiers : le menu ouvre une nouvelle boîte à chaque changement de valeur.

## Carte concept (Modélisation, Maths, Industrialisation)

Le corps est une suite de blocs séparés par une ligne vide.

### Blocs Markdown standard

| Écrire | Rendu |
|---|---|
| un paragraphe | bloc de texte |
| ` ```math ` (ou ` ```latex `) … ` ``` ` | formule centrée, en LaTeX |
| ` ``` ` … ` ``` ` (autre langage ou aucun) | bloc de code |
| `1.` `2.` `3.` | étapes numérotées |
| `> [!TIP]` puis `> texte` | encart « à retenir » (vert) |
| `> [!WARNING]` puis `> texte` | encart « piège » (orange) |
| tableau Markdown | mini-tableau |
| `![](../../diagrams/nom.svg)` seul sur sa ligne | schéma inséré tel quel |
| `---` entre deux lignes vides | filet de séparation au-dessus du bloc suivant |

Dans le texte :

- `**gras**` pour les mots-clés, `~~barré~~`, `` `code` `` ;
- `$...$` pour une formule en ligne, `$$...$$` pour une formule détachée au milieu d'un paragraphe.
  Leur contenu n'est pas interprété comme du Markdown : `_` et `\` y sont libres. KaTeX les affiche
  dans le navigateur ;
- `[texte](#id)` pour un lien interne (vérifié au build), `[texte](https://...)` pour un lien
  externe, suivi automatiquement de ↗.

Dans le code, en bloc comme en ligne, `**mot**` reste interprété comme du gras : c'est ainsi qu'on
met en évidence la fonction principale (`df.**dropna**()`). Une puissance Python (`x**2`)
s'écrit normalement tant qu'elle est seule sur sa ligne : deux `**` sur une même ligne encadrent
du gras.

### Conteneurs

Les blocs propres au site sont des conteneurs `:::nom` … `:::`, chacun sur sa ligne. Ils
s'imbriquent : une ligne `:::` ferme toujours le dernier conteneur ouvert. Le nombre de `:` est
libre (au moins trois) ; on en met un de plus sur le conteneur englobant pour la lisibilité.
Des attributs facultatifs se placent en fin de ligne d'ouverture, entre accolades :
`{#id clé=valeur}`.

**Cartes côte à côte** : une opposition entre deux éléments ou plus. Une puce par carte.

```
:::compare
- **Biais** : erreur due à des hypothèses trop simples
- **Variance** : sensibilité aux variations du jeu d'entraînement
:::
```

`{nom}` en tête de puce ajoute la classe CSS `role-nom` à la carte (`{outer}`, `{inner}`, `{p}`,
`{np}` sont stylés).

**Catégorie** : badge suivi d'une description, souvent placé sous un schéma de choix de modèle.
L'id sert de cible aux liens du schéma.

```
:::category Classification {#cat-classification}
prédire une catégorie parmi un nombre fini de classes connues.
:::
```

**Dérivation** : suite d'étapes numérotées, chacune contenant n'importe quels blocs (texte, formule,
code, encart, `:::compare`...).

```
::::derivation {start=1}

:::step Explorer {#wf0-explorer}

Texte, formules, code...

:::

:::step Nettoyer

...

:::

::::
```

- `start=N` : numéro de la première étape (0 par défaut) ;
- sur une étape, `#id` pose une ancre (cible de liens `[texte](#id)`) et `num=N` force son numéro.

### Badges de modèle

`[[P:Classe]]` (modèle paramétrique) ou `[[NP:Classe]]` (non paramétrique), avec deux segments
facultatifs : `[[P:LogisticRegression|Régression logistique|ml-linear-logistic]]`. Le 2ᵉ segment
s'affiche en infobulle, le 3ᵉ fait du badge un lien vers cette section. Dans une cellule de
tableau, écrire `\|` au lieu de `|`.

## Syntaxes (`type: syntax`)

Un tableau objectif → syntaxe → résultat, écrit ligne par ligne : un titre `##` par ligne du
tableau (1re colonne), puis une ligne `Colonne: valeur` par colonne suivante.

```
## Créer un tableau à partir d'une liste
Syntaxe: np.**array**([1, 2, 3])
Résultat: array([1, 2, 3])
```

Les valeurs sont du **texte brut** : seul `**gras**` est interprété, plus les liens
`[texte](#id)` et `[texte](https://...)` dans les colonnes de texte (toutes sauf `col-syntaxe`,
`col-formule` et `col-params`, où les crochets sont du code). Les formules `$...$` sont affichées
par KaTeX.

- **Valeur sur plusieurs lignes** : `Colonne:` seul sur sa ligne, suivi d'un bloc ` ``` `.
  ````
  Syntaxe:
  ```
  scaler = StandardScaler()
  X_scaled = scaler.**fit_transform**(X)
  ```
  ````
- **Colonne Params** (`col-params`) : une valeur par ligne, affichées séparément.
- **Cellule composée** : `Colonne:` suivi de blocs ` ```code ` (code), ` ```table ` (texte
  préformaté encadré) et de lignes `label: texte` (petite légende), dans l'ordre d'affichage.
- **Syntaxe à ne pas utiliser** : `Incorrect: ...` ajoute au-dessus de la 2e colonne une syntaxe
  barrée (le piège classique, avant la bonne syntaxe).

Colonnes par défaut : `Objectif`, `Syntaxe`, `Résultat`. Pour d'autres colonnes, les déclarer dans
le front matter avec leur classe CSS, qui fixe leur rendu :

```yaml
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
```

`col-syntaxe` et `col-formule` sont en police code, `col-params` affiche une valeur par ligne,
`col-resultat` et `col-explication` sont sur fond coloré.

## Refs (`type: refs`)

```
### Documentation officielle

- [NumPy](https://numpy.org/doc/stable/)
- [Pandas](https://pandas.pydata.org/docs/)

:::cards
- [Kaggle Datasets](https://www.kaggle.com/datasets) : catalogue de datasets réels, tous domaines
:::
```

Un titre `###` devient un sous-titre à puce ; une liste de liens s'affiche en ligne, entre
crochets ; `:::cards` produit une grille de cartes (nom, description).

## Lexique (`lexique.md`)

Un terme par titre `## Terme`, suivi de sa définition (une ou deux phrases) et d'un lien vers la
section qui le détaille :

```
## Accuracy

proportion de prédictions correctes. [Modélisation ▸ Métriques de classification](#ml-metrics-classification)
```

La page Lexique range chaque terme dans la vue « Groupe » d'après la section visée par son premier
lien : un terme sans lien atterrit dans « Autres / transverses ». Garder l'ordre alphabétique des
titres, c'est l'ordre d'affichage.

## Pièges

- **`---` juste sous un paragraphe** en fait un titre : toujours une ligne vide avant.
- **Caractères Markdown dans le texte** : un `*` ou un `_` isolé, un `<` suivi d'une lettre
  (`<PAD>`), une ligne qui commence par `1.` ou `-` doivent être précédés de `\` pour rester du
  texte. Le code entre accents graves et les formules `$...$` n'ont pas besoin d'échappement.
- **Barre verticale dans un tableau** : `\|`.
- **Titre de ligne Syntaxes** : tout ce qui suit `## ` jusqu'à la fin de la ligne, même long.
