---
title: Facebook Prophet — alternative à ARIMA
subgroup: Time Series
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Préparer les données au format imposé
Syntaxe:
```
df.columns = ['**ds**', '**y**']  # ds = date, y = valeur à prédire
df['ds'] = pd.to_datetime(df['ds'])
```
Params: -
Explication: Prophet impose ces deux noms de colonnes exacts, quel que soit le dataset d'origine

## Entraîner
Syntaxe:
```
from prophet import Prophet
model = **Prophet**()
model.fit(train)
```
Params: -
Explication: gère nativement tendance + saisonnalité(s) + jours fériés, sans passer par ACF/PACF/differencing comme ARIMA

## Générer le futur à prédire
Syntaxe:
```
future = model.**make_future_dataframe**(periods=24, freq='MS')
forecast = model.**predict**(future)
```
Params: periods : horizon ; freq : 'MS' (mois), 'D' (jour)...
Explication: future contient aussi les dates du train — forecast['yhat'] = prédiction, avec intervalle d'incertitude

## Visualiser prédiction / composantes
Syntaxe:
```
model.**plot**(forecast)
model.**plot_components**(forecast)
```
Params: -
Explication: plot() = série + prédiction + intervalle ; plot_components() = décompose en tendance + saisonnalité(s)

## Cross-validation spécifique aux séries temporelles
Syntaxe:
```
from prophet.diagnostics import cross_validation, performance_metrics
df_cv = **cross_validation**(model, initial='1825 days', period='180 days', horizon='365 days')
performance_metrics(df_cv)
```
Params: initial : taille de la 1ère fenêtre d'entraînement ; period : décalage entre folds ; horizon : durée de prédiction
Explication: fenêtres d'entraînement glissantes (jamais de shuffle) — renvoie MAPE/RMSE... par horizon de prédiction
