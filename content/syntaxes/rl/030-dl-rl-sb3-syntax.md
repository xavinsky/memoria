---
title: Stable Baselines3 — entraîner un agent
subgroup: Reinforcement Learning
type: syntax
---

## Rendre l'environnement compatible SB3
Syntaxe:
```
from stable_baselines3.common.vec_env import DummyVecEnv
env = **DummyVecEnv**([lambda: env])
```
Résultat: obligatoire avant de le passer à un modèle SB3 — standardise l'API attendue, même avec un seul environnement (facilite le passage à plusieurs en parallèle plus tard)

## Créer un modèle RL sur un environnement
Syntaxe:
```
from stable_baselines3 import DQN
model = **DQN**("MlpPolicy", env, tensorboard_log="./logs/")
```
Résultat: "MlpPolicy" = réseau Dense classique, adapté aux observations non-image — cf. page Modélisation ▸ Deep Q-Network (DQN) ; tensorboard_log = dossier de logs pour suivre l'entraînement (TensorBoard)

## Entraîner avec Policy Gradient (PPO)
Syntaxe:
```
from stable_baselines3 import **PPO**
model = PPO("MlpPolicy", env)
```
Résultat: même API que DQN (.learn/.save/.predict) — ajuste la policy directement plutôt qu'une Q-table/Q-network ; seul algorithme adapté à des actions CONTINUES — cf. page Modélisation ▸ Deep Q-Network (DQN)

## Entraîner l'agent
Syntaxe: model.**learn**(total_timesteps=10_000, progress_bar=True)
Résultat: total_timesteps = nombre d'interactions avec l'environnement (pas des epochs classiques) ; progress_bar = barre de progression tqdm

## Suivre/piloter l'entraînement avec un callback
Syntaxe:
```
from stable_baselines3.common.callbacks import BaseCallback

class MyCallback(BaseCallback):
    def _on_step(self) -> bool:
        # appelé à CHAQUE pas d'entraînement
        return True  # False = arrête l'entraînement

model.learn(total_timesteps=10_000, **callback**=MyCallback())
```
Résultat: permet de logger des métriques custom (récompense par épisode...) ou d'arrêter dynamiquement l'entraînement (ex: plateau de performance détecté) en retournant False

## Évaluer l'agent entraîné
Syntaxe:
```
from stable_baselines3.common.evaluation import evaluate_policy
evaluate_policy(model, env)
```
Résultat: exécute plusieurs épisodes SANS apprendre — mesure récompense moyenne et longueur d'épisode

## Sauvegarder / charger un modèle
Syntaxe:
```
model.**save**(model_path)
model = DQN.**load**(model_path, env=env)
```
Résultat: même logique que la sauvegarde d'un modèle Keras (cf. page Syntaxes ▸ Sauvegarder &amp; charger un modèle)

## Utiliser le modèle entraîné
Syntaxe:
```
action, info = model.**predict**(state)
state, reward, terminated, truncated, info = env.step(action)
```
Résultat: équivalent d'un .predict() — répéter jusqu'à terminated/truncated (environnement BRUT, non wrappé)

## Boucle complète sur un environnement wrappé DummyVecEnv
Syntaxe:
```
obs = env.reset()
done = [False]
while not done[0]:
    action, _ = model.predict(obs)
    obs, reward, done, info = env.**step**(action)
```
Résultat: ⚠️ une fois wrappé par DummyVecEnv, .step() renvoie 4 éléments (terminated/truncated FUSIONNÉS en un seul done), contre 5 pour un environnement brut (ligne ci-dessus) — ne pas mélanger les deux formes
