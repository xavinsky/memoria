---
title: Reshaping (pivot, melt)
subgroup: Transformation
type: syntax
---

## Tableau croisé dynamique (format long -> large)
Syntaxe:
label: df :
```table
  magasin mois  ventes
0   Paris  Jan     100
1   Paris  Fév     120
2    Lyon  Jan      80
3    Lyon  Fév      90
```
```code
df.**pivot_table**(index="magasin", columns="mois", values="ventes", aggfunc="mean")
```
Résultat:
label: DataFrame :
```table
mois      Fév  Jan
magasin
Lyon       90   80
Paris     120  100
```

## Format large -> long (inverse du pivot)
Syntaxe:
label: df :
```table
  magasin  Jan  Fév
0   Paris  100  120
1    Lyon   80   90
```
```code
df.**melt**(id_vars=["magasin"], value_vars=["Jan","Fév"],
        var_name="mois", value_name="ventes")
```
Résultat:
label: DataFrame :
```table
  magasin mois  ventes
0   Paris  Jan     100
1    Lyon  Jan      80
2   Paris  Fév     120
3    Lyon  Fév      90
```
