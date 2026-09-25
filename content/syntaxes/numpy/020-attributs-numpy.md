---
title: Attributs d'un tableau (ndim, shape, size, dtype)
type: syntax
---

## Nombre de dimensions
Syntaxe: a.**ndim**
Résultat: int — 1 pour un vecteur, 2 pour une matrice, etc.

## Forme (dimensions) du tableau
Syntaxe: a.**shape**
Résultat: tuple — (lignes, colonnes) pour un tableau 2D

## Nombre total d'éléments
Syntaxe: a.**size**
Résultat: int — produit de toutes les dimensions de shape

## Type des éléments
Syntaxe: a.**dtype**
Résultat: ex: int64, float64 — tous les éléments d'un ndarray ont le même type, contrairement à une liste Python

## Reconvertir en liste Python native
Syntaxe: a.**tolist**()
Résultat: list (ou liste de listes) — utile pour interopérer avec du code qui attend des listes plutôt que des ndarray
