---
title: Bagging, Boosting & Stacking
subgroup: Ensemble Methods
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## RandomForestClassifier / Regressor
Syntaxe:
```
from sklearn.ensemble import RandomForestRegressor
forest = **RandomForestRegressor**(n_estimators=100)
```
Params: n_estimators : nombre d'arbres
Explication: bagging d'arbres de décision — cf. page Modélisation ▸ Ensemble Methods

## Bagger n'importe quel modèle
Syntaxe:
```
from sklearn.ensemble import BaggingClassifier
bagged = **BaggingClassifier**(KNeighborsClassifier(), n_estimators=40)
```
Params: -
Explication: BaggingRegressor/Classifier applique le bagging à n'importe quel estimator, pas seulement des arbres

## AdaBoostClassifier / Regressor
Syntaxe:
```
from sklearn.ensemble import AdaBoostRegressor
ada = **AdaBoostRegressor**(DecisionTreeRegressor(max_depth=3), n_estimators=50)
```
Params: -
Explication: chaque arbre corrige les erreurs du précédent en repondérant les observations mal prédites

## GradientBoostingClassifier / Regressor
Syntaxe:
```
from sklearn.ensemble import GradientBoostingRegressor
gb = **GradientBoostingRegressor**(n_estimators=100, learning_rate=0.1, max_depth=3)
```
Params: learning_rate : poids de chaque arbre ajouté
Explication: chaque arbre prédit le résidu du précédent au lieu de repondérer — généralement plus performant qu'AdaBoost

## XGBoost
Syntaxe:
```
from xgboost import XGBRegressor
xgb = **XGBRegressor**(max_depth=10, n_estimators=100, learning_rate=0.1, early_stopping_rounds=5)
xgb.fit(X_train, y_train, eval_set=[(X_train,y_train),(X_val,y_val)])
```
Params: -
Explication: librairie dédiée optimisée, nécessite un jeu de validation (eval_set) pour early_stopping_rounds

## VotingClassifier / Regressor
Syntaxe:
```
from sklearn.ensemble import VotingClassifier
ensemble = **VotingClassifier**(estimators=[("rf",forest),("lr",logreg)], voting="soft")
```
Params: voting : hard (vote majoritaire) / soft (moyenne des probas)
Explication: agrège simplement les prédictions de plusieurs modèles déjà entraînés

## StackingClassifier / Regressor
Syntaxe:
```
from sklearn.ensemble import StackingClassifier
ensemble = **StackingClassifier**(estimators=[...], final_estimator=LogisticRegression())
```
Params: -
Explication: un modèle final apprend à combiner les prédictions des autres, au lieu d'un simple vote/moyenne
