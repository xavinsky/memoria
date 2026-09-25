---
title: Feature Store — Feast, Hopsworks
---

Un **Feature Store** centralise les features (colonnes calculées) utilisées pour entraîner un modèle, pour garantir que l'ENTRAÎNEMENT et le SERVING (inférence en prod) utilisent EXACTEMENT le même calcul de feature.

> [!WARNING]
> ⚠️ Sans feature store, un décalage entre le code de calcul de feature utilisé à l'entraînement et celui utilisé en prod (le **training-serving skew**) est un piège classique : le modèle performe bien en test, mal en prod, sans bug de code évident.

:::compare
- **Offline store** : historique complet des features, optimisé pour constituer un dataset d'entraînement
- **Online store** : accès à faible latence aux features les plus récentes, pour l'inférence temps réel en prod
:::

:::compare
- **Feast** : open-source — orchestre offline store + online store en réutilisant l'infra déjà en place (ex: BigQuery/Redis)
- **Hopsworks** : plateforme MLOps plus complète incluant un feature store managé et des pipelines de calcul de features
:::
