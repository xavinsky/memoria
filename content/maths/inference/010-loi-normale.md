---
title: Loi normale, LGN & Théorème Central Limite
---

```math
\mathcal{N}(\mu,\sigma) := f_{\mu,\sigma}(x) = \dfrac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
```

**Densité de probabilité (pdf)** d'une loi Normale N(µ,σ) (`norm(mu, sigma).pdf(x)`) — sert à tracer la courbe en cloche et calculer sa hauteur en un point x (ce n'est pas directement une probabilité). On note $X\sim\mathcal N(\mu,\sigma)$ pour dire que X suit cette loi, càd que sa densité est $f(x)$.

```math
\bar X = \dfrac{1}{n}\sum_{i=1}^{n} X_i \qquad \bar X \xrightarrow[n\to\infty]{} \mathbb{E}[X]
```

**Moyenne d'échantillon** (`samples.mean()`) et **Loi des Grands Nombres (LGN)** — garantit que $\bar X$ se rapproche de la vraie espérance théorique $\mathbb E[X]$ quand on multiplie les observations (espérance et variance doivent être finies).

```math
\bar X \approx_{n\to\infty} \mathcal{N}\!\left(\mu, \dfrac{\sigma}{\sqrt{n}}\right)
```

**Théorème Central Limite (TCL)** — quelle que soit la loi des $X_i$, l'approximation de $\bar X$ par une loi Normale s'affine quand n augmente (écart-type $\sigma/\sqrt n$ de plus en plus petit). $\sigma$ doit être fini.

```math
z = \dfrac{x-\mu}{\sigma} \qquad \Phi(z) = P(Z \le z) = \displaystyle\int_{-\infty}^{z} f_{0,1}(t)\,dt
```

**Score-z** (`(x - mu) / sigma`) : standardise une observation pour la comparer à la loi Normale centrée réduite N(0,1) ($\sigma>0$). **Φ(z)** (`norm.cdf(z)`) = aire sous la courbe de $\mathcal N(0,1)$ jusqu'à z, c'est la probabilité cumulée $P(Z\le z)$ — c'est ainsi qu'on en déduit une probabilité.
