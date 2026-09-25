---
title: Régression logistique — MLE et log-vraisemblance
---

```math
L(\beta) = \prod_{i=1}^n \hat p_i^{\,y_i}(1-\hat p_i)^{1-y_i}
```

**Vraisemblance (likelihood)** d'un modèle de Bernoulli ($y_i\in\{0,1\}$ : classe réelle, $\hat p_i$ : probabilité prédite) — produit des probabilités de Bernoulli de chaque observation. Contrairement à l'OLS (minimiser une somme de carrés), la régression logistique n'a pas de solution fermée : les coefficients sont estimés en maximisant cette vraisemblance (MLE, cf. [Théorème de Bayes](#bayes-naive-bayes)), par une méthode itérative.

```math
\log L(\beta) = \sum_{i=1}^n \Big(y_i\log \hat p_i + (1-y_i)\log(1-\hat p_i)\Big)
```

**Log-vraisemblance** (ce qu'on maximise en pratique) — maximiser le log plutôt que le produit direct transforme un produit de petits nombres (instable numériquement) en somme, sans changer l'argmax.

> [!TIP]
> 💡 La version à minimiser de cette expression (son opposé) est la **log-loss**, utilisée comme fonction de coût pour entraîner un classifieur en ML (cf. Log Loss, groupe Machine Learning ci-dessus).

**z au lieu de t** — contrairement à OLS, la variance d'une loi de Bernoulli est connue analytiquement (pas besoin de l'estimer par s) → test z plutôt que t, pas de degrés de liberté à choisir.

> [!TIP]
> 👉 **Conditions d'inférence allégées vs OLS** : pas besoin de résidus normaux ni de variance constante (homoscédasticité) comme pour OLS — la lecture des p-values et IC des coefficients reste la même.
