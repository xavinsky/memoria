---
title: Construire une Series / un DataFrame from scratch
subgroup: Import / export données
type: syntax
---

## Créer une Series à partir d'une liste
Syntaxe: pd.**Series**([10, 20, 30], index=["a","b","c"])
Résultat: Series indexée par a/b/c

## Créer une Series à partir d'un dict
Syntaxe: pd.**Series**({"a": 10, "b": 20})
Résultat: Series — les clés du dict deviennent l'index

## Créer un DataFrame à partir de listes de listes
Syntaxe: pd.**DataFrame**([[1,2],[3,4]], index=["r1","r2"], columns=["c1","c2"])
Résultat: DataFrame 2x2

## Créer un DataFrame à partir d'un dict de listes/Series
Syntaxe: pd.**DataFrame**({"col1": [1,2,3], "col2": [4,5,6]})
Résultat: DataFrame — chaque clé du dict devient une colonne, alignée sur le même index : un DataFrame est fondamentalement un dict de Series partageant le même index
