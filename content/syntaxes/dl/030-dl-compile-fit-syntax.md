---
title: Compiler & entraîner
subgroup: Keras
type: syntax
---

## Compiler (loss + optimizer)
Syntaxe: model.**compile**(loss='mse', optimizer='adam', metrics=['accuracy'])
Résultat: loss='binary_crossentropy' en classification binaire — cf. page Modélisation ▸ Entraînement

## Compiler — régression sur target positive étalée
Syntaxe: model.compile(loss='**msle**', optimizer='adam')
Résultat: Mean Squared Log Error — cf. page Modélisation ▸ Loss Functions — régression (groupe ml) ; dernière couche 'relu', pas 'linear'

## Personnaliser l'optimizer (learning rate...)
Syntaxe:
```
from keras.optimizers import Adam, SGD
model.compile(optimizer=**Adam**(learning_rate=0.01), loss='mse')
```
Résultat: instancier l'optimizer plutôt qu'un string ('adam') permet de régler learning_rate et les autres hyperparamètres — cf. page Modélisation ▸ Choisir un optimizer

## Learning rate qui décroît automatiquement (scheduler)
Syntaxe:
```
from keras.optimizers.schedules import ExponentialDecay
lr_schedule = **ExponentialDecay**(initial_learning_rate=0.1, decay_steps=200, decay_rate=0.5)
model.compile(optimizer=Adam(learning_rate=lr_schedule), loss='mse')
```
Résultat: decay_steps = nb d'iterations (mises à jour, pas epochs) avant chaque décroissance ; decay_rate = facteur multiplicatif appliqué

## Compiler quand la dernière couche n'a PAS de softmax
Syntaxe:
```
loss = tf.keras.losses.SparseCategoricalCrossentropy(**from_logits**=True)
model.compile(optimizer='adam', loss=loss)
```
Résultat: si la couche de sortie renvoie des logits bruts (pas d'activation), la loss doit le savoir (from_logits=True) pour appliquer elle-même le softmax en interne — sinon elle traite des logits comme des probabilités déjà normalisées et la loss est FAUSSÉE dès le départ

## Entraîner
Syntaxe: model.**fit**(X_train, y_train, batch_size=32, epochs=10)
Résultat: batch_size = taille des sous-ensembles utilisés à chaque update ; epochs = nb de passages complets sur le dataset

## Évaluer sur le test set
Syntaxe: model.**evaluate**(X_test, y_test)
Résultat: renvoie [loss, metrics] — équivalent de .score() côté Sklearn

## Prédire
Syntaxe: model.**predict**(X_new)
Résultat: tableau de sorties (probabilités si sigmoid/softmax en dernière couche)
