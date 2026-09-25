---
title: Model Tuning — Grid Search vs Random Search
subgroup: Model Tuning
---

Trouver les meilleurs **hyperparamètres** (ex: alpha) — à ne pas confondre avec `.fit()` qui trouve les **paramètres** (β) en minimisant la Loss (cf. [Que fait .fit() ?](#ml-fit-hood) ci-dessus).

> [!WARNING]
> ⚠️ **`scoring` ≠ Loss** : le `scoring` passé à `GridSearchCV`/`cross_validate` n'affecte PAS l'entraînement de chaque combinaison — chacune minimise sa propre Loss comme d'habitude pendant son `.fit()`. Le `scoring` agit uniquement sur la **comparaison entre modèles déjà entraînés** : il décide laquelle des combinaisons testées est retenue comme `best_estimator_`. Deux `scoring` différents sur la même grille peuvent donc désigner deux "meilleurs" hyperparamètres différents.

**Qu'est-ce qu'on met dans une grille ?** N'importe quel paramètre du constructeur de l'estimator (accessible via `.get_params()`, ou `étape__param` dans un pipeline) — mais tous ne sont pas gridés avec la même fréquence en pratique.

:::compare
- **Hyperparamètres numériques — usuel** : alpha, C, n_neighbors, gamma, max_depth... c'est l'usage normal : affiner un modèle déjà choisi (cf. Hyperparamètres ci-dessus).
- **kernel, solver, loss — techniquement possible, rarement fait** : ce sont aussi de simples paramètres du constructeur, donc gridables comme les autres (ex: `grid={'kernel':['linear','rbf'], 'C':[...]}` pour un SVC). Mais changer l'un d'eux change fondamentalement le modèle (l'hypothèse h pour le kernel, ce qui est optimisé pour la loss) — plus proche d'un choix de modèle que d'un réglage fin, donc rarement inclus dans la même grille que les hyperparamètres numériques.
- **Changer de famille de modèle — pas directement** : un `param_grid` s'applique à UN estimator déjà instancié, on ne peut pas passer de LogisticRegression à SVC dedans. Possible via une astuce avancée (pipeline avec étape placeholder + liste de dicts, chacun ciblant une classe différente), mais en pratique on fait plutôt une GridSearchCV séparée par famille candidate, puis on compare les meilleurs résultats entre elles (cf. Choisir son modèle ci-dessus).
:::

1. Réserver un jeu de **validation** — jamais le test set pour le tuning
2. Choisir une grille (Grid Search) ou un espace (Random Search) de valeurs à essayer
3. Mesurer la performance sur le jeu de validation pour chaque combinaison
4. Retenir les hyperparamètres qui maximisent la performance

:::compare
- **Grid Search** : teste TOUTES les combinaisons de la grille — exhaustif mais coûteux, peut manquer l'optimum entre deux valeurs testées, risque de surapprendre les hyperparamètres sur un petit dataset si trop de combinaisons essayées
- **Random Search** : tire aléatoirement N combinaisons dans un espace de valeurs — moins de code, contrôle direct du temps de calcul (n_iter), utile quand certains hyperparamètres comptent plus que d'autres
:::

> [!TIP]
> 👉 Démarrer par une recherche large (coarse grain, ex: `scipy.stats.loguniform` pour balayer plusieurs ordres de grandeur), puis affiner autour de la meilleure zone trouvée.

> [!TIP]
> 💡 `GridSearchCV` / `RandomizedSearchCV` combinent recherche d'hyperparamètres ET cross-validation en une seule syntaxe (cf. Model Tuning, page Syntaxes).

> [!WARNING]
> ⚠️ **Ne pas se fier qu'au meilleur score de validation** : une combinaison d'hyperparamètres peut avoir le meilleur score tout en ayant un gros écart train/validation (overfitting, cf. [Bias/Variance tradeoff](#ml-bias-variance)) — comparer aussi cet écart entre TOUTES les combinaisons testées, pas juste retenir `best_params_` les yeux fermés.

```
search = GridSearchCV(model, grid, cv=5, **return_train_score**=True)
search.fit(X_train, y_train)

import pandas as pd
results = pd.DataFrame(search.cv_results_)
results['gap'] = results['mean_train_score'] - results['mean_test_score']

# Comparer score et écart pour toutes les combinaisons testées
results[['params', 'mean_test_score', 'gap']].sort_values('mean_test_score', ascending=False)
```

**Classes/méthodes utilisables à cette étape** : `return_train_score` (paramètre de `GridSearchCV`/`RandomizedSearchCV`, `False` par défaut), `search.cv_results_`, `pd.DataFrame` (cf. Model Tuning, page Syntaxes).
