---
title: Data Leakage
subgroup: Data Preparation
---

**Définition** — information du test set (ou du futur) qui fuite dans l'entraînement, faussant l'évaluation à la hausse.

:::compare
- **Doublons** : partagés entre train et test
- **Scaler / encoder** : fit sur tout le dataset avant le split
- **Oversampling** : appliqué avant le split
- **Feature dérivée de la target** : ex: une colonne prix_euros ≈ target convertie dans une autre unité
:::

> [!TIP]
> 👉 **Règle générale** : toute transformation (scaler, encoder, imputer...) doit être fit uniquement sur le train set, puis appliquée (transform) identiquement au train et au test (cf. Train/test split, page Syntaxes).
