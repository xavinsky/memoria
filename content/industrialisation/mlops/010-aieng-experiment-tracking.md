---
title: Tracking d'expériences — MLflow, Weights & Biases
---

Un projet ML génère vite des dizaines d'expériences (hyperparamètres, dataset, code différents) — sans outil dédié, impossible de retrouver quelle run précise a produit quel modèle, avec quels paramètres.

:::compare
- **MLflow** : open-source, auto-hébergeable — logue paramètres/métriques/artifacts d'une run (`mlflow.log_param`/`log_metric`/`log_artifact`) et fournit un Model Registry pour versionner les modèles entraînés
- **Weights & Biases (W&B)** : SaaS — dashboards collaboratifs riches, et des **sweeps** (recherche d'hyperparamètres) intégrés directement à l'outil
:::

> [!TIP]
> 👉 Ces outils s'appellent typiquement AUTOUR de la boucle d'entraînement (avant : log des hyperparamètres ; à chaque epoch : log des métriques ; à la fin : log du modèle comme artifact) — ils ne remplacent pas le code d'entraînement, ils l'instrumentent.
