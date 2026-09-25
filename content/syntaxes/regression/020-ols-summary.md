---
title: Lire le résumé d'une régression (.summary())
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Afficher le résumé complet du modèle
Formule / Syntaxe:
```code
model.**summary**()
```
label: → extrait, valeurs fictives :
```table
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.712
Model:                            OLS   Adj. R-squared:                  0.706
Method:                 Least Squares   F-statistic:                     121.4
                                        Prob (F-statistic):           3.45e-28
No. Observations:                 200   Log-Likelihood:                -410.22
Df Residuals:                     197   AIC:                             826.4
Df Model:                            2   BIC:                             836.3
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      4.5678      0.512      8.921      0.000       3.559       5.577
x1             2.3456      0.187     12.545      0.000       1.977       2.714
x2            -1.2345      0.298     -4.142      0.000      -1.822      -0.647
==============================================================================
Omnibus:                        1.203   Durbin-Watson:                   1.987
Prob(Omnibus):                  0.548   Jarque-Bera (JB):                1.102
Skew:                           0.145   Prob(JB):                        0.577
Kurtosis:                       2.891   Cond. No.                         12.4
==============================================================================
```
Params: -
Explication: tableau texte avec tous les indicateurs détaillés ci-dessous — R-squared / Adj. R-squared / F-statistic / Prob (F-statistic) en haut à droite ; coef/std err/t/P>|t| par feature dans le tableau du milieu ; Omnibus/JB/Skew/Kurtosis/Durbin-Watson/Cond. No. en bas

## Accès direct aux valeurs clés (sans repasser par .summary())
Formule / Syntaxe:
```
model.**rsquared**
model.**resid**
```
Params: -
Explication: rsquared : float ; resid : Series des résidus, équivalent à model.predict(df) - df["y"] mais déjà calculé par statsmodels — formule du R² et pièges d'interprétation détaillés en page Maths ▸ Régression

## Coefficient, erreur standard, t-value, p-value
Formule / Syntaxe: **coef** / **std err** / **t** / **P>|t|**
Params:
```
coef : $\beta_i$ estimé
t = coef / std err
```
Explication: P>|t| < 0.05 (seuil usuel) ⇒ le coefficient est statistiquement significatif, on rejette $H_0: \beta_i=0$ (cf. [Test d'hypothèse](#test-hypothese), page Maths) — formule du std err en page Maths ▸ Régression

## Intervalle de confiance du coefficient
Formule / Syntaxe: **[0.025   0.975]**
Params: -
Explication: IC 95% de $\beta_i$ — s'il ne contient pas 0, le coefficient est significatif (cohérent avec sa p-value)
