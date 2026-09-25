---
title: Sortie complète & stacking — return_sequences
subgroup: Modèles de base
subsubgroup: RNN
type: syntax
---

## Ne garder que le dernier état (défaut)
Syntaxe: layers.SimpleRNN(10)
Résultat: sortie = (batch, units) — 1 vecteur par séquence

## Garder la sortie à chaque pas de temps
Syntaxe: layers.SimpleRNN(10, **return_sequences**=True)
Résultat: sortie = (batch, n_observations, units) — nécessaire pour prédire une séquence ou empiler un autre RNN

## Empiler deux couches récurrentes
Syntaxe:
```
model.add(layers.SimpleRNN(10, return_sequences=True))
model.add(layers.SimpleRNN(3))
```
Résultat: return_sequences=True sur TOUTES les couches sauf la dernière — cf. page Modélisation ▸ Sortie d'une couche RNN
