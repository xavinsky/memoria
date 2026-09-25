---
title: Définir / réinitialiser l'index
subgroup: Index
type: syntax
---

## Fixer une colonne comme index, en place
Syntaxe: df.**set_index**("col", inplace=True)
Résultat: l'index de df devient la colonne col (col n'est plus une colonne normale) — inverse de reset_index()

## Fixer une colonne comme index en refusant les doublons
Syntaxe: df.**set_index**("col", verify_integrity=True)
Résultat: lève une erreur si la colonne choisie contient des valeurs dupliquées, au lieu de laisser passer un index non unique

## Réinitialiser l'index (ancien index → colonne)
Syntaxe: df.**reset_index**()
Résultat: DataFrame avec un nouveau RangeIndex propre ; l'ancien index redevient une colonne normale

## Réinitialiser l'index en jetant l'ancien
Syntaxe: df.**reset_index**(drop=True)
Résultat: DataFrame avec un nouveau RangeIndex propre ; l'ancien index est perdu (pas remis en colonne) — utile après un filtrage ou un concat pour repartir sur un index 0..n-1 propre
