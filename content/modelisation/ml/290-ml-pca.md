---
title: PCA — Réduction de dimension
subgroup: Modèles
---

[[P:PCA]]

**Principal Component Analysis** — cherche la meilleure combinaison linéaire des features existantes pour "résumer" le dataset dans moins de dimensions, un peu comme combiner $X_2+X_3$ pour éviter la multicolinéarité en régression (cf. Régression), mais en systématique et automatique.

> [!WARNING]
> ⚠️ Les features doivent être **centrées-réduites** (StandardScaler) avant la PCA — sinon une feature à grande échelle domine artificiellement la variance. En interne, `PCA.transform()` ne fait que CENTRER (soustraire la moyenne), jamais réduire — d'où l'importance de scaler soi-même en amont.

Chaque **Principal Component (PC)** est une combinaison linéaire des features d'origine, orthogonale aux autres (0 multicolinéarité entre PCs), rangée par ordre décroissant de variance expliquée.

```math
Z_1 = a_{11}X_1 + a_{12}X_2 + a_{13}X_3
```

:::compare
- **Pourquoi réduire les dimensions** : compresser les données, accélérer et simplifier l'entraînement, réduire l'overfitting (curse of dimensionality), faciliter la visualisation (projeter en 2-3 dimensions)
- **Coût** : perte d'interprétabilité — chaque PC est un mélange de features d'origine, plus de sens métier direct ; perte d'information si k < nombre de features initial
:::

**Choisir k (nombre de PCs gardés)** — méthode du coude sur la variance expliquée cumulée : `pca.explained_variance_ratio_` puis chercher le point d'inflexion (au-delà, chaque PC supplémentaire apporte peu).

> [!TIP]
> 👉 **Limite** : la PCA capture uniquement des structures LINÉAIRES — sur des données en "manifold" (courbées), elle peut mal fonctionner ; alternatives non-linéaires : t-SNE (visualisation), Kernel PCA (même principe que le kernel trick des SVM, cf. ci-dessus).
