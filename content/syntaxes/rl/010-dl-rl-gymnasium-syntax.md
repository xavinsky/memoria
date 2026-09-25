---
title: Gymnasium — créer & piloter un environnement
subgroup: Reinforcement Learning
type: syntax
---

## Créer un environnement
Syntaxe:
```
import gymnasium as gym
env = gym.**make**('FrozenLake-v1', is_slippery=False)
```
Résultat: catalogue d'environnements prêts à l'emploi (grilles, Atari, contrôle continu...)

## Démarrer un épisode
Syntaxe: state, info = env.**reset**()
Résultat: renvoie l'état initial — à appeler au début de chaque épisode

## Échantillonner une action aléatoire
Syntaxe: action = env.action_space.**sample**()
Résultat: utile pour explorer, notamment en tout début d'entraînement

## Exécuter une action
Syntaxe: next_state, reward, terminated, truncated, info = env.**step**(action)
Résultat: terminated = objectif atteint/échoué ; truncated = arrêt anticipé (ex: limite de temps) — cf. page Modélisation ▸ Reinforcement Learning — composants &amp; boucle

## Afficher l'environnement visuellement
Syntaxe: env.**render**()
Résultat: nécessite render_mode="human" passé à gym.make() — inutile (et ralentit beaucoup) pendant un entraînement, à réserver pour observer/déboguer un agent

## Libérer l'environnement
Syntaxe: env.**close**()
Résultat: surtout utile avec du rendering ou plusieurs environnements en parallèle
