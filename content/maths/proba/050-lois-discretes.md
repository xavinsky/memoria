---
title: Lois de probabilité discrètes
---

```math
\mathbb{E}[X] = \sum_{x} x \cdot P(X=x)
```

**Espérance** d'une variable aléatoire — moyenne théorique des valeurs de X, pondérée par leur probabilité : le résultat "attendu en moyenne" si on répète l'expérience un grand nombre de fois (cf. Loi des Grands Nombres, page suivante).

```math
P(\text{succès}) = p \qquad P(\text{échec}) = 1-p
```

**Loi de Bernoulli(p)** : une expérience, 2 issues complémentaires (succès/échec), $p\in[0,1]$.

```math
P(X=k) = \dbinom{n}{k}\,p^k(1-p)^{n-k}
```

**Loi Binomiale(n,p)** : proba d'obtenir exactement k succès sur n essais (`math.comb(n, k) * pow(p, k) * pow(1-p, n-k)`). $p^k(1-p)^{n-k}$ = proba d'un tirage particulier (ex: k succès puis n-k échecs), multipliée par $\binom nk$, le nombre de combinaisons possibles de k succès parmi n essais. Espérance : $\mathbb E[X]=np$ (ex: n=10, p=0.7 → E[X]=7).

```math
P(X=n) = (1-p)^{n-1}\,p
```

**Loi Géométrique(p)** : proba de réussir pour la 1ère fois au n-ième essai. $(1-p)^{n-1}$ = proba de n-1 échecs consécutifs, multipliée par $p$, la proba du succès qui suit — décroît de façon exponentielle avec n.
