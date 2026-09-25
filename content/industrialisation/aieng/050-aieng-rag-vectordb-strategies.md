---
title: Vector Databases & recherche avancée — hybride, reranking
subgroup: RAG
---

Plusieurs **Vector Database** existent pour stocker et interroger des embeddings (cf. Pipeline RAG ci-dessus) — le choix dépend surtout du volume de données et du besoin ou non d'auto-hébergement.

:::compare
- **Chroma** : open-source, léger, facile à lancer en local — bon point de départ / prototypage
- **Qdrant** : open-source, auto-hébergeable ou managé — pensé pour la production à plus grande échelle, filtres riches sur les métadonnées
- **Pinecone** : SaaS entièrement managé — pas d'infra à gérer, mais dépendance à un service tiers payant
:::

La seule **similarity search** (cf. ci-dessus) a une limite : elle rate parfois un document pertinent qui partage peu de vocabulaire avec la question (recherche purement sémantique). Deux techniques la complètent :

:::compare
- **Recherche hybride (hybrid search)** : combine la recherche sémantique (embeddings) ET la recherche lexicale classique (mots-clés, ex: BM25) — récupère plus large avant de filtrer
- **Reranking** : un second modèle, plus coûteux mais plus précis, re-classe les documents déjà récupérés (souvent trop nombreux/bruts) pour ne garder que les meilleurs avant de les injecter dans le prompt
:::

> [!TIP]
> 👉 Pattern courant : récupérer large (ex: top 50) avec une recherche hybride rapide, puis reranker pour ne garder que le top 5-10 réellement injecté dans le prompt — compromis rappel/précision/coût.
