---
title: Opérations et stats
type: syntax
---

## Somme des éléments
Syntaxe: a.**sum**()
Résultat: scalaire

## Choisir l'axe d'agrégation sur un tableau 2D
Syntaxe:
```
a.sum(**axis=0**)  # somme par colonne (vertical)
a.sum(**axis=1**)  # somme par ligne (horizontal)
```
Résultat: même principe pour mean()/std()/min()/max() — axis=0 écrase les lignes (1 résultat par colonne), axis=1 écrase les colonnes (1 résultat par ligne) : piège fréquent d'inverser les deux

## Moyenne
Syntaxe: a.**mean**()
Résultat: scalaire

## Écart-type
Syntaxe: a.**std**()
Résultat: scalaire

## Min / max
Syntaxe: a.**min**(), a.**max**()
Résultat: scalaire

## Index du max
Syntaxe: a.**argmax**()
Résultat: position (int)

## Concaténer deux tableaux
Syntaxe: **np.concatenate**([a, b])
Résultat: tableau fusionné

## Produit matriciel
Syntaxe: **np.dot**(a, b)
Résultat: matrice ou scalaire selon dimensions

## Opération élément par élément
Syntaxe: **a + b**
Résultat: tableau (broadcasting)
