---
title: Test d'hypothèse (p-value)
---

```math
H_0 \text{ (hypothèse par défaut, "rien ne change")} \qquad H_a \text{ (ce qu'on cherche à démontrer)}
```

Ex: $H_0$: μ=300s (le mode sombre ne change rien) — $H_a$: μ>300s (le mode sombre augmente le temps passé). **A/B test** = nom donné en pratique (produit/data) à un test d'hypothèse appliqué à une expérience : control group (groupe témoin) vs. treatment group (groupe traitement) — (1) assigner aléatoirement les utilisateurs aux deux groupes, (2) comparer les résultats avec un test d'hypothèse classique.

```math
\text{p-value} = P(\bar X \ge \text{valeur observée} \mid H_0 \text{ vraie})
```

> [!WARNING]
> ⚠️ La **p-value** (`1 - norm(mu0, sigma/np.sqrt(n)).cdf(valeur_observee)`) est la probabilité d'observer un résultat au moins aussi extrême que celui mesuré, EN SUPPOSANT que $H_0$ est vraie — ce n'est PAS la probabilité que $H_0$ soit vraie (piège d'interprétation classique).

```math
\text{p-value} < \alpha \Rightarrow \text{on rejette } H_0 \text{ au profit de } H_a
```

**Règle de décision** ($\alpha$ = seuil de significativité, choisi AVANT l'expérience, souvent 0.05) — "on ne rejette pas $H_0$" ne veut pas dire "on accepte $H_0$", on manque juste de preuve pour la rejeter. Ne jamais changer $\alpha$ après coup pour faire pencher la décision dans le sens voulu.

:::compare
- **Type I (faux positif)** : rejeter $H_0$ alors qu'elle est vraie, proba = $\alpha$
- **Type II (faux négatif)** : ne pas rejeter $H_0$ alors qu'elle est fausse, proba = $\beta$
:::

```math
\text{Puissance} = 1 - \beta
```

**Puissance** = proba de détecter un effet réel quand il existe vraiment (ex: ne pas passer à côté d'une feature qui marche, ou d'un médicament efficace) — plus elle est grande, mieux c'est.
