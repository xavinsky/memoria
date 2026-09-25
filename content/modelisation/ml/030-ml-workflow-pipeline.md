---
title: Workflow Scikit-learn — avec pipeline (usage réel)
subgroup: Workflow
---

![](../../diagrams/ml-workflow-pipeline-1.html)

> [!TIP]
> 👉 Étapes 1-3 (Explorer, Nettoyer, Séparer train/test) détaillées une seule fois dans [Workflow ML](#ml-lifecycle) — identiques avec ou sans pipeline.

::::derivation {start=4}

:::step Preprocessing {#wf2-preprocessing}

**Conversion de types d'abord** — un `ColumnTransformer` route par dtype (`number` vs `object`) : une date ou un nombre écrit en texte (dtype `object`, repéré à l'étape Explorer) doit donc être converti et décomposé AVANT de construire le `ColumnTransformer`, sinon il finit dans la branche `OneHotEncoder` comme une catégorie au lieu d'être exploité comme une vraie date/un vrai nombre.

```
df['date'] = pd.**to_datetime**(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

df['price'] = pd.**to_numeric**(df['price'].str.replace(',', '.'), errors='coerce')
```

Ensuite, un `ColumnTransformer` applique en parallèle un traitement différent selon le type de colonne (numérique vs catégorielle) — remplace les étapes manuelles "Preprocessing" du workflow sans pipeline.

```
num_transformer = make_pipeline(SimpleImputer(), StandardScaler())
preproc = **make_column_transformer**(
    (num_transformer, make_column_selector(dtype_include='number')),
    (OneHotEncoder(), make_column_selector(dtype_include='object')),
    **remainder**='passthrough',
)
```

> [!WARNING]
> ⚠️ Ne pas oublier `remainder='passthrough'` : sans lui, toute colonne non sélectionnée par le `ColumnTransformer` (ni numérique ni catégorielle) est supprimée par défaut.

**Créer une nouvelle feature en parallèle** — un `FeatureUnion` applique plusieurs transformers au MÊME jeu de colonnes puis concatène les résultats, utile pour ajouter une feature calculée en plus du preprocessing existant.

```
ratio = FunctionTransformer(lambda df: pd.DataFrame(df['bmi'] / df['age']))
preproc_full = **make_union**(preproc, ratio)
```

> [!TIP]
> 👉 `FunctionTransformer` ne marche que pour une transformation **stateless** (qui n'apprend rien pendant `.fit()`, comme ce ratio). Si la feature a besoin de calculer ET stocker une information pendant le fit (ex: une moyenne apprise sur le train), il faut écrire sa propre classe (`MyCustomTransformer`, héritant de `TransformerMixin`/`BaseEstimator`) — cf. [Transformers personnalisés](#ml-pipelines-custom), page Syntaxes.

**Classes/méthodes utilisables à cette étape** : `pd.to_datetime`, `pd.to_numeric` (conversion de types), `ColumnTransformer`, `make_column_transformer`, `make_column_selector`, `SimpleImputer`, `StandardScaler`, `OneHotEncoder`, `FeatureUnion`, `make_union`, `FunctionTransformer` (cf. [Dates et temps](#dates), Nettoyage des données, Pipelines, page Syntaxes).

:::

:::step Implémentation {#wf2-implementation num=7}

Instancier la classe choisie à l'étape précédente, puis l'assembler avec le preprocessing en un seul objet `Pipeline` — plus besoin de garder le scaler et le modèle séparés.

```
from sklearn.linear_model import LinearRegression
model = **LinearRegression**()
pipeline = **make_pipeline**(preproc, model)
```

**Classes/méthodes utilisables à cette étape** : `LinearRegression`, `LogisticRegression`, `KNeighborsRegressor`/`KNeighborsClassifier`, `Ridge`, `Lasso`, `ElasticNet`, `SVC`, `SVR`, `SGDRegressor`/`SGDClassifier` (cf. Choix du modèle, page Syntaxes), `Pipeline`, `make_pipeline` (cf. Pipelines, page Syntaxes).

:::

:::step Valider par cross-validation (sur train) {#wf2-cv num=8}

Estime la performance avant de toucher au test set.

> [!TIP]
> 👉 **Choisir K** : compromis fiabilité / temps de calcul — règle empirique : K=5 ou K=10.

> [!WARNING]
> ⚠️ **Ce que `cross_validate` ne fait pas** : elle ne renvoie pas un modèle entraîné, elle ne fait que scorer un modèle hypothétique entraîné sur tout le dataset — pour obtenir un modèle utilisable, il faut ensuite le fit sur l'ensemble des données.

```
cv_results = **cross_validate**(pipeline, X_train, y_train, cv=5)
cv_results['test_score'].mean()
```

**Classes/méthodes utilisables à cette étape** : `cross_validate`, `cross_val_score`, `KFold` (cf. K-Fold Cross Validation, page Syntaxes).

:::

:::step (Optionnel) Fine-tuner via GridSearchCV {#wf2-gridsearch num=9}

Un pipeline permet de tuner en une seule recherche les hyperparamètres du preprocessing ET du modèle, avec la syntaxe `nom_étape__param`.

```
search = **GridSearchCV**(pipeline, param_grid={'linearregression__fit_intercept': [True, False]}, cv=5)
search.fit(X_train, y_train)
```

**Classes/méthodes utilisables à cette étape** : `GridSearchCV`, `RandomizedSearchCV` (cf. Model Tuning, page Syntaxes).

:::

:::step Entraîner puis évaluer sur le test set {#wf2-train num=10}

Jamais vu à l'entraînement — comparer au Baseline Score, puis choisir la métrique adaptée à la tâche (métrique par défaut dépendante du modèle : R² pour LinearRegression, accuracy pour LogisticRegression) — à comparer au score de cross-validation de l'étape précédente. `.fit()` sur le pipeline entraîne le preprocessing ET le modèle en un seul appel.

> [!TIP]
> 👉 **Pourquoi un modèle baseline** : point de comparaison minimal avant tout modèle réel — permet de juger si le modèle apporte vraiment de la valeur, et d'avancer rapidement dans le pipeline sans attendre d'avoir le modèle final.

```
pipeline.**fit**(X_train, y_train)
pipeline.**score**(X_test, y_test)
```

**Classes/méthodes utilisables à cette étape** : `.fit()`, `.score()`, `DummyRegressor`, `DummyClassifier` (cf. [Baseline Score](#ml-baseline), Métriques, page Syntaxes).

:::

:::step Diagnostiquer l'écart cross-val vs test {#wf2-diagnostic num=11}

Écart 0-5% normal, 5-10% limite, +10% overfitting (cf. [Bias/Variance tradeoff](#ml-bias-variance), ci-dessous).

```
cv_score = cv_results['test_score'].mean()
test_score = pipeline.score(X_test, y_test)
abs(cv_score - test_score)
```

**Classes/méthodes utilisables à cette étape** : `learning_curve` pour diagnostiquer plus finement (cf. [Bias/Variance tradeoff](#ml-bias-variance), ci-dessous).

> [!TIP]
> 👉 **Feature Selection, 2ᵉ passage** : une fois un premier modèle entraîné, `permutation_importance` révèle les features réellement utiles POUR CE modèle (contrairement à la corrélation, faite avant tout modèle) — retirer les features faibles puis reboucler sur l'étape Entraîner ("remodel") si ça améliore le score (cf. Feature Selection, page Syntaxes).

:::

:::step Réentraîner sur TOUT le dataset {#wf2-retrain num=12}

Comme sans pipeline, une fois validé on jette le split et on réentraîne — mais un seul `.fit()` suffit pour tout réentraîner (preprocessing inclus).

```
pipeline.**fit**(X, y)  # X, y = dataset complet
```

**Classes/méthodes utilisables à cette étape** : `.fit()`.

:::

:::step Prédire sur une donnée nouvelle {#wf2-predict num=13}

C'est là que le pipeline change tout : `.predict()` réapplique automatiquement le preprocessing (imputer, scaler, encoder déjà fit) avant de prédire — impossible d'oublier une étape, contrairement au workflow sans pipeline.

```
pipeline.**predict**(new_point)  # pas besoin de scaler.transform() à la main
```

**Classes/méthodes utilisables à cette étape** : `.predict()`.

:::

::::
