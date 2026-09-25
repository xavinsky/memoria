---
title: Dates et temps
subgroup: Dates
type: syntax
---

## Convertir en type date
Syntaxe: df["date"] = **pd.to_datetime**(df["date"], format="%Y-%m-%d")
Résultat: colonne au format datetime

## Extraire l'année
Syntaxe: df["date"].dt.**year**
Résultat: Series d'entiers

## Extraire le mois
Syntaxe: df["date"].dt.**month**
Résultat: Series d'entiers

## Extraire le jour de la semaine
Syntaxe: df["date"].dt.**day_name**()
Résultat: Series de noms de jours

## Agréger par mois
Syntaxe: df.set_index("date").**resample**("ME").sum()
Résultat: DataFrame agrégé mensuellement (fin de mois)
