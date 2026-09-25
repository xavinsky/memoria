---
title: Naive Bayes (classification de texte)
subgroup: Modèles
subsubgroup: NLP
---

[[P:MultinomialNB]]

Applique le théorème de Bayes (cf. [Théorème de Bayes](#bayes-naive-bayes), groupe Maths) pour classer un document à partir des mots qu'il contient — ex. classique : spam vs normal ("ham").

```math
P(S \mid x_1,...,x_k) = \dfrac{P(S)\prod_{i=1}^k P(x_i \mid S)}{P(S)\prod_{i=1}^k P(x_i \mid S) + P(N)\prod_{i=1}^k P(x_i \mid N)}
```

**Hypothèse "naïve"** — les mots d'un document sont supposés conditionnellement INDÉPENDANTS entre eux sachant la classe (ce qui est faux en réalité — d'où le nom), ce qui permet de remplacer $P(x_1,...,x_k \mid S)$ par le simple produit $\prod_i P(x_i \mid S)$.

> [!TIP]
> 👉 **Astuce argmax** — pour DÉCIDER de la classe, pas besoin de calculer le dénominateur (identique pour S et N, sert juste à normaliser) : $\arg\max$ du numérateur seul suffit. Point indépendant de l'hypothèse naïve ci-dessus (piège courant : l'argmax ne requiert AUCUNE indépendance, juste un dénominateur constant entre classes) — en pratique on somme des log-probabilités plutôt que multiplier des probabilités (évite l'underflow numérique sur beaucoup de mots) ; `predict_proba()` recalcule, lui, la vraie normalisation.

> [!WARNING]
> ⚠️ **Smoothing obligatoire** : si un mot du document à classer n'apparaît JAMAIS dans les exemples de spam vus à l'entraînement, $P(x_i \mid S) = 0$ annule tout le produit. On ajoute donc un paramètre de lissage α > 0 (souvent +1) aux fréquences de mots pour éviter les probabilités nulles.

:::compare
- **Avantages** : simple à implémenter, pas d'apprentissage itératif (rapide), gère bien un grand vocabulaire, aucun paramètre β/loss à ajuster
- **Inconvénient** : l'hypothèse d'indépendance des mots est fausse en pratique (le contexte compte) — reste malgré tout étonnamment performant
:::
