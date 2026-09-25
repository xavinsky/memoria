---
title: K-Means — Clustering
subgroup: Modèles
---

[[P:KMeans]]

**Clustering** = regrouper des observations similaires SANS target connue (non-supervisé) — contrairement à la classification, les "classes" (clusters) ne sont pas données à l'avance, elles émergent des données.

> [!TIP]
> 👉 Fonctionne mieux sur des données déjà bien séparées géométriquement — appliquer une PCA en amont aide souvent (les distances euclidiennes sont plus fiables en dimension réduite, cf. PCA ci-dessus).

1. Choisir le nombre de clusters K
2. Initialiser K centroïdes au hasard
3. Calculer la distance de chaque point à chaque centroïde
4. Assigner chaque point au centroïde le plus proche (un cluster se forme)
5. Recalculer chaque centroïde comme la moyenne des points de son cluster, puis répéter depuis l'étape 3

**Loss = inertia** — somme des distances au carré entre chaque point et le centroïde de son cluster (within-cluster sum of squares) ; `.fit()` cherche les centroïdes qui la minimisent, exactement comme `.fit()` minimise une Loss pour un modèle supervisé (cf. [Que fait .fit() ?](#ml-fit-hood), ci-dessous).

```math
inertia = \sum_{j=1}^{K}\sum_{x_i \in C_j} \lVert x_i - \mu_j \rVert^2
```

**Choisir l'hyperparamètre K** — même logique que pour PCA : méthode du coude sur l'inertia (`.inertia_`) pour plusieurs valeurs de K.

> [!TIP]
> 👉 K-Means peut aussi **prédire** le cluster d'une nouvelle donnée (`.predict()`), contrairement à un clustering purement descriptif — utile pour classer un nouveau point selon les groupes déjà trouvés.

**Cas d'usage** : segmentation client, exploration/visualisation de données, détection d'anomalies, classification semi-supervisée.
