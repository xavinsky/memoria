---
title: Filtrage
subgroup: Sélection, filtrage & tri
type: syntax
---

## Opérateurs autorisés dans une condition
Syntaxe:
```table
==   égal à
!=   différent de
>    strictement supérieur
>=   supérieur ou égal
<    strictement inférieur
<=   inférieur ou égal
&    ET logique
|    OU logique
~    négation (NON)
```
Résultat: chaque condition entre parenthèses, avec & | ~ — jamais and / or / not (ne fonctionnent pas sur une Series)

## Filtrer sur une condition
Syntaxe: df**[df["col"] > 10]**
Résultat: lignes où col > 10

## Filtrer avec ET
Syntaxe: df[(df["col1"] > 10) **&** (df["col2"] == "A")]
Résultat: lignes vérifiant les deux conditions

## Filtrer avec OU
Syntaxe: df[(df["col1"] > 10) **|** (df["col2"] == "A")]
Résultat: lignes vérifiant au moins une condition

## Filtrer sur une liste de valeurs
Syntaxe: df[df["col"].**isin**(["A", "B"])]
Résultat: lignes où col vaut A ou B

## Exclure une liste de valeurs
Syntaxe: df[**~**df["col"].isin(["A", "B"])]
Résultat: lignes où col n'est ni A ni B

## Filtrer un Index (mêmes opérateurs qu'une Series)
Syntaxe: serie.index[~serie.index.**isin**(liste_complete)]
Résultat: clés de serie.index absentes de liste_complete — ex: repérer les orphelins avant un reindex()

## Filtrer sur un texte contenu
Syntaxe: df[df["col"].str.**contains**("texte", na=False)]
Résultat: lignes contenant "texte"

## Filtrer en syntaxe lisible
Syntaxe: df.**query**("col1 > 10 and col2 == 'A'")
Résultat: équivalent au filtrage par masque

## Piège : après un filtrage, l'index n'est plus contigu
Syntaxe: df**[df["col"] > 0]**
Résultat: les lignes gardent leur label d'origine — l'index devient un sous-ensemble discontinu (ex: 0,1,3,4,6...), ce n'est plus un RangeIndex propre même s'il ressemble à des entiers croissants ; .reset_index(drop=True) pour repartir sur un index propre
