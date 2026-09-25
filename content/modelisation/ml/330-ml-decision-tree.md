---
title: Arbre de décision — Gini & croissance
subgroup: Modèles
---

[[NP:DecisionTreeClassifier]] · [[NP:DecisionTreeRegressor]]

Modèle hiérarchique — sépare les données par une suite de décisions binaires (feature, seuil), utilisable en classification comme en régression, capture des relations non-linéaires.

```math
\text{Gini}(node) = 1 - \sum_i p_i^2
```

**Gini Index** — mesure l'impureté d'un nœud (entre 0 et 1, plus bas = mieux) ; $p_i$ = proportion d'observations de la classe $i$ dans ce nœud. Un nœud pur (une seule classe) a un Gini de 0.

1. Partir du nœud racine (tout le dataset)
2. Essayer toutes les combinaisons (feature, seuil) possibles, chacune séparant le dataset en 2 nœuds enfants
3. Pour chaque combinaison, calculer le Gini moyen pondéré des 2 enfants
4. Garder la combinaison qui minimise ce Gini pondéré (nœuds enfants les plus "purs")
5. Répéter récursivement sur chaque nouveau nœud, jusqu'à ce qu'aucune coupure n'améliore plus l'impureté

> [!TIP]
> 👉 **Arbre de régression** : même principe mais avec la SSR (somme des carrés des résidus) à la place du Gini — le seuil retenu minimise la SSR pondérée des deux côtés.

> [!WARNING]
> ⚠️ **Sans limite, un arbre overfit quasi toujours** (pousse jusqu'à isoler chaque point) — se règle avec `max_depth` (profondeur max), `min_samples_split` (nombre min d'observations pour couper un nœud), `min_samples_leaf` (nombre min d'observations pour être une feuille).

:::compare
- **Avantages** : pas de scaling nécessaire, robuste aux outliers, interprétable (visualisable), capture le non-linéaire, donne une feature_importance\_ (basée sur la baisse de Gini apportée par chaque feature)
- **Inconvénients** : haute variance (un petit changement dans les données change beaucoup la structure de l'arbre), entraînement lent si profondeur importante, coupures toujours "orthogonales" aux axes des features (une PCA en amont peut aider à réorienter les données)
:::

> [!TIP]
> 👉 `predict_proba()` d'un arbre n'est PAS une vraie probabilité calibrée — c'est juste la proportion de chaque classe dans la feuille atteinte (contrairement à une régression logistique).
