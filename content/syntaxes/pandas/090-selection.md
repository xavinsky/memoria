---
title: Sélection
subgroup: Sélection, filtrage & tri
type: syntax
---

## Sélectionner une colonne
Syntaxe: df**["col"]**
Résultat: Series

## Sélectionner une colonne — notation par point (raccourci)
Syntaxe: df.**col**
Résultat: Series — équivalent à df["col"], mais seulement si "col" est un identifiant Python valide (pas d'espace, ne commence pas par un chiffre) et ne rentre pas en conflit avec une méthode/attribut existant de DataFrame (ex: df.count, df.shape) ; ne fonctionne pas pour créer une nouvelle colonne par assignation (df.nouvelle_col = ... échoue, il faut df["nouvelle_col"] = ...)

## Sélectionner plusieurs colonnes
Syntaxe: df**[["col1", "col2"]]**
Résultat: DataFrame

## Ligne par position
Syntaxe: df.**iloc**[0]
Résultat: 1ère ligne

## Plage de lignes par position
Syntaxe: df.**iloc**[0:5]
Résultat: 5 premières lignes

## Ligne par label d'index
Syntaxe: df.**loc**[3]
Résultat: ligne d'index 3

## Valeur précise par label
Syntaxe: df.**loc**[3, "col"]
Résultat: valeur unique

## Plage de lignes par label (bornes incluses des deux côtés)
Syntaxe: df.**loc**[3:7]
Résultat: lignes dont le label d'index va de 3 à 7 INCLUS — contrairement à .iloc[3:7] (borne de fin exclue), .loc inclut la borne de fin
