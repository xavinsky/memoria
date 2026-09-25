---
title: Réentraînement final & prédiction sur nouvelle donnée
subgroup: Prédictions
type: syntax
---

## Réentraîner sur l'ensemble des données
Syntaxe: model.**fit**(X, y)  # X, y = dataset complet, pas X_train/y_train
Résultat: remplace le modèle entraîné sur X_train par un modèle entraîné sur toutes les données disponibles

## Prédire sur une donnée nouvelle
Syntaxe:
```
new_point_scaled = scaler.transform(new_point)
model.**predict**(new_point_scaled)
```
Résultat: ne jamais oublier de réappliquer le même preprocessing (scaler déjà fit pendant l'étape Test, jamais refit) aux nouvelles données avant de prédire
