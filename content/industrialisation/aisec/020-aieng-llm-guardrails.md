---
title: LLM Guardrails — NeMo Guardrails, Llama Guard
---

Les **LLM Guardrails** sont des briques logicielles intermédiaires — des "firewalls de texte" — placées entre l'utilisateur et le LLM, pour filtrer les entrées toxiques/malveillantes (cf. Prompt Injection ci-dessus) et empêcher le modèle de divulguer des données confidentielles ou son propre system prompt.

:::compare
- **Input rail** : filtre l'entrée AVANT qu'elle n'atteigne le LLM (détection d'injection, de contenu toxique)
- **Dialog rail** : contraint le LLM à rester dans un périmètre de sujets autorisés
- **Output rail** : filtre la réponse générée APRÈS coup, avant de la renvoyer à l'utilisateur (fuite de données, contenu inapproprié)
:::

:::compare
- **NeMo Guardrails** : framework open-source (NVIDIA) — définit des règles programmables (scripts Colang) qui encadrent les échanges avec le LLM
- **Llama Guard** : un LLM (Meta) lui-même fine-tuné pour CLASSIFIER si un contenu (entrée ou sortie) est sûr ou non selon des catégories de risque prédéfinies
:::

> [!TIP]
> 👉 Les guardrails recoupent le monitoring des LLMs en prod (cf. [Monitorer un LLM en prod](#aieng-llm-monitoring), plus bas) : les mêmes détections (hallucination, contenu toxique) alimentent à la fois un blocage temps réel (guardrail) et un suivi de qualité dans le temps (monitoring).
