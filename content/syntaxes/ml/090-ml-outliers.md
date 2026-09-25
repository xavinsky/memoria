---
title: Nettoyer — Outliers
subgroup: Exploration & Nettoyage
type: syntax
---

## Visualiser les outliers
Syntaxe:
```
df[['col']].**boxplot**()
sns.**boxplot**(data=df, x='col')
```
Résultat: -

## Supprimer les valeurs clairement fausses
Syntaxe:
```
mask = (df['col'] > 0) & (df['col'] < 5000)
df = df[mask].**reset_index**(drop=True)
```
Résultat: ⚠️ un outlier n'est pas toujours une erreur — peut être une observation rare (novelty) ou une feature en soi ; à traiter au cas par cas
