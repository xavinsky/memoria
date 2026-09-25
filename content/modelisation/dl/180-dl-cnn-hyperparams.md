---
title: Hyperparamètres de la convolution — strides, padding, pooling
subgroup: Modèles de base
subsubgroup: CNN
---

[[P:Conv2D]] · [[P:MaxPooling2D]]

:::compare
- **Strides — pas de déplacement du kernel** : strides=1 (défaut) : le kernel glisse d'1 pixel à la fois ; strides=2 : il saute un pixel sur deux → feature map deux fois plus petite en sortie
- **Padding — bords de l'image** : 'valid' (défaut) : pas de remplissage, la feature map RÉTRÉCIT (le kernel ne peut pas dépasser les bords) ; 'same' : ajoute des pixels à 0 autour de l'image pour que la feature map garde LA MÊME taille que l'input
- **Pooling — après une convolution** : réduit la taille de la feature map sans aucun paramètre entraînable ; MaxPooling (le plus courant) garde le max de chaque sous-région, AveragePooling en fait la moyenne
:::

> [!TIP]
> 👉 Bonne pratique : une couche `MaxPooling2D` après chaque `Conv2D` — la feature map rétrécit progressivement pendant que le réseau s'enfonce dans les couches, jusqu'au `Flatten` final avant les couches Dense de classification/régression.
