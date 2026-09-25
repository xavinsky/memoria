---
title: Balancing (classes déséquilibrées)
subgroup: Transformation
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## SMOTE (oversampling synthétique)
Syntaxe:
```
from imblearn.over_sampling import SMOTE
X_res, y_res = **SMOTE**(random_state=42).fit_resample(X_train, y_train)
```
Params: -
Explication: génère de nouvelles observations minoritaires par combinaison linéaire d'observations existantes — équilibre parfaitement les deux classes

## RandomUnderSampler (undersampling aléatoire)
Syntaxe:
```
from imblearn.under_sampling import RandomUnderSampler
X_res, y_res = **RandomUnderSampler**(random_state=42).fit_resample(X_train, y_train)
```
Params: -
Explication: supprime aléatoirement des observations de la classe MAJORITAIRE jusqu'à équilibre parfait — simple mais perd de l'information (contrairement à SMOTE qui n'en ajoute que)

## TomekLinks (nettoyage de frontière)
Syntaxe:
```
from imblearn.under_sampling import TomekLinks
X_res, y_res = **TomekLinks**().fit_resample(X_train, y_train)
```
Params: -
Explication: ne rééquilibre PAS les classes — retire seulement les observations majoritaires formant une paire très proche avec une observation minoritaire (frontière ambiguë), pour rendre la frontière de décision plus nette

## ⚠️ Resampler uniquement le TRAIN set
Syntaxe:
```
X_train_res, y_train_res = SMOTE().fit_resample(X_train, y_train)
# jamais X_test/y_test — le test set doit refléter la vraie distribution
```
Params: -
Explication: resampler le test fausserait l'évaluation (des observations synthétiques ou dupliquées évaluées comme si elles étaient réelles)
