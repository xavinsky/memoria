---
title: Créer un environnement Gymnasium personnalisé
subgroup: Reinforcement Learning
type: syntax
---

## Définir l'espace d'actions/d'observation
Syntaxe:
```
from gymnasium import spaces
self.action_space = spaces.**Discrete**(4)
self.observation_space = spaces.**Box**(low=0, high=self.size-1, shape=(2,), dtype=np.int32)
```
Résultat: Discrete = choix parmi n valeurs (ex: 4 directions) ; Box = vecteur continu/discret borné ; Dict = combiner plusieurs sous-espaces (ligne suivante)

## Combiner plusieurs observations
Syntaxe:
```
self.observation_space = spaces.**Dict**({
    "agent": spaces.Box(low=0, high=self.size-1, shape=(2,), dtype=np.int32),
    "target": spaces.Box(low=0, high=self.size-1, shape=(2,), dtype=np.int32),
})
```
Résultat: observation = dict {"agent": [...], "target": [...]} — cf. note Modélisation sur MultiInputPolicy

## Sous-classer gym.Env
Syntaxe:
```
class CustomGridEnv(**gym.Env**):
    def reset(self, seed=None, options=None):
        ...
        return observation, info

    def step(self, action):
        ...
        return observation, reward, terminated, truncated, info
```
Résultat: même signature reset()/step() qu'un environnement Gymnasium natif — cf. page Modélisation ▸ [Créer son propre environnement Gymnasium](#dl-rl-custom-env)

## Vectoriser un environnement personnalisé pour SB3
Syntaxe:
```
from stable_baselines3.common.env_util import make_vec_env
vec_env = **make_vec_env**(lambda: CustomGridEnv(), n_envs=1)
```
Résultat: équivalent de DummyVecEnv([lambda: env]) — nécessaire pour entraîner avec Stable Baselines3

## Policy pour une observation en dictionnaire
Syntaxe: model = DQN("**MultiInputPolicy**", vec_env)
Résultat: obligatoire si observation_space est un spaces.Dict — "MlpPolicy" lève une ValueError dans ce cas

## Prédiction déterministe (pas d'exploration)
Syntaxe: action, _states = model.predict(obs, **deterministic**=True)
Résultat: toujours l'action de plus haute Q-value plutôt qu'une action échantillonnée selon la policy — utile pour observer un comportement stable une fois l'agent entraîné
