---
title: Autocorrélation (ACF & PACF)
subgroup: Modèles
subsubgroup: Time Series
---

**Autocorrélation** — corrélation entre une série Y(t) et une version décalée d'elle-même Y(t−i).

```math
ACF(k) = \dfrac{\sum_{t=k+1}^{n}(X_t-\bar X)(X_{t-k}-\bar X)}{\sum_{t=1}^{n}(X_t-\bar X)^2}
```

**ACF (Autocorrelation Function)** au lag k — le cône bleu affiché par `plot_acf` (page Syntaxes) représente un intervalle de confiance (95% par défaut) : un pic à l'intérieur n'est pas statistiquement significatif. Des pics tous les 12 lags révèlent une saisonnalité annuelle.

> [!WARNING]
> ⚠️ L'ACF mesure l'effet direct ET indirect d'un lag : la corrélation à t−2 inclut une partie de l'effet transmis via t−1. Elle décroît donc lentement, même quand seul le lag le plus récent a un effet réel.

:::compare
- **ACF — effet direct + indirect** : corrélation "brute" de la série avec elle-même — décroissance lente (image des étudiants qui copient sur leur voisin immédiat : l'info se propage de proche en proche jusqu'au bout de la rangée)
- **PACF — effet direct seulement** : retire l'influence des lags intermédiaires (Yule-Walker ou Durbin-Levinson sous le capot) — chute nette après le vrai nombre de lags utiles (mêmes étudiants, mais chacun isolé : on ne mesure plus que ce qu'il sait vraiment par lui-même)
:::

> [!TIP]
> 👉 **Ce que ça sert à choisir** : le nombre de lags où la PACF "coupe" (cutoff) donne l'ordre p d'un processus AR ; celui où l'ACF coupe donne l'ordre q d'un processus MA (cf. ci-dessous).
