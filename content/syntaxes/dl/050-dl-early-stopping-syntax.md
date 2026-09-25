---
title: Early Stopping (callback)
subgroup: Keras
type: syntax
---

## Créer le callback
Syntaxe:
```
from tensorflow.keras.callbacks import EarlyStopping
es = **EarlyStopping**(patience=20, restore_best_weights=True)
```
Résultat: patience = nb d'epochs tolérées sans amélioration de la loss de validation avant d'arrêter — cf. page Modélisation ▸ [Early Stopping & jeu de validation](#dl-early-stopping)

## Fournir un jeu de validation explicite
Syntaxe: model.fit(X_train, y_train, validation_data=(X_val, y_val), callbacks=[es])
Résultat: alternative : validation_split=0.3 (prend les 30% DERNIERS indices du train, AVANT le shuffle — pas de fuite de données)

## Entraîner avec beaucoup d'epochs
Syntaxe: model.**fit**(X_train, y_train, epochs=1000, callbacks=[es])
Résultat: epochs volontairement élevé : c'est l'EarlyStopping qui arrête réellement l'entraînement, pas ce nombre

## Surveiller une autre métrique que la loss
Syntaxe: es = EarlyStopping(**monitor**='val_accuracy', patience=5, restore_best_weights=True)
Résultat: monitor='val_loss' par défaut — utile quand l'accuracy (ou une autre métrique) est plus pertinente que la loss pour juger de l'arrêt
