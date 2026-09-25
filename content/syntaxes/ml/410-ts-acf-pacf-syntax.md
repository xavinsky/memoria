---
title: ACF & PACF
subgroup: Time Series
type: syntax
---

## Tracer l'ACF
Syntaxe:
```
from statsmodels.graphics.tsaplots import plot_acf
**plot_acf**(df.value, lags=50)
```
Résultat: cône bleu = intervalle de confiance ; cutoff donne l'ordre q d'un MA (cf. page Modélisation)

## Tracer la PACF
Syntaxe:
```
from statsmodels.graphics.tsaplots import plot_pacf
**plot_pacf**(df.value, lags=50, c='r')
```
Résultat: cutoff donne l'ordre p d'un AR (cf. page Modélisation)
