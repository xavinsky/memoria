---
title: Entraînement — loss & optimizer
subgroup: Fondamentaux
---

Comme pour tout modèle Sklearn (cf. [Que fait .fit() ?](#ml-fit-hood), groupe ml), entraîner un réseau = trouver le θ qui minimise une Loss — mais deux réglages sont désormais explicites plutôt qu'un `solver` unique.

:::compare
- **Loss (model.compile)** : façon de comparer $y_{true}$ à $y_{pred}$ — ex: 'mse' (régression), 'binary_crossentropy' (classification binaire, = Log Loss cf. groupe ml)
- **Optimizer (model.compile)** : façon de faire évoluer θ pour réduire la Loss (équivalent du `solver` Sklearn) — ex: 'adam', variante avancée de la descente de gradient (cf. [Gradient Descent](#ml-gradient-descent), groupe ml)
:::

**Fitting** (`model.fit`) — processus itératif et stochastique (même logique que le SGD, cf. groupe ml) : à chaque itération, un sous-ensemble de taille `batch_size` met à jour θ ; avoir parcouru tout le dataset une fois = un **epoch**.

> [!TIP]
> 💡 **Universal Approximation Theorem** : un réseau dense avec une seule couche cachée peut en théorie approximer n'importe quelle fonction continue avec une précision arbitraire — mais cela ne garantit PAS qu'on puisse facilement trouver ces paramètres optimaux (peut demander énormément de données ou de calcul).
