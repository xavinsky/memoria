---
title: Lecture / écriture de données
subgroup: Import / export données
type: syntax
---

## Lire un CSV
Syntaxe: **pd.read_csv**("fichier.csv", sep=",", encoding="utf-8")
Résultat: DataFrame

## Désactiver la détection auto des valeurs manquantes
Syntaxe: pd.read_csv("fichier.csv", **na_filter=False**)
Résultat: DataFrame — aucune valeur convertie en NaN, même "NA", "null", "" etc. — piège classique : le code pays ISO "NA" (Namibie) serait sinon lu comme valeur manquante par défaut

## Lire un Excel
Syntaxe: **pd.read_excel**("fichier.xlsx", sheet_name="Feuille1")
Résultat: DataFrame

## Lire un Parquet
Syntaxe: **pd.read_parquet**("fichier.parquet")
Résultat: DataFrame

## Lire un JSON
Syntaxe: **pd.read_json**("fichier.json")
Résultat: DataFrame

## Écrire un CSV
Syntaxe: df.**to_csv**("sortie.csv", index=False)
Résultat: fichier créé, sans colonne d'index

## Écrire un Excel
Syntaxe: df.**to_excel**("sortie.xlsx", index=False)
Résultat: fichier créé
