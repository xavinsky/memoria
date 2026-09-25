---
title: Exploration des colonnes
subgroup: Exploration
type: syntax
---

## Nombre de valeurs uniques
Syntaxe: df["col"].**nunique**()
Résultat: compte le nombre de valeurs uniques dans la colonne

## Valeurs uniques d'une colonne
Syntaxe: df["col"].**unique**()
Résultat: array des valeurs distinctes

## Fréquence des valeurs
Syntaxe: df["col"].**value_counts**()
Résultat: Series triée par fréquence

## Moyenne d'une colonne
Syntaxe: df["col"].**mean**()
Résultat: scalaire

## Médiane d'une colonne
Syntaxe: df["col"].**median**()
Résultat: scalaire — contrairement à la moyenne, robuste aux valeurs extrêmes (outliers)

## Écart-type d'une colonne
Syntaxe: df["col"].**std**()
Résultat: scalaire

## Asymétrie (skewness) d'une colonne
Syntaxe: df["col"].**skew**()
Résultat: scalaire — 0 si symétrique, >0 asymétrie à droite, <0 à gauche

## Aplatissement (kurtosis) d'une colonne
Syntaxe: df["col"].**kurtosis**()
Résultat: scalaire — équivalent à scipy.stats.kurtosis(), directement en méthode pandas
