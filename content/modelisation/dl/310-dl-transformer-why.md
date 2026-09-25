---
title: Pourquoi remplacer le RNN — les limites du traitement séquentiel
subgroup: LLM
subsubgroup: Transformers
---

Un RNN (même LSTM/GRU, cf. groupe RNN) souffre de 3 limites qui l'empêchent de passer à l'échelle :

:::compare
- **1\. Calcul forcément séquentiel** : un token doit attendre le résultat du précédent — impossible à paralléliser, entraînement lent sur de longues séquences
- **2\. Vanishing gradient** : persiste même avec LSTM/GRU sur de très longues séquences (cf. Forward & Backward Propagation)
- **3\. Recency bias** : le modèle tend à privilégier le contexte récent — le début d'une longue phrase est facilement "oublié"
:::

> [!TIP]
> 👉 Le **Transformer** (papier "Attention is All You Need", 2017) répond aux trois à la fois : il traite TOUTE la séquence EN PARALLÈLE, via un mécanisme d'**attention** plutôt qu'un état interne séquentiel — à la base des LLM actuels (ChatGPT, Claude, Gemini...).
