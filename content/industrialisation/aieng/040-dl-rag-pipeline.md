---
title: Pipeline RAG — Embedding, Vector Database, Retrieval
subgroup: RAG
---

1. **Indexation** (une fois) : découper les documents en chunks AVEC un léger chevauchement (pour ne pas perdre le contexte à une frontière de coupe), calculer leur **embedding** (cf. groupe NLP) et les stocker dans une **Vector Database** (ex: Chroma) avec leurs métadonnées (texte original, source, date...)
2. **Embed** la question posée, AVEC LE MÊME modèle d'embedding que celui utilisé pour les documents
3. **Similarity search** : chercher dans la vector database les documents dont l'embedding est le plus proche de celui de la question — la **Cosine Similarity** (angle entre les deux vecteurs) est la plus utilisée pour du RAG, devant les distances euclidienne/Manhattan (cf. KNN, groupe ml)
4. **Génération** : concaténer les documents retrouvés + la question dans le prompt, et le passer au LLM

> [!TIP]
> 👉 "Retrieval-Augmented Generation" = Information Retrieval (étapes 1-3) + Text Generation (étape 4) — le LLM ne génère qu'APRÈS avoir reçu le contexte pertinent.
