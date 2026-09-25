---
title: Adapter un LLM — Training, Fine-tuning, Grounding
---

:::compare
- **Training** : construire un modèle DEPUIS ZÉRO sur un dataset massif — très coûteux, réservé aux grands labs
- **Fine-tuning** : repartir d'un modèle pré-entraîné et l'AJUSTER pour le spécialiser — moins coûteux, mais devient obsolète dès que les données changent
- **Grounding** : connecter le modèle à des données externes AU MOMENT DE L'USAGE (typiquement via RAG, ci-dessous) — pas de ré-entraînement du tout
:::

Le **PEFT** (Parameter-Efficient Fine-Tuning) limite le coût du fine-tuning : on FREEZE le modèle pré-entraîné et on n'entraîne que quelques couches supplémentaires, légères — ex: **LoRA** (Low-Rank Adaptation), ajoutée EN PARALLÈLE des blocs existants.

> [!TIP]
> 💡 Autres variantes de fine-tuning : l'**instruction tuning** (entraîner sur des paires instruction→réponse, pour généraliser à des tâches non vues) et le **RLHF** (Reinforcement Learning from Human Feedback — le signal de récompense vient d'évaluations humaines) sont à la base des modèles "chat" grand public.
