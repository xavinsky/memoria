---
title: Lire ses résultats — analyse de sortie
subgroup: Métriques
---

Un score seul ne raconte jamais toute l'histoire (cf. [Error analysis](#ml-error-analysis), ci-dessus) — au-delà de la métrique choisie, chaque modèle expose des attributs différents pour comprendre CE QU'IL A APPRIS. Cette carte réunit les réflexes communs à tous les modèles, puis ce qui est spécifique à chaque famille.

**Partie commune — quel que soit le modèle**

:::compare
- **Comparer au Baseline Score** : un score seul ne veut rien dire sans référence — 92% d'accuracy est excellent si le baseline est à 70%, médiocre s'il est déjà à 91% (cf. [Baseline Score](#ml-baseline), page Syntaxes)
- **Écart train/cross-val vs test** : diagnostique overfitting (écart important) vs underfitting (les deux scores bas) — cf. [Bias/Variance tradeoff](#ml-bias-variance), ci-dessus
- **Confusion Matrix / résidus** : classification : où les erreurs se concentrent-elles (quelle classe) ? régression : les résidus tracés vs les prédictions forment-ils un motif (→ variable explicative manquante) ou un nuage sans structure ?
- **Error Analysis** : repérer des schémas récurrents dans les erreurs individuelles (sous-groupes, classes, erreurs extrêmes) plutôt que de s'arrêter à un score agrégé
:::

**Partie spécifique — par famille de modèle**

| Famille de modèle | Où regarder | Ce que ça révèle |
|---|---|---|
| OLS / Logit (Statsmodels) | `model.summary()` | coefficients, p-values, Cond. No. — cf. Lire le résumé d'une régression / régression logistique, page Syntaxes (détail complet déjà couvert) |
| Arbre de décision / Ensemble Methods | `.feature_importances_` | quelles features ont le plus contribué (basé sur la baisse de Gini) — cf. Arbre de décision, [Ensemble Methods](#ml-ensemble-methods), page Syntaxes |
| SVM | `.n_support_`, `.decision_function()` | nombre de vecteurs de support (complexité de la frontière) ; distance signée à l'hyperplan, avant application du seuil — cf. SVM, page Syntaxes |
| PCA | `.explained_variance_ratio_`, `.components_` | part de variance captée par composante ; poids de chaque feature d'origine dans chaque PC ("loadings") — cf. PCA, page Syntaxes |
| K-Means | `.inertia_`, `.cluster_centers_` | qualité du clustering (à comparer entre valeurs de K) ; profil moyen de chaque cluster — cf. K-Means, page Syntaxes |
| ARIMA / SARIMA | `.summary()` + résidus | coefficients, AIC/BIC (comparer plusieurs modèles) ; ACF/PACF des résidus doit ressembler à du bruit blanc (cf. Box-Jenkins Method, ci-dessus) |
| Naive Bayes / LDA (NLP) | `.predict_proba()` ; `.transform()`, `.components_` | probabilité par classe ; pour LDA, mixture de topics par document et mixture de mots par topic — cf. NLP ▸ LDA, ci-dessus |
