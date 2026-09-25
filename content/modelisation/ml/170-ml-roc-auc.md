---
title: ROC-AUC
subgroup: Métriques
---

**Courbe ROC** — trace le compromis TPR (recall) vs FPR pour TOUS les seuils de décision possibles, pas un seul comme Accuracy/Precision/Recall/F1.

```math
TPR = recall = \dfrac{TP}{TP+FN} \qquad FPR = \dfrac{FP}{FP+TN}
```

**AUC (Area Under Curve)** — aire sous la courbe ROC, ∈ [0,1] (0.5 = aléatoire, 1 = parfait) : mesure la capacité du modèle à distinguer les deux classes sur tous les seuils à la fois, sans dépendre d'un seuil choisi ; bonne métrique générale pour comparer des modèles entre eux.

**PR-AUC (Average Precision)** — aire sous la courbe precision-recall : à préférer à l'AUC-ROC sur un dataset FORTEMENT déséquilibré (l'AUC-ROC reste optimiste, le grand nombre de vrais négatifs écrasant le FPR ; la PR-AUC se concentre sur la classe positive rare).

> [!TIP]
> 👉 Implémentation Sklearn (`roc_curve`, `roc_auc_score`, `average_precision_score`) — cf. page Syntaxes ▸ [ROC-AUC](#ml-roc-auc-syntax).
