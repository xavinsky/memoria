---
title: Convolution — kernel, filtre, feature map
subgroup: Modèles de base
subsubgroup: CNN
---

[[P:Conv2D]]

Une **convolution** fait glisser un petit **kernel** (ex: 3×3) sur l'image : à chaque position, elle multiplie terme à terme (≠ produit matriciel) le kernel et la portion d'image qu'il recouvre, puis somme le résultat — ce qui produit une valeur en sortie par position.

1. Multiplication élément par élément entre le kernel et la sous-partie de l'image qu'il recouvre
2. Somme des produits → une valeur de sortie pour cette position
3. Le kernel glisse (convolue) sur toutes les positions possibles de l'image → une **feature map** en sortie

Les valeurs du kernel ne sont pas choisies à la main : comme les poids d'un neurone Dense, elles sont initialisées aléatoirement puis **apprises** pendant `model.fit()` (forward/backward propagation, cf. Forward & Backward Propagation, ci-dessus) — seule l'opération change (convolution au lieu de régression linéaire).

Pour une image à plusieurs channels, un **filtre** regroupe un kernel PAR channel — leurs sorties sont sommées (+ un biais) pour ne produire qu'UNE seule feature map par filtre. Une couche de convolution applique plusieurs filtres en parallèle, exactement comme un layer Dense applique plusieurs neurones en parallèle sur le même input.

```math
n_{param}(\text{1 filtre}) = (\text{channels} \times k_h \times k_w) + 1_{biais}
```

Ex: 1 filtre de kernels (3,3) sur une image à 3 channels → $3 \times (3\times3) + 1 = 28$ paramètres — indépendant de la taille de l'image (contrairement à un Dense), ce qui règle le problème #1 ci-dessus.
