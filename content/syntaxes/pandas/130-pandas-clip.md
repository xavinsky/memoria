---
title: Series.clip — borner une colonne
subgroup: Sélection, filtrage & tri
type: syntax
---

## Ramener toutes les valeurs négatives à 0
Syntaxe: df["col"].**clip**(lower=0)
Résultat: Series — plus court que .apply(lambda x: x if x>0 else 0) ou np.where(df["col"]>0, df["col"], 0)

## Borner entre deux valeurs
Syntaxe: df["col"].**clip**(lower=0, upper=100)
Résultat: Series bornée des deux côtés
