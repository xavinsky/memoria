---
title: Régression linéaire (OLS) — R² et diagnostic des résidus
---

```math
R^2 = 1 - \dfrac{\sum (y_i - \hat y_i)^2}{\sum (y_i - \bar y)^2}
```

**R-squared** (variance expliquée par le modèle) — compare le modèle à la prédiction naïve "toujours la moyenne" : R²=1 (parfait), R²=0 (aussi bon que la moyenne), et R² peut être négatif si le modèle est pire que prédire juste la moyenne (ex: sur de nouvelles données, en overfitting). Adj. R-squared pénalise l'ajout de features inutiles, à préférer pour comparer deux modèles avec un nombre de features différent.

> [!WARNING]
> ⚠️ **Piège** : en régression simple (une seule feature), R² = Corr(X,Y)² — mais en régression multivariée, cette égalité ne tient plus : le R² dépend de l'ensemble des features et de leurs corrélations croisées, pas d'une seule corrélation isolée.

```math
se(\beta_1) = \dfrac{1}{\sqrt{n-2}} \cdot \dfrac{s_{résidus}}{s_x}
```

**Erreur standard d'un coefficient** (régression simple) — explique la colonne "std err" de `.summary()` : plus les résidus sont dispersés (mauvais fit) ou x peu varié, plus l'incertitude sur $\beta_1$ est grande.

> [!WARNING]
> ⚠️ **Hétéroscédasticité** (variance des résidus non constante) : motif en "entonnoir" sur un scatter résidus vs. valeurs prédites — invalide l'hypothèse de variance constante de l'OLS : le R² reste valide, mais les p-values et IC des coefficients ne sont plus fiables.

> [!WARNING]
> ⚠️ **Résidus autocorrélés / motif non aléatoire** : si les résidus suivent un motif visible (au lieu d'un nuage sans structure) vs. les prédictions ou dans le temps, ça signale une variable explicative manquante — pistes : ajouter des features, transformer y (ex: log), ou changer de famille de modèle ; Durbin-Watson (`.summary()`) détecte spécifiquement l'autocorrélation temporelle.

> [!TIP]
> 👉 **Condition pour que le R² soit interprétable** : le R² n'a de sens que si le modèle contient un intercept (une colonne de 1 dans X) — `smf.ols` l'ajoute automatiquement, `sm.OLS` non (`sm.add_constant`, page Syntaxes).

**F-statistic / Prob (F-statistic)** — teste si le modèle dans son ensemble est significatif (au moins un $\beta_i \ne 0$) ; Prob(F-statistic) est la p-value associée, à regarder en premier avant les coefficients individuels.

> [!WARNING]
> ⚠️ **Cond. No. (nombre de conditionnement)** élevé (ex: >30) ⇒ possible multicolinéarité (deux features très corrélées entre elles), rend les coefficients individuels instables à interpréter isolément — signal global sur l'ensemble du modèle (cf. [Multicolinéarité — VIF](#ml-multicollinearity), ci-dessous, pour une détection feature par feature). Symptôme concret : deux features quasi-colinéaires (ex: `r=0.989`) peuvent rester chacune très significative (p<0.0001) tout en ayant des coefficients de **signes opposés qui se compensent presque exactement** — l'OLS "répartit" arbitrairement un même effet réel entre les deux plutôt que d'en écarter une comme non significative.

**Omnibus / Jarque-Bera (JB) / Skew / Kurtosis / Durbin-Watson** — diagnostics sur les résidus : Omnibus/JB testent leur normalité, Skew/Kurtosis leur forme, Durbin-Watson (≈2 si ok) détecte une autocorrélation (cf. Résidus autocorrélés ci-dessus) — utiles pour valider les hypothèses de l'OLS, mais secondaires par rapport à R² et p-values.

> [!TIP]
> 👉 **Variable confondante (confounding)** : une feature catégorielle (ex: `C(état)`) peut ressortir statistiquement significative seule, puis ne plus l'être du tout une fois qu'on AJOUTE une autre feature corrélée (ex: `wait_time`) à la formule — signe que son effet apparent était en réalité entièrement porté par cette 2ᵉ variable, pas un vrai effet propre. Ajouter une feature continue candidate et regarder si les coefficients catégoriels perdent leur significativité (`p < 0.05`) est une façon simple de tester ça.
