---
title: Contrôler la génération — Temperature, Top-k, Top-p
subgroup: LLM
subsubgroup: Transformers
---

Un modèle decoder-only choisit toujours son prochain token en fonction des probabilités du dernier softmax — ces paramètres contrôlent COMMENT ce token est choisi parmi ces probabilités, pas le modèle lui-même.

:::compare
- **Temperature** : contrôle le hasard du choix : basse = déterministe/répétitif, haute = créatif/aléatoire (typiquement entre 0 et 1 ou 2)
- **Top-k** : ne considère que les k tokens les plus probables, même s'ils cumulent une faible probabilité totale
- **Top-p (nucleus sampling)** : considère les tokens les plus probables jusqu'à cumuler une probabilité p, quel que soit leur nombre
- **Max tokens** : longueur maximale de la génération — arrête la génération, même en plein milieu d'une phrase
:::
