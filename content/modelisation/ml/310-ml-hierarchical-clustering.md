---
title: Clustering Hiérarchique — dendrogramme
subgroup: Modèles
---

Alternative à K-Means qui ne demande pas de fixer K à l'avance : construit un ARBRE de fusions successives (bottom-up), qu'on peut ensuite "couper" à la hauteur voulue pour obtenir le nombre de clusters souhaité.

1. Chaque observation démarre dans son PROPRE cluster
2. Fusionner les deux clusters les plus proches (selon un critère de linkage) en un seul
3. Répéter jusqu'à ce qu'il ne reste qu'un seul cluster englobant tout

**Linkage de Ward** (le plus courant) : fusionne à chaque étape les deux clusters dont la fusion minimise l'AUGMENTATION de la variance intra-cluster totale — même objectif que l'inertia de K-Means (cf. ci-dessus), juste construit de façon ascendante/hiérarchique plutôt qu'itérative.

Le résultat se lit sur un **dendrogramme** : chaque fusion est une branche, sa hauteur = la distance à laquelle les deux clusters ont été unis. Couper l'arbre à une hauteur donnée (ligne horizontale) donne directement le nombre de clusters à cette hauteur — pas besoin de relancer l'algorithme pour tester un autre K, contrairement à K-Means.

> [!WARNING]
> ⚠️ Algorithme **glouton (greedy)** : une fusion faite tôt n'est jamais remise en cause ensuite — peut tomber dans un optimum local, contrairement à une exploration plus globale.
