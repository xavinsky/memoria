---
title: Algèbre linéaire — résoudre un système, empiler des tableaux
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Produit matriciel
Syntaxe: a **@** b
Params: -
Explication: équivalent générique de np.dot(a, b) / np.matmul(a, b) — opérateur Python, pas une fonction spécifique à un cours

## Inverser une matrice carrée
Syntaxe: X_inv = np.linalg.**inv**(X)
Params: -
Explication: X : array carré (n,n) — condition nécessaire (X non carrée ⇒ erreur)

## Résoudre Xθ=y directement (plus stable que inv())
Syntaxe: theta = np.linalg.**solve**(X, y)
Params: -
Explication: évite de calculer explicitement X⁻¹ — équivalent numériquement plus stable de np.linalg.inv(X) @ y ; lève LinAlgError si X n'est pas carrée (système sur/sous-déterminé, cf. Maths ▸ Résoudre un système linéaire)

## Rang d'une matrice
Syntaxe: np.linalg.**matrix_rank**(X)
Params: -
Explication: rang < nb de colonnes ⇒ colonnes colinéaires, X non inversible (cf. Maths ▸ OLS — solution mathématique, condition d'existence de β̂)

## Trace (somme des éléments diagonaux)
Syntaxe: np.**diag**(X).sum()
Params: -
Explication: raccourci de np.diag(X) (extrait la diagonale) + .sum()

## Déterminant
Syntaxe: np.linalg.**det**(X)
Params: X : matrice carrée
Explication: det(X)=0 ⇔ X n'est PAS inversible (mêmes matrices singulières que rang < n colonnes, cf. matrix_rank ci-dessus) — deux façons différentes de détecter la même chose

## Comparer deux tableaux flottants (tolère les erreurs d'arrondi)
Syntaxe: np.**allclose**(a, b)
Params: -
Explication: bool — préférer à une égalité stricte a==b, qui échoue souvent à cause de la précision flottante

## Empiler des colonnes côte à côte
Syntaxe: X = np.**hstack**((x0, features))
Params: -
Explication: x0, features : même nombre de lignes — ex: ajouter une colonne de 1 (intercept) à une matrice de features

## Empiler des lignes (ajouter des observations)
Syntaxe: X_updated = np.**vstack**([X, nouvelle_ligne])
Params: -
Explication: X, nouvelle_ligne : même nombre de colonnes — ex: ajouter une nouvelle observation à un dataset existant
