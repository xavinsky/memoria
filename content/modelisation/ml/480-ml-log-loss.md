---
title: Log Loss — classification
subgroup: Entraînement (fit)
---

```math
LogLoss = -\dfrac1n\sum_i y_i\log(\hat y_i) + (1-y_i)\log(1-\hat y_i)
```

```
SGDClassifier(loss='**log_loss**')
```

Loss de la régression logistique, dérivée de la maximisation du log-likelihood (cf. [Régression logistique — MLE](#logit-theorie), groupe Maths) — pénalise infiniment une prédiction confiante et fausse ($\log(0) \to -\infty$).

```math
\nabla LogLoss = -\dfrac1n X^T(y-\hat y)
```

Même forme vectorielle que le gradient du MSE d'une régression linéaire (cf. Gradient de l'OLS ci-dessus, à un facteur 2 près) — seul $\hat y$ change : sigmoïde($X\beta$) en classification vs $X\beta$ en régression.

> [!TIP]
> 👉 Chaque famille de classifieur (Logit, SVC, Naive Bayes...) a sa propre Loss adaptée à son hypothèse h — `hinge` ≈ SVC, `log_loss` ≈ Logit.
