---
title: Hyperparamètres — comprendre les réglages clés
subgroup: Concepts Modèles
---

Tous les hyperparamètres des modèles vus jusqu'ici, regroupés au même endroit.

> [!TIP]
> 👉 **LinearRegression** n'a PAS d'hyperparamètre significatif à tuner (juste `fit_intercept`, rarement touché) — c'est le modèle de référence "sans réglage", contrairement à tous les autres ci-dessous.

**KNN**

:::compare
- **n_neighbors (K)** : nombre de voisins pris en compte — K petit → overfitting (sensible au bruit d'un seul point) ; K grand → underfitting (signal dilué parmi trop de voisins).
- **weights** : uniform (défaut) : chaque voisin compte pareil, stable mais un voisin proche peut être noyé par des voisins lointains ; distance : les voisins proches comptent plus, plus réactif mais plus sensible à une exception proche.
- **p (distance)** : 2 (défaut) : distance euclidienne, frontières de décision lisses ; 1 : distance de Manhattan, frontières plus anguleuses mais plus rapide en grande dimension.
:::

**LogisticRegression**

:::compare
- **C** : inverse de la force de régularisation (C = 1/α) — C petit = régularisation forte (modèle plus simple) ; C grand = régularisation faible, proche d'une régression non régularisée. Sens inversé par rapport à alpha (Ridge/Lasso) : attention à ne pas confondre.
- **class_weight** : ='balanced' compense automatiquement un déséquilibre de classes en pondérant l'erreur sur la classe minoritaire — alternative à SMOTE/undersampling (cf. Balancing) qui ne modifie pas les données elles-mêmes.
- **solver** : méthode d'optimisation utilisée pour maximiser la vraisemblance (cf. [Que fait .fit() ?](#ml-fit-hood)) — 'lbfgs' (défaut) convient à la plupart des cas ; 'liblinear' pour les petits datasets ou une pénalité L1 (Lasso).
:::

**Ridge / Lasso / ElasticNet** (cf. [Régularisation](#ml-regularization) pour le mécanisme complet)

:::compare
- **alpha** : force de la régularisation — α grand : modèle plus simple, ⤵ variance, ⤴ bias ; α → 0 : revient à une régression non régularisée.
- **l1_ratio (ElasticNet)** : proportion L1/L2 — 0 = Ridge pur, 1 = Lasso pur.
:::

**SVC / SVR** (cf. SVM, ci-dessous, pour le mécanisme complet)

:::compare
- **C** : force de la pénalité sur les points mal classés/mal placés — C grand = marge stricte (proche d'un Maximum Margin Classifier, risque d'overfitting) ; C petit = marge souple, plus régularisée.
- **kernel** : 'linear' (pas de transformation), 'poly' (frontières polynomiales), 'rbf' (défaut, similarité gaussienne) — cf. Kernel Trick pour le détail de chacun.
- **gamma (kernel rbf/poly)** : facteur de "myopie" de la similarité gaussienne — gamma grand → le modèle se focalise sur les points très proches → overfitting.
- **epsilon (SVR uniquement)** : largeur de la "rue" dans laquelle les points ne sont pas pénalisés.
:::

**SGDRegressor / SGDClassifier** (cf. [Variantes de la descente de gradient](#ml-solvers), groupe Entraînement (fit), pour le mécanisme SGD)

:::compare
- **loss** : définit quel modèle est émulé — squared_error ≈ LinearRegression (OLS), huber (robuste aux outliers) ; log_loss ≈ LogisticRegression, hinge ≈ SVC.
- **penalty** : 'l2' (défaut, ≈ Ridge), 'l1' (≈ Lasso), 'elasticnet' — même rôle que pour Ridge/Lasso/ElasticNet.
- **alpha** : force de la régularisation — même sens que pour Ridge/Lasso.
- **learning_rate / eta0** : taille du pas de la descente de gradient (η, cf. [Gradient Descent](#ml-gradient-descent)) — trop grand : ne converge jamais ; trop petit : convergence lente.
:::

**Arbre de décision** (DecisionTreeClassifier/Regressor — cf. [Arbre de décision](#ml-decision-tree) pour le mécanisme complet)

:::compare
- **max_depth** : profondeur maximale de l'arbre — sans limite (None), overfitting quasi garanti (pousse jusqu'à isoler chaque point) ; petit = underfitting.
- **min_samples_split** : nombre minimum d'observations pour qu'un nœud soit encore coupé — grand = arbre plus simple, moins d'overfitting.
- **min_samples_leaf** : nombre minimum d'observations pour qu'une feuille existe — évite des feuilles ne représentant qu'un point isolé (bruit).
:::

**Random Forest / Bagging** (cf. [Ensemble Methods](#ml-ensemble-methods) pour le mécanisme complet)

:::compare
- **n_estimators** : nombre d'arbres (weak learners) — plus il y en a, plus la variance baisse, mais coût de calcul plus élevé ; rendements décroissants au-delà d'un certain nombre.
- **max_depth / min_samples_leaf** : mêmes hyperparamètres qu'un arbre seul, appliqués à chaque arbre de la forêt.
- **max_features** : nombre de features tirées au hasard à chaque coupure — diversifie les arbres entre eux (en plus du bootstrap sur les observations).
:::

**AdaBoost / Gradient Boosting / XGBoost** (cf. [Ensemble Methods](#ml-ensemble-methods) pour le mécanisme complet)

:::compare
- **n_estimators** : nombre d'arbres ajoutés séquentiellement — contrairement au bagging, trop en ajouter peut overfitter (chaque arbre corrige de plus en plus finement les erreurs du train).
- **learning_rate** : poids de chaque arbre ajouté à la prédiction finale — petit = apprentissage plus prudent (moins d'overfitting) mais nécessite plus de n_estimators pour converger.
- **max_depth** : profondeur de chaque arbre — généralement bien plus faible qu'en Random Forest (souvent 3-6) : des "weak learners" volontairement simples, la force venant de leur nombre.
:::

**PCA** (cf. [PCA](#ml-pca) pour le mécanisme complet)

:::compare
- **n_components** : nombre de composantes principales gardées (k) — choisi via la méthode du coude sur `explained_variance_ratio_` (cf. Syntaxes ▸ PCA).
:::

**K-Means** (cf. [K-Means](#ml-kmeans) pour le mécanisme complet)

:::compare
- **n_clusters (K)** : nombre de clusters — choisi via la méthode du coude sur `inertia_` (cf. Syntaxes ▸ K-Means).
- **n_init** : nombre d'initialisations aléatoires des centroïdes essayées — K-Means peut converger vers un optimum local selon le tirage de départ ; n_init garde le meilleur résultat parmi plusieurs essais.
:::

**ARIMA / SARIMA** (cf. [ARMA, ARIMA & SARIMA](#ts-arima) pour le mécanisme complet)

:::compare
- **p, d, q** : ordre AR (nombre de lags), ordre de différenciation, ordre MA — lus sur PACF/ACF ou trouvés par `auto_arima` (grid search sur l'AIC).
- **P, D, Q, S (SARIMA)** : mêmes rôles que p, d, q mais au niveau saisonnier — S = période de la saisonnalité (ex: 12 pour un cycle annuel mensuel), à choisir manuellement (pas trouvé par grid search).
:::

**CountVectorizer / TfidfVectorizer** (NLP — cf. [Vectorizing](#nlp-vectorizing) pour le mécanisme complet)

:::compare
- **max_df / min_df** : retirent les mots trop fréquents / trop rares du vocabulaire — construisent des "stopwords" spécifiques au corpus.
- **max_features** : limite le vocabulaire aux k mots les plus fréquents — lutte contre la curse of dimensionality.
- **ngram_range** : longueur des séquences de mots capturées (unigrams/bigrams/trigrams) — capture une partie du contexte perdu par un simple comptage de mots isolés.
:::

**MultinomialNB / LatentDirichletAllocation** (NLP — cf. [Naive Bayes](#nlp-naive-bayes), [LDA](#nlp-lda) pour le mécanisme complet)

:::compare
- **alpha (MultinomialNB)** : paramètre de smoothing — évite les probabilités nulles pour un mot jamais vu dans une classe à l'entraînement.
- **n_components (LDA)** : nombre de topics à découvrir dans le corpus — pas de méthode automatique simple, se choisit en inspectant si les topics obtenus "font sens".
:::
