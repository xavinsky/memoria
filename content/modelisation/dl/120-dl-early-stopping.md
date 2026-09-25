---
title: Early Stopping & jeu de validation
subgroup: Optimisation
---

[[P:EarlyStopping]]

Utiliser le TEST SET pour décider quand arrêter l'entraînement revient à s'en servir pour OPTIMISER le modèle — une fuite de données (cf. [Cross-Validation](#ml-cross-validation-concept), groupe ml). On utilise à la place un sous-ensemble du train set dédié : le **jeu de validation**.

L'entraînement s'arrête quand la loss de validation cesse de s'améliorer d'une epoch à l'autre — mais la loss étant stochastique, il faut tolérer un nombre d'epochs sans amélioration avant de stopper : la **patience**.

> [!WARNING]
> ⚠️ Le K-fold cross-validation reste préférable à un simple holdout, mais est très coûteux en Deep Learning (K entraînements complets) — en pratique, on se contente souvent d'un split train/validation unique.

> [!TIP]
> 👉 `restore_best_weights` (cf. page Syntaxes) restaure à la fin les poids de l'epoch qui avait la MEILLEURE loss de validation, pas ceux de la dernière epoch (potentiellement dégradée depuis).
