---
title: NearestNeighbors — recherche de similarité
subgroup: Unsupervised Learning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Indexer un jeu de données
Syntaxe:
```
from sklearn.neighbors import NearestNeighbors
nn = **NearestNeighbors**(n_neighbors=11)
nn.fit(X)
```
Params: n_neighbors : k+1 si on interroge un point déjà dans X (le point lui-même sera son propre plus proche voisin, distance 0)
Explication: non supervisé : pas de .predict(), .fit() ne fait que STOCKER les données — contrairement à KNeighborsRegressor/Classifier, ne prédit ni ne classe rien

## Trouver les k plus proches voisins d'un point
Syntaxe: distances, indices = nn.**kneighbors**(X_query)
Params: -
Explication: renvoie deux arrays parallèles (distance + indice dans X) — base d'un système de recommandation par similarité

## ⚠️ Toujours scaler avant de calculer des distances
Syntaxe:
```
scaler = MinMaxScaler().fit(X)
nn.fit(scaler.transform(X))
```
Params: -
Explication: des features sur des échelles très différentes dominent le calcul de distance — même piège que pour KNeighborsClassifier/Regressor (cf. Feature Scaling)
