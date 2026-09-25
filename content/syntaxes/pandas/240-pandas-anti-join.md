---
title: Anti-jointure — repérer les lignes sans correspondance
subgroup: Jointures
type: syntax
---

## Compter les order_id sans review, via une jointure outer
Syntaxe:
```
merged = orders[["order_id"]].**merge**(reviews[["order_id","review_id"]], on="order_id", how="outer")
merged.**isna**().sum()["review_id"]
```
Résultat: nb de order_id qui n'ont trouvé aucune review — how="outer" garde toutes les lignes des deux côtés ; un NaN dans review_id signifie "pas de review pour cette commande" (à comparer à l'approche isin()+~ de la section Filtrage, plus directe si on n'a pas besoin des colonnes de droite)

## Indicateur explicite de la provenance de chaque ligne après un merge
Syntaxe: pd.merge(orders, reviews, on="order_id", how="outer", **indicator=True**)
Résultat: ajoute une colonne _merge ("left_only" / "right_only" / "both") — utile pour diagnostiquer précisément quelles lignes ne matchent pas de chaque côté
