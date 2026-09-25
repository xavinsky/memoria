---
title: Cross-Validation
subgroup: Test
type: syntax
---

## Valider sur K sous-échantillons
Syntaxe:
```
from sklearn.model_selection import cross_validate
cv_results = **cross_validate**(model, X, y, cv=5)
cv_results['test_score'].mean()
```
Résultat: moyenne les scores sur K splits différents plutôt qu'un seul split — plus robuste qu'un simple train_test_split ; cv=5 (entier) choisit automatiquement KFold (régression) ou StratifiedKFold (classification), cf. Modélisation ▸ [Cross-Validation](#ml-cross-validation-concept)

## Variante : cross_val_score
Syntaxe:
```
from sklearn.model_selection import cross_val_score
**cross_val_score**(model, X, y, cv=5, scoring="r2").mean()
```
Résultat: renvoie directement un array de scores (une seule métrique, via scoring) au lieu du dict de cross_validate (test_score, fit_time, ...) — pratique pour un score rapide sans les à-côtés

## Classification : préserver les proportions de classes
Syntaxe:
```
from sklearn.model_selection import StratifiedKFold
cross_validate(model, X, y, **cv=StratifiedKFold(5)**)
```
Résultat: déjà le comportement par défaut si on passe cv=5 à un classifieur — utile à expliciter si on veut personnaliser (shuffle=True, random_state)

## Time Series : respecter l'ordre chronologique
Syntaxe:
```
from sklearn.model_selection import TimeSeriesSplit
cross_validate(model, X, y, **cv=TimeSeriesSplit(5)**)
```
Résultat: chaque fold d'entraînement précède chronologiquement son fold de test — jamais de shuffle (cf. page Modélisation ▸ Modèles ▸ Time Series ▸ [Décomposition](#ts-decomposition))

## Données groupées : garder chaque groupe entier dans un seul fold
Syntaxe:
```
from sklearn.model_selection import GroupKFold
cross_validate(model, X, y, **cv=GroupKFold(5)**, groups=groups)
```
Résultat: évite qu'un même groupe (ex: plusieurs lignes par patient/utilisateur) se retrouve à la fois en train et en test — sinon data leakage
