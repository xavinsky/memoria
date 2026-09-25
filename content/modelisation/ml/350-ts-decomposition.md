---
title: Décomposition
subgroup: Modèles
subsubgroup: Time Series
---

**Time Series** — suite d'observations prises à intervalles de temps réguliers. Deux objectifs distincts : **comprendre** (décomposer, expliquer le comportement) et **prévoir** (prédire les valeurs futures à partir du passé seul).

> [!WARNING]
> ⚠️ Un `train_test_split` classique (aléatoire) est interdit sur une Time Series : il utiliserait des valeurs futures pour prédire le passé (data leakage temporel) — split forcément CONTIGU (cf. [Train/test split contigu](#ts-splitting), page Syntaxes).

La plupart des Time Series se décomposent en 3 composantes : **Trend** (tendance long terme), **Seasonal/Periodic** (motif qui se répète, calendaire ou non) et **Irregularities** (résidus).

```math
Y = Y_{trend} + Y_{season} + Y_{resid} \qquad\text{(additive)}
```

```math
Y = Y_{trend} \times Y_{season} \times Y_{resid} \qquad\text{(multiplicative)}
```

:::compare
- **Additive** : l'amplitude de la saisonnalité reste CONSTANTE au cours du temps, indépendamment du niveau de la tendance
- **Multiplicative** : l'amplitude de la saisonnalité VARIE proportionnellement au niveau de la tendance (ex: ventes qui augmentent en valeur absolue autour de Noël, d'autant plus que la tendance de fond est haute)
:::

> [!TIP]
> 👉 **Repère rapide** : résidus qui semblent "perdre la notion du temps" (bruit stable, pas de forme résiduelle) → bon modèle. Comparer visuellement les résidus additifs vs multiplicatifs pour choisir (cf. `seasonal_decompose`, page Syntaxes).

1. **Retirer la saisonnalité à la main** (alternative à SARIMA, qui la gère en interne) : soustraire (additif) ou diviser (multiplicatif) la série par sa composante `.seasonal` — la composante se répète à l'identique, ses 12 (ou S) premières valeurs suffisent à la caractériser pour n'importe quelle période future
2. Modéliser/prédire sur la série DÉSAISONNALISÉE (souvent avec un ARIMA simple, cf. page Syntaxes)
3. **Réincorporer la saisonnalité** sur les prédictions : ré-additionner ou re-multiplier par la composante saisonnière du mois/période correspondant, avant de comparer aux vraies valeurs
