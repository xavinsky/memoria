---
title: Baseline Score
subgroup: Métriques
type: syntax
---

## Baseline régression
Syntaxe:
```
from sklearn.dummy import DummyRegressor
baseline = **DummyRegressor**(strategy="mean")
baseline.fit(X_train, y_train)
baseline.score(X_test, y_test)
```
Résultat: strategy : mean, median, constant — prédit toujours la même valeur, quel que soit X

## Baseline classification
Syntaxe:
```
from sklearn.dummy import DummyClassifier
baseline = **DummyClassifier**(strategy="most_frequent")
```
Résultat: strategy : most_frequent (prédit toujours la classe majoritaire), stratified (tire aléatoirement selon les proportions de classes), uniform

## Baseline séquence/série temporelle — persistence
Syntaxe: y_pred_baseline = X_test[:, **-1**, 0]  # dernière valeur observée de la séquence
Résultat: DummyRegressor ignore X (prédit une constante) — pour une séquence, une baseline plus dure à battre est "rien ne change" : prédire la DERNIÈRE valeur connue plutôt qu'une moyenne globale
