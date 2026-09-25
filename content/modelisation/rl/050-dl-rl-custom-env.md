---
title: Créer son propre environnement Gymnasium
subgroup: Reinforcement Learning
---

Pour entraîner un agent sur une tâche qui n'existe pas déjà dans le catalogue Gymnasium (cf. page Syntaxes), on définit son propre environnement en sous-classant `gym.Env` — l'agent (DQN, Stable Baselines3...) l'utilise ensuite exactement comme un environnement prêt à l'emploi.

1. **Définir les espaces** dans `__init__` : `action_space` (les actions possibles) et `observation_space` (la forme d'une observation) — `Discrete(n)` pour un choix parmi n valeurs, `Box(low, high, shape)` pour un vecteur borné, `Dict({...})` pour combiner plusieurs sous-espaces (ex: position de l'agent + position de la cible)
2. **`reset(seed, options)`** : réinitialise l'état interne à chaque nouvel épisode, renvoie `(observation, info)`
3. **`step(action)`** : applique l'action, calcule la récompense et si l'épisode est terminé, renvoie `(observation, reward, terminated, truncated, info)` — même signature qu'un environnement Gymnasium natif
4. **`render()`** (optionnel) : affichage visuel de l'état courant, pour debug/démo

> [!WARNING]
> ⚠️ Si `observation_space` est un `Dict` (plusieurs entrées combinées), la policy `"MlpPolicy"` (réseau Dense classique, cf. DQN ci-dessus) ne fonctionne PAS — elle lève une `ValueError`. Utiliser `"MultiInputPolicy"` à la place, qui sait traiter une observation composée de plusieurs sous-tableaux.

> [!TIP]
> 👉 Un `VecEnv` (`make_vec_env`/`DummyVecEnv`) fait un AUTO-RESET silencieux dès que `done=True` : l'`observation` renvoyée par `.step()` appartient déjà au NOUVEL épisode, alors que `reward`/`done`/`info` décrivent encore l'ancien — l'observation réellement terminale reste accessible dans `info[0]['terminal_observation']`.
