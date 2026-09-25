---
title: Métriques de régression
subgroup: Métriques
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Mean Squared Error (MSE)
Syntaxe:
```
from sklearn.metrics import mean_squared_error
**mean_squared_error**(y_true, y_pred)
```
Params: -
Explication: formule et quand l'utiliser : cf. page Modélisation ▸ [Métriques de régression](#ml-metrics-regression)

## Root Mean Squared Error (RMSE)
Syntaxe:
```
import math
math.**sqrt**(mean_squared_error(y_true, y_pred))
```
Params: -
Explication: pas de fonction sklearn dédiée, se calcule à partir du MSE — cf. page Modélisation ▸ [Métriques de régression](#ml-metrics-regression)

## Mean Absolute Error (MAE)
Syntaxe:
```
from sklearn.metrics import mean_absolute_error
**mean_absolute_error**(y_true, y_pred)
```
Params: -
Explication: cf. page Modélisation ▸ [Métriques de régression](#ml-metrics-regression)

## Max Error
Syntaxe:
```
from sklearn.metrics import max_error
**max_error**(y_true, y_pred)
```
Params: -
Explication: cf. page Modélisation ▸ [Métriques de régression](#ml-metrics-regression)

## Coefficient de détermination R²
Syntaxe:
```
from sklearn.metrics import r2_score
**r2_score**(y_true, y_pred)
```
Params: -
Explication: métrique .score() par défaut d'un régresseur Sklearn — cf. page Modélisation ▸ [Métriques de régression](#ml-metrics-regression)

## Comparer plusieurs métriques en cross-validation
Syntaxe:
```
from sklearn.model_selection import cross_validate
cross_validate(model, X, y, cv=5, **scoring**=['r2','max_error','neg_mean_absolute_error','neg_mean_squared_error'])
```
Params: scoring : liste de noms de métriques Sklearn — préfixe neg_ obligatoire pour les métriques "plus petit = meilleur", car cross_validate maximise toujours son score
Explication: permet de comparer plusieurs métriques sans relancer un cross_validate par métrique
