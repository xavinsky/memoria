---
title: Seaborn — jeux de données & distributions
type: syntax
---

## Importer seaborn
Syntaxe: import **seaborn** as sns
Résultat: -

## Charger un dataset d'exemple intégré
Syntaxe: tips_df = sns.**load_dataset**("tips")
Résultat: DataFrame (ex: dataset 'tips')

## Histogramme rapide, sans import supplémentaire
Syntaxe: df.**hist**("col", bins=20)
Résultat: affiche directement un histogramme matplotlib — pratique en exploration rapide, mais rendu moins soigné que sns.histplot ci-dessous

## Histogramme (rendu plus soigné que plt.hist / df.hist)
Syntaxe: sns.**histplot**(data, bins=20)
Résultat: histogramme affiché directement

## Histogramme sur un axe précis, avec courbe de densité (KDE)
Syntaxe: sns.histplot(data, bins=10, ax=ax, **kde=True**)
Résultat: ax= dessine dans un sous-graphique particulier (utile avec plt.subplots), kde=True superpose une courbe de densité lissée

## Histogramme en densité, avec un pas discret (ex: notes entières, variable 0/1)
Syntaxe: sns.**histplot**(df["col"], kde=False, stat="density", discrete=True)
Résultat: stat="density" normalise l'aire totale à 1 (comparable à une pdf, cf. page Maths) ; discrete=True centre une barre par valeur entière plutôt que des bins continus

## Superposer deux distributions pour les comparer (ex: valeurs réelles vs. prédites)
Syntaxe:
```
sns.**histplot**(y_true, label="actual", kde=True)
sns.**histplot**(y_pred, label="predicted", kde=True)
plt.legend()
```
Résultat: deux histogrammes sur le même axe, avec légende — utile pour juger visuellement la qualité d'une régression

## Histogramme cumulatif (fonction de répartition empirique)
Syntaxe: sns.**histplot**(df["col"], binwidth=5, **cumulative=True**, stat="percent")
Résultat: cumulative=True cumule les effectifs bin par bin, stat="percent" affiche des % plutôt que des comptes — version empirique/graphique de la cdf théorique (cf. Probabilité à partir du z-score, page Maths)

## Distributions côte à côte, une par catégorie
Syntaxe:
```
g = sns.**FacetGrid**(df, hue="dimension", col="dimension")
g.map(sns.kdeplot, "variable")
```
Résultat: une grille de courbes de densité (kde), une par valeur de dimension — pattern utilisé dans olist/utils.py::plot_kde_plot

## Compter les occurrences par catégorie
Syntaxe: sns.**countplot**(data=df, x="categorie", hue="autre_categorie", stat="percent")
Résultat: diagramme en barres du nombre de lignes par modalité — hue= ajoute une sous-répartition par couleur, stat="percent" affiche des % plutôt que des comptes bruts
