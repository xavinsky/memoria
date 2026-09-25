---
title: Stratégies multiclasse (One-vs-Rest vs One-vs-One)
subgroup: Modèles
---

Certains classifieurs sont nativement BINAIRES (2 classes seulement). Pour les étendre à un problème à k classes, deux stratégies génériques combinent plusieurs classifieurs binaires — utilisables avec n'importe quel modèle de base.

:::compare
- **One-vs-Rest (OvR / One-vs-All)** : entraîne k modèles, chacun "cette classe" vs "toutes les autres" combinées — à la prédiction, la classe de plus forte probabilité l'emporte. Moins coûteux (k modèles), mais dilue les différences propres à chaque paire de classes
- **One-vs-One (OvO)** : entraîne un modèle par PAIRE de classes (k(k-1)/2 modèles) — à la prédiction, vote majoritaire entre tous les sous-modèles. Capture mieux les différences spécifiques à chaque paire, mais le nombre de modèles explose avec k
:::

> [!TIP]
> 👉 Beaucoup de modèles Sklearn (LogisticRegression, SVC...) gèrent déjà nativement le multiclasse en interne (souvent OvR par défaut) — `OneVsRestClassifier`/`OneVsOneClassifier` ne sont utiles que pour FORCER une stratégie précise, ou l'appliquer à un modèle purement binaire.
