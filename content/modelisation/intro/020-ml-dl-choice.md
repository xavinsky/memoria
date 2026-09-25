---
title: ML, DL ou RL ?
---

![](../../diagrams/ml-dl-choice-1.svg)

> [!TIP]
> \* Des exceptions existent dans les deux sens (gros volume de données tabulaires, Transfer Learning sur peu de données...).

| Critère | ML classique (arbres, régressions...) | Deep Learning | Reinforcement Learning |
|---|---|---|---|
| Type de données | tabulaire/structuré — lignes/colonnes avec un sens métier clair | non-structuré — image, texte, audio, vidéo (CNN/RNN/Transformer, cf. groupe dl) | pas de dataset fixe — expérience générée par interaction avec un environnement (simulateur ou réel) |
| Volume de données | fonctionne dès quelques centaines/milliers de lignes | a besoin de BEAUCOUP de données (dizaines de milliers et +) pour ne pas overfitter | pas un volume à collecter à l'avance — dépend du nombre d'épisodes nécessaires pour converger (souvent très élevé) |
| Feature engineering | souvent manuel, demande une expertise métier | extraction automatique par le modèle lui-même (cf. [Convolution — kernel, filtre, feature map](#dl-cnn-convolution)) | définir observation_space/action_space/reward function (cf. groupe rl) — l'effort porte sur la récompense, pas les features |
| Calcul / temps d'entraînement | secondes à minutes, CPU suffit | GPU quasi indispensable, entraînement long | long, souvent simulé massivement en parallèle (nombreux épisodes) |
| Interprétabilité | coefficients/règles lisibles (OLS, arbre de décision) | boîte noire — explicabilité seulement approximative | boîte noire — la policy résultante est difficile à interpréter |

> [!TIP]
> 👉 Sur données TABULAIRES, les ensembles d'arbres (Random Forest, XGBoost — cf. [Ensemble Methods](#ml-ensemble-methods)) dominent quasi systématiquement le DL dans les benchmarks — le type de donnée est donc souvent le critère le plus déterminant entre ML classique et DL, avant même le volume disponible.

> [!TIP]
> 👉 Le manque de données pour du DL peut être contourné par le **Transfer Learning** — repartir d'un modèle déjà entraîné sur un gros dataset, plutôt que d'entraîner from scratch.
