---
title: Résoudre un système linéaire par inversion de matrice
---

```math
y = X\theta
```

Un système de n équations à n inconnues (ex: n appartements observés, n coefficients θ à trouver) s'écrit sous forme matricielle : X (n×n, une ligne par observation, une colonne par feature + une colonne de 1 pour l'intercept), θ (n×1, les coefficients cherchés), y (n×1, les cibles observées).

```math
\theta = X^{-1} y
```

Si **X est carrée et inversible**, la solution est exacte : multiplier à gauche par $X^{-1}$ (`np.linalg.inv(X)`, ou directement `np.linalg.solve(X, y)`, plus stable numériquement) isole θ. Vérifier $X^{-1}X = I$ avec `np.allclose()` plutôt qu'une égalité stricte (erreurs d'arrondi flottant).

> [!TIP]
> 👉 **Déterminant** — scalaire qui caractérise une matrice carrée et permet de tester l'inversibilité SANS calculer $X^{-1}$ : déterminant = 0 ⇔ matrice NON inversible (`np.linalg.det(X)`), équivalent à dire que ses colonnes sont colinéaires (rang < nombre de colonnes).

> [!WARNING]
> ⚠️ **Système surdéterminé (plus d'équations que d'inconnues, n_lignes > n_colonnes)** : X n'est plus carrée, donc pas inversible — `np.linalg.solve` lève `LinAlgError`. Pas de solution exacte qui satisfasse toutes les équations à la fois (ex: un 5ᵉ appartement observé ne colle jamais parfaitement à un modèle calibré sur 4). C'est exactement le problème que la régression linéaire (OLS) résout : au lieu d'une solution exacte, trouver le θ qui minimise l'erreur globale — cf. $\hat\beta=(X^\top X)^{-1}X^\top Y$ ci-dessous, qui généralise cette même idée d'inversion à un système non carré.
