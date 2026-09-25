---
title: Transformers personnalisés — quand utiliser quoi
subgroup: Data Preparation
---

Au-delà des transformers Sklearn standards (SimpleImputer, StandardScaler, OneHotEncoder...), on a parfois besoin d'encapsuler sa propre logique dans un objet compatible Pipeline/ColumnTransformer.

:::compare
- **FunctionTransformer** : transformation STATELESS — qui n'apprend rien pendant `.fit()` (ex: log(X), un ratio entre deux colonnes). Encapsule une simple fonction Python, aucune classe à écrire.
- **Classe custom (TransformerMixin + BaseEstimator)** : transformation STATEFUL — qui doit calculer ET stocker une information pendant `.fit()` (ex: une moyenne apprise sur le train, réutilisée telle quelle sur le test). `FunctionTransformer` ne convient pas ici : rien n'est mémorisé entre `fit()` et `transform()`.
- **FeatureUnion** : pas une transformation en soi — applique plusieurs transformers en PARALLÈLE sur le même jeu de colonnes puis concatène les résultats. Utile pour AJOUTER une feature calculée en plus du preprocessing existant, sans remplacer les colonnes d'origine.
:::

> [!TIP]
> 👉 `BaseEstimator` fournit `get_params()`/`set_params()` (requis par toute Pipeline) ; `TransformerMixin` fournit `fit_transform()` automatiquement à partir de `fit()` et `transform()` — cf. [Transformers personnalisés](#ml-pipelines-custom), page Syntaxes, pour le squelette de classe.
