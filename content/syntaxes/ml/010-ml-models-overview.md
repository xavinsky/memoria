---
title: Modèles Sklearn vus — Régression vs Classification
subgroup: Choix du modèle
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Métrique .score(): col-params
  Explication: col-explication
---

## LinearRegression — régression
Syntaxe:
```
from sklearn.linear_model import LinearRegression
model = **LinearRegression**()
```
Métrique .score(): R²
Explication: target continue (ex: prix) — équivalent Sklearn de smf.ols, sans les p-values/IC (cf. page Maths ▸ Régression pour l'inférence statistique)

## LogisticRegression — classification
Syntaxe:
```
from sklearn.linear_model import LogisticRegression
model = **LogisticRegression**()
```
Métrique .score(): accuracy
Explication: malgré le nom « regression », c'est un modèle de CLASSIFICATION : target catégorielle (ex: churn oui/non) — prédit une probabilité puis une classe ; équivalent Sklearn de smf.logit (cf. logit-fit pour l'inférence statistique)

## KNeighborsRegressor / KNeighborsClassifier — KNN
Syntaxe:
```
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
model = **KNeighborsClassifier**(n_neighbors=5)
```
Métrique .score(): R² / accuracy
Explication: modèle non-linéaire basé sur la distance : prédit à partir des K plus proches voisins du point (moyenne de leurs y en régression, vote majoritaire en classification) — sensible à l'échelle des features, toujours scaler avant (cf. Feature Scaling) ; existe aussi en NearestNeighbors pour la similarité/clustering (cf. Unsupervised Learning) et en KNNImputer pour imputer les valeurs manquantes
