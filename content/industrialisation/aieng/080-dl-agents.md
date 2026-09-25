---
title: Agents LLM — de répondeur à exécutant
subgroup: Agents
---

Un **Agent LLM** utilise un LLM pour PRENDRE DES ACTIONS vers un objectif — pas seulement répondre à une question, mais raisonner et utiliser des outils pour l'atteindre.

```math
\text{Observe} \rightarrow \text{Think} \rightarrow \text{Act} \rightarrow \text{Repeat}
```

:::compare
- **LLM = cerveau** : raisonne, décide de la prochaine action
- **Tools = mains** : exécutent des actions concrètes (Tool Calling, ci-dessus) — chercher sur le web, réserver, exécuter du code...
- **Memory = contexte dans le temps** : historique de la conversation/des actions passées, éventuellement une base de connaissances (RAG)
:::

Un **Multi-Agent System** répartit une tâche complexe entre plusieurs agents spécialisés (ex: un agent "recherche", un agent "résumé", un agent "rédaction") qui collaborent — permet la spécialisation, le parallélisme, et de découper un objectif en sous-tâches plus simples.

> [!TIP]
> 👉 En pratique (LangChain/LangGraph) : `create_agent(model, tools)` construit l'agent, `.invoke()`/`.stream()` l'exécute, un `checkpointer` lui donne une mémoire persistante par conversation (`thread_id`), et un `system_prompt` oriente son comportement — cf. page Syntaxes ▸ LangGraph — construire un agent. **LlamaIndex** est une alternative/complément à LangChain, plutôt orientée indexation/retrieval (RAG) mais propose aussi ses propres design patterns d'agents autonomes.
