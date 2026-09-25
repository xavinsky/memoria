---
title: Bias/Variance tradeoff & Learning Curves
subgroup: Test
---

:::compare
- **Bias (underfitting)** : le modèle est trop simple pour capter les patterns des données — scores train ET test bas
- **Variance (overfitting)** : le modèle capte le bruit en plus du signal — score train haut, score test bas
:::

> [!TIP]
> 💡 **No Free Lunch Theorem** : aucun modèle n'est optimal pour tous les problèmes — le choix dépend des hypothèses faites sur les données.

**Pas de variable dédiée** : Sklearn n'a pas d'attribut `model.bias_` ou `model.variance_` — on lit les deux séparément à partir de `train_score` et `test_score` (cf. `return_train_score`, groupe Model Tuning).

|  | train_score | test_score |
|---|---|---|
| Low bias, low variance (idéal) | élevé | élevé, proche du train |
| High bias (underfitting) | bas | bas |
| High variance (overfitting) | élevé | nettement plus bas que train |

```
from sklearn.model_selection import learning_curve
train_sizes, train_scores, test_scores = **learning_curve**(estimator=model, X=X, y=y, train_sizes=[...], cv=5)
train_scores.mean(axis=1)  # score moyen train par taille
test_scores.mean(axis=1)   # score moyen test par taille
```

**Courbes d'apprentissage** — évalue les scores train/test pour des tailles croissantes de training set : diagnostique underfitting / overfitting / besoin de plus de données.

**Lecture des courbes** : convergence + plateau haut = idéal ; convergence + plateau bas = underfitting (plus de données n'aidera pas) ; écart persistant train ≫ test = overfitting (plus de données peut aider).

> [!TIP]
> 👉 **Repère chiffré** : écart de 0-5% entre cross-val et test set = normal ; 5-10% = ok mais limite ; +10% = overfitting (le modèle a mémorisé le train plutôt que généralisé) — à ajuster selon le contexte, mais donne un premier seuil d'alerte rapide.
