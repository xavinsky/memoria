---
title: Une image (ou un son) est un tableau NumPy
type: syntax
---

## Charger un tableau sauvegardé (.npy)
Syntaxe: array = **np.load**("fichier.npy")
Résultat: recharge un array NumPy tel quel (dtype/shape préservés) — plus rapide qu'un CSV pour de gros tableaux numériques

## Deviner ce qu'un array représente
Syntaxe: array.ndim, array.shape, array.dtype
Résultat: 1D + valeurs ±grandes = son ; 2D 0-255 = image niveaux de gris ; 3D avec 3/4 canaux = image RGB/RGBA ; 4D = suite d'images (vidéo/animation)

## Afficher une image (tableau 2D ou 3D)
Syntaxe:
```
plt.**imshow**(array, cmap="gray")
plt.axis("off")
```
Résultat: cmap="gray" obligatoire pour une image 2D en niveaux de gris (sinon fausses couleurs par défaut) ; ignoré si l'array a déjà 3 canaux (RGB)

## Sauvegarder un array comme image
Syntaxe: plt.**imsave**("out.png", array, cmap="gray")
Résultat: PNG (pas JPEG) si l'array a un canal alpha (RGBA, transparence) — JPEG ne supporte pas la transparence

## Isoler une portion / sous-échantillonner
Syntaxe:
```
crop = array[:500, :500]
sous_ech = array[::3, ::3]
```
Résultat: slicing 2D classique — un pas (`::3`) sous-échantillonne 1 pixel sur 3 dans chaque dimension, réduit la résolution sans redimensionner
