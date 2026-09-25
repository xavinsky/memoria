---
title: Combinatoire (factorielle, combinaisons)
---

```
import **math**
```

```math
n! = 1\times2\times...\times n
```

**Factorielle** (`math.factorial(n)`, $n$ entier ≥ 0) — nombre de façons d'ordonner (permuter) un n-uplet de n éléments distincts.

```math
A_n^k = \dfrac{n!}{(n-k)!}
```

**Arrangements de k parmi n** (`math.perm(n, k)`, sélection ordonnée sans répétition) — n possibilités pour le 1er élément choisi, n-1 pour le 2e, ..., n-k+1 pour le k-ième ($n\times(n-1)\times...\times(n-k+1)$) : il manque $(n-k)!$ pour retrouver $n!$.

```math
\dbinom{n}{k} = \dfrac{A_n^k}{k!} = \dfrac{n!}{k!\,(n-k)!}
```

**Combinaisons de k parmi n** (`math.comb(n, k)`, choix non ordonné) — Arrangement = Permutation × Combinaison.

```math
2^n
```

nombre total de résultats pour n tirages à 2 issues (pile/face) — ex: $2^4=16$ combinaisons possibles.

```math
P = \dfrac{\text{possibilités favorables}}{\text{possibilités totales}}
```
