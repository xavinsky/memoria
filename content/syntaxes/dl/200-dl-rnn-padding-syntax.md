---
title: Séquences de longueurs différentes — padding & Masking
subgroup: Modèles de base
subsubgroup: RNN
type: syntax
---

## Uniformiser la longueur des séquences
Syntaxe:
```
from tensorflow.keras.preprocessing.sequence import pad_sequences
X_pad = **pad_sequences**(X, dtype='float32', padding='post', value=-1000)
```
Résultat: padding='post' = ajoute le padding à LA FIN (recommandé) ; value = valeur absente des vraies données

## Ignorer le padding pendant l'entraînement
Syntaxe: model.add(layers.**Masking**(mask_value=-1000))
Résultat: 1ère couche du modèle — même valeur que celle utilisée dans pad_sequences
