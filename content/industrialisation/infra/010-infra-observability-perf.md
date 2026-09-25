---
title: Observabilité de performance — latence, débit
subgroup: Supervision & Maintenance en Production
---

Une fois un modèle déployé (cf. page MLOps ▸ Format d'inférence & moteurs), le monitoring d'infra classique (CPU/RAM/uptime) ne suffit pas — l'inférence, surtout pour un LLM, a ses propres métriques de performance à suivre en continu (**Observabilité**).

:::compare
- **Latence** : pour un LLM en streaming, se décompose en **TTFT** (Time To First Token — délai avant le premier token renvoyé) et **TPOT** (Time Per Output Token — délai entre chaque token suivant) ; TTFT domine la réactivité perçue, TPOT domine la vitesse de lecture perçue
- **Débit (throughput)** : volume traité par unité de temps — tokens/seconde ou requêtes/seconde ; se règle surtout au niveau du moteur d'inférence plutôt qu'au niveau applicatif (cf. [vLLM/TGI](#aieng-inference-optimization), page MLOps)
:::

> [!TIP]
> 👉 Ces deux métriques s'opposent souvent en pratique : le **continuous batching** (regrouper plusieurs requêtes ensemble) augmente le débit global, mais peut allonger la latence individuelle de chaque requête prise à part.
