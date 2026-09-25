---
title: Choisir sa métrique
subgroup: Métriques
---

> [!TIP]
> 👉 Cette carte aide à CHOISIR — cliquer sur le nom d'une métrique renvoie à sa définition et sa formule (ci-dessous).

**Régression** — target continue

:::compare
- **[MSE / RMSE](#ml-metrics-regression)** : les grosses erreurs doivent être pénalisées plus que proportionnellement (ex: essai clinique)
- **[MAE](#ml-metrics-regression)** : chaque erreur pénalisée proportionnellement à sa taille (ex: prévision météo)
- **[Max Error](#ml-metrics-regression)** : borner l'erreur la plus grave (ex: sécurité)
- **[R²](#ml-metrics-regression)** : comparer des modèles/datasets entre eux, indépendamment de l'unité
:::

**Classification** — target catégorielle

:::compare
- **[Accuracy](#ml-metrics-classification)** : classes équilibrées, aucune classe prioritaire
- **[Recall](#ml-metrics-classification)** : coût élevé à rater un positif (faux négatif)
- **[Precision](#ml-metrics-classification)** : coût élevé à une fausse alerte (faux positif)
- **[F1](#ml-metrics-classification)** : compromis global entre precision et recall
- **[ROC-AUC](#ml-roc-auc)** : robustesse générale, indépendante du seuil
:::

**Compromis precision/recall** — les deux évoluent en sens inverse selon le seuil de décision (0.5 par défaut) : baisser le seuil augmente le recall (plus de points classés positifs) mais fait baisser la precision, et inversement (cf. [Precision-Recall Tradeoff](#ml-precision-recall-tradeoff), page Syntaxes, pour l'implémentation).
