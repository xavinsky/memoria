---
title: Scipy — Optimisation (minimize, curve_fit, interpolate)
subgroup: Optimisation
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Minimiser une fonction depuis un point de départ (minimum LOCAL)
Formule / Syntaxe:
```
from scipy import optimize
res = optimize.**minimize**(f, x0)
res.x, res.fun
```
Params:
```
f : fonction à minimiser (accepte un scalaire ou un array)
x0 : point de départ
```
Explication: ne trouve qu'un minimum LOCAL — reste bloqué dedans si f n'est pas convexe, sauf si x0 est déjà proche du minimum global (cf. minimum local, page Modélisation ▸ Descente de gradient)

## Minimiser sous contraintes et bornes
Formule / Syntaxe: optimize.minimize(h, X0, **method**="SLSQP", **bounds**=((1,5),)*4, **constraints**=[{"type":"eq","fun":c1}, {"type":"ineq","fun":c2}])
Params:
```
bounds : une paire (min,max) par variable
constraints : liste de dicts — type "eq" (=0 requis) ou "ineq" (≥0 requis)
```
Explication: SLSQP est la méthode qui supporte contraintes ET bornes simultanément ; une contrainte d'égalité s'écrit comme une fonction qui doit valoir 0 à la solution, une inégalité comme une fonction qui doit rester ≥0

## Trouver le minimum GLOBAL (recherche multi-départs)
Formule / Syntaxe:
```
optimize.**shgo**(g, bounds)
# ou, plus stochastique :
optimize.**dual_annealing**(g, bounds)
```
Params: bounds : une paire (min,max) par dimension
Explication: optimize.minimize seul ne garantit qu'un minimum local — shgo (déterministe, efficace en petite dimension) et dual_annealing (recuit simulé, stochastique) explorent l'espace plus largement pour approcher le minimum global

## Ajuster les paramètres d'une fonction à un nuage de points
Formule / Syntaxe:
```
def f(x, a, b, c):
    return a*x**2 + b*x + c

popt, pcov = optimize.**curve_fit**(f, x, y)
```
Params:
```
popt : paramètres optimaux trouvés (a,b,c)
pcov : matrice de covariance (incertitude sur popt), souvent ignorée
```
Explication: trouve directement les paramètres qui minimisent l'erreur quadratique entre f(x, *popt) et y — pas besoin d'implémenter soi-même la recherche (cf. optimize.minimize)

## Interpoler entre des points connus (remplir les blancs)
Formule / Syntaxe:
```
from scipy import interpolate
f_interp = interpolate.**interp1d**(x, y, kind="cubic")
y_dense = f_interp(x_dense)
```
Params: kind : "linear" (défaut, coudes aux points connus), "quadratic", "cubic" (plus lisse)
Explication: renvoie une fonction continue calée exactement sur les points connus (x,y) — appelable sur n'importe quelle grille dense (x_dense) pour combler les blancs entre eux
