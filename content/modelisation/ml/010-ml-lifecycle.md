---
title: Workflow ML
subgroup: Workflow
---

![](../../diagrams/ml-lifecycle-1.html)

> [!TIP]
> 👉 Étape 4 et suivantes selon le type de workflow : [sans pipeline](#ml-workflow) (pédagogique/PoC), ou [avec pipeline](#ml-workflow-pipeline) (usage réel).

::::derivation {start=1}

:::step Explorer {#wf0-explorer}

Vérifier NaN, **types de colonnes**, doublons et équilibre des classes avant tout.

> [!TIP]
> 👉 **Pourquoi ces vérifications avant tout** : NaN → un modèle Sklearn ne fit pas avec des NaN (sauf modèles spécifiques) ; types de colonnes → une date ou un nombre stocké en texte n'est utilisable par aucun modèle tel quel ; doublons → faussent l'évaluation s'ils se répartissent entre train et test (cf. [Data Leakage](#ml-data-leakage-concept), ci-dessous) ; classes déséquilibrées → le modèle apprend mal la classe minoritaire (cf. Balancing, ci-dessous).

```
df.**isnull**().sum()
df.**dtypes**
df.**duplicated**().sum()
df['target'].**value_counts**()
```

> [!WARNING]
> ⚠️ Le dtype ne reflète pas toujours le contenu réel : une date au format texte (`"2023-01-15"`) ou un nombre écrit en texte (`"1 200"`, `"3,5"`) apparaissent tous les deux comme `object`, exactement comme une vraie colonne catégorielle — à repérer ici, à convertir dans Preprocessing (cf. [Workflow ML — sans pipeline](#wf1-preprocessing) ou [avec pipeline](#wf2-preprocessing)).

**Classes/méthodes utilisables à cette étape** : `.isnull()`, `.duplicated()`, `.value_counts()`, `.describe()`, `.dtypes`, `.info()` (cf. [Explorer avant de modéliser](#ml-explore), page Syntaxes).

:::

:::step Nettoyer (doublons, outliers) {#wf0-nettoyer}

Uniquement ce qui ne nécessite PAS de `.fit()` — donc safe à faire avant le split (contrairement à l'imputation, cf. Preprocessing dans chaque workflow).

> [!WARNING]
> ⚠️ Un outlier n'est pas toujours une erreur — peut être une observation rare (novelty) ou une feature en soi ; à traiter au cas par cas (cf. Outliers, page Syntaxes).

```
df = df.**drop_duplicates**()
mask = (df['col'] > 0) & (df['col'] < 5000)
df = df[mask].**reset_index**(drop=True)
```

**Classes/méthodes utilisables à cette étape** : `.drop_duplicates()`, `.boxplot()` (cf. Doublons, Outliers, page Syntaxes).

:::

:::step Séparer train / test {#wf0-split}

AVANT de fitter quoi que ce soit — le split doit précéder le fit du scaler/encoder, sinon data leakage (cf. [Data Leakage](#ml-data-leakage-concept), ci-dessous).

> [!TIP]
> 👉 **Limites du Holdout** : split aléatoire → score qui varie selon le tirage ; perte d'information (les données de test ne servent pas à l'entraînement), surtout gênant sur un petit dataset.

> [!WARNING]
> ⚠️ **Stratify** — un split purement aléatoire peut, par hasard, déséquilibrer une classe rare entre train et test (ex: 8% de fraude dans train, 2% dans test). `stratify=y` force chaque classe de y à garder les mêmes proportions des deux côtés — indispensable sur une target déséquilibrée.

```
X_train, X_test, y_train, y_test = **train_test_split**(X, y, test_size=0.2, random_state=42)
```

**Classes/méthodes utilisables à cette étape** : `train_test_split` (cf. Train/test split, page Syntaxes).

:::

::::
