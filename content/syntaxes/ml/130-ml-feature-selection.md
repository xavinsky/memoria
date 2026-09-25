---
title: Feature selection — corrélation & permutation importance
subgroup: Test
type: syntax
---

## Repérer les features redondantes (corrélation univariée)
Syntaxe:
```
corr = df.select_dtypes('number').**corr**()
corr_df = corr.stack().reset_index()
corr_df.columns = ['f1','f2','correlation']
```
Résultat: deux features très corrélées entre elles portent une information redondante — envisager d'en retirer une

## Piège : exclure la diagonale avant de trier
Syntaxe: corr_df = corr_df[corr_df['f1'] **!= corr_df['f2']**]
Résultat: chaque feature est corrélée à 1.0 avec elle-même — sans ce filtre, la diagonale (corrélation=1) noie le classement dès qu'on trie par force de corrélation

## Trier par force de corrélation
Syntaxe:
```
corr_df['abs_corr'] = corr_df['correlation'].**abs**()
corr_df.sort_values('abs_corr', ascending=False)
```
Résultat: sans abs(), une corrélation négative forte (-0.9) passerait après une positive faible (0.5) — trie par force du lien, pas par signe

## Feature Permutation Importance
Syntaxe:
```
from sklearn.inspection import permutation_importance
model.fit(X, y)
result = **permutation_importance**(model, X, y, n_repeats=10)
result.importances_mean
```
Résultat: n_repeats (nombre de mélanges aléatoires par feature) : mélange aléatoirement une feature et mesure la chute de score — grosse chute = feature importante, chute nulle/négative = feature peu utile

## Éliminer les features faibles et re-valider
Syntaxe:
```
weak = importance_df[importance_df['importance_mean'] <= 0]['feature']
X_reduced = X.**drop**(columns=weak)
cross_validate(model, X_reduced, y, cv=5)['test_score'].mean()
```
Résultat: seuil ≤ 0 : une importance nulle/négative signifie que mélanger la feature n'a pas dégradé (voire a amélioré) le score — comparer au score de base pour vérifier qu'il ne chute pas significativement
