---
title: Exploration initiale
subgroup: Exploration
type: syntax
---

## Voir les premières lignes
Syntaxe: df.**head**()
Résultat: 5 premières lignes

## Voir les dernières lignes
Syntaxe: df.**tail**(3)
Résultat: 3 dernières lignes

## Lignes prises au hasard (souvent préféré à head/tail)
Syntaxe: df.**sample**(5)
Résultat: 5 lignes aléatoires — head/tail montrent toujours les mêmes lignes (biais si le fichier est trié/groupé), sample donne une vue plus représentative

## Sous-échantillon reproductible, sans remise (ex: exploration rapide sur un gros dataset)
Syntaxe: df.**sample**(10000, random_state=42)
Résultat: DataFrame de 10000 lignes distinctes tirées au hasard — random_state fixe le tirage pour obtenir le même résultat à chaque exécution

## Tirage avec remise sur une colonne
Syntaxe: df["col"].**sample**(10, replace=True)
Résultat: Series de 10 valeurs tirées au hasard dans la colonne, doublons possibles

## Dimensions du DataFrame
Syntaxe: df.**shape**
Résultat: tuple (lignes, colonnes)

## Résumé des types et valeurs non nulles
Syntaxe: df.**info**()
Résultat: affichage console — liste chaque colonne avec son type et son nombre de valeurs non nulles

## Stats descriptives
Syntaxe: df.**describe**()
Résultat: DataFrame avec, pour chaque colonne numérique : count, mean, std, min, 25%, 50%, 75%, max

## Liste des colonnes
Syntaxe: df.**columns**
Résultat: Index des noms de colonnes

## Types des colonnes
Syntaxe: df.**dtypes**
Résultat: Series type par colonne

## Nombre de NaN par colonne
Syntaxe: df.**isna**().sum()
Résultat: Series (nb de NaN)

## Nombre de NaN par colonne (alias)
Syntaxe: df.**isnull**().sum()
Résultat: identique à isna().sum(), juste un autre nom

## Nombre de valeurs uniques par colonne
Syntaxe: df.**nunique**()
Résultat: compte le nombre de valeurs uniques de toutes les colonnes
