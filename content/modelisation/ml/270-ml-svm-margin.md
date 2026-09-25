---
title: SVM — marge maximale et Soft Margin
subgroup: Modèles
---

[[NP:SVC]] · [[NP:SVR]]

Pour un problème de classification linéairement séparable, il existe une infinité d'hyperplans séparant les classes. Le meilleur pour généraliser est celui qui maximise la **marge** — la distance aux points les plus proches de chaque classe.

Les points sur la frontière de la marge sont les **support vectors** — ce sont eux, et eux seuls, qui déterminent l'hyperplan (problème d'optimisation convexe, solution unique).

> [!WARNING]
> ⚠️ Ce Maximum Margin Classifier est très sensible aux outliers : un seul point mal placé peut fortement déplacer la frontière → overfitting.

**Soft Margin Classifier** — autorise certains points à être à l'intérieur de la marge, voire du mauvais côté, moyennant une pénalité ξᵢ proportionnelle à leur écart. Cette pénalité, la **Hinge Loss**, est linéaire (comme la MAE) : plus un point est enfoncé dans la marge, plus sa perte est grande, mais sans jamais exploser.

**Hyperparamètre C** — force de la pénalité appliquée aux points mal placés :

:::compare
- **C grand** : marge stricte — proche d'un Maximum Margin Classifier (C → +∞), risque d'overfitting
- **C petit** : marge souple, davantage régularisée — C joue un rôle analogue à 1/α dans Ridge
:::

> [!TIP]
> 👉 Tous les modèles à vecteurs de support nécessitent un scaling des features au préalable (cf. Feature Scaling, page Syntaxes).
