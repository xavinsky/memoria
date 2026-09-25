---
title: Discretizing — pourquoi/quand discrétiser
subgroup: Data Preparation
---

Transforme une variable continue en catégories (ex: prix → Low/High) — change la NATURE du problème : une tâche de régression devient une tâche de classification.

:::compare
- **Pourquoi discrétiser** : simplifie l'interprétation ("prix élevé" plutôt qu'un chiffre précis), robustesse à des variations continues sans grande importance métier, ou tâche métier naturellement catégorielle (ex: churn oui/non plutôt qu'une probabilité).
- **Coût** : perte d'information — deux valeurs proches d'un seuil de coupure se retrouvent dans deux classes différentes ; les bornes doivent être choisies avec soin (cf. `pd.cut`, page Syntaxes).
:::

> [!TIP]
> 👉 Discrétiser change la métrique d'évaluation attendue : on passe de R²/MSE (régression) à accuracy/F1 (classification) — cf. [Choisir sa métrique](#ml-choose-metric).
