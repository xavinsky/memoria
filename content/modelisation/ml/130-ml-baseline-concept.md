---
title: Baseline — pourquoi comparer avant de complexifier
subgroup: Métriques
---

Un score seul ne veut RIEN dire sans référence : 92% d'accuracy est excellent si un modèle trivial plafonne à 70%, mais médiocre s'il atteint déjà 91%. La **Baseline** est ce modèle trivial — le plancher minimal à battre avant de juger qu'un modèle "réel" apporte quelque chose.

:::compare
- **DummyRegressor** : prédit toujours la même valeur, quel que soit X — la moyenne (par défaut), la médiane, ou une constante choisie
- **DummyClassifier** : prédit toujours la classe majoritaire (par défaut), ou tire au hasard selon les proportions de classes observées (stratified) / de façon uniforme (uniform)
:::

> [!TIP]
> 👉 **Repère pratique** (rasoir d'Ockham) : commencer simple, ne complexifier que si ça bat clairement la baseline — un modèle sophistiqué qui ne fait pas mieux qu'une constante n'apporte rien, et un score "élevé" peut simplement refléter un déséquilibre des classes plutôt qu'un vrai apprentissage.
