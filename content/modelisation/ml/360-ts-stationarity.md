---
title: Stationnarité & test ADF
subgroup: Modèles
subsubgroup: Time Series
---

**Stationnarité** — une Time Series est stationnaire quand le temps n'influence PAS ses propriétés statistiques (moyenne, variance, autocorrélation). La plupart des méthodes de prévision (AR, MA, ARMA...) sont conçues pour des séries stationnaires : elles capturent des propriétés statistiques et les extrapolent dans le futur, ce qui suppose que ces propriétés restent valables.

```math
H_0 : \text{la série n'est PAS stationnaire}
```

**Augmented Dickey-Fuller (ADF)** — test d'hypothèse sur la stationnarité (cf. [Test d'hypothèse](#test-hypothese), groupe Maths) : p-value proche de 0 (p < 0.05) → on rejette H0 → série stationnaire.

:::compare
- **Décomposition** : retirer trend + seasonal, ne garder/prédire que les résidus (cf. ci-dessus)
- **Differencing** : $Y_{diff} = Y_t - Y_{t-1}$ — souvent suffisant en un seul ordre ; répéter (2nd ordre, etc.) jusqu'à stationnarité, sans sur-différencier
- **Transformation** : log, exp... — utile quand la série a un comportement exponentiel plutôt qu'un simple décalage de niveau
:::

> [!TIP]
> 👉 Ces trois méthodes se combinent : ex. déseasonnaliser (décomposition) PUIS linéariser (log) PUIS différencier une fois — cf. `ndiffs` (page Syntaxes) pour estimer automatiquement l'ordre de differencing nécessaire.
