---
title: Régularisation (Ridge / Lasso / ElasticNet)
subgroup: Régularisation & Tuning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Ridge (pénalité L2)
Syntaxe:
```
from sklearn.linear_model import Ridge
model = **Ridge**(alpha=0.2)
```
Params: alpha : force de la régularisation (α grand → plus de bias, moins de variance)
Explication: pénalise les gros coefficients sans jamais les mettre à 0 — bon choix par défaut si toutes les features comptent un peu

## Lasso (pénalité L1)
Syntaxe:
```
from sklearn.linear_model import Lasso
model = **Lasso**(alpha=0.2)
```
Params: alpha : idem Ridge
Explication: peut ramener des coefficients exactement à 0 → fait aussi office de sélection de features (meilleure interprétabilité)

## ElasticNet (L1 + L2)
Syntaxe:
```
from sklearn.linear_model import ElasticNet
model = **ElasticNet**(alpha=1, l1_ratio=0.2)
```
Params: l1_ratio : proportion L1/L2 (0 = Ridge pur, 1 = Lasso pur)
Explication: moyenne pondérée Ridge/Lasso — 2 hyperparamètres à tuner (cf. page Modélisation ▸ Régularisation pour le détail des formules)

## ⚠️ Toujours scaler avant de régulariser
Syntaxe: StandardScaler().fit_transform(X)  # AVANT Ridge/Lasso/ElasticNet
Params: -
Explication: sinon chaque βᵢ n'est pas pénalisé équitablement (cf. Feature Scaling)
