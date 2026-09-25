---
title: Feature Scaling (Standard / MinMax / Robust)
subgroup: Transformation
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## StandardScaler (standardiser)
Formule / Syntaxe:
```
$$z = \dfrac{x - mean}{std}$$
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.**fit**(df[['col']])
df[['col']] = scaler.**transform**(df[['col']])
```
Params: -
Explication: centre à 0 (μ=0) et réduit à écart-type 1 (σ=1) — sensible aux outliers ; bon choix par défaut pour la plupart des modèles (ex: régression linéaire, réseaux de neurones) — doubles crochets df[['col']] des deux côtés (cf. piège 2D/1D dans Valeurs manquantes)

## MinMaxScaler (normaliser)
Formule / Syntaxe:
```
$$X' = \dfrac{X - X_{min}}{X_{max}-X_{min}}$$
from sklearn.preprocessing import **MinMaxScaler**
```
Params: -
Explication: compresse dans [0,1] — préserve la sparsité (0 reste 0), ne réduit pas l'effet des outliers — utile pour features positives/sparse (ex: pixels) ou pour KNN

## RobustScaler
Formule / Syntaxe:
```
$$RobustScaled = \dfrac{x - median}{IQR}$$
from sklearn.preprocessing import **RobustScaler**
```
Params: IQR : écart interquartile Q3 − Q1
Explication: utilise médiane + IQR au lieu de moyenne + écart-type → moins sensible aux outliers que Standard/MinMax

## Fit sur train seulement, transform sur train ET test
Formule / Syntaxe:
```
scaler.**fit**(X_train)
X_train = scaler.**transform**(X_train)
X_test = scaler.**transform**(X_test)  # jamais de .fit() sur X_test
```
Params: -
Explication: cf. Data Leakage — fitter un scaler sur tout le dataset (avant le split) fait fuiter de l'information du test set dans l'entraînement

## Réassigner plusieurs colonnes scalées d'un coup, par leur nom
Formule / Syntaxe:
```
X_train[cols] = scaler.transform(X_train[cols])
X_train.columns  # ou : scaler.**get_feature_names_out**()
```
Params: cols : liste de colonnes numériques
Explication: évite de retaper les noms de colonnes à la main quand on scale plusieurs features en une seule fois (contrairement à df[['col']] utilisé ci-dessus pour une seule colonne) — même pattern que pour OneHotEncoder (cf. Encoding)

## Récupérer directement un DataFrame (pas un array)
Formule / Syntaxe:
```
scaler.**set_output**(transform='pandas')
X_scaled = scaler.fit_transform(X_num)  # DataFrame, colonnes/index conservés
```
Params: -
Explication: évite de ré-assembler soi-même noms de colonnes et index après transform() — marche pour n'importe quel transformer Sklearn (scaler, encoder...)

## Même réglage, pour TOUS les transformers d'un coup
Formule / Syntaxe:
```
from sklearn import set_config
**set_config**(transform_output="pandas")  # une seule fois, en tête de notebook
```
Params: -
Explication: équivalent global de .set_output(transform='pandas') — ⚠️ incompatible avec une sortie sparse : ajouter OneHotEncoder(sparse_output=False) sinon ValueError
