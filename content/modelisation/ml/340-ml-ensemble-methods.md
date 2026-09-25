---
title: Ensemble Methods — Bagging, Boosting, Stacking
subgroup: Modèles
---

[[NP:RandomForestClassifier]] · [[NP:RandomForestRegressor]] · [[NP:BaggingClassifier]] · [[NP:AdaBoostClassifier]] · [[NP:GradientBoostingClassifier]] · [[NP:XGBRegressor]] · [[NP:VotingClassifier]] · [[NP:StackingClassifier]]

**Ensemble learning** = combiner plusieurs modèles de base (souvent des arbres de décision) pour obtenir une prédiction plus robuste qu'un seul modèle.

:::compare
- **Bagging (Bootstrap Aggregating) — parallèle** : entraîne plusieurs "weak learners" EN PARALLÈLE, chacun sur un échantillon bootstrap (tirage aléatoire AVEC remise) du dataset, puis moyenne (régression) ou vote (classification) leurs prédictions. Réduit la VARIANCE. **Random Forest** = bagging d'arbres de décision.
- **Boosting — séquentiel** : entraîne les weak learners EN SÉQUENCE, chacun corrigeant les erreurs du précédent (plus de poids sur les observations mal prédites) ; les meilleurs weak learners pèsent plus dans le vote final. Réduit le BIAIS.
- **Stacking** : entraîne des modèles DIFFÉRENTS (KNN, LogReg, arbre...) qui capturent chacun une structure différente des données, puis agrège leurs prédictions — par simple vote/moyenne (Voting) ou en entraînant un modèle final sur leurs prédictions (Stacking à proprement parler).
:::

**Bootstrapping** — les échantillons d'entraînement de chaque weak learner sont tirés aléatoirement AVEC remise dans le dataset d'origine (les features peuvent aussi être sous-échantillonnées pour diversifier davantage les weak learners).

> [!TIP]
> 👉 Le bagging s'applique à N'IMPORTE QUEL modèle (`BaggingClassifier`/`BaggingRegressor` avec n'importe quel estimator, pas seulement des arbres) — Random Forest n'est qu'un cas particulier optimisé pour les arbres.

**AdaBoost** — repondère les observations mal classées à chaque itération pour que le weak learner suivant s'y concentre davantage.

**Gradient Boosting** — au lieu de repondérer, chaque arbre apprend à prédire le RÉSIDU (l'erreur) du précédent ; la prédiction finale = somme des prédictions de tous les arbres. Généralement plus performant qu'AdaBoost.

```math
D(x) = d_{tree\,1}(x) + d_{tree\,2}(x) + ... + d_{tree\,n}(x)
```

> [!TIP]
> 👉 **XGBoost** — implémentation dédiée et très optimisée du gradient boosting (inspirée de certaines idées du Deep Learning), avec early stopping via un jeu de validation dédié.

:::compare
- **Avantages Bagging** : réduit la variance/overfitting, applicable à n'importe quel modèle
- **Inconvénients Bagging** : structure complexe, entraînement plus long, ignore la performance individuelle de chaque sous-modèle
- **Avantages Boosting** : les sous-modèles forts pèsent plus dans la décision finale, réduit le biais
- **Inconvénients Boosting** : coûteux (séquentiel, pas parallélisable), overfit facilement, sensible aux outliers (temps passé à essayer de bien les prédire)
:::

> [!WARNING]
> ⚠️ Les modèles à base d'arbres (Random Forest, Gradient Boosting, XGBoost...) coupent sur des SEUILS (ordre, pas magnitude) — pas besoin de scaling, SAUF si on les combine à une PCA en amont (qui a besoin de features scalées) ou dans une pipeline où on veut pouvoir switcher facilement entre modèles.
