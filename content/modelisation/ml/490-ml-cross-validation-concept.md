---
title: Cross-Validation
subgroup: Test
---

Répète le split train/test K fois sur des sous-échantillons différents, puis moyenne les K scores obtenus — réduit la dépendance au hasard d'un split unique (Holdout Method), qui peut donner un score optimiste ou pessimiste selon le tirage.

**Le splitter par défaut n'est pas toujours un K-Fold classique** : `cross_validate(model, X, y, cv=5)` choisit automatiquement KFold (régression) ou StratifiedKFold (classification, préserve les proportions de classes dans chaque fold) — mais d'autres splitters existent pour des données qui ne sont PAS i.i.d., utilisés notamment dans les pipelines Sklearn en passant un objet splitter plutôt qu'un entier à `cv=`.

:::compare
- **KFold — régression, données i.i.d.** : K folds découpés sans tenir compte d'une structure particulière des données
- **StratifiedKFold — classification** : préserve la proportion de chaque classe dans chaque fold — choisi automatiquement par cv=entier sur un classifieur
- **TimeSeriesSplit — Time Series** : chaque fold d'entraînement précède chronologiquement son fold de test, jamais de shuffle (cf. groupe Time Series ci-dessous)
- **GroupKFold — données groupées** : garde chaque groupe (ex: patient, utilisateur) entier dans un seul fold — évite qu'un même groupe fuite entre train et test
:::

> [!WARNING]
> ⚠️ **Ce que la cross-validation ne fait PAS** : elle n'entraîne pas un modèle utilisable, elle ne fait qu'ESTIMER la performance attendue. Une fois validé, il faut réentraîner sur l'ensemble des données (cf. [Workflow ML](#ml-lifecycle), ci-dessus).

> [!TIP]
> 👉 **Choisir K** : compromis fiabilité / temps de calcul — règle empirique K=5 ou K=10.
