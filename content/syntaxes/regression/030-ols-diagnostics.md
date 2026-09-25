---
title: Prédictions, résidus, RMSE et coefficients significatifs
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Prédire à partir du modèle
Formule / Syntaxe: y_pred = model.**predict**(df)
Params: df : mêmes colonnes que celles utilisées pour fit()
Explication: applique les coefficients appris aux lignes de df

## Résidus
Formule / Syntaxe:
```
$$\epsilon_i = \hat y_i - y_i$$
**residuals** = y_pred - df["y"]
```
Params: -
Explication: toujours vérifier que residuals.mean() ≈ 0 après un fit OLS — sinon, il y a une erreur dans le calcul ; diagnostics des résidus (hétéroscédasticité, autocorrélation) détaillés en page Maths ▸ Régression

## RMSE (Root Mean Squared Error)
Formule / Syntaxe:
```
$$RMSE = \sqrt{\dfrac{1}{n}\sum_{i=1}^n (\hat y_i - y_i)^2}$$
rmse = pow((residuals ** 2).mean(), 0.5)
```
Params: -
Explication: erreur moyenne de prédiction, dans la même unité que y — plus petit = mieux, mais dépend de l'échelle de y (contrairement au R², sans unité)

## Récupérer coefficients et p-values du modèle
Formule / Syntaxe:
```
model.**params**    # Series des coefficients (dont Intercept)
model.**pvalues**   # Series des p-values associées
```
Params: -
Explication: utile pour filtrer/trier les coefficients programmatiquement plutôt que lire .summary() à l'œil

## Ne garder que les coefficients statistiquement significatifs
Formule / Syntaxe:
```
p = model.pvalues.reset_index()
p.columns = ["variable","p_value"]
c = model.params.reset_index()
c.columns = ["variable","coef"]
p.**merge**(c, on="variable").**query**("p_value<0.05").sort_values("coef")
```
Params: -
Explication: pattern utilisé dans olist/utils.py::return_significative_coef — combine pvalues et params par jointure (cf. [Fusion/jointures](#fusion)), puis filtre p<0.05

## Graphiques de régression partielle (une feature à la fois, effet des autres neutralisé)
Formule / Syntaxe:
```
import statsmodels.api as sm
fig = plt.figure(figsize=(10,10))
sm.graphics.**plot_partregress_grid**(model, fig=fig)
```
Params: -
Explication: visualise, pour chaque feature, sa relation avec y une fois l'effet des autres features retiré — équivalent graphique des partial correlation coefficients (coefficients de la régression multivariée)

## Visualiser les résidus pour détecter hétéroscédasticité/autocorrélation
Formule / Syntaxe: sns.**scatterplot**(x=y_pred, y=residuals)
Params: -
Explication: scatter résidus vs. valeurs prédites — motifs à repérer et leur signification détaillés en page Maths ▸ Régression

## QQ-plot — vérifier la normalité des résidus
Formule / Syntaxe:
```
import statsmodels.api as sm
sm.**qqplot**(residuals, line="s")
```
Params: line="s" : trace la droite de référence (standardisée)
Explication: compare les quantiles des résidus à ceux d'une loi normale — points alignés sur la droite = résidus ≈ normaux ; écart aux extrémités = queues plus lourdes/asymétrie (visible aussi sur l'histogramme des résidus, mais le QQ-plot est plus sensible aux écarts dans les queues)
