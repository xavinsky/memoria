---
title: Q-Learning manuel — Q-table avec NumPy
subgroup: Reinforcement Learning
type: syntax
---

## Initialiser la Q-table
Syntaxe: q = np.**zeros**((env.observation_space.n, env.action_space.n))
Résultat: une ligne par état, une colonne par action — toutes les valeurs Q(s,a) partent à 0, l'agent n'a encore rien appris

## Choisir une action — epsilon-greedy
Syntaxe:
```
if np.random.random() < epsilon:
    action = env.action_space.sample()  # explore
else:
    action = np.**argmax**(q[state, :])  # exploite
```
Résultat: cf. page Modélisation ▸ Exploration vs Exploitation ; np.argmax = indice de l'action à la plus haute valeur Q connue pour cet état

## Mettre à jour la Q-table — équation de Bellman
Syntaxe:
```
q[state, action] += learning_rate * (
    reward + discount_factor * np.**max**(q[new_state, :]) - q[state, action]
)
```
Résultat: traduction directe de la formule Q(s,a) ← Q(s,a) + α[R + γ·maxQ(s',a') − Q(s,a)] — cf. page Modélisation ▸ Q-Learning

## Décroître epsilon au fil des épisodes
Syntaxe: epsilon = max(epsilon - epsilon_decay, 0)
Résultat: explore moins et exploite davantage à mesure que l'agent apprend — jamais en dessous de 0
