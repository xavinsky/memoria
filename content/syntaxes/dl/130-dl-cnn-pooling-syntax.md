---
title: Pooling — réduire la taille sans paramètres
subgroup: Modèles de base
subsubgroup: CNN
type: syntax
---

## Max-pooling (garde le max de chaque zone)
Syntaxe: model.add(layers.**MaxPool2D**(pool_size=(2, 2)))
Résultat: bonne pratique : une couche MaxPool2D après chaque Conv2D — cf. page Modélisation ▸ Hyperparamètres de la convolution

## Average-pooling (moyenne de chaque zone)
Syntaxe: model.add(layers.**AveragePooling2D**(pool_size=(2, 2)))
Résultat: moins courant que MaxPooling en pratique
