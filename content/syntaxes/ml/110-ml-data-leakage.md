---
title: Train/test split — Data Leakage, piège transversal
subgroup: Test
type: syntax
---

## Règle générale
Syntaxe:
```
transformer.**fit**(X_train)  # jamais X_test ou X entier
X_train = transformer.**transform**(X_train)
X_test = transformer.**transform**(X_test)
```
Résultat: toute transformation (scaler, encoder, imputer...) doit être fit uniquement sur le train set, puis appliquée (transform) identiquement au train et au test
