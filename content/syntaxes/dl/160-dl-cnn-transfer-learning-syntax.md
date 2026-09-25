---
title: Transfer Learning — charger & greffer un modèle pré-entraîné
subgroup: Modèles de base
subsubgroup: CNN
type: syntax
---

## Charger un modèle pré-entraîné sans sa tête
Syntaxe:
```
from keras.applications.vgg16 import VGG16
base_model = **VGG16**(weights='imagenet', include_top=False, input_shape=(256, 256, 3))
```
Résultat: include_top=False retire les couches Dense de classification d'origine (spécifiques à ImageNet) — ne garde que les couches de convolution

## Geler ses poids
Syntaxe: base_model.**trainable** = False
Résultat: empêche ces couches d'être mises à jour pendant model.fit() — cf. page Modélisation ▸ Architecture typique &amp; Transfer Learning

## Greffer de nouvelles couches par-dessus
Syntaxe:
```
model = Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(500, activation='relu'),
    layers.Dense(num_classes, activation='softmax'),
])
```
Résultat: un modèle pré-entraîné entier peut être passé comme premier élément de la forme liste de Sequential, exactement comme une couche normale

## Preprocessing spécifique au modèle pré-entraîné
Syntaxe:
```
from keras.applications.vgg16 import preprocess_input
X_train_vgg = **preprocess_input**(X_train)
```
Résultat: chaque modèle pré-entraîné attend un preprocessing précis (ici : centrage RGB selon les stats ImageNet) — PAS le /255 habituel ; alternative : l'insérer comme couche via layers.Lambda(preprocess_input) dans le Sequential

## Learning rate réduit pour le fine-tuning
Syntaxe: model.compile(optimizer=optimizers.Adam(learning_rate=**1e-4**), loss='categorical_crossentropy')
Résultat: plus faible que le défaut d'Adam (1e-3) — on ne veut ajuster les nouvelles couches qu'en douceur
