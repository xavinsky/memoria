---
title: Prompt Engineering — principes
subgroup: LLM
subsubgroup: Transformers
---

Formuler soigneusement l'instruction donnée à un LLM pour améliorer sa réponse — SANS toucher à ses poids (contrairement au fine-tuning, cf. [Adapter un LLM](#dl-llm-adapt), groupe AI Engineering). Le prompt fait partie du contexte fourni au moment de l'usage, pas de l'entraînement.

:::compare
- **Zero-shot** : seulement l'instruction, aucun exemple — repose entièrement sur ce que le modèle a déjà appris pendant son pré-entraînement
- **Few-shot** : quelques exemples (entrée → sortie attendue) inclus dans le prompt, pour montrer le format/style voulu sans ré-entraîner
- **Chain-of-thought** : demander explicitement au modèle de raisonner étape par étape avant de donner sa réponse finale — améliore nettement les tâches qui demandent plusieurs étapes de raisonnement (calcul, logique)
:::

> [!TIP]
> 👉 Un prompt bien structuré (rôle donné au modèle, format de sortie attendu explicite, contraintes précisées) réduit la variance des réponses — surtout utile avant d'envisager un fine-tuning, nettement plus coûteux.
