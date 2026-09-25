---
title: Transformers personnalisés
subgroup: Pipelines
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## FunctionTransformer — encapsuler une fonction
Syntaxe:
```
from sklearn.preprocessing import FunctionTransformer
rounder = **FunctionTransformer**(lambda x: np.round(x, decimals=2))
```
Params: -
Explication: encapsule une fonction Python en Transformer Sklearn, utilisable en Pipeline/ColumnTransformer — uniquement pour des transformations stateless (qui n'apprennent rien pendant .fit(), ex: log(X))

## Classe custom — transformation stateful
Syntaxe:
```
from sklearn.base import TransformerMixin, BaseEstimator
class MyTransformer(TransformerMixin, BaseEstimator):
    def **fit**(self, X, y=None):
        ...  # stocker ce qui doit être appris
        return self
    def **transform**(self, X, y=None):
        ...
        return X
```
Params: BaseEstimator fournit get_params()/set_params() ; TransformerMixin fournit fit_transform() à partir de fit()+transform()
Explication: nécessaire si la transformation est stateful (stocke une info pendant fit(), réutilisée dans transform(), ex: un scaler maison) — FunctionTransformer ne le permet pas
