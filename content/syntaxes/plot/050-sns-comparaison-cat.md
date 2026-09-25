---
title: Seaborn — comparer une distribution par catégorie
type: syntax
---

## Nuage de points coloré par catégorie
Syntaxe: sns.**scatterplot**(data=df, x="col1", y="col2", **hue**="categorie")
Résultat: un point par ligne, coloré selon la modalité de categorie — syntaxe de base à privilégier sur plt.scatter dès qu'il y a une dimension catégorielle à distinguer

## Boîte à moustaches (médiane, quartiles, outliers) par catégorie
Syntaxe: sns.**boxplot**(data=df, x="categorie", y="valeur", hue="autre_categorie")
Résultat: une boîte par modalité de categorie — les moustaches représentent $[Q_1-1.5\,IQR,\ Q_3+1.5\,IQR]$, les points au-delà sont les outliers (cf. Écart interquartile, page Maths)

## Violon (boxplot + densité KDE combinés)
Syntaxe: sns.**violinplot**(data=df, x="categorie", y="valeur")
Résultat: même info qu'un boxplot mais avec la forme de la distribution en plus (silhouette symétrique = densité kde de chaque côté)

## Nuage de points par catégorie (alternative au boxplot pour peu de données)
Syntaxe: sns.**stripplot**(data=df, x="categorie", y="valeur")
Résultat: affiche chaque observation individuelle plutôt qu'un résumé statistique — utile quand il y a peu de points, où un boxplot serait trompeur
