---
title: Nettoyer — Valeurs manquantes
subgroup: Exploration & Nettoyage
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Compter les NaN par colonne (nombre / %)
Syntaxe:
```
df.**isnull**().sum().sort_values(ascending=False)
df.**isnull**().sum() / len(df)   # en proportion
```
Params: -
Explication: -

## Imputer avec SimpleImputer
Syntaxe:
```
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")
imputer.**fit**(df[['col']])
df[['col']] = imputer.**transform**(df[['col']])
imputer.**statistics_**
```
Params: -
Explication: strategy : mean, median, most_frequent, constant — .fit() apprend la valeur de remplacement, .transform() l'applique (logique commune à tous les transformers Sklearn) — garder les doubles crochets df[['col']] des DEUX côtés (et pas df['col'] à gauche) marche pour toutes les colonnes, numériques ou catégorielles

## Piège (si jamais assigné en simple crochet df['col'])
Syntaxe: df['col'] = imputer.transform(df[['col']]).**ravel**()  # ou .flatten()
Params: -
Explication: transform() renvoie toujours un array **2D** (n,1) ; assigné à df['col'] (Series 1D), ça passe silencieusement sur une colonne numérique (pandas squeeze tout seul) mais lève une ValueError sur une colonne texte/objet (ex: most_frequent) — le plus simple est d'éviter le problème en assignant à df[['col']] (double crochets) plutôt que d'ajouter .ravel()

## Imputer avec KNNImputer
Syntaxe:
```
from sklearn.impute import KNNImputer
imputer = **KNNImputer**(n_neighbors=5)
df[cols] = imputer.fit_transform(df[cols])
```
Params: n_neighbors : nb de voisins utilisés pour la moyenne
Explication: remplace par la moyenne des k plus proches voisins (sur les AUTRES colonnes) au lieu d'une statistique globale — scaler les features avant (sensible à l'échelle, comme tout KNN)
