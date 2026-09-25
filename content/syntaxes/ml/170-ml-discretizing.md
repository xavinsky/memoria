---
title: Discretizing — pd.cut
subgroup: Transformation
type: syntax
---

## Transformer une variable continue en catégories
Syntaxe: df['col_bin'] = pd.**cut**(x=df['col'], bins=[min-1, mean, max+1], labels=['low','high'])
Résultat: bins : n+1 bornes pour n labels — transforme une tâche de régression en tâche de classification (ex: prix → Low/High)
