---
title: Les axes de configuration d'un modèle
subgroup: Concepts Modèles
---

Un modèle Sklearn se décrit selon 5 axes distincts — reprend le cadre de [Que fait .fit() ?](#ml-fit-hood).

```math
y = h(X, \beta) + error
```

:::compare
- **Hypothèse (h)** : la forme du modèle (linéaire, sigmoïde, kernel...) — déterminée par le choix de la famille de modèle (cf. [Choisir son modèle](#ml-model-selection), ci-dessus).
- **Paramètres (β)** : appris automatiquement par .fit() — PAS un réglage qu'on choisit soi-même.
- **Loss (L)** : ce qui est minimisé pendant .fit() pour trouver β (MSE, Log Loss, Hinge...) — dépend de h (à ne pas confondre avec le `scoring` du Model Tuning, cf. ci-dessous, qui agit différemment).
- **Solver** : comment on minimise L (SGD, lbfgs, résolution exacte...) — cf. [Que fait .fit() ?](#ml-fit-hood), groupe Entraînement (fit).
- **Hyperparamètres** : tout ce qui n'est ni β ni appris — K, C, alpha, kernel, gamma... — choisis avant .fit(), potentiellement affinés par Model Tuning (cf. ci-dessous).
:::

> [!TIP]
> 👉 Le **kernel** est un cas particulier d'hyperparamètre (propre aux modèles à noyau, ex: SVM) : il définit implicitement une partie de l'hypothèse h, sans jamais transformer explicitement les données (cf. [Kernel Trick](#ml-svm-kernels), ci-dessous).

> [!WARNING]
> ⚠️ La **métrique** n'est PAS un réglage du modèle — c'est un outil d'ÉVALUATION utilisé après le fit pour juger le résultat, à ne pas confondre avec la Loss qui pilote l'entraînement (cf. [Choisir sa métrique](#ml-choose-metric), groupe Métriques).
