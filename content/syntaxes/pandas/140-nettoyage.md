---
title: Nettoyage des données
subgroup: Transformation
type: syntax
---

## Supprimer les lignes avec NaN
Syntaxe: df.**dropna**()
Résultat: DataFrame sans lignes incomplètes

## Supprimer si NaN dans une colonne précise
Syntaxe: df.**dropna**(subset=["col"])
Résultat: DataFrame filtré

## Remplacer les NaN par une valeur
Syntaxe: df.**fillna**(0)
Résultat: DataFrame sans NaN

## Remplacer les NaN par la moyenne
Syntaxe: df["col"].**fillna**(df["col"].mean())
Résultat: Series sans NaN

## Supprimer les doublons
Syntaxe: df.**drop_duplicates**()
Résultat: DataFrame sans lignes dupliquées

## Supprimer les doublons sur une colonne
Syntaxe: df.**drop_duplicates**(subset=["col"])
Résultat: DataFrame filtré

## Renommer des colonnes
Syntaxe: df.**rename**(columns={"ancien": "nouveau"})
Résultat: DataFrame avec nouveaux noms

## Supprimer des colonnes
Syntaxe: df.**drop**(columns=["col1", "col2"])
Résultat: DataFrame sans ces colonnes

## Convertir un type de colonne
Syntaxe: df["col"] = df["col"].**astype**(int)
Résultat: colonne convertie en int

## Convertir un nombre écrit en texte, sans planter sur ce qui ne parse pas
Syntaxe: df["col"] = **pd.to_numeric**(df["col"], errors="coerce")
Résultat: colonne numérique — les valeurs non convertibles deviennent NaN (traitées ensuite comme des valeurs manquantes classiques) plutôt que de lever une exception comme .astype()

## Retirer les espaces parasites en début/fin de chaîne
Syntaxe: df["col"] = df["col"].str.**strip**()
Résultat: Series nettoyée — piège classique : un isin()/comparaison qui ne matche rien peut être causé par des espaces invisibles, repérables avec .unique()

## Piège : filtrer les valeurs manquantes (NaN). NaN n'est jamais égal à lui-même en Python/numpy (même deux NaN comparés entre eux donnent False), donc comparer avec == ne peut jamais fonctionner pour les repérer — et pire, ça ne renvoie aucune erreur ni aucun warning, juste un résultat vide.
Syntaxe: df[df["col"].**isna**()]
Résultat: lignes où col est NaN
Incorrect: df[df["col"] == np.nan]
