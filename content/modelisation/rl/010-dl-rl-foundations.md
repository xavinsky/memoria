---
title: Reinforcement Learning — composants & boucle
subgroup: Reinforcement Learning
---

Le **Reinforcement Learning (RL)** est une branche du ML où un **agent** apprend à prendre des décisions en interagissant avec un **environnement**, pour atteindre un objectif.

:::compare
- **Supervised Learning** : apprend à partir de données ÉTIQUETÉES (une bonne réponse connue pour chaque exemple)
- **Unsupervised Learning** : trouve des patterns dans des données NON étiquetées
- **Reinforcement Learning** : apprend par ESSAI-ERREUR pour maximiser une récompense — pas de "bonne réponse" donnée, seulement de l'expérience
:::

1. **Observe** : l'agent regarde l'état (state) actuel de l'environnement
2. **Act** : il choisit une action parmi celles disponibles
3. **Receive Reward** : l'environnement renvoie une récompense (positive ou négative)
4. **Learn** : l'agent met à jour sa stratégie en fonction du résultat
5. **Repeat** : la boucle recommence

La **policy** est la stratégie de l'agent — une fonction qui associe à chaque état la (ou les) action(s) à prendre. Un bon policy maximise la récompense cumulée sur le long terme, pas juste la récompense immédiate.
