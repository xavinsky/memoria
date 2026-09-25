---
title: Indexation et masques
type: syntax
---

## Élément précis (ligne, colonne)
Syntaxe: a**[1, 2]**
Résultat: valeur unique à la position [1,2]

## Une ligne entière
Syntaxe: a**[1]**
Résultat: tableau 1D, la ligne d'index 1

## Une colonne entière
Syntaxe: a**[:, 0]**
Résultat: tableau 1D, la colonne d'index 0

## Sous-matrice (plage de lignes et colonnes)
Syntaxe: a**[1:3, 0:2]**
Résultat: matrice 2x2 extraite

## Toutes les lignes, colonnes choisies
Syntaxe: a[:, **[0, 2]**]
Résultat: colonnes 0 et 2 pour toutes les lignes

## Un axe entier avec un pas
Syntaxe: a[**::2**, **::2**]
Résultat: 1 ligne sur 2, 1 colonne sur 2

## Inverser l'ordre d'un axe
Syntaxe: a[**::-1**]
Résultat: lignes dans l'ordre inverse

## Filtrer par condition
Syntaxe: a[**a > 5**]
Résultat: tableau 1D des éléments > 5

## Combiner plusieurs conditions
Syntaxe: a[(a > 2) **&** (a < 8)]
Résultat: éléments entre 2 et 8 (exclus)

## Remplacer selon condition
Syntaxe: **np.where**(a > 5, 1, 0)
Résultat: 1 si > 5, sinon 0

## Remplacer en place tous les éléments vérifiant une condition
Syntaxe: a[**a > 4**] = 99
Résultat: modifie a directement (contrairement à np.where qui renvoie un nouveau tableau sans toucher a)
