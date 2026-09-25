---
title: Cross-Validation manuelle en Deep Learning
subgroup: Optimisation
---

`cross_val_score` (Sklearn, cf. [Cross-Validation](#ml-cross-validation-concept), groupe ml) ne fonctionne pas directement sur un modèle Keras — quand un simple holdout ne suffit pas (score jugé trop instable selon le split), il faut coder la boucle K-Fold à la main.

1. Découper les indices avec `KFold` (Sklearn) plutôt que les données elles-mêmes — permet d'indexer X ET y de façon cohérente à chaque fold
2. À CHAQUE fold : refaire le preprocessing (`.fit_transform` sur le train du fold, `.transform` sur sa validation) — jamais le préprocesseur global, sous peine de fuite de données entre folds
3. Réinitialiser un modèle NEUF à chaque fold (`initialize_model()`) — jamais réutiliser les poids d'un fold précédent
4. Entraîner avec `validation_data=` puis lire `history.history['val_loss']` pour récupérer le score de ce fold

> [!WARNING]
> ⚠️ Cette boucle entraîne K modèles complets — d'où le coût déjà signalé ci-dessus. En pratique, on la réserve aux cas où le budget de calcul le permet ET où le holdout seul laisse un doute réel sur la stabilité du score (grande variance suspectée entre splits).
