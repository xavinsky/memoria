---
title: ARIMA & SARIMA
subgroup: Time Series
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Fitter un ARIMA(p,d,q)
Syntaxe:
```
from statsmodels.tsa.arima.model import ARIMA
arima = **ARIMA**(df['value'], order=(2,1,1), trend='t')
arima = arima.fit()
```
Params: -
Explication: order=(p,d,q) ; trend='t' ajoute une tendance linéaire

## Chercher (p,d,q) automatiquement
Syntaxe:
```
import pmdarima as pm
smodel = pm.**auto_arima**(df['value'], start_p=1, max_p=2, start_q=1, max_q=2, seasonal=False, trace=True)
```
Params: -
Explication: grid search sur l'AIC — trace=True affiche chaque combinaison testée

## Prédire avec pmdarima (API différente de statsmodels)
Syntaxe: preds, conf_int = smodel.**predict**(n_periods=len(test), return_conf_int=True)
Params: n_periods (pas steps), return_conf_int=True (pas alpha=)
Explication: le modèle retourné par auto_arima a sa PROPRE API .predict() — ne pas confondre avec .get_forecast() de statsmodels (ligne au-dessus), noms de paramètres différents

## Résumé du modèle (AIC, coefficients)
Syntaxe: arima.**summary**()
Params: -
Explication: coefficients + p-values + AIC/BIC pour comparer plusieurs modèles

## Prédire avec intervalle de confiance
Syntaxe:
```
results = arima.**get_forecast**(len(test), alpha=0.05)
forecast = results.**predicted_mean**
conf_int = results.**conf_int**()
```
Params: -
Explication: get_forecast expose la moyenne prédite ET l'intervalle de confiance ; forecast() seul ne renvoie que la moyenne

## SARIMA (saisonnalité intégrée)
Syntaxe:
```
from statsmodels.tsa.statespace.sarimax import SARIMAX
sarima = **SARIMAX**(train, order=(0,1,1), seasonal_order=(2,0,2,12))
sarima = sarima.fit()
```
Params: -
Explication: seasonal_order=(P,D,Q,S) — S = période saisonnière (ex: 12 pour une saisonnalité annuelle mensuelle)

## SARIMAX avec variables exogènes
Syntaxe:
```
sarimax = SARIMAX(y_train, **exog**=X_train[exog_cols], order=(1,0,1), seasonal_order=(1,0,0,24))
res = sarimax.fit()
res.**get_forecast**(steps=48, exog=X_test[exog_cols])
```
Params: exog : DataFrame de features externes (ex: météo, prix) — mêmes lignes/index que y
Explication: le X, en plus du passé de y — exog doit être fourni à la fois au fit() ET au get_forecast() (les vraies valeurs futures si connues, ex: prévisions météo)

## Chercher (p,d,q)(P,D,Q)[S] automatiquement
Syntaxe: pm.auto_arima(train, seasonal=True, **m**=12, start_p=0, max_p=1, start_P=0, max_P=2, trace=True)
Params: -
Explication: m = période saisonnière ; grid search combinée sur les deux jeux d'hyperparamètres

## Cross-valider un ARIMA (boucle manuelle)
Syntaxe:
```
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=3)
for train_idx, test_idx in tscv.split(y):
    m = ARIMA(y.iloc[train_idx], order=(1,1,1)).**fit**()
    ...
```
Params: -
Explication: ARIMA (statsmodels) n'a pas l'API sklearn compatible avec cross_validate — même raison/pattern que la CV manuelle en Deep Learning (cf. groupe dl)
