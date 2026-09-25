---
title: KNN — K-Nearest Neighbors
subgroup: Modèles
---

[[NP:KNeighborsClassifier]] · [[NP:KNeighborsRegressor]]

Modèle non-paramétrique (cf. Choisir sa famille de modèle, ci-dessus) utilisable aussi bien en régression qu'en classification — la seule chose qui change entre les deux est la façon d'agréger les voisins.

1. Calculer la distance entre le nouveau point et TOUS les points du training set
2. Garder les K plus proches
3. Régression : moyenne (éventuellement pondérée par la distance) de leurs valeurs cible
4. Classification : vote majoritaire (ou proportion de chaque classe pour predict_proba)

> [!TIP]
> 👉 **"Lazy learner"** — `.fit()` ne fait que STOCKER les données d'entraînement, aucun calcul n'a lieu à cette étape (contrairement à un modèle paramétrique qui résout un système ou fait une descente de gradient) ; tout le coût de calcul est reporté à `.predict()`, qui doit comparer chaque nouveau point à l'ensemble du training set.

:::compare
- **K petit** : frontière de décision très sensible au bruit — un seul point isolé peut faire basculer la prédiction (overfitting)
- **K grand** : frontière lissée, mais le signal local se dilue parmi trop de voisins parfois non pertinents (underfitting)
:::

> [!WARNING]
> ⚠️ **Curse of Dimensionality** — en haute dimension, la notion de "proche voisin" perd son sens : toutes les distances entre points tendent à se ressembler, rendant le K-NN peu discriminant (cf. Feature Selection / PCA, ci-dessus, pour réduire la dimension en amont).

> [!TIP]
> 👉 Toujours scaler les features avant KNN (cf. Feature Scaling, ci-dessus) — une feature à grande échelle domine artificiellement le calcul de distance.
