---
title: PolynomialFeatures — capturer non-linéarités & interactions
subgroup: Transformation
type: syntax
---

## Générer les termes polynomiaux et croisés
Syntaxe:
```
from sklearn.preprocessing import **PolynomialFeatures**
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.**fit_transform**(X)
```
Résultat: pour chaque paire de features (a,b) : ajoute a², b², a·b (et plus haut degré si demandé) — permet à un modèle LINÉAIRE de capturer des relations non-linéaires/des interactions entre features

## Nommer les nouvelles colonnes générées
Syntaxe: poly.**get_feature_names_out**(X.columns)
Résultat: utile pour reconstruire un DataFrame lisible à partir du array retourné par fit_transform
