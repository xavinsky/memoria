---
title: Charger un gros dataset — tf.data.Dataset
subgroup: Keras
type: syntax
---

## Charger des images depuis un dossier, batch par batch
Syntaxe:
```
from tensorflow.keras.utils import image_dataset_from_directory
ds = **image_dataset_from_directory**(data_dir, batch_size=32)
```
Résultat: les classes sont inférées automatiquement depuis la structure des sous-dossiers ; les images ne sont chargées en RAM qu'au moment de leur utilisation, pas toutes d'un coup

## Entraîner directement sur le Dataset
Syntaxe: model.**fit**(ds, epochs=10)
Résultat: pas besoin de X_train/y_train séparés — Keras itère lui-même sur ds batch par batch

## Construire un Dataset à partir d'un array/tensor
Syntaxe: ds = tf.data.Dataset.**from_tensor_slices**(array)
Résultat: point de départ générique (pas seulement des images) — ex: un long texte encodé en entiers, un array Numpy...

## Chaîner les opérations (shuffle, batch, prefetch)
Syntaxe:
```
ds = (ds
    .**shuffle**(buffer_size=10000)
    .**batch**(64, drop_remainder=True)
    .**prefetch**(tf.data.AUTOTUNE))
```
Résultat: shuffle = mélange par blocs de buffer_size (pas tout le dataset d'un coup) ; prefetch prépare le batch suivant PENDANT que le GPU traite le batch courant
