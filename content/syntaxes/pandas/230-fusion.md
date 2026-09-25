---
title: Fusion / jointures
subgroup: Jointures
type: syntax
---

## Jointure sur une clé commune
Syntaxe: **pd.merge**(df1, df2, on="cle", how="inner")
Résultat: DataFrame fusionné (lignes communes)

## Jointure avec clés différentes
Syntaxe: **pd.merge**(df1, df2, left_on="cle1", right_on="cle2", how="left")
Résultat: toutes les lignes de df1 + correspondances

## Empiler des lignes
Syntaxe: **pd.concat**([df1, df2], axis=0)
Résultat: DataFrame concaténé verticalement

## Ajouter des colonnes côte à côte
Syntaxe: **pd.concat**([df1, df2], axis=1)
Résultat: DataFrame concaténé horizontalement

## Piège : concaténer sans régénérer l'index → doublons
Syntaxe: pd.**concat**([df1, df2])
Résultat: chaque morceau garde son propre index d'origine : si df1 et df2 ont tous les deux un label 0, le résultat a deux lignes d'index 0 — utiliser ignore_index=True ou reset_index(drop=True) après pour éviter ça

## Forcer une erreur plutôt qu'un doublon silencieux
Syntaxe: pd.**concat**([df1, df2], verify_integrity=True)
Résultat: lève une erreur si le résultat contient des labels d'index dupliqués, au lieu de les laisser passer
