---
title: Métriques de régression
subgroup: Métriques
---

Mesurent l'écart entre prédiction et réalité pour une target continue — calculées après `.fit()`, pour ÉVALUER le modèle (cf. [Choisir sa métrique](#ml-choose-metric), ci-dessus, pour le critère de choix).

**Mean Squared Error (MSE)** — moyenne des erreurs au carré : pénalise fortement les grosses erreurs, mais pas dans l'unité de la target (unité²) ; très sensible aux outliers.

```math
MSE = \dfrac{1}{n}\sum_{i=1}^n (y_i-\hat y_i)^2
```

**Root Mean Squared Error (RMSE)** — racine du MSE : ramène l'erreur dans l'unité de la target, donc plus interprétable ; garde la forte pénalisation des grosses erreurs du MSE.

```math
RMSE = \sqrt{MSE}
```

**Mean Absolute Error (MAE)** — moyenne des erreurs absolues : pénalise chaque erreur proportionnellement à sa taille (contrairement au MSE) ; moins sensible aux outliers que MSE/RMSE.

```math
MAE = \dfrac{1}{n}\sum_{i=1}^n |y_i-\hat y_i|
```

**Max Error** — la plus grosse erreur commise par le modèle : utile pour borner l'erreur maximale tolérable (ex: équipement qui surchauffe au-delà d'un seuil).

```math
ME = \max_i |y_i-\hat y_i|
```

**Coefficient de détermination R²** — proportion de la variance de y expliquée par le modèle : sans unité (généralement ∈ [0,1]), donc comparable entre datasets différents ; métrique `.score()` par défaut d'un régresseur Sklearn (cf. [Choisir son modèle](#ml-model-selection), ci-dessous).

```math
R^2 = 1 - \dfrac{\sum_i (y_i-\hat y_i)^2}{\sum_i (y_i-\bar y)^2}
```

> [!TIP]
> 👉 Implémentation Sklearn de chacune (cf. page Syntaxes ▸ [Métriques de régression](#ml-metrics-regression-syntax)).
