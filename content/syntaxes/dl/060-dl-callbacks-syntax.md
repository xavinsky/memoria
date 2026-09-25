---
title: Autres callbacks — ModelCheckpoint, ReduceLROnPlateau
subgroup: Keras
type: syntax
---

## Sauvegarder automatiquement le meilleur modèle
Syntaxe:
```
from keras.callbacks import ModelCheckpoint
mc = **ModelCheckpoint**('best_model.keras', monitor='val_loss', save_best_only=True)
```
Résultat: écrit sur disque à CHAQUE amélioration de val_loss pendant l'entraînement — utile pour ne rien perdre même si l'entraînement est interrompu

## Réduire le learning rate quand la loss stagne
Syntaxe:
```
from keras.callbacks import ReduceLROnPlateau
rlr = **ReduceLROnPlateau**(monitor='val_loss', factor=0.1, patience=3)
```
Résultat: si val_loss ne s'améliore plus pendant patience epochs, multiplie le learning rate par factor — alternative/complément à un scheduler fixe (cf. page Modélisation ▸ Hyperparamètres)

## Combiner plusieurs callbacks
Syntaxe: model.fit(X_train, y_train, validation_data=(X_val, y_val), callbacks=[es, mc, rlr])
Résultat: tous les callbacks passés dans la liste s'exécutent en parallèle, chacun à sa propre logique

## Suivre l'entraînement visuellement — TensorBoard
Syntaxe:
```
from keras.callbacks import TensorBoard
tb = **TensorBoard**(log_dir='logs/fit', histogram_freq=1)
model.fit(X_train, y_train, callbacks=[tb])
# puis, dans le notebook :
%load_ext tensorboard
%tensorboard --logdir logs/fit
```
Résultat: écrit les métriques à chaque epoch dans log_dir ; l'interface TensorBoard permet de suivre/comparer plusieurs entraînements en direct
