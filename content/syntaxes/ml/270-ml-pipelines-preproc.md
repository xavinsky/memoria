---
title: Pipeline, ColumnTransformer, FeatureUnion
subgroup: Pipelines
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Pipeline — chaîne d'étapes en séquence
Syntaxe:
```
from sklearn.pipeline import Pipeline
pipe = **Pipeline**([('imputer', SimpleImputer()), ('scaler', StandardScaler())])
pipe.fit(X_train)
```
Params: -
Explication: exécute .fit()/.transform() de chaque étape dans l'ordre — hérite des méthodes du dernier objet (transform si un transformer, predict/score si un modèle)

## ColumnTransformer — étapes en parallèle par colonne
Syntaxe:
```
from sklearn.compose import ColumnTransformer
preproc = **ColumnTransformer**([('num', num_pipe, ['age','bmi']), ('cat', OneHotEncoder(), ['region'])], remainder='passthrough')
```
Params: remainder='passthrough' : conserve les colonnes non listées telles quelles (sinon supprimées par défaut)
Explication: applique des transformations différentes à des colonnes différentes EN PARALLÈLE (contrairement à Pipeline, séquentiel)

## Récupérer les noms de colonnes après transformation
Syntaxe: preproc.**get_feature_names_out**()
Params: -
Explication: fit_transform() renvoie un array sans noms de colonnes — disponible sur tous les transformers depuis Sklearn 1.1.3

## FeatureUnion — transformers en parallèle, résultats concaténés
Syntaxe:
```
from sklearn.pipeline import FeatureUnion
union = **FeatureUnion**([('preprocess', preproc), ('ratio', ratio_constructor)])
```
Params: -
Explication: contrairement à ColumnTransformer (colonnes différentes), applique plusieurs transformers au MÊME jeu de colonnes puis concatène — utile pour ajouter une feature entièrement nouvelle en plus du preprocessing

## Raccourcis make_*** (noms d'étapes auto-générés)
Syntaxe:
```
from sklearn.pipeline import make_pipeline, make_union
from sklearn.compose import make_column_transformer
**make_pipeline**(SimpleImputer(), StandardScaler())
```
Params: -
Explication: équivalents de Pipeline/ColumnTransformer/FeatureUnion sans nommer chaque étape (nom = classe en minuscules)

## make_column_selector — sélection par dtype
Syntaxe:
```
from sklearn.compose import make_column_selector
num_col = **make_column_selector**(dtype_include=['float64'])
cat_col = make_column_selector(dtype_include=['object','bool'])
```
Params: dtype_include / dtype_exclude
Explication: sélectionne des colonnes automatiquement par type plutôt que de lister leurs noms — pratique quand les colonnes concernées varient d'un dataset à l'autre
