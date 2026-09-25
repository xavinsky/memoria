---
title: Calibration de probabilités
subgroup: Métriques
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Tracer la courbe de calibration
Syntaxe:
```
from sklearn.calibration import CalibrationDisplay
**CalibrationDisplay**.from_estimator(model, X_test, y_test)
```
Params: -
Explication: à faire sur un jeu de TEST dédié (pas le train) — diagonale = bien calibré ; cf. page Modélisation ▸ [Calibration de probabilités](#ml-calibration)

## Calculer les points de la courbe soi-même
Syntaxe:
```
from sklearn.calibration import calibration_curve
prob_true, prob_pred = **calibration_curve**(y_test, y_proba, n_bins=10)
```
Params: n_bins : nombre de buckets de probabilité
Explication: version "bas niveau" de CalibrationDisplay — utile pour calculer un écart chiffré (ex: |prob_true - prob_pred|) plutôt que juste visualiser

## Recalibrer un modèle mal calibré
Syntaxe:
```
from sklearn.calibration import CalibratedClassifierCV
calibrated = **CalibratedClassifierCV**(model, cv=5)
calibrated.fit(X_train, y_train)
calibrated.predict_proba(X_new)
```
Params: -
Explication: entraîne des clones du modèle sur des sous-folds puis recalibre leurs probabilités — les prédictions de classe (predict()) ne changent pas, seules les probabilités sont corrigées
