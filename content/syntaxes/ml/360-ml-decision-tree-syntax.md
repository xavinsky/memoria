---
title: Arbre de décision — DecisionTreeClassifier / Regressor
subgroup: Ensemble Methods
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Instancier et fitter
Syntaxe:
```
from sklearn.tree import DecisionTreeClassifier
tree = **DecisionTreeClassifier**(max_depth=3)
tree.fit(X, y)
```
Params: max_depth, min_samples_split, min_samples_leaf
Explication: sans limite de profondeur, overfit quasi garanti — cf. page Modélisation ▸ Arbres de décision

## Importance des features
Syntaxe: tree.**feature_importances_**
Params: -
Explication: basé sur la baisse de Gini apportée par chaque feature — utile pour une sélection de features (cf. Feature Selection)
