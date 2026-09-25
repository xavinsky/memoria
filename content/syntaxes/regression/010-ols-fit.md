---
title: Régression linéaire multivariée (OLS) avec statsmodels
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Modèle de régression multivariée (OLS)
Formule / Syntaxe:
```
$$y = \beta_0 + \beta_1 x_1 + ... + \beta_p x_p + \epsilon$$
import statsmodels.formula.api as smf
model = smf.**ols**("y ~ x1 + x2", data=df).**fit**()
```
Params:
```
$y$ : variable cible (dépendante)
$x_i$ : features (indépendantes)
$\beta_i$ : coefficients estimés — $\beta_0$ est l'Intercept
```
Explication: OLS = Ordinary Least Squares, minimise la MSE (Mean Squared Error) entre prédictions et valeurs réelles ; la formule texte façon R décrit le modèle, .fit() calcule les coefficients

## Ce que produit .fit()
Formule / Syntaxe:
```
model.params
model.**fittedvalues**
model.resid
model.**summary**()
```
Params:
```
params : Series des $\beta_i$ estimés, indexée par nom de feature (+ Intercept) — une valeur par feature, pas par ligne
fittedvalues : $\hat y$, une valeur par ligne de df
resid : $y - \hat y$, une valeur par ligne
```
Explication: fit() renvoie un objet Results complet, pas juste les coefficients — model.fittedvalues donne directement ŷ (les prédictions sur les données d'entraînement, même échelle que y) ; à comparer avec Logit ci-dessous, où fittedvalues n'est PAS sur l'échelle de y

## Ajouter une variable catégorielle à la formule
Formule / Syntaxe: model = smf.ols("y ~ x1 + **C(**cat_feature**)**", data=df).fit()
Params: cat_feature : colonne catégorielle (str)
Explication: C() crée une variable indicatrice (dummy 0/1) par catégorie — une modalité sert de référence (dans l'Intercept), les autres apparaissent en coefficients séparés

## Standardiser les features avant régression (rendre les coefficients comparables)
Formule / Syntaxe: df_std = (df[features] - df[features].**mean**()) / df[features].**std**()
Params: features : liste de colonnes numériques
Explication: transforme chaque feature en z-score (moyenne 0, écart-type 1, cf. Score-z) — sans ça, les coefficients ne sont pas comparables entre eux à cause des différences d'échelle des variables d'origine

## Ajuster un modèle via l'API bas niveau (tableaux plutôt que formule texte)
Formule / Syntaxe:
```
import statsmodels.api as sm
model = sm.**OLS**(y, X).fit()
```
Params:
```
y : array/Series cible
X : DataFrame/array des features
```
Explication: alternative à smf.ols(formula=...) — utile quand X/y sont déjà construits séparément ; contrairement à smf.ols, il faut ajouter l'intercept soi-même avec sm.add_constant(X) (sinon le modèle passe par l'origine)

## Supprimer l'intercept dans une formule (un coefficient par catégorie, sans référence)
Formule / Syntaxe: model = smf.ols("y ~ C(cat_feature) **- 1**", data=df).fit()
Params: -
Explication: sans le -1, une modalité sert de référence (absorbée dans l'Intercept) et les autres coefficients représentent des écarts à cette référence ; avec -1, chaque modalité reçoit directement son propre coefficient, égal à sa moyenne
