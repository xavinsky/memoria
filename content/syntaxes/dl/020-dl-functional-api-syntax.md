---
title: Architectures non-linéaires — Functional API
subgroup: Keras
type: syntax
---

## Définir les entrées
Syntaxe:
```
from keras import Input
inputs = **Input**(shape=(10,))
```
Résultat: point de départ obligatoire de la Functional API — pas de Sequential() ici

## Appeler les couches comme des fonctions
Syntaxe:
```
x = layers.Dense(50, activation='relu')(inputs)
outputs = layers.Dense(1, activation='sigmoid')(x)
```
Résultat: chaque couche prend le tensor précédent en argument, au lieu d'un .add() séquentiel — permet de brancher plusieurs sorties sur un même tensor (architectures non-linéaires)

## Assembler le modèle
Syntaxe:
```
from keras import Model
model = **Model**(inputs=inputs, outputs=outputs)
```
Résultat: model se compile/entraîne ensuite exactement comme un Sequential (.compile(), .fit()...)

## Exposer la sortie de couches intermédiaires
Syntaxe: sub_model = Model(inputs=model.inputs, outputs=[l.output for l in model.layers])
Résultat: utile pour inspecter/visualiser ce qu'une couche a appris (ex: feature maps d'un CNN), sans ré-entraîner

## Modèle à PLUSIEURS entrées — fusionner deux branches
Syntaxe:
```
inputs_a = Input(shape=(60,))       # ex: branche texte
inputs_b = Input(shape=(18,))       # ex: branche tabulaire
...
combined = layers.**concatenate**([outputs_a, outputs_b])
x = layers.Dense(10, activation='relu')(combined)
outputs = layers.Dense(1, activation='linear')(x)
model = Model(inputs=[inputs_a, inputs_b], outputs=outputs)
```
Résultat: chaque branche a son propre Input et sa propre suite de couches ; concatenate() les fusionne en un seul tensor juste avant la tête commune

## Entraîner un modèle à plusieurs entrées
Syntaxe: model.fit(x=[X_a, X_b], y=y, validation_split=0.3, epochs=50)
Résultat: x = LISTE d'arrays (un par Input, dans le même ordre que inputs=[...] à la création du modèle), pas un seul array

## Visualiser l'architecture (utile si multi-branches)
Syntaxe: tf.keras.utils.**plot_model**(model, "model.png", show_shapes=True)
Résultat: alternative à model.summary() — un schéma est souvent plus lisible qu'un texte pour un modèle à plusieurs entrées/branches
