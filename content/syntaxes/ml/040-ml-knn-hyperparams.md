---
title: KNN — hyperparamètres
subgroup: Choix du modèle
type: syntax
---

## n_neighbors (K)
Syntaxe: KNeighborsClassifier(**n_neighbors**=5)
Résultat: nombre de voisins pris en compte — K petit → overfitting (sensible au bruit d'un seul point) ; K grand → underfitting (signal dilué parmi trop de voisins)

## weights
Syntaxe: KNeighborsClassifier(n_neighbors=5, **weights**="distance")
Résultat: uniform (défaut) : chaque voisin compte pareil, stable mais un voisin proche peut être noyé par des voisins lointains ; distance : les voisins proches comptent plus, plus réactif mais plus sensible à une exception proche

## p (distance utilisée)
Syntaxe: KNeighborsClassifier(n_neighbors=5, **p**=1)
Résultat: 2 (défaut) : distance euclidienne, frontières de décision lisses ; 1 : distance de Manhattan, frontières plus anguleuses mais plus rapide en grande dimension
