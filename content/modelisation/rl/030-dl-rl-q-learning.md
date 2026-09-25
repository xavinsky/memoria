---
title: Q-Learning — apprendre la valeur d'une action
subgroup: Reinforcement Learning
---

Une **Value Function** estime à quel point une situation ou une décision est bonne :

:::compare
- **V(s) — State Value Function** : à quel point est-il bon d'être dans l'état s ?
- **Q(s,a) — State-Action Value Function** : à quel point est-il bon de prendre l'action a dans l'état s ? (Q = Quality)
:::

Si l'agent connaissait Q pour toute paire (état, action), sa policy serait triviale : toujours choisir l'action de plus haut Q. Le **Q-Learning** apprend cette fonction en construisant une **Q-table**, mise à jour à chaque interaction via l'**équation de Bellman** :

```math
Q(s,a) \leftarrow Q(s,a) + \alpha\Big[R(s,a) + \gamma \max_{a'} Q(s',a') - Q(s,a)\Big]
```

$\alpha$ (learning rate) contrôle l'ampleur de la mise à jour (haut = rapide mais instable, bas = stable mais lent) ; $\gamma$ (discount factor, < 1) pondère les récompenses futures par rapport à l'immédiate (proche de 1 = vision long terme, proche de 0 = récompense immédiate priorisée).

> [!WARNING]
> ⚠️ La Q-table grandit avec le nombre d'états × d'actions — impraticable pour des environnements grands ou continus (ex: des pixels d'image). Adapté seulement aux petits environnements discrets.

> [!TIP]
> 👉 Implémentation "à la main" (sans bibliothèque RL) — cf. page Syntaxes ▸ Q-Learning manuel.
