---
title: Choisir son modèle
subgroup: Concepts Modèles
---

![](../../diagrams/ml-model-selection-1.svg)

:::category Classification {#cat-classification}
prédire une catégorie parmi un nombre fini de classes connues : target discrète, labels disponibles.
:::

| Échantillons | Données textuelles ? | Modèle(s) à essayer d'abord | Si insuffisant |
|---|---|---|---|
| <100K | Oui | [[P:MultinomialNB\|Naive Bayes\|nlp-naive-bayes]] | \- |
| <100K | Non | [[P:LogisticRegression\|Régression logistique\|ml-linear-logistic]] / [[P:LinearSVC\|SVM linéaire]] | [[NP:KNeighborsClassifier\|KNN\|ml-knn]] → [[NP:DecisionTreeClassifier\|Arbre de décision\|ml-decision-tree]] → [[NP:RandomForestClassifier\|Random Forest\|ml-ensemble-methods]] / [[NP:SVC\|SVM à noyau\|ml-svm-margin]] |
| ≥100K | \- | [[P:SGDClassifier\|SGD linéaire\|ml-solvers]] | [[P:Nystroem\|Approximation de kernel]] |

---

:::category Régression {#cat-regression}
prédire une quantité continue : target numérique, labels disponibles.
:::

| Échantillons | Peu de features vraiment importantes ? | Modèle(s) à essayer d'abord | Si insuffisant |
|---|---|---|---|
| <100K | Oui | [[P:Lasso\|Régularisation L1\|ml-regularization]] / [[P:ElasticNet\|Régularisation L1+L2\|ml-regularization]] | \- |
| <100K | Non | [[P:LinearRegression\|Régression linéaire (OLS)\|ml-linear-logistic]] / [[P:Ridge\|Régularisation L2\|ml-regularization]] / [[P:SVR(kernel='linear')\|SVM linéaire\|ml-svm-margin]] | [[NP:DecisionTreeRegressor\|Arbre de décision\|ml-decision-tree]] → [[NP:SVR(kernel='rbf')\|SVM à noyau\|ml-svm-margin]] / [[NP:RandomForestRegressor\|Random Forest\|ml-ensemble-methods]] |
| ≥100K | \- | [[P:SGDRegressor\|SGD linéaire\|ml-solvers]] | \- |

> [!TIP]
> 👉 **Escalade Ensemble Methods** (au-delà de Random Forest, en classification comme en régression) : AdaBoost, GradientBoosting, XGBoost — mêmes cas d'usage, souvent plus performants mais plus longs à tuner ; Voting/Stacking combinent plusieurs des modèles ci-dessus plutôt que d'en remplacer un seul (cf. [Ensemble Methods](#ml-ensemble-methods), ci-dessus). **Time Series** (structure temporelle, ex: ARIMA/SARIMA) est un cas particulier de régression que ce radar générique sklearn ne couvre pas — cf. groupe Modèles ▸ Time Series ▸ [Décomposition](#ts-decomposition).

---

:::category Clustering {#cat-clustering}
regrouper des observations similaires entre elles, SANS target/labels connus au départ.
:::

| Nb catégories connu ? | Échantillons | Modèle(s) à essayer d'abord | Si insuffisant |
|---|---|---|---|
| Oui | <10K | [[P:KMeans\|K-Means\|ml-kmeans]] | [[NP:SpectralClustering\|Clustering spectral]] / [[P:GaussianMixture\|Mélange de gaussiennes]] |
| Oui | ≥10K | [[P:MiniBatchKMeans\|K-Means (mini-batch)]] | \- |
| Non | <10K | [[NP:MeanShift\|Mean Shift]] / [[NP:BayesianGaussianMixture\|Mélange de gaussiennes bayésien]] | \- |
| Non | ≥10K | \- | cas difficile — pas de recommandation directe |

---

:::category Réduction de dimension {#cat-reddim}
compresser le nombre de features (visualiser en 2D/3D, accélérer un modèle en aval, débruiter), SANS target non plus.
:::

| Juste explorer ? | Échantillons | Modèle(s) à essayer d'abord | Si insuffisant |
|---|---|---|---|
| Oui | <10K | [[P:PCA(svd_solver='randomized')\|PCA\|ml-pca]] | [[NP:Isomap\|Isomap]] / [[NP:SpectralEmbedding\|Plongement spectral]] → [[NP:LocallyLinearEmbedding\|LLE]] |
| Oui | ≥10K | [[P:Nystroem\|Approximation de kernel]] | \- |
| Non | \- | \- | cas difficile — pas de recommandation directe |

> [!TIP]
> 👉 **Cas spécifique texte** : LDA (topic modeling) est une forme de "clustering" de documents par thème sur données textuelles — hors du radar sklearn générique ci-dessus, cf. groupe Modèles ▸ NLP ▸ LDA.

:::compare
- {p} **Modèles paramétriques [P]** : nombre fixe de paramètres β à apprendre, indépendant de n (ex: LinearRegression, LogisticRegression, réseaux de neurones) — rapides à entraîner même sur de gros datasets (Stochastic Gradient Descent), mais nécessitent une hypothèse h a priori sur la structure des données
- {np} **Modèles non-paramétriques [NP]** : aucune hypothèse a priori — le nombre de paramètres appris dépend des données elles-mêmes (ex: KNN stocke tout le dataset, kernel-SVM calcule un noyau entre chaque paire de points) — capturent des patterns complexes automatiquement, mais plus lents et plus sujets à l'overfitting sur de gros datasets
:::

> [!WARNING]
> ⚠️ **Modèles à investiguer** : [[P:LinearSVC]] (SVM optimisée grande dimension), [[P:Nystroem]] (approximation de kernel), [[NP:SpectralClustering]], [[P:GaussianMixture]], [[P:BayesianGaussianMixture]], [[P:MiniBatchKMeans]] (variante KMeans grands datasets), [[NP:MeanShift]], [[NP:Isomap]], [[NP:SpectralEmbedding]], [[NP:LocallyLinearEmbedding]]
