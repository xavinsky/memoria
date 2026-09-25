---
title: Explorer avant de modéliser
subgroup: Exploration & Nettoyage
type: syntax
---

## Vérifier NaN, doublons, équilibre des classes
Syntaxe:
```
df.**isnull**().sum()
df.**duplicated**().sum()
df['target'].**value_counts**()
```
Résultat: cf. section Pandas ▸ Exploration pour les commandes générales (head, describe, dtypes...) — ici on regarde spécifiquement ce qui impacte un modèle ML

## Séparer colonnes numériques / catégorielles
Syntaxe:
```
X_num = X.**select_dtypes**(exclude=['object'])
X_cat = X.**select_dtypes**(include=['object'])
```
Résultat: pratique pour appliquer un scaler aux unes et un encoder aux autres sans lister les noms de colonnes à la main
