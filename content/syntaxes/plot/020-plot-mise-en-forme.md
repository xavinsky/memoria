---
title: Matplotlib — mise en forme
type: syntax
---

## Définir la taille de la figure
Syntaxe: plt.**figure**(figsize=(20, 10))
Résultat: figure plus grande (largeur, hauteur en pouces)

## Titre du graphique
Syntaxe: plt.**title**("mon titre")
Résultat: -

## Titre au-dessus de toute la figure (utile avec plt.subplot)
Syntaxe: plt.**suptitle**("mon titre global")
Résultat: -

## Titres des axes
Syntaxe:
```
plt.**xlabel**("x")
plt.**ylabel**("y")
```
Résultat: -

## Limiter un axe pour masquer des outliers (un seul côté possible)
Syntaxe:
```
plt.**xlim**(right=70)
plt.**ylim**(bottom=0)
```
Résultat: tronque la vue sans modifier les données — right=/left=/top=/bottom= bornent un seul côté, l'autre reste automatique

## Afficher la légende (labels définis dans bar/scatter/plot)
Syntaxe: plt.**legend**(loc="best")
Résultat: légende positionnée automatiquement
