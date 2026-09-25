---
title: Couche récurrente — SimpleRNN, LSTM, GRU
subgroup: Modèles de base
subsubgroup: RNN
type: syntax
---

## Ajouter une couche récurrente simple
Syntaxe: model.add(layers.**SimpleRNN**(units=10, activation='tanh'))
Résultat: units = n_h (taille de l'état interne / nombre de "mémoires" parallèles) — cf. page Modélisation ▸ [Sous le capot d'une couche RNN](#dl-rnn-mechanics)

## Variantes plus robustes au vanishing gradient
Syntaxe:
```
model.add(layers.**LSTM**(units=10))
model.add(layers.**GRU**(units=10))
```
Résultat: même syntaxe que SimpleRNN — cf. page Modélisation ▸ SimpleRNN, LSTM, GRU

## Préciser la forme d'entrée
Syntaxe: model.add(Input(shape=(n_observations, n_features)))
Résultat: shape = (longueur de séquence, nb de features par pas de temps) — PAS de dimension batch
