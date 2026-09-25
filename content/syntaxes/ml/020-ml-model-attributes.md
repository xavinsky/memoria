---
title: Travailler avec un estimator déjà choisi
subgroup: Choix du modèle
type: syntax
---

## Coefficients appris (régression linéaire)
Syntaxe:
```
model.**coef_**
model.**intercept_**
```
Résultat: pente(s) a et ordonnée à l'origine b — attributs suffixés _ par convention Sklearn (disponibles seulement après fit)

## Trouver les valeurs valides d'un paramètre (ex: strategy)
Syntaxe:
```
**SimpleImputer?**  # Jupyter : ouvre la docstring
# ou Shift+Tab dans SimpleImputer(strategy=|)
# ou provoquer l'erreur exprès :
SimpleImputer(strategy="bogus").fit([[1],[2]])
```
Résultat: le message d'erreur liste les valeurs acceptées : "... must be a str among {'most_frequent', 'constant', 'median', 'mean'}..." — marche pour n'importe quel paramètre/classe Sklearn
