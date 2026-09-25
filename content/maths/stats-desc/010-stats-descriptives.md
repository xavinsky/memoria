---
title: Statistiques descriptives (moyenne, dispersion, corrélation)
---

```math
\mu = \dfrac{1}{N}\sum_{i=1}^{N} x_i \qquad \bar x = \dfrac{1}{n}\sum_{i=1}^{n} x_i
```

**Moyenne** (`np.mean(data)`) — même formule, notation différente selon qu'on calcule sur toute la population ($\mu$, N éléments) ou sur un échantillon extrait de cette population ($\bar x$, n < N éléments).

```math
\text{Med}(X) = \begin{cases} x_{(\frac{n+1}{2})} & \text{si } n \text{ impair} \\ \dfrac{1}{2}\left(x_{(n/2)} + x_{(n/2+1)}\right) & \text{si } n \text{ pair} \end{cases}
```

**Médiane** (`np.median(data)`) — sépare les données triées en deux moitiés égales. n impair, ex: 1 3 3 6 7 8 9 → médiane = 6 (valeur du milieu). n pair, ex: 1 2 3 4 5 6 8 9 → médiane = (4+5)/2 = 4.5 (moyenne des deux valeurs du milieu). Contrairement à la moyenne, robuste aux outliers.

**Mode** (`statistics.mode(data)` ou `df["col"].mode()`) — il peut y avoir plusieurs modes (distribution bimodale).

```math
\sigma^2 = \dfrac{1}{N}\sum_{i=1}^{N}(x_i-\mu)^2 \qquad \sigma = \sqrt{\sigma^2}
```

**Variance** (`np.var(data)`) et **écart-type** (`np.std(data)`) de la population — ddof=0 par défaut. La variance mesure la dispersion autour de la moyenne (en unités au carré) ; l'écart-type ramène cette dispersion dans l'unité des données.

```math
s = \sqrt{\dfrac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2}
```

> [!WARNING]
> ⚠️ **Écart-type d'échantillon (correction de Bessel)** : diviser par n sous-estimerait la vraie variance de la population (biais) — diviser par n-1 corrige ce biais. Piège : `pd.Series(data).std()` utilise ddof=1 par défaut, `np.std(data)` utilise ddof=0 par défaut — même donnée, résultat différent si on ne fait pas attention.

```math
IQR = Q_3 - Q_1
```

```
q1, q3 = **np.percentile**(data, [25, 75])
iqr = q3 - q1
outliers = data[(data < q1 - 1.5*iqr) | (data > q3 + 1.5*iqr)]
```

**Écart interquartile (IQR)** — un point est un outlier s'il sort de $[Q_1 - 1.5\,IQR,\ Q_3 + 1.5\,IQR]$ : c'est la règle utilisée par les moustaches d'un boxplot (`sns.boxplot`).

```math
r = Corr(X,Y) = \dfrac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}{n\,\sigma_x\,\sigma_y}
```

**Corrélation de Pearson** (`df["col1"].corr(df["col2"])`, $r\in[-1,1]$) mesure la dépendance **linéaire** entre deux variables. X,Y indépendants ⇒ r=0, mais r=0 n'implique PAS indépendant — r ne capture que le lien linéaire (cf. Datasaurus / quartet d'Anscombe : mêmes stats, formes de nuage de points totalement différentes).
