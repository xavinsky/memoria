---
title: Train/test split — train_test_split (Holdout Method)
subgroup: Test
type: syntax
---

## Séparer train / test
Syntaxe:
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = **train_test_split**(X, y, test_size=0.3, random_state=88)
```
Résultat: ~70/30 usuel — random_state fixe le tirage aléatoire pour la reproductibilité

## Conserver les proportions de classes (target déséquilibrée)
Syntaxe: train_test_split(X, y, test_size=0.3, **stratify**=y, random_state=88)
Résultat: répartit chaque classe de y dans les mêmes proportions entre train et test — indispensable sur un dataset déséquilibré (cf. Balancing, groupe ml)

## Split en 3 : train / validation / test
Syntaxe:
```
X_tv, X_test, y_tv, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_tv, y_tv, test_size=0.25, stratify=y_tv)
```
Résultat: pas de split 3-voies natif dans Sklearn — on enchaîne deux train_test_split ; ici 60/20/20 (0.25 × 0.8 restant = 0.2)

## Piège : scorer un modèle sur ses données d'entraînement
Syntaxe:
```
model.fit(X_train, y_train)
model.score(**X_test**, **y_test**)  # jamais X_train, y_train
```
Résultat: sinon on mesure la mémorisation, pas la capacité à généraliser sur des données non vues

## Stratifier sur une FEATURE plutôt que la target
Syntaxe: train_test_split(X, y, **stratify**=X['col'], random_state=88)
Résultat: cross_validate(cv=5) stratifie AUTOMATIQUEMENT sur la target pour un classifieur (StratifiedKFold en interne), mais jamais sur une feature — à faire soi-même si une catégorie (ex: une feature binaire) doit rester équilibrée entre folds
