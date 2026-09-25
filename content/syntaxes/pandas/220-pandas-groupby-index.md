---
title: 'Groupby : gérer l''index (to_frame, reset_index, reindex)'
subgroup: Agrégation
type: syntax
---

## Nombre de lignes par groupe, en colonne directement nommée
Syntaxe: df.groupby("order_id").**size**().**to_frame**("number_of_items").reset_index()
Résultat: DataFrame à 2 colonnes ["order_id", "number_of_items"] : .size() (Series) -> .to_frame(nom) (nomme la colonne) -> .reset_index() (l'index de groupe redevient une colonne)

## Repasser en DataFrame "plat" après groupby
Syntaxe: df.groupby("col").mean().**reset_index**()
Résultat: index de groupe redevenu colonne — même logique utilisée dans to_frame().reset_index() ci-dessus

## Combler les groupes absents avec une valeur par défaut
Syntaxe: df.groupby("col").size().**reindex**(liste_complete, fill_value=0)
Résultat: recale la Series sur toutes les clés de liste_complete — les groupes manquants du groupby prennent 0 au lieu d'être absents

## Piège : reindex() droppe silencieusement ce qui n'est pas dans la nouvelle liste
Syntaxe: serie.**reindex**(liste_complete)
Résultat: toute clé présente dans serie mais absente de liste_complete disparaît sans avertissement — utile si liste_complete est bien exhaustive, dangereux sinon (incohérence de données, ex: order_id de reviews absent de orders)
