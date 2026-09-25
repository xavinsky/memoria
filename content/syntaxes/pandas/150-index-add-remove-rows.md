---
title: Ajouter / enlever des lignes
subgroup: Transformation
type: syntax
---

## Ajouter une ligne
Syntaxe: pd.**concat**([df, pd.DataFrame([{"col1": val1, "col2": val2}])], ignore_index=True)
Résultat: concat garde l'index d'origine de chaque morceau — la nouvelle ligne a par défaut un index qui recommence à 0, donc sans ignore_index=True elle peut dupliquer un label déjà présent dans df ; ignore_index=True régénère un RangeIndex propre pour tout le résultat

## Ajouter une ligne à un label précis
Syntaxe: df.**loc**[len(df)] = [val1, val2]
Résultat: ajoute une ligne au label len(df) — ne fonctionne proprement que si l'index est déjà un RangeIndex 0..n-1 sans trou, sinon le label choisi peut déjà exister

## Supprimer une ligne cible le label, pas la position
Syntaxe: df.**drop**(1)
Résultat: supprime la ligne dont le label d'index vaut 1 — si l'index n'est plus un RangeIndex propre (après un filtrage précédent), ça peut ne pas être la 2e ligne du DataFrame

## Supprimer une ligne par position (peu importe son label)
Syntaxe: df.**drop**(df.index[1])
Résultat: supprime la 2e ligne du DataFrame, quel que soit son label — équivalent positionnel de drop(1)

## Sélection par label vs par position
Syntaxe: df.**loc**[1] / df.**iloc**[1]
Résultat: loc cherche le label 1 dans l'index (peut échouer ou renvoyer plusieurs lignes si doublon) ; iloc prend toujours la 2e ligne, par position, indépendamment des labels
