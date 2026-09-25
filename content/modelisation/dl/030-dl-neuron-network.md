---
title: Neurone, Layer, Réseau de neurones
subgroup: Fondamentaux
---

Un **neurone** = une régression linéaire suivie d'une fonction d'activation non-linéaire — brique de base de tout réseau de neurones.

```math
output = f\Big(\sum_{k=1}^{n} w_k x_k + b\Big)
```

$w_k$ = poids, $b$ = biais (constante, équivalent de l'intercept β₀ d'une régression), $f$ = fonction d'activation.

Un **layer (couche)** = plusieurs neurones EN PARALLÈLE, recevant tous le même input X — chaque neurone du layer a ses propres poids, mais généralement la même fonction d'activation.

Empiler les sorties d'un layer comme input du layer suivant = un **réseau de neurones**. Le **Deep Learning** ne désigne rien de plus qu'un réseau de neurones avec BEAUCOUP de layers.

```math
\hat y = f_\theta(x)
```

Un réseau de neurones entier n'est qu'une fonction $f_\theta$ paramétrée par θ (l'ensemble des poids et biais de tous les neurones) — exactement comme une régression linéaire est paramétrée par β, mais avec beaucoup plus de paramètres et une structure en couches.

> [!TIP]
> 👉 Autrement dit : le Deep Learning n'est "rien de plus" que plusieurs régressions linéaires empilées, entrecoupées de fonctions non-linéaires (cf. [Fonctions d'activation](#dl-activation), ci-dessous).
