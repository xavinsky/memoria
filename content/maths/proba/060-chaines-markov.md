---
title: Chaînes de Markov
---

Modélise un système qui passe d'un **état** à un autre selon des probabilités de transition FIXES — **propriété de Markov** : seul l'état ACTUEL détermine les probabilités futures, peu importe comment on y est arrivé (pas de mémoire du passé).

```math
Q_{ij} = P(\text{état } j \text{ demain} \mid \text{état } i \text{ aujourd'hui})
```

**Matrice de transition Q** — chaque ligne i liste les probabilités de passer de l'état i vers chaque autre état ; chaque ligne SOMME À 1 (l'état suivant est certain, même si on ne sait pas lequel).

```math
P_{t+1} = P_t \cdot Q \qquad P_{t+n} = P_0 \cdot Q^n
```

$P_t$ = vecteur ligne de probabilités d'être dans chaque état au temps t. Avancer d'un pas = multiplier par Q ; avancer de n pas = multiplier par $Q^n$ (ou répéter la multiplication n fois).

> [!TIP]
> 👉 Beaucoup de chaînes convergent vers une **distribution stationnaire** ($P_{t+1} = P_t$, un point fixe de Q) après un grand nombre d'étapes — mais pas toutes (contre-exemple : un système à 2 états qui bascule à coup sûr à chaque étape ne converge jamais).

> [!TIP]
> 👉 Base du **PageRank** de Google (pages web = états, liens = transitions) et du **Markov Decision Process** en Reinforcement Learning (cf. groupe Reinforcement Learning) — un environnement RL suppose justement que l'état actuel suffit à décider de la suite, sans historique.
