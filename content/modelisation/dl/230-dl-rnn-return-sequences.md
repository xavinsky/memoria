---
title: Sortie d'une couche RNN — return_sequences & stacking
subgroup: Modèles de base
subsubgroup: RNN
---

Par défaut, une couche RNN ne renvoie que l'état interne du DERNIER pas de temps ($y = h_n$) — un seul vecteur par séquence, quelle que soit sa longueur.

> [!WARNING]
> ⚠️ Ce vecteur de sortie n'est PAS directement la prédiction — c'est un résumé de taille $n_h$, passé ensuite à une couche Dense pour produire la vraie prédiction.

:::compare
- **return_sequences=False (défaut)** : une seule sortie par séquence (le dernier état) — adapté pour prédire UNE valeur future
- **return_sequences=True** : une sortie à CHAQUE pas de temps — nécessaire pour prédire une séquence complète, OU pour empiler une autre couche RNN par-dessus
:::

> [!TIP]
> 👉 Pour empiler plusieurs couches RNN, TOUTES sauf la DERNIÈRE doivent avoir `return_sequences=True` — sinon la couche suivante ne reçoit qu'un seul vecteur au lieu d'une séquence à traiter.
