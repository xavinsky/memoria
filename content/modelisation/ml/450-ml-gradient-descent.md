---
title: Gradient Descent
subgroup: Entraînement (fit)
---

Descend itérativement la Loss Function en suivant la pente inverse de son gradient.

1. Initialiser aléatoirement le(s) paramètre(s), ex: $\beta_0 = 0$
2. Calculer la dérivée (le gradient) de la Loss à ce point
3. Avancer dans la direction **opposée** au gradient, proportionnellement à un **learning rate** η
4. Répéter jusqu'à un critère d'arrêt

```math
\beta^{(k+1)} = \beta^{(k)} - \eta \nabla L(\beta^{(k)})
```

η (eta) = learning rate. Le gradient s'annule au minimum, donc les pas rétrécissent en approchant du minimum — la descente de gradient fait ainsi peu de calculs loin du minimum, plus près de lui.

:::compare
- **η petit** : convergence lente mais précise — risque de rester bloqué dans un minimum local
- **η grand** : convergence rapide — risque de ne jamais converger
:::

> [!TIP]
> 👉 **Minimum local vs global** — un minimum local minimise la Loss au VOISINAGE d'un point, sans être forcément le minimum absolu (global) sur tout le domaine ; si la fonction n'est pas convexe, la descente peut y rester bloquée selon le point de départ (une Loss convexe comme la SSR de l'OLS n'a qu'un seul minimum, donc ce risque n'existe pas pour elle).

> [!TIP]
> 💡 Toujours scaler les features (cf. Feature Scaling, Syntaxes) : la descente de gradient converge plus vite quand les features sont à la même échelle.

**Critères d'arrêt** : minimum step size (ex: 0.001) ou nombre maximum d'epochs (ex: 1000).

> [!TIP]
> 👉 Même principe qu'en Deep Learning (cf. [Early Stopping & jeu de validation](#dl-early-stopping), groupe dl) : la loss du TRAIN set décroît toujours, mais celle d'un jeu de VALIDATION dédié (jamais le test set) finit par remonter (overfitting) — s'arrêter dès cette remontée, avec de la patience si la loss est bruitée (mini-batch/SGD).

```math
\nabla SSR(\beta) = -2X^T(y-\hat y)
```

Gradient vectoriel de la Sum of Squared Residuals pour l'OLS — simple et rapide à calculer, ce qui rend la descente de gradient très efficace pour l'OLS.
