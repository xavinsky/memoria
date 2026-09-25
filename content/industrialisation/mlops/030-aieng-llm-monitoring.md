---
title: Monitorer un LLM en prod — hallucinations, drift, LLM-as-a-judge
subgroup: Évaluation & Monitoring des LLMs
---

Une fois en prod, un LLM peut se dégrader SILENCIEUSEMENT — pas d'erreur explicite comme un crash logiciel classique. D'où le besoin d'un monitoring dédié, en plus des métriques d'entraînement classiques (Accuracy/F1, BLEU/ROUGE, Perplexité — cf. Modélisation ▸ Évaluer un LLM).

:::compare
- **Détection d'hallucinations** : le modèle génère une information fausse, présentée avec assurance — détectable via un second LLM "juge" ou des règles de cohérence factuelle par rapport aux sources (RAG)
- **Drift** : la distribution des requêtes ou des réponses change dans le temps par rapport aux données d'évaluation initiales — la performance se dégrade sans qu'aucun code n'ait changé (cas particulier LLM du [Data Drift / Concept Drift](#infra-drift), notion générale valable pour tout modèle ML, cf. page Infrastructure)
:::

👉 L'**Évaluation automatisée (LLM-as-a-judge)** utilise un LLM (souvent plus puissant que celui évalué) pour noter la qualité d'une réponse selon des critères définis (pertinence, factualité, ton) — scalable comparé à une évaluation humaine systématique, mais hérite des biais du LLM juge lui-même.

> [!TIP]
> 👉 Sécurité et robustesse (gardes-fous / guardrails) font aussi partie du monitoring — cf. [LLM Guardrails](#aieng-llm-guardrails), plus haut, mêmes détections réutilisées en blocage temps réel ET en suivi de qualité dans le temps.
