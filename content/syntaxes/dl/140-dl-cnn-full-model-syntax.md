---
title: 'Modèle CNN complet (ex: MNIST)'
subgroup: Modèles de base
subsubgroup: CNN
type: syntax
---

## Architecture — convolutions + pooling puis Dense
Syntaxe:
```
model = Sequential([
    Input(shape=(28, 28, 1)),
    layers.**Rescaling**(scale=1./255.),
    layers.Conv2D(16, (3, 3), padding='same', activation='relu'),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Conv2D(32, (2, 2), padding='same', activation='relu'),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.**Flatten**(),
    layers.Dense(50, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax'),
])
```
Résultat: Rescaling intégré au modèle (cf. page Syntaxes ▸ Preprocessing intégré au modèle) ; Flatten uniquement à la FIN, juste avant les couches Dense ; kernel_size decroît / filtres augmentent en profondeur — cf. page Modélisation ▸ [Architecture typique & Transfer Learning](#dl-cnn-transfer-learning)

## Compiler sans One-Hot Encoder la target
Syntaxe: model.compile(loss='**sparse_categorical_crossentropy**', optimizer='adam', metrics=['accuracy'])
Résultat: équivalent de categorical_crossentropy + to_categorical(y), mais prend directement des labels entiers (0,1,2...) en target
