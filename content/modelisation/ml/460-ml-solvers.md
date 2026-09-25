---
title: Variantes de la descente de gradient (solvers)
subgroup: Entraînement (fit)
---

:::compare
- **Batch Gradient Descent** : calcule le gradient sur TOUTES les observations à chaque epoch — précis mais coûteux quand n est grand
- **Mini-Batch Gradient Descent** : gradient approché sur un petit sous-ensemble (ex: 16 observations) à chaque itération — compromis vitesse/précision
- **Stochastic Gradient Descent (SGD)** : mini-batch de taille 1 — moins stable (la loss ne décroît pas à chaque étape) mais beaucoup plus rapide sur les gros datasets (n à 6 chiffres ou plus), permet de sortir d'un minimum local
:::

```
from sklearn.linear_model import SGDRegressor, SGDClassifier
model = **SGDRegressor**(loss='squared_error')
```

**SGDRegressor** / **SGDClassifier** : modèle linéaire entraîné par SGD au lieu d'une résolution exacte — même hypothèse h que LinearRegression/LogisticRegression, solver différent, beaucoup plus rapide quand n ou p sont grands. Loss régression : squared_error (≈ OLS), huber... Loss classification : log_loss (≈ Logit), hinge (≈ SVC)...

> [!TIP]
> 👉 **Solvers du second ordre** (Hessienne, ex: newton-cg, lbfgs) : approxime la Loss par une fonction quadratique plutôt qu'une pente — convergent en peu d'epochs mais coûteux par epoch ; solver par défaut de LogisticRegression sur des problèmes de taille raisonnable.

> [!WARNING]
> ⚠️ `SGDClassifier(loss='hinge')` (défaut) émule un SVM linéaire, qui n'a pas de notion de probabilité — `.predict_proba()` lève une `AttributeError`. Pour obtenir des probabilités (ex: ajuster un seuil), passer explicitement `loss='log_loss'` (émule une régression logistique).
