---
title: ARMA, ARIMA & SARIMA
subgroup: Modèles
subsubgroup: Time Series
---

[[P:ARIMA]] · [[P:SARIMAX]] (statsmodels)

**ARMA(p,q)** — combine AR et MA : la plupart des séries réelles ont besoin des deux composantes à la fois.

```math
Y_t = \alpha + \beta_1 Y_{t-1} + \cdots + \beta_p Y_{t-p} + \phi_1 \epsilon_{t-1} + \cdots + \phi_q \epsilon_{t-q}
```

**ARIMA(p,d,q)** — ajoute le "I" (Integrated) : au lieu de modéliser Y directement, on modélise sa version différenciée d fois $Y^{(d)}$, pour la rendre stationnaire avant d'appliquer AR+MA (cf. Stationnarité, ci-dessus). Le choix de d se fait via l'ADF test ou `ndiffs` ; p et q se lisent sur PACF/ACF de la série différenciée.

:::compare
- **p (AR)** : nombre de lags de Y — lu sur la PACF
- **d (I)** : nombre de différenciations pour stationnariser — via ADF test / `ndiffs`
- **q (MA)** : nombre de lags d'erreurs — lu sur l'ACF
:::

1. Rendre la série stationnaire (décomposition, transformation, differencing) — noter l'ordre d retenu
2. Confirmer la stationnarité (visuellement, ACF, test ADF)
3. Lire p et q sur les graphes PACF / ACF de la série stationnarisée
4. Fitter un ARIMA(p,d,q) sur la série ORIGINALE (non différenciée manuellement — `d` s'en charge)
5. Essayer quelques valeurs voisines de p, q ; à AIC comparable, garder le modèle le plus simple
6. Inspecter les résidus (ACF/PACF) : bruit blanc → terminé, sinon itérer

> [!TIP]
> 👉 **Box-Jenkins Method** — nom de cette démarche complète ; `auto_arima` (page Syntaxes) automatise l'étape 3-5 par grid search sur l'AIC.

> [!TIP]
> 👉 **SARIMA(p,d,q)(P,D,Q)[S]** — étend ARIMA avec 3 hyperparamètres supplémentaires pour la saisonnalité (mêmes rôles que p,d,q mais au niveau du lag saisonnier m=S, ex: S=12 pour une saisonnalité annuelle) — évite d'avoir à déseasonnaliser la série manuellement en amont.
