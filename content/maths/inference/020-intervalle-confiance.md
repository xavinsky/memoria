---
title: Intervalle de confiance
---

```math
\mu = \bar x \pm z^* \dfrac{\sigma}{\sqrt n}
```

```
from scipy.stats import norm
mu_estim = norm(x_bar, sigma / np.sqrt(n))
lower = mu_estim.**ppf**((1 - confidence) / 2)
upper = mu_estim.**ppf**((1 + confidence) / 2)
```

**Intervalle de confiance pour μ** — s'appuie directement sur le TCL (page précédente) : $\bar X \approx \mathcal N(\mu, \sigma/\sqrt n)$, donc $\mu$ est probablement proche de $\bar x$ (notre MLE), à $z^*\sigma/\sqrt n$ près. Ex: n=1000, x̄=170cm, s=20cm → IC95% = [168.7, 171.2]cm.

> [!TIP]
> ✅ "si on répétait l'échantillonnage plein de fois, 95% des intervalles construits contiendraient la vraie valeur μ"<br>❌ PAS "il y a 95% de chances que μ soit dans cet intervalle" — μ n'est pas aléatoire, c'est une valeur fixe (inconnue) ; c'est l'intervalle qui varie d'un échantillon à l'autre.

:::compare
- **1σ (68%)** : "likely"
- **90%** : "very likely"
- **2σ (95%)** : "extremely likely"
- **3σ (99.7%)** : "virtually certain"
- **5σ** : seuil de "preuve" en physique théorique
:::

**Taille d'échantillon n suffisante pour appliquer le TCL** : n > 30 → le TCL s'applique, on peut utiliser l'écart-type d'échantillon s pour approximer σ. n > 10 ET données non skewed / sans outliers → le TCL s'applique encore. Population déjà connue comme normale → le TCL s'applique quel que soit n, même très petit (à part : n < 10% × N pour considérer les tirages indépendants même sans remise).
