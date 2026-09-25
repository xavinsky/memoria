---
title: Pipeline complet (preprocessing + modèle)
subgroup: Pipelines
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Brancher un modèle en bout de pipeline
Syntaxe:
```
pipeline = **make_pipeline**(preproc, Ridge())
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)
```
Params: -
Explication: rend le preprocessing + modèle utilisable comme n'importe quel estimator Sklearn (cross_validate, GridSearchCV...) tout en gardant le preprocessing synchronisé

## Cross-valider un pipeline complet
Syntaxe:
```
from sklearn.model_selection import cross_val_score
**cross_val_score**(pipeline, X_train, y_train, cv=5, scoring='r2')
```
Params: -
Explication: identique à cross-valider un modèle seul — le preprocessing est refit à chaque fold, sans fuite entre folds

## GridSearch un pipeline (preprocessing + modèle)
Syntaxe:
```
GridSearchCV(pipeline, param_grid={
  '**ridge__alpha**': [0.1,1,10],
  '**columntransformer__pipeline__simpleimputer__strategy**': ['mean','median']
}, cv=5)
```
Params: syntaxe : nom_étape__param (nom_étape__sous_étape__param si étape imbriquée)
Explication: pipeline.get_params() liste tous les hyperparamètres accessibles, à tous les étages — permet de tuner preprocessing ET modèle en une seule GridSearch

## Debug — inspecter une étape intermédiaire
Syntaxe:
```
pipeline.**named_steps**.keys()
pipeline.named_steps['columntransformer'].fit_transform(X_train).shape
```
Params: -
Explication: accède à chaque étape par son nom pour inspecter un résultat intermédiaire (ex: shape avant/après preprocessing)

## Exporter / recharger un pipeline entraîné
Syntaxe:
```
import pickle
pickle.**dump**(pipeline_tuned, open('pipeline.pkl','wb'))
my_pipeline = pickle.**load**(open('pipeline.pkl','rb'))
```
Params: -
Explication: sauvegarde preprocessing + modèle entraînés pour les recharger sans réentraîner — utile pour le déploiement (module ML Ops)
