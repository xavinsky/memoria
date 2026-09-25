---
title: Évaluer un LLM — BLEU, ROUGE, Perplexité
subgroup: LLM
subsubgroup: Transformers
---

Les métriques de classification classiques (Accuracy, Precision, Recall, F1 — cf. groupe ml) restent valables quand un LLM sert à CLASSIFIER. Pour des tâches Seq2Seq (traduction, résumé), il faut d'autres métriques : il existe souvent plusieurs bonnes réponses différentes, pas UNE seule vérité terrain.

:::compare
- **BLEU** : proportion des n-grammes du texte généré qui apparaissent dans la référence (proche d'une precision), pénalise les textes trop courts — utilisé en traduction
- **ROUGE** : proportion de l'information de la référence retrouvée dans le texte généré (proche d'un recall) — utilisé en résumé
- **Perplexité** : mesure à quel point le modèle est "surpris" par les données (probabilité qu'il assigne à chaque token suivant) — utilisée surtout pendant l'entraînement
:::

> [!TIP]
> 👉 Pour des tâches ouvertes (génération libre), on complète souvent par de l'évaluation humaine (fluidité, pertinence, cohérence) ou du **LLM-as-a-judge** (un autre LLM évalue la sortie).
