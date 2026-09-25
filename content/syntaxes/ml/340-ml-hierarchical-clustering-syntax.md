---
title: Clustering Hiérarchique — dendrogramme
subgroup: Unsupervised Learning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Calculer les fusions successives
Syntaxe:
```
from scipy.cluster.hierarchy import linkage
Z = **linkage**(X, method='ward')
```
Params: method : 'ward' (minimise la variance intra-cluster, le plus courant), 'average', 'complete'...
Explication: Z encode l'arbre complet des fusions — cf. page Modélisation ▸ Clustering Hiérarchique

## Visualiser le dendrogramme
Syntaxe:
```
from scipy.cluster.hierarchy import dendrogram
**dendrogram**(Z, color_threshold=50)
```
Params: color_threshold : hauteur de coupe affichée
Explication: couper à une hauteur donnée = choisir un nombre de clusters, sans relancer l'algorithme
