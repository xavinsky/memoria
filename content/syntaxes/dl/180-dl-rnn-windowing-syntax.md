---
title: Fenêtrage — transformer une série en séquences
subgroup: Modèles de base
subsubgroup: RNN
type: syntax
---

## Construire (X, y) par fenêtres glissantes
Syntaxe:
```
sequence_length = 7
X, y = [], []
for i in range(len(series) - sequence_length):
    X.append(series[i:i+sequence_length])
    y.append(series[i+sequence_length])
X, y = np.array(X), np.array(y)
```
Résultat: chaque fenêtre de sequence_length observations consécutives devient une séquence d'entrée ; l'observation suivante devient sa cible — cf. page Modélisation ▸ Pourquoi un RNN

## Ajouter la dimension features (univarié)
Syntaxe: X = X.reshape(X.shape[0], X.shape[1], **1**)
Résultat: passe de (n_sequences, n_observations) à (n_sequences, n_observations, 1) — 1 seule feature observée par pas de temps
