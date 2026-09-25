---
title: Hyperparamètres — learning rate, batch size, epochs
subgroup: Optimisation
---

Le **learning rate** contrôle l'amplitude du changement de θ à chaque update (cf. [Gradient Descent](#ml-gradient-descent), groupe ml) — plus petit ⇒ plus d'epochs nécessaires pour converger. Un **scheduler** (ex: `ExponentialDecay`, cf. page Syntaxes) fait décroître automatiquement le learning rate pendant l'entraînement — grands pas au début (convergence rapide), petits pas vers la fin (évite d'osciller autour du minimum).

:::compare
- **batch_size petit** : processus plus stochastique, converge potentiellement plus vite, mais généralise moins bien
- **batch_size grand** : meilleure généralisation, mais plus coûteux en calcul par update
:::

En pratique : 16 ou 32 pour des données réelles (images...), davantage pour de petits datasets tabulaires. Une puissance de 2 pour des raisons purement computationnelles (alignement mémoire).

```math
n_{updates/epoch} = \left\lceil \dfrac{n_{lignes\ train}}{batch\_size} \right\rceil
```

Le nombre d'**epochs** n'a pas besoin d'être fixé à l'avance : on en met "autant que possible", et on laisse l'**Early Stopping** (ci-dessous) arrêter l'entraînement au bon moment plutôt que de deviner un nombre fixe.
