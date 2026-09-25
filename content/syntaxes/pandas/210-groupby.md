---
title: Groupby / agrégation
subgroup: Agrégation
type: syntax
---

## Moyenne par groupe
Syntaxe: df.groupby("col").**mean**()
Résultat: DataFrame indexé par groupe

## Somme d'une colonne par groupe
Syntaxe: df.groupby("col")["valeur"].**sum**()
Résultat: Series indexée par groupe

## Agrégations multiples nommées
Syntaxe: df.groupby("col").**agg**(total=("valeur","sum"), moyenne=("valeur","mean"))
Résultat: DataFrame avec colonnes nommées

## Agrégations multiples, forme dict (équivalente, plus rapide à écrire)
Syntaxe: df.groupby("col").**agg**({"valeur": "sum", "autre": "mean"})
Résultat: DataFrame — une colonne par clé du dict, nommée comme la colonne d'origine (pas de renommage possible contrairement à la forme nommée ci-dessus)

## Nombre de lignes par groupe(s)
Syntaxe: df.groupby(["col1", "col2"]).**size**()
Résultat: Series du nb de lignes (NaN inclus) — pour compter, c'est size(), pas count()

## Nombre de valeurs non-nulles par groupe, colonne par colonne
Syntaxe: df.groupby("col").**count**()
Résultat: DataFrame du nb de valeurs non-NaN pour chaque colonne (peut différer de size() s'il y a des NaN)
