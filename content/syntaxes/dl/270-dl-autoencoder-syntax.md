---
title: Construire un Autoencoder
subgroup: LLM
subsubgroup: Autoencoder
type: syntax
---

## Décodeur — upsampling avec Conv2DTranspose
Syntaxe:
```
from keras.layers import Conv2DTranspose, Reshape
decoder = Sequential([
    layers.Dense(7*7*8, activation='tanh'),
    Reshape((7, 7, 8)),
    **Conv2DTranspose**(8, (2,2), strides=2, padding='same', activation='relu'),
    Conv2DTranspose(1, (2,2), strides=2, padding='same', activation='relu'),
])
```
Résultat: strides=2 double la taille spatiale à chaque couche (7→14→28) — inverse d'un MaxPooling2D, cf. page Modélisation ▸ Conv2DTranspose

## Assembler encodeur + décodeur
Syntaxe:
```
from keras import Model
inputs = Input(shape=(28, 28, 1))
outputs = decoder(encoder(inputs))
autoencoder = **Model**(inputs, outputs)
```
Résultat: Functional API (cf. page Syntaxes ▸ Architectures non-linéaires) — encoder et decoder restent utilisables séparément après coup

## Entraîner — la target EST l'input
Syntaxe:
```
autoencoder.compile(loss='mse', optimizer='adam')
autoencoder.fit(**X_train, X_train**, epochs=20)
```
Résultat: pas de label externe ; pour du débruitage : fit(X_train_noisy, X_train) — entrée bruitée, target propre

## Encoder seul — obtenir la représentation compressée
Syntaxe: X_encoded = encoder.**predict**(X_train)
Résultat: ex: (60000, 28, 28, 1) → (60000, 2) — chaque image compressée en 2 valeurs
