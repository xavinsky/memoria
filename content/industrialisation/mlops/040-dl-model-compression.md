---
title: Compresser un modèle — Quantization & Distillation
subgroup: Déploiement & Optimisation Hardware
---

Un LLM entier pèse souvent des dizaines/centaines de Go — trop lourd et lent pour un déploiement offline, mobile, ou sur du matériel limité. Deux techniques réduisent sa taille sans repartir de zéro.

:::compare
- **Quantization** : remplace des poids en flottant 32-bit par une précision plus faible (16-bit float, voire 8-bit int) — modèle plus petit, calculs plus rapides, perte de précision minime
- **Distillation** : entraîne un petit modèle ("élève") à imiter la DISTRIBUTION DE PROBABILITÉ d'un grand modèle ("professeur") — pas seulement ses labels finaux — ex: DistilBERT, 40% plus petit que BERT pour 97% de ses performances
:::

> [!TIP]
> 👉 Les deux techniques sont combinables et cumulables avec le PEFT (cf. [Adapter un LLM](#dl-llm-adapt), ci-dessus) — ex: QLoRA = LoRA appliqué à un modèle déjà quantizé.
