---
title: Nettoyer une série — dates manquantes & fréquence
subgroup: Time Series
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Combler les dates manquantes dans l'index
Syntaxe:
```
full_range = pd.**date_range**(df.index.min(), df.index.max(), freq="D")
df = df.**reindex**(full_range)
```
Params: freq : "D" (jour), "ME" (fin de mois), "MS" (début de mois)...
Explication: reindex() fait apparaître des NaN exactement aux dates absentes de l'index d'origine — combler ensuite avec interpolate()

## Combler les NaN par interpolation linéaire
Syntaxe: df['col'] = df['col'].**interpolate**("linear")
Params: -
Explication: relie les points connus par une droite — mieux qu'une imputation par moyenne/médiane qui casserait la continuité temporelle

## Changer la fréquence — agréger (ex: jour → mois)
Syntaxe: monthly = df.**resample**("ME").mean()
Params: "ME" (fin de mois) vs "MS" (début de mois) : change l'index résultant — vérifier lequel est attendu en aval
Explication: peut laisser un NaN résiduel sur la dernière période (incomplète) — interpolate() après resample() si besoin
