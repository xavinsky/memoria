---
title: t-test (petits échantillons)
---

**Pourquoi pas un z-test ?** Le z-score $Z=\frac{\bar X-\mu}{\sigma/\sqrt n}$ suppose $\sigma$ (écart-type de la population) connu — si $n$ est petit et $\sigma$ inconnu, on doit l'estimer par $s$ (écart-type d'échantillon), ce qui rend l'approximation par $\mathcal N(0,1)$ imprécise.

```math
T = \dfrac{\bar X - \mu}{s/\sqrt n} \sim T_{n-1}
```

**Statistique t** (`(x_bar - mu0) / (s / n**0.5)`, $s$ = écart-type d'échantillon avec correction de Bessel) — même construction que le z-score, mais en remplaçant $\sigma$ (inconnu) par son estimation $s$ : cette substitution introduit une incertitude supplémentaire, d'où une loi différente (**Student**, $n-1$ degrés de liberté) plutôt que Normale.

**Loi de Student $T_\nu$** — queues plus "épaisses" que la loi Normale (plus de chances d'observer une valeur extrême) ; $T_\nu \to \mathcal N(0,1)$ quand $\nu\to\infty$ : avec beaucoup de données, t-test et z-test convergent (accessible via `scipy.stats.t`).

> [!TIP]
> 👉 Une fois $T$ à la place de $Z$, tout le reste fonctionne pareil : intervalle de confiance via la cdf de Student, p-value et décision du test — il faut juste bien choisir le nombre de degrés de liberté ($n-1$).
