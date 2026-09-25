---
title: Embedding appris pour la tâche — layers.Embedding
subgroup: LLM
subsubgroup: NLP
---

[[P:Embedding]]

Option 1 : apprendre un embedding SPÉCIFIQUE à la tâche en cours. `layers.Embedding` est une couche à part entière, dont les poids (= les vecteurs de chaque mot) sont appris comme n'importe quelle autre couche pendant `model.fit()`.

```math
X.shape = (n_{phrases},\ max\_length,\ embedding\_dim)
```

En amont, chaque phrase est **tokenisée** (mot → entier, via `Tokenizer`) puis **paddée** (cf. Séquences de longueurs différentes, ci-dessus) pour obtenir des séquences d'entiers de même longueur — c'est CE tensor d'entiers qui est passé en entrée de la couche `Embedding`, qui le transforme en vecteurs.

```math
n_{param} = (vocab\_size + 1) \times embedding\_dim
```

Le "+1" correspond à l'entier 0 réservé au padding. Ex: 10 000 mots en 100 dimensions ≈ 1M de paramètres rien que pour cette couche.

> [!WARNING]
> ⚠️ Plus l'espace d'embedding est grand, plus le modèle a de paramètres à apprendre → epochs plus lents ET convergence plus lente. Un embedding appris "from scratch" peut être long à entraîner.
