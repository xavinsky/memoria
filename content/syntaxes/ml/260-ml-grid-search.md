---
title: Model Tuning — GridSearchCV / RandomizedSearchCV
subgroup: Régularisation & Tuning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## GridSearchCV — recherche exhaustive
Syntaxe:
```
from sklearn.model_selection import GridSearchCV
grid = {'alpha':[0.01,0.1,1], 'l1_ratio':[0.2,0.5,0.8]}
search = **GridSearchCV**(model, grid, scoring='r2', cv=5, n_jobs=-1)
search.fit(X_train, y_train)
```
Params: n_jobs=-1 : parallélise le calcul sur tous les cœurs disponibles
Explication: teste toutes les combinaisons de la grille — search.best_score_ / search.best_params_ / search.best_estimator_ une fois fit

## RandomizedSearchCV — recherche aléatoire
Syntaxe:
```
from sklearn.model_selection import RandomizedSearchCV
from scipy import stats
grid = {'alpha':[0.001,0.01,0.1,1], 'l1_ratio': stats.uniform(0,1)}
search = **RandomizedSearchCV**(model, grid, n_iter=100, cv=5, n_jobs=-1)
```
Params: n_iter : nombre de tirages aléatoires
Explication: tire n_iter combinaisons au hasard dans l'espace des hyperparamètres — scalable à un grand espace, contrairement à GridSearchCV

## Distributions pour une recherche coarse-grain
Syntaxe:
```
from scipy import stats
stats.uniform(1, 100)      # pas d'a priori
stats.**loguniform**(0.01, 1)  # balaie plusieurs ordres de grandeur
stats.norm(10, 2)          # si on a une valeur pressentie
```
Params: -
Explication: loguniform : idéal pour un premier balayage large (ex: alpha) avant d'affiner autour de la meilleure zone trouvée

## Optimiser sur une métrique maison
Syntaxe:
```
from sklearn.metrics import make_scorer

def precision_classe_2(y_true, y_pred):
    tp2 = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 2 and yp == 2)
    fp2 = sum(1 for yt, yp in zip(y_true, y_pred) if yt != 2 and yp == 2)
    return tp2 / (tp2 + fp2)

search = RandomizedSearchCV(model, grid, **scoring**=make_scorer(precision_classe_2))
```
Params: -
Explication: une fonction brute `(y_true, y_pred) -> score` n'est PAS un scorer sklearn valide — make_scorer() l'enveloppe pour la rendre utilisable partout où sklearn attend un `scoring` (cross_validate, GridSearchCV...)

## Grilles différentes selon une valeur catégorielle (ex: kernel)
Syntaxe:
```
param_distributions = [
    {"kernel": ["linear"], "C": loguniform(1e-1, 1e4)},
    {"kernel": ["rbf"], "C": loguniform(1e-1, 1e4), "**gamma**": loguniform(1e-3, 1e2)},
]
RandomizedSearchCV(SVC(), param_distributions, n_iter=400)
```
Params: une LISTE de dicts au lieu d'un seul
Explication: chaque dict ne contient que les hyperparamètres pertinents pour SA valeur (ex: gamma n'a pas de sens pour un kernel linéaire) — à chaque tirage, un dict est choisi au hasard puis échantillonné
