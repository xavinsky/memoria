---
title: Historique d'entraînement — History
subgroup: Keras
type: syntax
---

## Récupérer l'historique d'entraînement
Syntaxe: history = model.**fit**(X_train, y_train, epochs=100)
Résultat: le retour de .fit() est un objet History — history.history est un dict {"loss": [...], "accuracy": [...]}, une valeur par epoch

## Tracer la courbe de loss
Syntaxe: plt.plot(history.history['**loss**'])
Résultat: clé toujours présente, quelle que soit la tâche

## Comparer train vs validation
Syntaxe:
```
model.fit(X_train, y_train, **validation_data**=(X_val, y_val), epochs=100)
plt.plot(history.history['loss']); plt.plot(history.history['**val_loss**'])
```
Résultat: les clés val_* n'existent QUE si validation_data (ou validation_split) est passé à .fit() — mêmes clés pour une métrique : val_accuracy, etc.
