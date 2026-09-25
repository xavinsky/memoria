---
title: Data Drift vs Concept Drift
subgroup: Supervision & Maintenance en Production
---

Un modèle en prod peut se dégrader sans aucun bug de code ni changement de son propre comportement — parce que le MONDE qu'il observe a changé. Deux phénomènes distincts, souvent confondus :

:::compare
- **Data Drift** : la distribution des FEATURES en entrée change dans le temps (ex: nouveaux profils d'utilisateurs, saisonnalité, nouvelle source de données) — le modèle reste valide en théorie, mais s'applique à des données différentes de celles vues à l'entraînement
- **Concept Drift** : la relation entre features et cible change (la fonction P(y|X) apprise par le modèle n'est plus la bonne) — même distribution d'entrée, mais le modèle devient FAUX car le phénomène réel qu'il modélise a changé (ex: comportement d'achat après un choc économique)
:::

> [!WARNING]
> ⚠️ Les deux se détectent différemment : le Data Drift se surveille en comparant les distributions des features entre entraînement et prod (ex: test de Kolmogorov-Smirnov) ; le Concept Drift demande d'observer la performance RÉELLE du modèle dans le temps — donc d'avoir accès aux vrais labels, souvent en différé.

> [!TIP]
> 👉 Notion générale, valable pour tout modèle ML — cf. [Monitorer un LLM en prod](#aieng-llm-monitoring) (page MLOps) pour le cas particulier des LLM (hallucinations, LLM-as-a-judge).
