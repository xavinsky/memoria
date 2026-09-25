---
title: Définir l'architecture — Sequential
subgroup: Keras
type: syntax
---

## Créer un modèle séquentiel
Syntaxe:
```
from keras import Sequential, layers
model = **Sequential**()
```
Résultat: empile les couches ajoutées ensuite dans l'ordre — cf. page Modélisation ▸ [Neurone, Layer, Réseau](#dl-neuron-network)

## Ajouter une couche Dense (fully connected)
Syntaxe: model.**add**(layers.Dense(10, activation='relu'))
Résultat: 10 neurones, activation ReLU — cf. page Modélisation ▸ [Fonctions d'activation](#dl-activation)

## Préciser la forme des inputs
Syntaxe:
```
from keras import Input
model.add(**Input**(shape=(4,)))
```
Résultat: shape = tuple ; permet à Keras d'allouer le modèle immédiatement plutôt que d'inférer au 1er batch

## Dernière couche — régression (1 ou k valeurs)
Syntaxe: model.add(layers.Dense(1, activation='**linear**'))
Résultat: 1 pour une seule valeur prédite, k pour un vecteur de k valeurs

## Dernière couche — classification binaire
Syntaxe: model.add(layers.Dense(1, activation='**sigmoid**'))
Résultat: 1 neurone, sortie interprétable comme une probabilité

## Dernière couche — classification multi-classe
Syntaxe: model.add(layers.Dense(k, activation='**softmax**'))
Résultat: k = nombre de classes, sortie = probabilités qui somment à 1

## Préparer la target pour du softmax (One-Hot)
Syntaxe:
```
from tensorflow.keras.utils import to_categorical
y_cat = **to_categorical**(y)
```
Résultat: transforme un vecteur d'entiers (0,1,2...) en matrice One-Hot (n, k) — nécessaire pour loss='categorical_crossentropy' ; alternative : garder y tel quel avec loss='sparse_categorical_crossentropy'

## Résumé du modèle (couches, nombre de params)
Syntaxe: model.**summary**()
Résultat: affiche chaque couche, sa output shape, son nombre de paramètres entraînables
