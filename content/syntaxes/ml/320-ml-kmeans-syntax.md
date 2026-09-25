---
title: K-Means — clustering
subgroup: Unsupervised Learning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## KMeans — fit
Syntaxe:
```
from sklearn.cluster import KMeans
km = **KMeans**(n_clusters=3)
km.fit(X)
```
Params: n_clusters : K
Explication: cf. page Modélisation ▸ K-Means pour l'algorithme (centroïdes, inertia)

## Récupérer les clusters trouvés
Syntaxe:
```
km.**labels_**          # cluster de chaque observation
km.**cluster_centers_**  # coordonnées des centroïdes
```
Params: -
Explication: -

## Choisir K (méthode du coude)
Syntaxe: km.**inertia_**   # somme des distances au carré aux centroïdes
Params: -
Explication: tracer inertia_ pour plusieurs K et chercher le coude — même logique que pour choisir k en PCA

## Prédire le cluster d'une nouvelle donnée
Syntaxe: km.**predict**(new_X)
Params: -
Explication: K-Means peut aussi bien fitter que prédire, contrairement à un clustering purement descriptif
