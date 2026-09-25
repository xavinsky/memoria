---
title: MCP (Model Context Protocol) — standardiser l'accès aux outils
subgroup: Agents
---

Avant MCP, connecter un agent à N outils/sources de données demandait autant d'intégrations sur-mesure que de combinaisons agent × outil (le **problème M×N**) — chaque framework devait réécrire son propre connecteur pour chaque API/base de données. Le **MCP** (Anthropic, novembre 2024) résout ça en standardisant l'accès : un outil exposé UNE SEULE FOIS via un serveur MCP devient utilisable par N'IMPORTE QUEL agent compatible MCP, sans code de connexion dédié.

:::compare
- **MCP Server** : expose des Tools (fonctions appelables, cf. [Tool Calling](#dl-tool-calling) ci-dessus), des Resources (données consultables) et des Prompts (templates réutilisables) — un serveur par source/outil (ex: un serveur GitHub, un serveur PostgreSQL, un serveur Slack)
- **MCP Client** : intégré dans l'application agent (Claude, un IDE, un framework custom...) — découvre les capacités d'un serveur MCP et les rend disponibles au LLM, via un protocole standard (JSON-RPC)
:::

> [!TIP]
> 👉 MCP ne remplace pas le Tool Calling — il en standardise le CÂBLAGE. Le Tool Calling reste la capacité du LLM à choisir quelle fonction appeler ; MCP est le protocole qui permet à cette fonction d'être exposée une seule fois et réutilisée par n'importe quel agent, plutôt que réécrite pour chacun — un peu comme un port USB-C plutôt qu'un câble propriétaire par paire modèle/outil. Devenu un standard de facto adopté au-delà d'Anthropic (OpenAI, Google, Microsoft).
