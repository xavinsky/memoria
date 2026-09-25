---
title: Régression linéaire (OLS) — solution mathématique
---

```math
Y = X\beta + u
```

**Écriture matricielle du modèle** ($Y$ : vecteur cible n×1, $X$ : matrice des features n×p avec une colonne de 1 pour l'intercept, $\beta$ : coefficients p×1, $u$ : erreurs résiduelles) — forme équivalente à la formule texte "y ~ x1 + x2 + ..." (cf. statsmodels, Syntaxes).

```math
\hat\beta = (X^\top X)^{-1} X^\top Y
```

**Solution exacte** qui minimise la somme des carrés des résidus, obtenue en annulant la dérivée de $\|u\|^2$ par rapport à $\beta$ — c'est ce calcul que `.fit()` effectue en interne, **pas de descente de gradient nécessaire** pour l'OLS.

> [!WARNING]
> ⚠️ **Condition d'existence de la solution** : $(X^\top X)^{-1}$ n'existe que si X est de rang plein, i.e. rank(X) = nombre de features — sinon (features parfaitement colinéaires), pas de solution unique pour β. Vérifiable avec `np.linalg.matrix_rank(X)`, à relier au Cond. No. de `.summary()`.
