---
title: darts — API unifiée multi-modèles
subgroup: Time Series
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Créer une TimeSeries depuis un DataFrame
Syntaxe:
```
from darts import TimeSeries
series = TimeSeries.**from_dataframe**(df, 'date_col', 'value_col')
```
Params: -
Explication: objet natif darts — resample()/diff()/fill_missing_values() intégrés, sans repasser par pandas à chaque étape

## N'importe quel modèle : même API .fit()/.predict()
Syntaxe:
```
from darts.models import NaiveSeasonal, ExponentialSmoothing, AutoARIMA, Prophet, AutoTBATS
model = **AutoARIMA**()
model.fit(train)
preds = model.predict(len(val))
```
Params: -
Explication: tous les modèles (naïf, ARIMA, Prophet, TBATS...) partagent la même interface — permet de boucler sur plusieurs modèles pour comparer sans réécrire le code à chaque fois

## Évaluer avec une métrique TS dédiée
Syntaxe:
```
from darts.metrics import mape
**mape**(val, preds)
```
Params: -
Explication: équivalent MAPE prêt à l'emploi, pas besoin de le recalculer à la main

## Ajouter une covariable connue à l'avance (ex: météo)
Syntaxe:
```
model.fit(train, **future_covariates**=weather_ts)
model.predict(len(val), future_covariates=weather_ts)
```
Params: -
Explication: même principe que exog= pour SARIMAX (cf. ci-dessus) — covariables PASSÉES (connues seulement dans le passé) vs FUTURES (ex: prévisions météo) vs STATIQUES (constantes, ex: ID produit)
