---
title: Décomposition & stationnarité
subgroup: Time Series
type: syntax
---

## Décomposer (additive / multiplicative)
Syntaxe:
```
from statsmodels.tsa.seasonal import seasonal_decompose
result = **seasonal_decompose**(df['value'], model='additive')
```
Résultat: result.trend / .seasonal / .resid — cf. page Modélisation ▸ [Décomposition](#ts-decomposition)

## Visualiser la décomposition
Syntaxe: result.**plot**()
Résultat: 4 sous-graphiques : série, trend, seasonal, résidus

## Test de stationnarité (ADF)
Syntaxe:
```
from statsmodels.tsa.stattools import adfuller
p_value = **adfuller**(df.value)[1]
```
Résultat: p < 0.05 → série stationnaire (cf. page Modélisation ▸ Stationnarité)

## Différencier (rendre stationnaire)
Syntaxe:
```
df.value.**diff**(1)   # ordre 1
df.value.diff().diff()  # ordre 2
```
Résultat: chaque diff() supplémentaire = un ordre de differencing en plus

## Estimer automatiquement l'ordre de differencing
Syntaxe:
```
from pmdarima.arima.utils import ndiffs
**ndiffs**(df['value'])
```
Résultat: renvoie directement le d optimal, plutôt que de tester diff() par diff()
