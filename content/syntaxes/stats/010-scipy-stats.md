---
title: Scipy.stats — lois continues & statistiques
type: syntax
columns:
  Nom: col-nom
  Formule: col-formule
  Params: col-params
  Explication: col-explication
---

## Importer les fonctions utiles
Formule: from scipy.stats import **norm, skew, kurtosis**
Params: -
Explication: -

## Asymétrie d'une distribution (skewness)
Formule: **skew**(array)
Params: -
Explication: 0 si symétrique, >0 asymétrie à droite, <0 à gauche

## Aplatissement d'une distribution (kurtosis)
Formule: **kurtosis**(array)
Params: -
Explication: proche de 0 pour une gaussienne

## Créer une loi Normale N(µ,σ)
Formule: **norm**(mu, sigma)
Params:
```
$\mu$ : moyenne
$\sigma$ : écart-type
```
Explication: objet distribution, réutilisable avec .pdf / .cdf

## Densité de probabilité (pdf) en un point x
Formule: norm(mu, sigma).**pdf**(x)
Params: $x$ : point où évaluer la densité
Explication: float ou array — hauteur de la courbe

## Fonction de répartition (cdf)
Formule:
```
$$F(x) = P(X \le x)$$
norm(mu, sigma).**cdf**(x)
```
Params:
```
$x$ : valeur seuil
$X \sim \mathcal{N}(\mu,\sigma)$
```
Explication: -

## Probabilité que X dépasse une valeur
Formule:
```
$$P(X>v) = 1 - F(v)$$
1 - norm(mu, sigma).**cdf**(valeur)
```
Params:
```
$v$ : valeur seuil
$X \sim \mathcal{N}(\mu,\sigma)$
```
Explication: -

## cdf de la loi normale centrée réduite N(0,1), à partir d'un z-score
Formule:
```
$$\Phi(z) = P(Z \le z)$$
norm.**cdf**(z)
```
Params:
```
$z$ : score-z
$Z \sim \mathcal{N}(0,1)$
```
Explication: -

## Loi Binomiale(n,p) — raccourci scipy
Formule:
```
from scipy.stats import binom
binom(n, p).**pmf**(k)
```
Params:
```
$n$ : nombre d'essais
$p$ : probabilité de succès
$k$ : nombre de succès recherché
```
Explication: équivalent scipy de la formule manuelle math.comb(n,k) * p**k * (1-p)**(n-k) (cf. [Lois de probabilité discrètes](#lois-discretes), page Maths) — même logique que norm(mu, sigma) ci-dessus, mais pour une loi discrète
