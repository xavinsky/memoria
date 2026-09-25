---
title: Matplotlib — quadrillage de sous-graphiques
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Grille de sous-graphiques (lignes, colonnes, position)
Syntaxe: plt.**subplot**(2, 2, 1)
Params: -
Explication: sélectionne le 1er graphique d'une grille 2x2 — les plt.plot suivants s'y appliquent

## Créer une grille de sous-graphiques indépendants (objets Axes)
Syntaxe:
```
fig, axes = plt.**subplots**(nrows=2, ncols=3, figsize=(15, 10))
# cas le plus courant, 2 côte à côte :
fig, (ax1, ax2) = plt.**subplots**(1, 2, figsize=(12, 5))
ax1.bar(x, y)
ax2.scatter(x, y)
```
Params: -
Explication:
```
fig = la figure entière, axes = tableau 2D d'objets Axes (ou directement (ax1, ax2) si on dépaquette 1x2)
figsize=(largeur, hauteur) en pouces — ex: (12, 5) = plus large que haut, adapté à 2 graphiques côte à côte
```

## Parcourir tous les axes d'une grille
Syntaxe:
```
for ax in axes.**flat**:
    ...
```
Params: -
Explication: aplatit le tableau 2D d'axes en liste 1D pour boucler dessus

## Configurer un axe précis (titre, limites)
Syntaxe:
```
ax.**set_title**(f"n={n}")
ax.**set_xlim**(0, 40)
```
Params: -
Explication: équivalent de plt.title / plt.xlim mais appliqué à un axe particulier de la grille

## Deuxième axe Y (échelles très différentes sur le même graphe)
Syntaxe:
```
fig, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(x, commandes, color="tab:blue")
ax2 = ax1.**twinx**()
ax2.plot(x, paiements, color="tab:orange")
# fusionner les 2 légendes
l1, la1 = ax1.get_legend_handles_labels()
l2, la2 = ax2.get_legend_handles_labels()
ax1.legend(l1+l2, la1+la2)
```
Params: -
Explication: twinx() crée un 2ᵉ axe Y partageant le même axe X — indispensable quand deux séries ont des échelles trop différentes pour partager un axe (sinon l'une s'écrase en ligne plate) ; chaque axe garde sa propre légende, à fusionner manuellement pour n'en afficher qu'une
