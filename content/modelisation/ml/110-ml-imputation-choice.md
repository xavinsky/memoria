---
title: Imputation — quelle stratégie choisir
subgroup: Data Preparation
---

Combler les valeurs manquantes (NaN) avant `.fit()` — la plupart des modèles Sklearn ne tolèrent aucun NaN.

:::compare
- **mean / median (SimpleImputer)** : colonne numérique — mean si distribution à peu près symétrique sans outliers ; median si distribution asymétrique ou avec outliers (plus robuste, même logique que RobustScaler).
- **most_frequent (SimpleImputer)** : colonne catégorielle — remplace par la modalité la plus fréquente.
- **constant (SimpleImputer)** : valeur fixe imposée (ex: 0, "Unknown") — utile quand NaN a un sens propre plutôt qu'une vraie donnée manquante (cf. Nettoyer, dans chaque workflow).
- **KNNImputer** : remplace par la moyenne des k plus proches voisins (calculée sur les autres colonnes) — plus précis qu'une moyenne globale, mais plus coûteux et sensible à l'échelle des features (scaler les colonnes avant).
:::

> [!TIP]
> 👉 **Repère rapide** : peu de NaN et pas de structure particulière → SimpleImputer (median par défaut) ; NaN corrélés à d'autres colonnes (ex: features géographiques proches) → KNNImputer peut capter cette structure (cf. [Valeurs manquantes](#ml-missing-data), page Syntaxes, pour la syntaxe).
