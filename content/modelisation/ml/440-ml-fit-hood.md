---
title: Que fait .fit() ? — hypothèse, loss, solver
subgroup: Entraînement (fit)
---

Tout modèle s'écrit comme une fonction d'**hypothèse h** appliquée à X, paramétrée par β.

```math
y = h(X, \beta) + error
```

$h(X,\beta)$ est la **prédiction** $\hat y$ (ex: $h(X,\beta) = \beta_0 + \beta_1 X_1$ pour une régression linéaire simple).

```math
\beta = \arg\min_\beta L(\beta, X, y, h)
```

`.fit()` trouve les paramètres β qui minimisent une **Loss Function** L de l'erreur — pas l'erreur brute directement ; le choix de L définit ce que "meilleur modèle" veut dire.

```
LogisticRegression(**solver**='newton-cg')
```

> [!TIP]
> 👉 Le **solver** est la méthode utilisée pour trouver ce β qui minimise L : résolution exacte (inversion matricielle, ex: SVD) ou itérative (Gradient Descent, Newton...) — cf. les sections suivantes.
