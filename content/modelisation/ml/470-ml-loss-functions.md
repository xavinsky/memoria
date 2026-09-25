---
title: Loss Functions — régression
subgroup: Entraînement (fit)
---

> [!TIP]
> 💡 La Loss sert à ENTRAÎNER le modèle (`.fit()`), la métrique sert à ÉVALUER après coup (cf. Métriques, Syntaxes) — une Loss doit être (sous-)différentiable, ce que l'accuracy n'est pas (donc jamais utilisable comme Loss).

```math
L_2 = MSE = \dfrac1n\sum_i (\hat y_i - y_i)^2 \qquad L_1 = MAE = \dfrac1n\sum_i |\hat y_i - y_i|
```

:::compare
- **MSE (L2)** : très sensible aux outliers (erreur au carré) — Loss par défaut de LinearRegression / SGDRegressor(loss='squared_error')
- **MAE (L1)** : moins sensible aux outliers, mais nécessite un learning rate qui décroît à chaque epoch pour bien converger (pente constante même près du minimum)
:::

> [!TIP]
> 👉 `SGDRegressor` n'a pas de `loss='mae'` directement — `loss='epsilon_insensitive', epsilon=0` revient exactement à une MAE (cette loss ignore les erreurs sous `epsilon`, donc avec `epsilon=0` toute erreur compte, en valeur absolue).

```math
L_\delta = \begin{cases}\frac12(y-\hat y)^2 & \text{si } |y-\hat y|<\delta\\ \delta(|y-\hat y|-\frac12\delta) & \text{sinon}\end{cases}
```

```
SGDRegressor(loss='**huber**')
```

**Huber Loss** (δ = seuil de bascule MSE ↔ MAE) — mélange MSE (proche du minimum, pente utilisable comme indicateur) et MAE (loin du minimum, peu sensible aux outliers).

```math
MSLE = \dfrac1n\sum_i \big(\log(\hat y_i+1) - \log(y_i+1)\big)^2
```

```
model.compile(loss='**msle**', optimizer='adam')
```

**MSLE** (Mean Squared Log Error, Keras) — un MSE calculé sur le LOG de la prédiction/target : pénalise l'ERREUR RELATIVE plutôt que l'écart absolu (une erreur de 100 pèse pareil sur une cible de 500 ou de 50 000), adapté à une target positive très étalée (ex: prix). ⚠️ Exige $\hat y \geq 0$ (sinon $\log$ indéfini) — utiliser une dernière couche `'relu'`, pas `'linear'` (cf. [Construire l'architecture](#dl-architecture-rules), ci-dessus).
