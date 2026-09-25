---
title: Régression linéaire & logistique
subgroup: Modèles
---

[[P:LinearRegression]] · [[P:LogisticRegression]]

Les deux modèles les plus simples, et les premiers à essayer avant d'aller vers plus complexe — combinent tous deux linéairement les features ($X\beta$), mais diffèrent dans la façon de passer de cette combinaison à la prédiction.

```math
\text{LinearRegression : } \hat y = X\beta \qquad\qquad \text{LogisticRegression : } \hat y = \sigma(X\beta) = \dfrac{1}{1+e^{-X\beta}}
```

:::compare
- **LinearRegression — régression** : target continue, sortie non bornée ; solution EXACTE en une étape ($\hat\beta=(X^\top X)^{-1}X^\top y$, cf. [Régression linéaire (OLS) — solution mathématique](#ols-theorie-fermee), groupe Maths), pas de descente de gradient nécessaire ; Loss = MSE
- **LogisticRegression — classification** : target binaire, sortie = probabilité bornée [0,1] via la sigmoïde ; PAS de solution fermée, coefficients estimés par MLE de façon itérative (cf. [Régression logistique — MLE](#logit-theorie), groupe Maths) ; Loss = Log Loss
:::

> [!WARNING]
> ⚠️ **Piège** : contrairement à LinearRegression (aucune régularisation par défaut), `LogisticRegression` est régularisée L2 PAR DÉFAUT (hyperparamètre `C`, cf. Hyperparamètres ci-dessus) — un `LogisticRegression()` "nu" n'est donc pas un pur MLE, sauf à passer explicitement `penalty=None`.

:::compare
- **Avantages** : rapides à entraîner, coefficients directement interprétables (effet de chaque feature, toutes choses égales par ailleurs), bons baselines avant d'essayer un modèle plus complexe
- **Limites** : supposent une relation linéaire entre features et target (ou log-odds pour Logit) — aucune non-linéarité captée sans feature engineering manuel ; sensibles aux outliers et à la multicolinéarité (cf. VIF, page Syntaxes)
:::

> [!TIP]
> 👉 Pour lire les résultats d'un modèle déjà entraîné (coefficients, p-values, R²/Pseudo R²...), cf. [Lire ses résultats](#ml-read-results), ci-dessus, et Lire le résumé d'une régression / régression logistique, page Syntaxes.
