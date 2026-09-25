---
title: Lire le résumé d'une régression logistique (.summary())
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
                           Logit Regression Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  200
Model:                          Logit   Df Residuals:                      197
Method:                           MLE   Df Model:                            2
                                        Pseudo R-squ.:                  0.2130
                                        Log-Likelihood:                -98.234
                                        LL-Null:                       -124.79
                                        LLR p-value:                 1.234e-12
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -1.2345      0.321     -3.845      0.000      -1.864      -0.605
x1             0.6789      0.145      4.682      0.000       0.395       0.963
x2            -0.3456      0.198     -1.745      0.081      -0.734       0.043
==============================================================================
```
Params: -
Explication: tableau texte avec tous les indicateurs détaillés ci-dessous — Pseudo R-squ. / Log-Likelihood / LL-Null en haut à droite ; coef/std err/z/P>|z| par feature dans le tableau du bas (z au lieu de t, cf. ligne ci-dessous) — mêmes emplacements que pour OLS, avec z à la place de t

## Log-Likelihood (LL) et Pseudo R²
Formule / Syntaxe:
```
$$\text{Pseudo } R^2 = 1 - \dfrac{LL(\text{model})}{LL(\text{null})}$$
model.**llf**        # LL(model)
model.**llnull**     # LL(null)
model.**prsquared**  # Pseudo R²
```
Params:
```
LL(model) : log-vraisemblance du modèle ajusté
LL(null) : log-vraisemblance du modèle sans aucune feature (intercept seul)
```
Explication: les 3 sont déjà calculés par statsmodels, pas besoin de les recalculer à la main — accessibles en attributs (llf/llnull/prsquared) ET affichés directement dans l'en-tête de model.summary() ("Log-Likelihood", "LL-Null", "Pseudo R-squ.") ; LL ∈ ]-∞,0], plus proche de 0 = meilleur fit (rôle analogue au SSR pour OLS) ; Pseudo R² ∈ [0,1] permet de comparer des modèles entre eux, mais est moins directement interprétable qu'un vrai R²

## Vérifier LL(null) en ajustant soi-même le modèle nul (intercept seul)
Formule / Syntaxe:
```
model_null = smf.**logit**("y ~ 1", data=df).fit()
model_null.**llf**  # == model.llnull
```
Params: "y ~ 1" : formule sans aucune feature, juste l'intercept
Explication: optionnel : sert surtout à vérifier/comprendre d'où vient model.llnull (log-vraisemblance d'un modèle qui ne fait que prédire la fréquence moyenne de y) — la même syntaxe "y ~ 1" fonctionne avec smf.ols pour une régression linéaire
