---
title: Data Augmentation — ImageDataGenerator
subgroup: Modèles de base
subsubgroup: CNN
type: syntax
---

## Définir les transformations
Syntaxe:
```
from keras.preprocessing.image import ImageDataGenerator
datagen = **ImageDataGenerator**(rotation_range=20, width_shift_range=0.1, zoom_range=0.1, horizontal_flip=True)
datagen.fit(X_train)
```
Résultat: chaque paramètre active un type de variation aléatoire ; .fit() calcule les stats nécessaires (ex: pour un centrage) sur X_train

## Entraîner sur le flux augmenté
Syntaxe:
```
train_flow = datagen.**flow**(X_train, y_train, batch_size=64)
model.fit(train_flow, validation_data=(X_val, y_val), epochs=50)
```
Résultat: validation_data OBLIGATOIRE ici (validation_split impossible avec un flow) — cf. page Modélisation ▸ [Data Augmentation](#dl-cnn-data-augmentation) ; le split train/val doit être fait AVANT d'appeler flow()

## Alternative — augmentation intégrée au modèle (couches)
Syntaxe:
```
model.add(layers.**RandomFlip**('horizontal'))
model.add(layers.**RandomZoom**(0.1))
model.add(layers.**RandomRotation**(0.1))
```
Résultat: ajoutées juste après Rescaling ; actives UNIQUEMENT pendant model.fit() (comme Dropout), inactives à l'inférence — mêmes avantages que Normalization intégrée (cf. page Syntaxes ▸ Preprocessing intégré au modèle) : pas de logique séparée à maintenir
