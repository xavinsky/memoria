---
title: Évaluer un Agent — au-delà des métriques LLM classiques
subgroup: Agents
---

Les métriques vues précédemment (Accuracy/F1, BLEU/ROUGE, Perplexité — cf. [Évaluer un LLM](#dl-transformer-evaluation), groupe Transformers) restent valables pour évaluer LE LLM sous-jacent. Évaluer un AGENT est plus difficile : il prend des actions, utilise des outils, raisonne en plusieurs étapes.

:::compare
- **Goal completion rate** : l'agent a-t-il atteint l'objectif final ?
- **Tool usage correctness** : a-t-il utilisé les bons outils, avec les bons arguments ?
- **Efficacité** : en combien d'étapes / de temps ?
- **Robustesse** : le comportement reste-t-il correct si l'input change légèrement ?
:::

> [!TIP]
> 👉 Des benchmarks standardisés existent pour comparer les LLM entre eux (GLUE/MMLU pour la compréhension, HumanEval pour le code, ToolBench/AgentBench pour les agents...) — souvent disponibles sur Hugging Face.
