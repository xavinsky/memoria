---
title: Forme et tri des tableaux
type: syntax
---

## Changer la forme d'un tableau
Syntaxe: a.**reshape**(3, 4)
Résultat: même données, forme 3x4

## Aplatir un tableau
Syntaxe: a.**flatten**()
Résultat: tableau 1D

## Transposer
Syntaxe: a.**T**
Résultat: lignes/colonnes inversées

## Trier un tableau (nouvelle copie)
Syntaxe: **np.sort**(a)
Résultat: tableau trié croissant, a n'est pas modifié

## Trier un tableau sur place
Syntaxe: a.**sort**()
Résultat: modifie a directement, ne renvoie rien

## Indices qui donneraient le tableau trié
Syntaxe: **np.argsort**(a)
Résultat: tableau des positions, dans l'ordre de tri
