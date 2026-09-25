---
title: Deep Q-Network (DQN) — dépasser la Q-table
subgroup: Reinforcement Learning
---

Le **DQN** remplace la Q-table par un RÉSEAU DE NEURONES : au lieu de stocker une valeur Q par paire (état, action) dans un tableau, le réseau prend un état en entrée et prédit directement les Q-values de toutes les actions possibles — exactement comme un CNN peut estimer un état à partir d'une image brute (cf. groupe CNN).

:::compare
- **Q-Learning (table)** : traite chaque état séparément — ingérable pour de grands espaces d'états (ex: pixels)
- **DQN (réseau de neurones)** : généralise entre états similaires — passe à l'échelle sur des environnements complexes (jeux vidéo, robotique)
:::

> [!TIP]
> 👉 Au-delà du DQN, d'autres familles d'algorithmes existent (Policy Gradient, PPO, A2C...) — cf. bibliothèques Gymnasium (environnements) et Stable Baselines3 (algorithmes), page Syntaxes.

:::compare
- **DQN — value-based** : apprend la Q-value de chaque action puis en déduit la policy (toujours la meilleure) — fiable et efficace en données (experience replay, target network), mais limité aux espaces d'ACTIONS DISCRÈTES (un nombre fini de choix)
- **PPO — policy-based (Policy Gradient)** : ajuste la policy DIRECTEMENT et progressivement (avec un clipping qui limite l'ampleur des mises à jour) — seul choix pour des actions CONTINUES (ex: angle de direction, force appliquée), et progresse plus régulièrement dès le début sur des tâches complexes
:::
