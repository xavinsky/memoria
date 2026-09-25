---
title: Création de tableaux
type: syntax
---

## Créer un tableau à partir d'une liste
Syntaxe: **np.array**([1, 2, 3])
Résultat: array([1, 2, 3])

## Tableau de zéros
Syntaxe: **np.zeros**((3, 4))
Résultat: matrice 3x4 remplie de 0

## Tableau de uns
Syntaxe: **np.ones**((2, 2))
Résultat: matrice 2x2 remplie de 1

## Matrice identité
Syntaxe: **np.eye**(3)
Résultat: matrice 3x3 avec des 1 sur la diagonale, 0 ailleurs

## Suite régulière (début, fin, pas)
Syntaxe: **np.arange**(0, 10, 2)
Résultat: array([0, 2, 4, 6, 8])

## N valeurs régulières entre deux bornes
Syntaxe: **np.linspace**(0, 1, 5)
Résultat: array([0., 0.25, 0.5, 0.75, 1.])

## Tableau aléatoire uniforme [0,1)
Syntaxe: **np.random.rand**(3, 3)
Résultat: matrice 3x3 de floats aléatoires

## Tableau d'entiers aléatoires
Syntaxe: **np.random.randint**(0, 10, size=(2, 3))
Résultat: matrice 2x3 d'entiers entre 0 et 9
