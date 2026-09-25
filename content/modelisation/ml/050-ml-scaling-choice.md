---
title: Feature Scaling — quel scaler choisir
subgroup: Data Preparation
---

Nécessaire pour tout modèle basé sur une distance ou un gradient (KNN, SVM, régression régularisée, réseaux de neurones) — inutile pour les modèles à base d'arbres (Random Forest, etc.), invariants à l'échelle des features.

:::compare
- **StandardScaler** : choix par défaut — distribution à peu près symétrique, pas d'outliers extrêmes. Sensible aux outliers : une valeur extrême déforme la moyenne et l'écart-type utilisés.
- **MinMaxScaler** : features déjà bornées ou sparse (ex: pixels 0-255), ou modèle qui a besoin d'un intervalle fixe [0,1]. Ne réduit PAS l'effet des outliers — un seul point extrême écrase toute la plage pour les autres valeurs.
- **RobustScaler** : présence d'outliers qu'on ne veut pas (ou ne peut pas) retirer avant de modéliser — médiane/IQR au lieu de moyenne/écart-type, donc peu sensible aux valeurs extrêmes.
:::

> [!TIP]
> 👉 **Repère rapide** : outliers significatifs → RobustScaler ; sinon StandardScaler par défaut ; MinMaxScaler seulement si un intervalle borné [0,1] est spécifiquement requis (cf. Feature Scaling, page Syntaxes, pour la syntaxe).
