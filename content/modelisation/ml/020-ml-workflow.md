---
title: Workflow Scikit-learn — sans pipeline (pédagogique)
subgroup: Workflow
---

![](../../diagrams/ml-workflow-1.html)

> [!TIP]
> 👉 Étapes 1-3 (Explorer, Nettoyer, Séparer train/test) détaillées une seule fois dans [Workflow ML](#ml-lifecycle) — identiques avec ou sans pipeline.

::::derivation {start=4}

:::step Preprocessing {#wf1-preprocessing}

Fit sur train, transform partout ; jamais de `.fit()` sur X_test — tout ce qui suit s'enchaîne dans cet ordre : **conversion de types** → imputation → scaling → balancing (train seulement) → feature engineering → feature selection.

**Conversion de types** — une date ou un nombre stocké en texte (repéré à l'étape Explorer, dtype `object`) doit être converti AVANT tout traitement numérique : `pd.to_datetime()` pour une date, puis en extraire des features numériques (un modèle ne comprend pas un `datetime` brut) ; `pd.to_numeric(errors="coerce")` pour un nombre écrit en texte — `errors="coerce"` transforme en NaN ce qui ne parse pas, traité ensuite comme une valeur manquante classique.

```
df['date'] = pd.**to_datetime**(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['dayofweek'] = df['date'].dt.dayofweek

df['price'] = pd.**to_numeric**(df['price'].str.replace(',', '.'), errors='coerce')
```

> [!WARNING]
> ⚠️ **NaN ne veut pas toujours dire "donnée manquante"** : ex: NaN sur une colonne Alley peut signifier "pas d'allée", pas une erreur de mesure — nécessite la connaissance métier du dataset. Règle empirique : > 30% de NaN → envisager de supprimer la feature (ou la ligne) ; < 30% → envisager une imputation adaptée au sens de la colonne.

```
imputer = SimpleImputer(strategy="median")
df[['col']] = imputer.**fit_transform**(df[['col']])

scaler = StandardScaler()
X_train = scaler.**fit_transform**(X_train)
X_test = scaler.**transform**(X_test)
```

**Classes/méthodes utilisables à cette étape** : `pd.to_datetime`, `pd.to_numeric` (conversion de types), `SimpleImputer`, `KNNImputer`, `StandardScaler`, `MinMaxScaler`, `RobustScaler`, `OneHotEncoder`, `OrdinalEncoder`, `pd.cut` (discretizing), `SMOTE` (balancing) (cf. [Dates et temps](#dates), Nettoyage des données, Valeurs manquantes, Feature Scaling, Encoding, Discretizing, Balancing, page Syntaxes).

**Feature engineering & feature selection** — une fois les features propres et à l'échelle : encoder/discrétiser/créer de nouvelles features, puis réduire aux plus pertinentes (corrélation, VIF) AVANT le premier modèle. Cf. [Feature Selection](#ml-feature-selection-concept) — cette étape revient une seconde fois après le premier modèle entraîné (cf. Diagnostiquer l'écart, ci-dessous).

:::

:::step Implémentation {#wf1-implementation num=7}

Instancier la classe choisie à l'étape précédente.

```
from sklearn.linear_model import LinearRegression
model = **LinearRegression**()
```

**Classes/méthodes utilisables à cette étape** : `LinearRegression`, `LogisticRegression`, `KNeighborsRegressor`/`KNeighborsClassifier`, `Ridge`, `Lasso`, `ElasticNet`, `SVC`, `SVR`, `SGDRegressor`/`SGDClassifier` (cf. Choix du modèle, page Syntaxes).

:::

:::step Valider par cross-validation (sur train) {#wf1-cv num=8}

Estime la performance avant de toucher au test set.

> [!TIP]
> 👉 **Choisir K** : compromis fiabilité / temps de calcul — règle empirique : K=5 ou K=10.

> [!WARNING]
> ⚠️ **Ce que `cross_validate` ne fait pas** : elle ne renvoie pas un modèle entraîné, elle ne fait que scorer un modèle hypothétique entraîné sur tout le dataset — pour obtenir un modèle utilisable, il faut ensuite le fit sur l'ensemble des données.

```
cv_results = **cross_validate**(model, X_train, y_train, cv=5)
cv_results['test_score'].mean()
```

**Classes/méthodes utilisables à cette étape** : `cross_validate`, `cross_val_score`, `KFold` (cf. K-Fold Cross Validation, page Syntaxes).

:::

:::step Entraîner puis évaluer sur le test set {#wf1-train num=9}

Jamais vu à l'entraînement — comparer au Baseline Score, puis choisir la métrique adaptée à la tâche (métrique par défaut dépendante du modèle : R² pour LinearRegression, accuracy pour LogisticRegression) — à comparer au score de cross-validation de l'étape précédente.

> [!TIP]
> 👉 **Pourquoi un modèle baseline** : point de comparaison minimal avant tout modèle réel — permet de juger si le modèle apporte vraiment de la valeur, et d'avancer rapidement dans le pipeline sans attendre d'avoir le modèle final.

```
model.**fit**(X_train, y_train)
model.**score**(X_test, y_test)
```

**Classes/méthodes utilisables à cette étape** : `.fit()`, `.score()`, `DummyRegressor`, `DummyClassifier` (cf. [Baseline Score](#ml-baseline), Métriques, page Syntaxes).

:::

:::step Diagnostiquer l'écart cross-val vs test {#wf1-diagnostic num=10}

Écart 0-5% normal, 5-10% limite, +10% overfitting (cf. [Bias/Variance tradeoff](#ml-bias-variance), ci-dessous).

```
cv_score = cv_results['test_score'].mean()
test_score = model.score(X_test, y_test)
abs(cv_score - test_score)
```

**Classes/méthodes utilisables à cette étape** : `learning_curve` pour diagnostiquer plus finement (cf. [Bias/Variance tradeoff](#ml-bias-variance), ci-dessous).

> [!TIP]
> 👉 **Feature Selection, 2ᵉ passage** : une fois un premier modèle entraîné, `permutation_importance` révèle les features réellement utiles POUR CE modèle (contrairement à la corrélation, faite avant tout modèle) — retirer les features faibles puis reboucler sur l'étape Entraîner ("remodel") si ça améliore le score (cf. Feature Selection, page Syntaxes).

:::

:::step Réentraîner sur TOUT le dataset {#wf1-retrain num=11}

Une fois validé — on jette le split et on réentraîne sur 100% des données disponibles.

> [!TIP]
> 👉 **Pourquoi réentraîner sur tout le dataset** : le split train/test et la cross-validation ne servent qu'à ESTIMER la performance — une fois le modèle validé, on jette le split et on réentraîne sur 100% des données pour obtenir le modèle final le plus informé possible.

```
model.**fit**(X, y)  # X, y = dataset complet, pas X_train/y_train
```

**Classes/méthodes utilisables à cette étape** : `.fit()` (cf. [Réentraînement final](#ml-predictions), page Syntaxes).

:::

:::step Prédire sur une donnée nouvelle {#wf1-predict num=12}

Ne jamais oublier de réappliquer le même preprocessing (scaler déjà fit à l'étape Preprocessing, jamais refit) aux nouvelles données.

```
new_point_scaled = scaler.**transform**(new_point)
model.**predict**(new_point_scaled)
```

**Classes/méthodes utilisables à cette étape** : `.transform()`, `.predict()` (cf. [Réentraînement final & prédiction](#ml-predictions), page Syntaxes).

:::

::::
