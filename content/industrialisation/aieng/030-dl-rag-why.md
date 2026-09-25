---
title: Pourquoi le RAG — les limites d'un LLM figé
subgroup: RAG
---

Un LLM ne connaît QUE ce qui était dans ses données d'entraînement — ses connaissances deviennent obsolètes, et il n'a jamais vu VOS données privées. Le ré-entraîner ou le fine-tuner à chaque mise à jour est coûteux, lent, et redevient obsolète aussitôt.

✅ Solution : donner le contexte pertinent directement DANS LE PROMPT (grounding, cf. ci-dessus), plutôt que de le graver dans les poids du modèle.

> [!WARNING]
> ⚠️ Mais la fenêtre de contexte (context window) d'un Transformer reste limitée en pratique — même à 128k-2M tokens (GPT-4/Claude/Gemini), on ne peut pas y faire tenir TOUTE une base documentaire, et le coût d'inférence croît avec sa taille (cf. [Self-Attention](#dl-transformer-attention), coût quadratique).

👉 Le **RAG** (Retrieval-Augmented Generation) répond à ce compromis : ne récupérer QUE les documents (ou passages) pertinents pour la question posée, et les injecter dans le prompt — au lieu de tout injecter, ou de fine-tuner.
