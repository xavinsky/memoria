---
title: Métriques de classification
subgroup: Métriques
---

**Matrice de confusion** — croise prédictions et réalité : TP (positif bien prédit), TN (négatif bien prédit), FP (faux positif : prédit positif à tort), FN (faux négatif : prédit négatif à tort). Base de toutes les métriques ci-dessous.

**Accuracy** — proportion de prédictions correctes, toutes classes confondues : trompeuse sur un dataset déséquilibré (un modèle qui prédit toujours la classe majoritaire peut avoir une accuracy élevée sans rien détecter) ; à réserver aux classes équilibrées.

```math
accuracy = \dfrac{TP+TN}{TP+TN+FP+FN}
```

**Recall** — capacité à détecter les occurrences réelles d'une classe : à privilégier quand rater un positif coûte cher (ex: fraude, maladie) ; augmente quand on baisse le seuil de décision (cf. [Precision-Recall Tradeoff](#ml-precision-recall-tradeoff), page Syntaxes).

```math
recall = \dfrac{TP}{TP+FN}
```

**Precision** — fiabilité d'une prédiction positive : à privilégier quand une fausse alerte coûte cher (ex: publicité ciblée, sécurité alimentaire) ; augmente quand on monte le seuil de décision.

```math
precision = \dfrac{TP}{TP+FP}
```

**F1 score** — moyenne harmonique de precision et recall : combine les deux en une seule métrique, utile pour comparer des modèles entre eux quand aucune des deux n'est clairement prioritaire.

```math
F_1 = 2\cdot\dfrac{precision \times recall}{precision + recall}
```

> [!TIP]
> 👉 Implémentation Sklearn de chacune, matrice de confusion et `classification_report` (cf. page Syntaxes ▸ [Métriques de classification](#ml-metrics-classification-syntax)).
