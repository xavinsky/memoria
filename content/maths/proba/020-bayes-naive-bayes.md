---
title: Théorème de Bayes
---

```math
P(A \mid B) = \dfrac{P(B \mid A)\,P(A)}{P(B)}
```

**Théorème de Bayes** — permet d'inverser une conditionnelle : passer de P(B|A) (facile à estimer) à P(A|B) (ce qu'on veut vraiment). Se déduit de la conditionnelle en y substituant la règle du produit (page précédente) ; le $P(B)$ du dénominateur se calcule souvent via la loi des probabilités totales.

:::compare
- **P(A) — prior** : proba de A avant d'observer B
- **P(B|A) — vraisemblance** : proba de B si A est vrai
- **P(A|B) — posterior** : proba de A après avoir observé B
:::

```math
p(H \mid \text{data}) \propto p(\text{data} \mid H)\,p(H)
```

**Inférence bayésienne** : mettre à jour une croyance (prior → posterior). Ex : on lance une pièce n=10 fois pour estimer sa probabilité de faire face H — on observe $\bar x = 0.7$.

:::compare
- **Sans prior informatif (ou prior uniforme)** : la vraisemblance domine, posterior ≈ $\mathcal N(0.7,\, s/\sqrt n)$ — 0.7 est le MLE (Maximum Likelihood Estimate)
- **Avec un prior informatif** : ex: on pense la pièce probablement équilibrée, $p(H)=\mathcal N(0.5, 0.3)$ — Bayes combine prior et vraisemblance pour un posterior entre les deux ; plus on a de données, moins le prior pèse face à la vraisemblance
:::

```math
\text{MLE} = \arg\max_H\,p(\text{data}\mid H) \qquad \text{MAP} = \arg\max_H\,p(H\mid\text{data})
```

:::compare
- **MLE (Maximum Likelihood Estimate)** : sommet de la vraisemblance $p(\text{data}\mid H)$ — ignore le prior
- **MAP (Maximum A Posteriori)** : sommet du posterior $p(H\mid\text{data})$ — tient compte du prior
:::

> [!TIP]
> 💡 Avec un prior plat (non informatif), MAP = MLE ; plus le prior est informatif, plus MAP s'écarte du MLE en se rapprochant du prior.
