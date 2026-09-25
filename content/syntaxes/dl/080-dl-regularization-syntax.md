---
title: Régularisation — L1/L2 & Dropout
subgroup: Keras
type: syntax
---

## Régulariser les poids d'une couche (L1/L2)
Syntaxe:
```
from keras import regularizers
reg = regularizers.**L2**(0.01)
layers.Dense(50, activation='relu', kernel_regularizer=reg)
```
Résultat: kernel_regularizer = poids W, le choix par défaut ; regularizers.L1(...) / regularizers.l1_l2(l1=..., l2=...) existent aussi

## Régulariser les biais / la sortie d'une couche
Syntaxe:
```
layers.Dense(20, activation='relu', bias_regularizer=reg)
layers.Dense(10, activation='relu', activity_regularizer=reg)
```
Résultat: bias_regularizer = biais b (rare) ; activity_regularizer = sortie f(W·X+b) (sparsité, ex: autoencoders)

## Ajouter du Dropout
Syntaxe: model.add(layers.**Dropout**(rate=0.2))
Résultat: rate = fraction de neurones "tués" à chaque itération d'entraînement — actif seulement pendant model.fit()
