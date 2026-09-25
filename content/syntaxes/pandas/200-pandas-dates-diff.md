---
title: 'Différence entre deux dates : précision'
subgroup: Dates
type: syntax
---

## Piège : .dt.days tronque à l'entier (perte de précision)
Syntaxe: (df["date_livree"] - df["date_achat"]).**dt.days**
Résultat: int — arrondit vers le bas, 8.9 jours devient 8 : à éviter si la valeur exacte compte (ex: variable d'entrée d'une régression)

## Différence de dates en jours, avec décimales
Syntaxe: (df["date_livree"] - df["date_achat"]) / **np.timedelta64**(24, "h")
Résultat: float — ex: 8.9, garde la précision

## Équivalent avec pd.Timedelta
Syntaxe: (df["date_livree"] - df["date_achat"]) / **pd.Timedelta**(days=1)
Résultat: float, même résultat que np.timedelta64(24,"h"), lisibilité différente
