---
title: Nettoyer — Doublons
subgroup: Exploration & Nettoyage
type: syntax
---

## Détecter / compter les doublons
Syntaxe:
```
df.**duplicated**()          # booléen par ligne
df.duplicated().**sum**()    # nombre de doublons
```
Résultat: -

## Supprimer les doublons
Syntaxe: df = df.**drop_duplicates**()
Résultat: cf. Data Leakage : des lignes dupliquées présentes à la fois en train et en test faussent l'évaluation
