---
title: Transformation de colonnes
subgroup: Transformation
type: syntax
---

## Créer une colonne à partir de deux autres
Syntaxe: df["**nouvelle**"] = df["col1"] + df["col2"]
Résultat: nouvelle colonne calculée

## Appliquer une fonction à une colonne
Syntaxe: df["nouvelle"] = df["col"].**apply**(lambda x: x * 2)
Résultat: colonne transformée

## Transformer une colonne simplement (opération vectorisée)
Syntaxe: **df["col"] * 2**
Résultat: plus rapide que .apply(lambda x: x * 2) pour les opérations simples

## Remplacer des valeurs (mapping)
Syntaxe: df["col"] = df["col"].**map**({"A": 1, "B": 2})
Résultat: valeurs remplacées

## Remplacer une valeur exacte par une autre
Syntaxe: df["col"] = df["col"].**replace**("OLD", "NEW")
Résultat: toutes les valeurs égales à OLD deviennent NEW

## Remplacer un sous-texte (substring) dans chaque valeur
Syntaxe: df["col"] = df["col"].str.**replace**("OLD", "NEW", regex=False)
Résultat: chaque occurrence du texte OLD remplacée par NEW à l'intérieur des valeurs

## Anti-pattern à reconnaître (et éviter) : boucler ligne par ligne
Syntaxe:
```
for index, row in df.**iterrows**():
    ...
```
Résultat: très lent sur un gros DataFrame — préférer une opération vectorisée (df["col"] * 2), .apply(), ou du boolean indexing ; utile seulement pour reconnaître ce pattern dans du code existant, pas pour en écrire

## Réordonner les colonnes
Syntaxe: df = df**[["col3", "col1", "col2"]]**
Résultat: DataFrame avec les colonnes dans l'ordre de la liste — pratique pour remonter des colonnes clés (ex: id) en première position

## Arrondir toutes les valeurs numériques
Syntaxe: df.**round**(3)
Résultat: DataFrame avec les valeurs arrondies à 3 décimales
