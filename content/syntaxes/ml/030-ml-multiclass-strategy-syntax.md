---
title: Forcer une stratégie multiclasse (One-vs-Rest / One-vs-One)
subgroup: Choix du modèle
type: syntax
---

## One-vs-Rest — un modèle par classe
Syntaxe:
```
from sklearn.multiclass import OneVsRestClassifier
model = **OneVsRestClassifier**(LogisticRegression())
```
Résultat: cf. page Modélisation ▸ [Stratégies multiclasse (One-vs-Rest vs One-vs-One)](#ml-multiclass-strategies)

## One-vs-One — un modèle par paire de classes
Syntaxe:
```
from sklearn.multiclass import OneVsOneClassifier
model = **OneVsOneClassifier**(LogisticRegression())
```
Résultat: utilisable ensuite comme n'importe quel estimator Sklearn (cross_validate, .fit/.predict...)
