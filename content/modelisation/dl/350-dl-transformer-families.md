---
title: Encoder-only, Decoder-only, Encoder-Decoder
subgroup: LLM
subsubgroup: Transformers
---

:::compare
- **Encoder-only (ex: BERT)** : attention bidirectionnelle (lit toute la séquence d'un coup), ne génère pas de texte — produit des embeddings contextuels pour classification, NER...
- **Decoder-only (ex: GPT)** : génération autorégressive, un token à la fois, de gauche à droite, à partir d'un prompt
- **Encoder-Decoder (ex: T5)** : combine les deux — pour les tâches séquence→séquence (traduction, résumé, question-réponse)
:::

Pour réutiliser un modèle encoder-only déjà entraîné (ex: BERT) sur une nouvelle tâche : ajouter une "tête" de classification par-dessus ses embeddings de sortie — même logique que le Transfer Learning en CNN (cf. groupe CNN) — soit en gelant l'encodeur, soit en le ré-entraînant aussi.

> [!TIP]
> 👉 **Token [CLS]** — un token spécial que BERT place au tout début de chaque séquence ; son embedding de sortie résume l'information de la phrase ENTIÈRE (grâce à l'attention bidirectionnelle) — c'est LUI qu'on réutilise comme feature pour la tête de classification, plutôt que les embeddings des mots individuels.
