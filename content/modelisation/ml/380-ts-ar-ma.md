---
title: AR & MA (processus autorégressifs et moyenne mobile)
subgroup: Modèles
subsubgroup: Time Series
---

```math
AR(p): \quad Y_t = \alpha + \beta_1 Y_{t-1} + \beta_2 Y_{t-2} + \cdots + \beta_p Y_{t-p} + \epsilon_t
```

**AR (AutoRegressive)** — régression linéaire multivariée de Y sur ses propres valeurs passées ; les coefficients βᵢ (lus sur la PACF, cf. ci-dessus) mesurent l'influence isolée de chaque lag. Un choc (ϵ) se propage loin dans le futur — pas nécessairement stationnaire (ex intuitif : un choc économique dont l'effet s'atténue progressivement mais dure plusieurs périodes).

```math
MA(q): \quad Y_t = \alpha + \epsilon_t + \phi_1 \epsilon_{t-1} + \phi_2 \epsilon_{t-2} + \cdots + \phi_q \epsilon_{t-q}
```

**MA (Moving Average)** — combinaison linéaire de chocs aléatoires récents (pas des valeurs de Y). Un choc n'a d'effet que pendant q périodes puis disparaît complètement — toujours stationnaire (ex intuitif : un système de chauffage qui absorbe une perturbation ponctuelle en 2-3 minutes).

:::compare
- **AR(p) — mémoire longue** : lu sur la PACF (cutoff au lag p) — un choc influence indéfiniment, avec une décroissance progressive
- **MA(q) — mémoire courte** : lu sur l'ACF (cutoff au lag q) — un choc influence exactement q périodes puis s'arrête net
:::
