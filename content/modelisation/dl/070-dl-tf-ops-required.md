---
title: Pourquoi tf.* et pas Numpy/Pandas dans un modèle Keras
subgroup: Fondamentaux
---

Keras retrace en interne le CODE de toute fonction qu'il appelle PENDANT l'entraînement — custom loss, custom metric (cf. [Entraînement — loss & optimizer](#dl-training-loss-optim), ci-dessus), ou couche custom (`Layer.call()`) — pour construire un graphe de calcul et pouvoir en calculer automatiquement le gradient (cf. Backpropagation, ci-dessous).

> [!WARNING]
> ⚠️ Les opérations Numpy/Pandas/Python natif (`np.mean`, `.sum()`, une boucle `for`...) s'exécutent EN DEHORS de ce graphe : TensorFlow ne peut ni les tracer, ni calculer leur gradient. À l'intérieur de toute fonction appelée par Keras pendant l'entraînement, il faut donc exclusivement utiliser les opérations `tf.*` équivalentes.

```
def custom_mse(y_true, y_pred):
    squared_diff = **tf**.square(y_true - y_pred)  # PAS np.square
    return **tf**.reduce_mean(squared_diff)      # PAS np.mean / .mean()

model.compile(loss=custom_mse)
```

> [!TIP]
> 👉 Cette règle ne s'applique QU'À L'INTÉRIEUR du graphe Keras (loss/metric/layer custom appelés pendant `.fit()`/`.evaluate()`/`.predict()`). En dehors — préparer X/y AVANT `.fit()`, analyser des résultats APRÈS `.predict()` — Numpy, Pandas et Sklearn restent parfaitement utilisables (cf. `StandardScaler`, page Syntaxes ▸ Preprocessing intégré au modèle).

Équivalents Numpy → TensorFlow les plus courants : cf. page Syntaxes ▸ TensorFlow — manipuler des tensors.

**`tf.data.Dataset`** répond à un problème DIFFÉRENT (rien à voir avec le graphe de calcul ci-dessus) : charger un gros dataset (ex: des milliers d'images) qui ne tient pas entièrement en RAM. Au lieu de tout charger d'un coup dans un array Numpy, il streame les données batch par batch depuis le disque, directement compatible avec `model.fit(ds, ...)`.
