---
title: Plotly Express — scatter interactif
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Importer plotly express
Syntaxe: import **plotly.express** as px
Params: -
Explication: -

## Scatter interactif : position, taille et couleur encodent 4 variables à la fois
Syntaxe:
```
fig = px.**scatter**(data_frame=df, x="col1", y="col2", size="col3", color="col4", size_max=60, opacity=0.5)
fig.**show**()
```
Params: -
Explication: graphique interactif (zoom, survol pour voir les valeurs) — utile en exploration pour repérer des points ou groupes atypiques sans faire un scatter par paire de variables

## Courbe interactive (évolution dans le temps)
Syntaxe:
```
fig = px.**line**(df, x="annee", y="valeur", color="pays")
fig.show()
```
Params: -
Explication: graphique le plus utilisé pour visualiser une série temporelle par catégorie (une courbe par valeur de color) — équivalent interactif de plt.plot / sns.lineplot

## Scatter enrichi : marges + droite de régression + label au survol
Syntaxe: px.scatter(df, x="col1", y="col2", **marginal_x**="histogram", **marginal_y**="box", **trendline**="ols", **hover_name**="pays")
Params: -
Explication: marginal_x/marginal_y ajoutent un histogramme/boxplot en marge de chaque axe, trendline="ols" superpose une droite de régression, hover_name affiche un libellé personnalisé au survol plutôt que juste (x,y)

## Boxplot interactif par catégorie
Syntaxe:
```
fig = px.**box**(df, x="categorie", y="valeur", category_orders={"categorie":["A","B","C"]})
fig.show()
```
Params: category_orders : force l'ordre des catégories sur l'axe X (sinon ordre alphabétique/premier vu)
Explication: équivalent interactif de sns.boxplot — survol affiche médiane/quartiles/outliers exacts de chaque boîte

## Histogramme interactif + ligne de référence
Syntaxe:
```
fig = px.**histogram**(df, x="valeur", nbins=60)
fig.**add_vline**(x=0, line_dash="dash", line_color="red")
fig.show()
```
Params: -
Explication: add_vline : trace une ligne verticale (ex: seuil à 0) par-dessus le graphique — utile pour repérer visuellement combien d'observations passent sous/au-dessus d'un seuil
