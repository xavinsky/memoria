---
title: Schéma d'infrastructure — RAG
subgroup: Local
---

Exemple d'architecture LOCALE pour du RAG — deux flux distincts partagent la même Vector Database : l'**indexation** des documents (hors ligne, en haut) et la **requête** utilisateur (à la demande, en bas).

![](../../diagrams/infra-arch-rag-1.svg)

> [!TIP]
> 👉 Le Moteur d'inférence reçoit la question + le contexte récupéré (cf. [Pipeline RAG](#dl-rag-pipeline), ci-dessus) — la réponse générée revient ensuite au Client (flux retour non représenté ici).
