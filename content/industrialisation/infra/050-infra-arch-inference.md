---
title: Schéma d'infrastructure — Inférence
subgroup: Local
---

Exemple d'architecture LOCALE pour servir un modèle en inférence — la réponse repasse par les mêmes Guardrails (filtrage de sortie) avant de revenir au Client (flux retour non représenté ici, cf. carte dédiée).

![](../../diagrams/infra-arch-inference-1.svg)

> [!TIP]
> 👉 Le modèle chargé par le Moteur d'inférence est en général déjà compressé (cf. [Quantization / Distillation](#dl-model-compression), page MLOps) — réduit la VRAM nécessaire (cf. [Configuration Hardware](#infra-hardware-gpu), ci-dessus) et améliore le débit.
