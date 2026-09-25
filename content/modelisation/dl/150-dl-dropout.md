---
title: Dropout
subgroup: Régularisation
---

[[P:Dropout]]

À CHAQUE itération d'entraînement, le Dropout "tue" (=0) aléatoirement l'activité d'une fraction des neurones d'une couche — ces neurones ne participent pas à la prédiction ni à la mise à jour des poids pour cette itération.

Empêche un neurone de se sur-spécialiser sur un pattern particulier de l'input — force le réseau à répartir l'information sur plusieurs neurones, donc à mieux généraliser.

> [!TIP]
> 👉 Le Dropout n'est actif que PENDANT l'entraînement, jamais lors de `.predict()`/`.evaluate()` — et il n'ajoute lui non plus aucun paramètre entraînable (`rate` = pourcentage de neurones tués, ex: 0.2).
