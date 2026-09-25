---
title: Sauvegarder & charger un modèle
subgroup: Keras
type: syntax
---

## Sauvegarder un modèle entraîné
Syntaxe:
```
from tensorflow.keras import models
models.**save_model**(model, 'my_model.keras')
```
Résultat: format .keras (Keras 3) — indispensable pour partager/déployer un modèle sans le ré-entraîner

## Charger un modèle sauvegardé
Syntaxe: loaded_model = models.**load_model**('my_model.keras')
Résultat: renvoie un modèle directement utilisable avec .predict()/.evaluate()

## Sauvegarder/charger UNIQUEMENT les poids
Syntaxe:
```
model.**save_weights**('weights.h5')
model.**load_weights**('weights.h5')
```
Résultat: fichier plus léger (pas l'architecture) — il faut redéfinir/reconstruire le même modèle avant de charger les poids dedans
