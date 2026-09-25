---
title: Régression logistique avec statsmodels
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Modèle de régression logistique
Formule / Syntaxe:
```
$$\hat p = \dfrac{1}{1+e^{-(\beta_0+\beta_1 x_1+...+\beta_p x_p)}}$$
import statsmodels.formula.api as smf
model = smf.**logit**("y ~ x1 + x2", data=df).fit()
```
Params:
```
$y$ : cible binaire (0/1)
$\hat p$ : probabilité prédite d'appartenir à la classe 1
même syntaxe formule que smf.ols : C() pour catégorielles, -1 pour retirer l'intercept
```
Explication: fit() maximise la log-vraisemblance par une méthode itérative, pas de solution fermée comme pour OLS (cf. page Maths ▸ Régression)

## Ce que produit .fit()
Formule / Syntaxe:
```
model.params
model.**fittedvalues**
model.**predict**(df)
model.**summary**()
```
Params:
```
params : Series des $\beta_i$ estimés, indexée par nom de feature (+ Intercept) — une valeur par feature, pas par ligne
fittedvalues : le prédicteur linéaire Xβ (log-odds), une valeur par ligne — PAS une probabilité
```
Explication: piège : contrairement à OLS, model.fittedvalues n'est pas sur l'échelle de y ni une probabilité — c'est le log-odds brut, non borné ]-∞,+∞[ ; pour la probabilité (bornée 0-1), il faut model.predict(df) (cf. carte 'chaîne concrète' ci-dessous)

## Prédire une classe à partir d'une probabilité
Formule / Syntaxe: y_pred = (model.**predict**(df) > 0.5).astype(int)
Params: 0.5 : seuil de décision par défaut
Explication: au-dessus du seuil → classe 1, en dessous → classe 0 ; le seuil peut être ajusté selon le coût respectif des faux positifs / faux négatifs (cf. Erreurs de Type I/II, page Maths)

## La chaîne concrète, une valeur PAR LIGNE : de Xβ à la probabilité
Formule / Syntaxe:
```
$$\text{odds} = \dfrac{p}{1-p} \qquad \text{logit}(p) = \log(\text{odds}) = X\beta$$
logit_p = model.**fittedvalues**        # = X.β, log-odds brut du modèle
p       = model.**predict**(df)          # = sigmoïde(logit_p), la probabilité
odds    = p / (1 - p)                # = repasse de p aux odds
```
Params: logit_p, p, odds : trois Series de même longueur que df, un trio de valeurs par ligne — juste 3 façons d'exprimer la même chose
Explication: le modèle apprend une droite sur l'échelle logit (comme une régression linéaire classique) ; predict() applique la sigmoïde pour la ramener en probabilité (bornée 0-1, interprétable) ; repasser en odds est optionnel, seulement utile pour retrouver le lien direct avec les coefficients (ligne suivante)

## Interpréter un coefficient, une valeur PAR FEATURE : l'effet de βᵢ sur les odds
Formule / Syntaxe:
```
$$\text{OR}_i = \dfrac{\text{odds}(x_i+1)}{\text{odds}(x_i)} = e^{\beta_i}$$
import numpy as np
odds_ratios = np.**exp**(model.params)
```
Params: $\beta_i$ : coefficient de $x_i$ (model.params) — effet de +1 unité de $x_i$ sur logit(p), à additionner à Xβ ci-dessus
Explication: odds_ratios : Series indexée comme model.params (une valeur par feature + Intercept, pas par ligne) — OR_i (= exp(βᵢ)) est le rapport entre les odds à xᵢ+1 et les odds à xᵢ : le facteur multiplicatif sur les odds pour +1 unité de xᵢ, toutes les autres features fixées ; ex: odds_ratios["x1"]=1.01 ⇒ +1% des odds ; <1 ⇒ effet négatif sur la probabilité de succès
