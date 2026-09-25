---
title: Log Loss / Cross-Entropy — dérivation pas à pas
intro: D'où vient la formule −1/n Σ [yᵢ log(ŷᵢ) + (1−yᵢ) log(1−ŷᵢ)], et pourquoi yᵢ et (1−yᵢ) y jouent le rôle d'interrupteurs.
---

::::derivation

:::step Le problème posé

Rappel : un Loss n'est pas une Performance Metric. On calcule une métrique (accuracy, recall...) **après** avoir entraîné le modèle, pour juger sa qualité. On calcule un Loss **pendant** l'entraînement, pour piloter la descente de gradient — il doit donc être dérivable, ce qu'accuracy n'est pas (elle "saute" entre des valeurs discrètes).

Pour la régression on a déjà vu L1 (MAE), L2 (MSE) et Huber. Reste la question pour la **classification** : on prédit un vecteur binaire

```math
y = [0, 0, 1, 0, ..., 1]
```

taille n — la vraie classe de chaque observation, 0 ou 1. Le modèle produit une **probabilité** par observation (sortie d'une sigmoïde) :

```math
\hat y = [0.1, 0.3, ..., 0.8] = h(X,\beta)
```

> [!TIP]
> **Question** : quelle fonction de perte comparer entre y (des 0/1) et ŷ (des probabilités) ?

:::

:::step Ce qu'on veut, en une phrase

:::compare
- {outer} **yᵢ = 1** : ŷᵢ proche de 1
- {inner} **yᵢ = 0** : (1−ŷᵢ) proche de 1, donc ŷᵢ proche de 0
:::

Toute la construction qui suit n'est qu'une façon rigoureuse d'écrire mathématiquement cette phrase, puis de la transformer en quelque chose qu'on peut dériver et minimiser.

:::

:::step Traduire ça en un seul nombre : la vraisemblance

Idée : si les observations sont indépendantes, on peut multiplier entre elles la "qualité" de chaque prédiction, en piochant le bon facteur selon la vraie classe :

```math
\prod_{i:\,y_i=1} \textcolor{#2E6F82}{\hat y_i} \;\cdot\; \prod_{i:\,y_i=0} \textcolor{#9C3B31}{(1-\hat y_i)}
```

un grand produit de nombres entre 0 et 1, un par observation. Ce produit s'appelle la **vraisemblance** (likelihood) : la probabilité, sous l'hypothèse du modèle h, d'observer exactement les y réels qu'on a dans les données. Plus il est proche de 1, meilleur est le modèle — on veut donc le **maximiser**.

> [!TIP]
> 💡 C'est exactement le même principe que le Maximum de Vraisemblance vu en régression logistique (cf. Théorème de Bayes — MLE vs MAP, groupe Maths) — ici on l'exprime juste en fonction de β via ŷ = h(X,β).

:::

:::step Pourquoi on abandonne le produit pour une somme

:::compare
- {outer} **Numériquement fragile** : Multiplier des centaines de nombres < 1 entre eux donne un résultat qui s'écrase vers 0 (underflow) — l'ordinateur perd la précision.
- {inner} **Dur à dériver** : Dériver un produit de n termes est bien plus lourd que dériver une somme de n termes.
:::

Solution : appliquer log avant de maximiser. Le logarithme est strictement croissant, donc maximiser L(β) ou maximiser log(L(β)) donne exactement le même β optimal — on ne perd rien. Et log transforme un produit en somme :

```math
\log(a\cdot b) = \log(a) + \log(b)
```

:::

:::step Le tour de l'interrupteur — d'où vient yᵢ·log(ŷᵢ)+(1−yᵢ)·log(1−ŷᵢ)

En appliquant log au produit de l'étape 2, chaque facteur devient un terme d'une somme :

```math
\log(L) = \sum_{i:\,y_i=1}\log(\hat y_i) + \sum_{i:\,y_i=0}\log(1-\hat y_i)
```

deux sommes séparées, chacune sur un sous-ensemble d'observations. Cette écriture est correcte mais peu pratique à coder : elle oblige à filtrer les observations avant de sommer. L'astuce consiste à **fusionner les deux sommes en une seule**, valable pour toutes les observations à la fois, en utilisant yᵢ lui-même (qui vaut 0 ou 1) comme un interrupteur :

```math
\sum_{i=1}^n \textcolor{#2E6F82}{y_i\cdot\log(\hat y_i)} + \textcolor{#9C3B31}{(1-y_i)\cdot\log(1-\hat y_i)}
```

| yᵢ | yᵢ·log(ŷᵢ) | (1−yᵢ)·log(1−ŷᵢ) | résultat |
|---|---|---|---|
| 1 | log(ŷᵢ) | 0 | log(ŷᵢ) |
| 0 | 0 | log(1−ŷᵢ) | log(1−ŷᵢ) |

> [!TIP]
> 👉 yᵢ et ŷᵢ "se mélangent" dans la même formule parce que yᵢ n'est pas utilisé ici comme une probabilité : il est utilisé comme un **multiplicateur binaire** qui active un terme et désactive l'autre. Pour chaque observation, un seul des deux termes de la somme est réellement non nul — la formule à un seul Σ est juste une manière compacte d'écrire les deux sommes séparées, sans avoir à trier les observations.

:::

:::step De la vraisemblance (à maximiser) au Log Loss (à minimiser)

:::compare
- {outer} **Un signe moins** : On veut maximiser la vraisemblance, mais par convention la descente de gradient minimise un Loss. Minimiser −log(L) revient exactement à maximiser log(L).
- {inner} **Une moyenne 1/n** : On divise par n pour obtenir un Loss moyen par observation, indépendant de la taille du dataset — comme pour MAE/MSE.
:::

```math
LogLoss = -\dfrac1n\sum_{i=1}^n \big[y_i\log(\hat y_i) + (1-y_i)\log(1-\hat y_i)\big]
```

c'est la formule officielle — identique à l'étape 4, juste négée et moyennée.

:::

:::step Pourquoi une prédiction confiante et fausse est punie "à l'infini"

Grâce au tableau de vérité de l'étape 4, pour une seule observation le Log Loss se réduit toujours à un seul terme :

```math
y=1 \Rightarrow LogLoss = -\log(\hat y) \qquad y=0 \Rightarrow LogLoss = -\log(1-\hat y)
```

| ŷ (proba prédite pour la vraie classe) | 0.99 | 0.8 | 0.5 | 0.1 | 0.01 | → 0 |
|---|---|---|---|---|---|---|
| LogLoss = −log(ŷ) | 0.01 | 0.22 | 0.69 | 2.30 | 4.61 | → +∞ |

> [!WARNING]
> ⚠️ Quand le modèle est confiant et correct (ŷ proche de 1), la pénalité est presque nulle. Mais quand le modèle est confiant et FAUX (ŷ proche de 0 alors que la vraie classe est 1), la pénalité explose vers l'infini — log(0) = −∞. C'est une différence fondamentale avec l'accuracy : le Log Loss ne se contente pas de compter les erreurs, il punit sévèrement les erreurs confiantes.

:::

:::step D'où vient le nom « Cross-Entropy »

En théorie de l'information (Shannon), l'**entropie** d'une distribution de probabilité mesure son imprévisibilité. La **cross-entropie** entre une distribution "vraie" et une distribution "prédite" mesure l'écart entre les deux — exactement ce que fait notre formule entre y (la vraie distribution, 0 ou 1) et ŷ (la distribution prédite par le modèle). Le Log Loss d'un classifieur binaire est un cas particulier de cross-entropie, ce qui explique pourquoi les deux noms désignent la même formule.

:::

:::step Le gradient, et son écho avec le MSE

Sans refaire tout le calcul de dérivation (même démarche qu'avec la SSR — chain rule, terme par terme, puis somme, cf. Chain rule appliquée à la SSR ci-dessus), le résultat sous forme vectorielle pour un classifieur sigmoïde :

```math
\nabla LogLoss_{sigmoid} = -\dfrac1n X^T(y-\hat y)
```

à comparer avec le gradient du MSE pour une régression linéaire ($\nabla SSR = -2X^T(y-\hat y)$, MSE = SSR/n donne le facteur 2/n) :

```math
\nabla MSE_{linear} = -\dfrac2n X^T(y-\hat y)
```

> [!WARNING]
> ⚠️ **Même forme, pas les mêmes nombres** : les deux gradients ont la structure $X^T(y-\hat y)$ (à un facteur près), mais ŷ n'est pas calculé pareil dans les deux cas — $\hat y_{linear} = X\beta$ (une droite) contre $\hat y_{sigmoid} = 1/(1+e^{-X\beta})$ (une courbe en S bornée entre 0 et 1). C'est cette ressemblance de forme, malgré des ŷ différents, qui rend la descente de gradient aussi simple à coder pour les deux modèles (~4 lignes NumPy).

:::

:::step Carte résumé

```math
LogLoss = -\dfrac1n\sum_{i=1}^n \big[y_i\log(\hat y_i) + (1-y_i)\log(1-\hat y_i)\big]
```

yᵢ et (1−yᵢ) sont des **interrupteurs** : selon la vraie classe, un seul des deux termes de la somme est actif. Le signe moins transforme un problème de maximisation (vraisemblance) en minimisation (Loss). Une prédiction confiante et fausse tend vers +∞ ; une prédiction confiante et juste tend vers 0.

:::

::::
