---
title: Régularisation — Ridge, Lasso, ElasticNet
subgroup: Modèles
---

[[P:Ridge]] · [[P:Lasso]] · [[P:ElasticNet]]

Solution à l'overfitting (cf. [Bias/Variance tradeoff](#ml-bias-variance), ci-dessous) : ajoute à la Loss un terme de pénalité qui augmente avec les β, pour limiter la complexité du modèle sans changer les features utilisées.

```math
Loss_{régularisée} = Loss(X,y,\beta) + Penalty(\beta)
```

:::compare
- {outer} **Ridge (L2)** : pénalité $\alpha\sum_j \beta_j^2$ — rétrécit les coefficients vers 0 sans jamais les annuler
- {inner} **Lasso (L1)** : pénalité $\alpha\sum_j |\beta_j|$ — peut ramener des coefficients exactement à 0 → sélectionne les features automatiquement
:::

```math
ElasticNet: L = \|y-\hat y\|^2 + \alpha\big(\lambda|\beta| + (1-\lambda)\|\beta\|^2\big)
```

**ElasticNet** : moyenne pondérée Ridge/Lasso — 2 hyperparamètres à tuner (α, λ = l1_ratio).

> [!WARNING]
> ⚠️ L'intercept β₀ n'est **jamais** régularisé — seuls β₁...βₚ (les coefficients associés à une feature) le sont. Toujours scaler les features avant de régulariser, pour pénaliser chaque βᵢ équitablement (cf. Feature Scaling, page Syntaxes).

> [!TIP]
> 👉 **α (alpha)** contrôle la force de la régularisation — α grand : modèle plus simple, ⤵ variance, ⤴ bias ; α → 0 : revient à une régression non régularisée. Ridge/Lasso tendent à pénaliser davantage les features les moins statistiquement significatives (cf. p-values, page Maths ▸ Régression).

> [!TIP]
> 💡 **Repère pratique** : Ridge quand on pense que tous les coefficients ont un impact ; Lasso comme outil de sélection de features (meilleure interprétabilité) ; la régularisation est presque toujours pertinente — Ridge est souvent activé par défaut dans les modèles Sklearn.
