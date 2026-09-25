---
title: Dash — structure d'une app minimale
type: syntax
---

## Installer Dash
Syntaxe: **pip install dash dash-bootstrap-components**
Résultat: -

## Structure minimale d'une app
Syntaxe:
```code
from dash import Dash, html, dcc

app = **Dash**(__name__)
app.**layout** = [html.H1("Titre"), dcc.Graph(figure=fig)]

if __name__ == "__main__":
    app.**run**(debug=True)
```
Résultat: lance un serveur local sur http://127.0.0.1:8050/ — debug=True recharge l'app automatiquement à chaque modification du fichier

## Deux familles de composants
Syntaxe:
```
dcc.**Graph**(...), dcc.**Dropdown**(...), dcc.**Slider**(...)   # Dash Core Components
html.**H1**(...), html.**Div**(...), html.**P**(...)            # wrappers HTML
```
Résultat: dcc = composants interactifs (graphiques, filtres) ; html = équivalents des balises HTML classiques — ensemble ils composent app.layout

## Appliquer un thème Bootstrap
Syntaxe:
```
import dash_bootstrap_components as dbc
app = Dash(external_stylesheets=[dbc.**themes**.BOOTSTRAP])
```
Résultat: applique un thème CSS prêt à l'emploi à toute l'app

## Grille responsive (12 colonnes)
Syntaxe: dbc.**Row**([dbc.**Col**(comp1, width=8), dbc.**Col**(comp2, width=4)])
Résultat: dispose des composants côte à côte, largeur en douzièmes de la ligne (8+4=12)
