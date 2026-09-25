---
title: PCA — réduction de dimension
subgroup: Unsupervised Learning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## PCA — fit + projeter
Syntaxe:
```
from sklearn.decomposition import PCA
pca = **PCA**(n_components=3)
X_proj = pca.**fit_transform**(X)
```
Params: n_components : k dimensions gardées
Explication: toujours scaler (StandardScaler) avant de fitter une PCA — cf. page Modélisation ▸ PCA

## Variance expliquée par composante
Syntaxe: pca.**explained_variance_ratio_**
Params: -
Explication: sert à choisir k avec la méthode du coude (cf. Modélisation ▸ PCA)

## Choisir k via un seuil de variance cumulée
Syntaxe:
```
cum_var = np.**cumsum**(pca.explained_variance_ratio_)
k = int(np.argmax(cum_var >= 0.80) + 1)
```
Params: seuil (ex: 0.80)
Explication: alternative chiffrée à la méthode du coude — plus petit k qui atteint au moins X% de variance cumulée totale

## Revenir à l'espace d'origine (approx.)
Syntaxe: X_reconstructed = pca.**inverse_transform**(X_proj)
Params: -
Explication: reconstruction imparfaite si k < nombre de features initial (perte d'info)

## Chercher k par GridSearch, dans un pipeline
Syntaxe:
```
pipe = make_pipeline(PCA(), SVC())
GridSearchCV(pipe, {'**pca__n_components**': [50,100,200,300]}, cv=5)
```
Params: -
Explication: laisse la cross-validation trancher k au lieu d'un seuil de variance fixé à l'avance — syntaxe étape__param, cf. GridSearch un pipeline (groupe ml, Model Tuning)
