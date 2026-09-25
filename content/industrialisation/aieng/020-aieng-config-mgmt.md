---
title: Configuration & Versionning — Hydra, Pydantic, DVC
---

Un projet ML/LLM accumule vite des paramètres épars (hyperparamètres, chemins, clés d'API) et des fichiers trop gros pour un `git commit` classique (datasets, poids de modèle) — deux problèmes distincts, deux familles d'outils.

:::compare
- **Hydra** : framework de configuration hiérarchique (fichiers YAML composables) — surcharge des paramètres en ligne de commande (`python train.py model=resnet lr=0.01`) sans toucher au code
- **Pydantic** : valide et TYPE le schéma d'une config (ou d'une réponse API) — lève une erreur explicite si un champ manque ou a le mauvais type, au lieu d'un bug silencieux détecté plus loin
:::

:::compare
- **git-lfs (Git Large File Storage)** : remplace un gros fichier par un pointeur léger DANS le commit — le fichier réel est stocké et téléchargé à part
- **DVC (Data Version Control)** : versionne datasets ET modèles comme du code (`dvc add`/`dvc push`, en parallèle de `git add`/`git push`), avec des pipelines reproductibles (`dvc.yaml`) qui ne ré-exécutent une étape que si son entrée a changé
:::

> [!TIP]
> 👉 Les deux familles se combinent : une config Hydra versionnée par git détermine QUELS paramètres ont produit un modèle, DVC garantit que les données/poids correspondant à ce commit précis sont retrouvables plus tard.
