---
title: Schéma d'infrastructure — Plateforme d'agents IA
subgroup: Local
---

Exemple d'architecture LOCALE pour une **plateforme d'agents IA** — plusieurs agents spécialisés collaborent via un orchestrateur et un état partagé, exposée comme un service unique derrière des Guardrails.

![](../../diagrams/infra-arch-agents-1.svg)

> [!TIP]
> 👉 Ce pattern (orchestrateur + agents spécialisés + état partagé) correspond à un graphe LangGraph multi-agents avec `checkpointer` — cf. [Agents LLM](#dl-agents) (page AI Engineering, plus haut) pour le détail du Multi-Agent System.
