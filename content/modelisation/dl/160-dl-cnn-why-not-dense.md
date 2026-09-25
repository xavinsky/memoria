---
title: Pourquoi pas un réseau Dense pour les images
subgroup: Modèles de base
subsubgroup: CNN
---

Une image est un tensor `(height, width, channels)` — 3 channels (RGB) pour une image couleur, 1 pour du noir et blanc. La fléchir (`Flatten`) pour la passer à un réseau Dense classique pose deux problèmes.

:::compare
- **1\. Explosion du nombre de paramètres** : une image (225,225,3) aplatie donne un vecteur de 151875 valeurs — une seule couche Dense de 100 neurones dessus crée déjà plus de 15 millions de paramètres
- **2\. Pas d'invariance par translation** : la même forme (ex: un carré rouge) décalée de quelques pixels produit un vecteur aplati complètement différent — le réseau doit réapprendre à la reconnaître à chaque position possible, au lieu de reconnaître un pattern local indépendamment d'où il se trouve
:::

> [!TIP]
> 👉 Les deux limites viennent du même geste : `Flatten` détruit la structure spatiale 2D de l'image avant même que le réseau ait pu l'exploiter — cf. Convolution, ci-dessous, qui la préserve.
