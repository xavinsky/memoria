---
title: Tirages aléatoires (lois usuelles)
type: syntax
---

## Entier aléatoire entre low (inclus) et high (exclu)
Syntaxe: **np.random.randint**(1, 6+1)
Résultat: int aléatoire entre 1 et 6 (ex: lancer de dé)

## Plusieurs tirages d'un coup
Syntaxe: **np.random.randint**(1, 6+1, 3)
Résultat: array de 3 entiers aléatoires

## Tirage(s) suivant une loi Binomiale(n,p)
Syntaxe: **np.random.binomial**(n=10, p=0.7, size=20)
Résultat: array de 20 résultats, chacun = nb de succès sur n essais

## N valeurs régulières pour tracer une courbe continue
Syntaxe: **np.linspace**(mu - 4*sigma, mu + 4*sigma, 1000)
Résultat: array de 1000 valeurs, utile pour une pdf
