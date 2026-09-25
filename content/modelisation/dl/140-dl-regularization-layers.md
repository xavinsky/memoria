---
title: Régularisation par couche — L1/L2, kernel/bias/activity
subgroup: Régularisation
---

[[P:regularizers.L1]] · [[P:regularizers.L2]]

Même principe que Ridge/Lasso (cf. Régularisation, groupe ml) : la Loss régularisée pénalise la magnitude de θ, pondérée par α.

```math
Loss_{reg} = Loss + \alpha\sum_i|\theta_i| \ \ (L1) \qquad Loss_{reg} = Loss + \alpha\sum_i\theta_i^2 \ \ (L2)
```

Nouveau par rapport à Sklearn : la régularisation se définit **couche par couche**, et on choisit QUELLE partie de la couche pénaliser.

:::compare
- **kernel_regularizer — les poids W** : équivalent direct de Ridge/Lasso — garde les poids petits (L2) ou en pousse certains à 0 (L1) ; le meilleur choix pour démarrer
- **bias_regularizer — les biais b** : garde les biais petits — rarement utilisé
- **activity_regularizer — la sortie f(W·X+b)** : rend la sortie de la couche sparse (peu de neurones "actifs") — utile pour les autoencoders, moins pour la régression/classification classique
:::

> [!TIP]
> 💡 La régularisation n'ajoute AUCUN paramètre entraînable au modèle — α est un hyperparamètre fixé à l'avance, pas appris (vérifiable avec `model.summary()`, cf. page Syntaxes).
