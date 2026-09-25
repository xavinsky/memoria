---
title: Architecture — Positional Encoding, blocs, masquage
subgroup: LLM
subsubgroup: Transformers
---

Un token perd son ordre dans la séquence dès qu'on le traite en parallèle (contrairement à un RNN) — le **Positional Encoding** (appris, ou construit via des sinusoïdes) est donc ADDITIONNÉ à l'embedding de chaque token pour réintroduire l'information de position.

Encodeur ET décodeur sont des piles de blocs IDENTIQUES en structure (poids différents, input_dim = output_dim à chaque bloc). Chaque bloc combine : Self-Attention (multi-têtes) → **skip connection** (n'apprend que la différence par rapport à l'entrée, cf. logique résiduelle) + normalisation → Feed-Forward Network (mélange les features D'UN MÊME token, ajoute de la non-linéarité).

:::compare
- **Self-Attention (encodeur)** : chaque token regarde TOUS les tokens de la séquence, y compris ceux qui suivent
- **Masked Self-Attention (décodeur)** : chaque token ne regarde que les tokens PRÉCÉDENTS (les suivants sont masqués à $-\infty$ avant le softmax) — indispensable pour ne pas "tricher" en s'entraînant à prédire le futur
- **Cross-Attention (décodeur)** : la query vient du décodeur, mais les keys/values viennent de la sortie de l'ENCODEUR — c'est ce qui relie les deux blocs
:::
