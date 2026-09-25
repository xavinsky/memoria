---
title: Transformation conditionnelle
subgroup: Transformation
type: syntax
---

## Créer une colonne indicatrice 0/1 à partir d'une condition
Syntaxe: df["dim_is_five_star"] = (df["review_score"] == 5).**astype**(int)
Résultat: colonne de 0/1 — le masque booléen (True/False) se convertit directement en (1/0) avec .astype(int), plus direct qu'un .apply(lambda x: 1 if x==5 else 0)

## Colonne conditionnelle simple
Syntaxe: df["cat"] = **np.where**(df["col"] > 10, "haut", "bas")
Résultat: colonne "haut"/"bas"

## Calculer une valeur seulement si la condition est vraie, sinon garder la valeur d'origine
Syntaxe: df["col"] = **np.where**(df["col"] > 10, df["col"] + 1, df["col"])
Résultat: +1 si col > 10, valeur inchangée sinon

## Même chose, en ne touchant que les lignes concernées
Syntaxe: df.**loc**[df["col"] > 10, "col"] += 1
Résultat: +1 uniquement sur les lignes où col > 10, le reste n'est pas modifié

## Colonne à conditions multiples
Syntaxe: df["cat"] = **np.select**(conditions, choix, default="grand")
Résultat: colonne selon plusieurs seuils
