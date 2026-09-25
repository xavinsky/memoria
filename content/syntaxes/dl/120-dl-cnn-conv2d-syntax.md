---
title: Couche de convolution — Conv2D
subgroup: Modèles de base
subsubgroup: CNN
type: syntax
---

## Ajouter le canal manquant (images en niveaux de gris)
Syntaxe:
```
X = X.**reshape**(len(X), 28, 28, 1)
# ou : from keras.ops import expand_dims
X = **expand_dims**(X, axis=-1)
```
Résultat: Conv2D exige (n_images, hauteur, largeur, CANAUX) — un dataset grayscale (n, h, w) n'a pas cette 4e dimension, à ajouter avant de fitter

## Ajouter une couche de convolution
Syntaxe: model.add(layers.**Conv2D**(16, kernel_size=(3, 3), activation='relu'))
Résultat: 16 = nombre de filtres ; kernel_size=3 <=> (3,3) — cf. page Modélisation ▸ [Convolution — kernel, filtre, feature map](#dl-cnn-convolution)

## Contrôler le pas de déplacement du kernel
Syntaxe: layers.Conv2D(16, (3, 3), **strides**=(2, 2), activation='relu')
Résultat: strides=1 par défaut ; strides=2 divise par ~2 la taille de la feature map en sortie

## Contrôler le remplissage des bords
Syntaxe: layers.Conv2D(16, (3, 3), **padding**='same', activation='relu')
Résultat: 'valid' (défaut) : la feature map rétrécit ; 'same' : padding à 0 pour garder la même taille que l'input — cf. page Modélisation ▸ Hyperparamètres de la convolution
