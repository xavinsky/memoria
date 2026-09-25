---
title: Prompt Injection — une faille logicielle inédite
---

L'IA générative introduit des failles logicielles inédites : contrairement à du code classique, un LLM ne distingue pas nativement "instructions" et "données" — le system prompt, l'historique et l'input utilisateur ne sont, techniquement, qu'un seul et même texte.

👉 Le **Prompt Injection** exploite ça : un utilisateur malveillant glisse de nouvelles instructions dans son propre message pour pousser le LLM à IGNORER ses consignes de sécurité initiales (ex: "ignore tes instructions précédentes et...").

:::compare
- **Injection directe** : l'attaquant tape lui-même l'attaque dans le chat
- **Injection indirecte** : l'attaque est cachée dans un contenu EXTERNE que le LLM va lire (page web, document RAG, email) — l'utilisateur final n'est pas complice, souvent pas même conscient de l'attaque
:::

> [!WARNING]
> ⚠️ Le RAG (source de documents externes) et les Agents (Tool Calling, navigation web) augmentent la surface d'attaque : tout contenu externe injecté dans le contexte peut contenir des instructions cachées — cf. LLM Guardrails ci-dessous pour s'en prémunir.
