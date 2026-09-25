---
title: Filtrage — Piège
subgroup: Sélection, filtrage & tri
type: syntax
---

## Cas sûr : lecture seule après filtrage, aucune modification prévue
Syntaxe:
```
sous_df = df[df["col"] > 10]
print(sous_df.**describe**())
```
Résultat: aucun risque : tu ne fais que lire, .copy() est inutile

## Cas sûr : modifier l'original en une seule étape
Syntaxe: df.**loc**[df["col"] > 10, "autre_col"] = 0
Résultat: modification directe et sûre de df, aucune ambiguïté

## Piège : sélection puis modification en deux étapes, sans copie
Syntaxe:
```
sous_df = df[df["col"] > 10].**copy**()
sous_df["nouvelle_col"] = 1
```
Résultat:
```
avec .copy() : sous_df devient un objet à part entière, le modifier ne touche jamais df
sans .copy() : ambigu -> SettingWithCopyWarning, pandas ne sait pas si tu voulais modifier df ou créer un objet séparé
```
Incorrect:
```
sous_df = df[df["col"] > 10]
sous_df["nouvelle_col"] = 1
```
