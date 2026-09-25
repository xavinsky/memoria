---
title: Manipuler des tensors (équivalents Numpy)
subgroup: TensorFlow
type: syntax
---

## Créer un tensor constant
Syntaxe:
```
import tensorflow as tf
tf.**constant**([1, 2, 3])  # ou tf.ones((3,3)), tf.zeros((3,3))
```
Résultat: un tf.Tensor — équivalent de np.array()/np.ones()/np.zeros(), PAS un ndarray

## Reconvertir un tensor en tableau Numpy
Syntaxe: x.**numpy**()
Résultat: ndarray — pour inspecter/afficher un résultat EN DEHORS du graphe, jamais dans une loss/metric/layer custom (cf. page Modélisation ▸ Pourquoi tf.* et pas Numpy/Pandas)

## Élever au carré
Syntaxe: **tf**.square(x)
Résultat: équivalent de np.square(x) / x**2

## Valeur absolue
Syntaxe: **tf**.abs(x)
Résultat: équivalent de np.abs(x)

## Racine carrée
Syntaxe: **tf**.sqrt(x)
Résultat: équivalent de np.sqrt(x)

## Moyenne (réduit le tensor à un scalaire)
Syntaxe: **tf**.reduce_mean(x)
Résultat: équivalent de np.mean(x) — 'reduce' = agrège en réduisant une dimension du tensor

## Somme (réduit le tensor à un scalaire)
Syntaxe: **tf**.reduce_sum(x)
Résultat: équivalent de np.sum(x)

## Convertir un array/une liste en tensor
Syntaxe: tf.**convert_to_tensor**(array)  # ou tf.constant(liste)
Résultat: équivalent de np.array() — convert_to_tensor pour un array Numpy, constant pour une liste Python

## Changer le dtype
Syntaxe: tf.**cast**(tensor, dtype=tf.float32)
Résultat: équivalent de .astype() côté Numpy/Pandas

## Ajouter/reformer les dimensions
Syntaxe:
```
tf.**expand_dims**(x, axis=0)   # équivalent de np.expand_dims
tf.**reshape**(x, (1, 3, 3))     # équivalent de x.reshape(...)
```
Résultat: mêmes usages qu'en Numpy — utile pour ajouter la dimension batch/canal attendue par une couche

## Produit matriciel
Syntaxe: tf.**matmul**(a, b, transpose_b=True)
Résultat: équivalent de a @ b / np.matmul — transpose_a/transpose_b évitent un .T explicite avant l'appel

## Empiler / répéter des tensors
Syntaxe:
```
tf.**concat**([t1, t2], axis=0)   # équivalent de np.concatenate
tf.**tile**(t, [50, 1])            # répète t 50 fois sur l'axe 0
```
Résultat: concat assemble des tensors déjà existants ; tile répète UN SEUL tensor plusieurs fois
