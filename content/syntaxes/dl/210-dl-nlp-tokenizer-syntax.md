---
title: Tokenizer — mots vers entiers
subgroup: LLM
subsubgroup: NLP
type: syntax
---

## Construire le vocabulaire (mots → entiers)
Syntaxe:
```
from tensorflow.keras.preprocessing.text import Tokenizer
tk = Tokenizer()
tk.**fit_on_texts**(X)
```
Résultat: équivalent d'un .fit() Sklearn — construit le dictionnaire mot→entier à partir du corpus

## Convertir les phrases en séquences d'entiers
Syntaxe: X_token = tk.**texts_to_sequences**(X)
Résultat: équivalent d'un .transform() — remplace chaque mot par son entier

## Uniformiser la longueur des séquences
Syntaxe:
```
from tensorflow.keras.preprocessing.sequence import pad_sequences
X_pad = **pad_sequences**(X_token, padding='post')
```
Résultat: même logique que pour un RNN classique — cf. page Modélisation ▸ Séquences de longueurs différentes (groupe RNN)

## Plafonner la longueur (accélère l'entraînement)
Syntaxe: X_pad = pad_sequences(X_token, padding='post', **maxlen**=200)
Résultat: sans maxlen, TOUTES les séquences sont paddées à la longueur de la plus longue phrase du corpus — souvent démesurée à cause de quelques outliers ; tronquer à une longueur raisonnable réduit fortement le temps d'entraînement, pour une perte de performance généralement négligeable

## Alternative — tokenisation intégrée au modèle
Syntaxe:
```
from keras.layers import TextVectorization
vec = **TextVectorization**(standardize='lower', output_mode='int', output_sequence_length=200)
vec.adapt(X)
model.add(vec)
```
Résultat: même logique que Normalization/Rescaling intégrées (cf. page Syntaxes ▸ Preprocessing intégré au modèle) : combine Tokenizer + pad_sequences en UNE couche, fait partie du modèle sauvegardé
