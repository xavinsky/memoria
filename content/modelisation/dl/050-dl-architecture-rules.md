---
title: Construire l'architecture — règles de choix
subgroup: Fondamentaux
---

:::compare
- **Couche d'entrée (Input) — imposée par les données** : shape = nombre de features de X ; la préciser en amont permet à Keras d'allouer la mémoire et de construire le modèle immédiatement, plutôt que d'inférer la taille au premier batch vu
- **Couches cachées — expérimentation** : nombre de layers, nombre de neurones par layer : pas de règle fixe, relève de la pratique et de l'expérimentation (contrairement aux deux autres, dictées par le problème)
- **Dernière couche — imposée par la tâche** : nombre de neurones = dimension de la sortie attendue ; activation = dictée par le type de tâche (cf. tableau ci-dessous)
:::

| Tâche | Neurones (dernière couche) | Activation |
|---|---|---|
| Régression (1 valeur) | 1 | linear |
| Régression (k valeurs) | k | linear |
| Classification binaire | 1 | sigmoid |
| Classification multi-classe (k classes) | k | softmax |

> [!TIP]
> 👉 `model.summary()` affiche le détail des couches et le nombre de paramètres entraînables par couche — utile pour vérifier une architecture avant de l'entraîner (cf. page Syntaxes).

> [!TIP]
> 💡 `Sequential` suffit tant que l'architecture est une pile LINÉAIRE de couches (une entrée, une sortie, un seul chemin). Dès qu'il faut plusieurs entrées/sorties, ou faire converger plusieurs branches en parallèle vers un même point, il faut la **Functional API** (`Input` + appeler les couches comme des fonctions + `Model(inputs, outputs)`, cf. page Syntaxes) — plus verbeuse, mais qui autorise n'importe quel graphe de couches.

> [!WARNING]
> ⚠️ **Exception régression** : si la target ne peut être que POSITIVE (ex: un prix, une surface — jamais négative), préférer une dernière couche `'relu'` à `'linear'` — `'linear'` autorise des prédictions négatives, ce qui n'a pas de sens métier et peut fragiliser certaines loss (ex: MSLE, cf. [Loss Functions — régression](#ml-loss-functions), groupe ml, qui calcule un log et exige $\hat y \geq 0$).
