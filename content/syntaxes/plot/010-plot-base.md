---
title: Matplotlib — graphiques de base
type: syntax
---

## Importer matplotlib
Syntaxe: import **matplotlib.pyplot** as plt
Résultat: -

## Diagramme en barres
Syntaxe: plt.**bar**(x, y)
Résultat: graphique à barres

## Nuage de points
Syntaxe: plt.**scatter**(x=x, y=y, label="...", s=8)
Résultat: nuage de points, s = taille des points

## Courbe / ligne
Syntaxe: plt.**plot**(x, y, label="...", color="red")
Résultat: courbe reliant les points

## Ligne horizontale constante (ex: valeur théorique)
Syntaxe: plt.**plot**([valeur] * len(y), label="...", color="red")
Résultat: ligne droite horizontale à hauteur 'valeur'

## Afficher le graphique
Syntaxe: plt.**show**()
Résultat: affiche la figure à l'écran

## Tracer directement depuis une Series/DataFrame (sans passer par plt.bar/scatter)
Syntaxe: serie.**plot**(kind="barh")
Résultat: graphique en barres horizontales — pratique pour trier et visualiser des coefficients de régression (model.params.sort_values().plot(kind="barh")) ou toute autre Series
