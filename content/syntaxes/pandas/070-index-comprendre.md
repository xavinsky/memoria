---
title: Comprendre l'index
subgroup: Index
type: syntax
---

## Labels d'index (lignes) d'un DataFrame/Series
Syntaxe: df.**index**
Résultat: par défaut RangeIndex(start=0, stop=n, step=1) — un simple compteur, pas forcément lié aux données

## Labels des colonnes
Syntaxe: df.**columns**
Résultat: aussi un objet Index (même type d'objet que df.index, mais sur l'axe des colonnes)

## Vérifier que l'index n'a pas de doublons
Syntaxe: df.**index.is_unique**
Résultat: bool — l'index n'est PAS unique par nature (contrairement à une clé primaire SQL) : rien n'empêche deux lignes de porter le même label sauf si on le vérifie soi-même

## Nombre de lignes portant un label donné
Syntaxe: (df.index == 0).**sum**()
Résultat: int — si > 1, plusieurs lignes partagent ce label (df.loc[0] renverrait alors un DataFrame, pas une Series)
