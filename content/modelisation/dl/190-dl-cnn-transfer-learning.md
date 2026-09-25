---
title: Architecture typique & Transfer Learning
subgroup: Modèles de base
subsubgroup: CNN
---

:::compare
- **Premières couches de convolution** : capturent des features spatiales générales (contours, formes) — kernels plus grands (ex: 5×5), peu de filtres (32, 64...)
- **Dernières couches de convolution** : capturent des détails plus fins et abstraits — kernels plus petits (ex: 3×3), plus de filtres (128, 256...)
:::

Ré-entraîner depuis zéro un réseau au niveau des architectures SOTA (AlexNet, VGG16...) est coûteux en temps de calcul et demande énormément de données. Le **Transfer Learning** réutilise à la place les couches de convolution d'un modèle déjà entraîné sur un très grand dataset d'images (ex: ImageNet) — ces couches savent déjà extraire des patterns visuels génériques.

1. Charger un modèle SOTA pré-entraîné (ex: VGG16) et **freezer** (geler) ses couches de convolution — leurs poids ne sont plus mis à jour pendant `model.fit()`
2. Retirer ses couches Dense d'origine (entraînées pour SA tâche de classification)
3. Ajouter de nouvelles couches Dense adaptées à la tâche courante
4. N'entraîner (forward/backward propagation) QUE ces nouvelles couches Dense

> [!TIP]
> 👉 Plusieurs modèles pré-entraînés sont disponibles directement dans Keras (`tensorflow.keras.applications` — VGG16, VGG19, ResNet50...), avec leurs poids ImageNet.
