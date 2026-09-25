---
title: Sous le capot d'une couche RNN
subgroup: Modèles de base
subsubgroup: RNN
---

Une couche RNN traite les observations d'une séquence UNE À LA FOIS, dans l'ordre temporel, en maintenant un **état interne** (hidden state) $h$ qui résume ce qu'elle a vu jusque-là.

```math
h^{(t)} = f_W\big(h^{(t-1)},\ x^{(t)}\big)
```

1. Initialiser l'état interne $h_0$ (vecteur nul)
2. À chaque pas de temps $t$ : combiner l'état précédent $h^{(t-1)}$ et l'observation courante $x^{(t)}$ via les MÊMES poids $W$ pour produire le nouvel état $h^{(t)}$
3. Répéter jusqu'au dernier pas de temps de la séquence

Les mêmes poids $W$ sont réutilisés à CHAQUE pas de temps (contrairement à un réseau Dense où chaque couche a ses propres poids) — c'est ce partage qui permet à un RNN de traiter des séquences de longueur arbitraire avec un nombre de paramètres FIXE.

```math
n_{param} = n_h(n_h + n_x + 1)
```

$n_h$ = nombre d'unités de la couche (taille de l'état interne), $n_x$ = nombre de features par pas de temps — indépendant de la longueur de la séquence.
