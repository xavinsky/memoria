---
title: Self-Attention — Query, Key, Value
subgroup: LLM
subsubgroup: Transformers
---

Le **Self-Attention** permet à chaque token d'une séquence de "regarder" tous les autres tokens pour calculer sa propre représentation, contextualisée par l'ensemble de la phrase.

Intuition (comme un dictionnaire Python, mais en lookup FLOU plutôt qu'exact) : chaque token est projeté en 3 vecteurs — **query** ("qu'est-ce que je cherche ?"), **key** ("qui suis-je ?"), **value** ("quelle information est-ce que j'apporte ?"). La similarité entre une query et toutes les keys détermine combien de chaque value est utilisé dans la sortie.

```math
\text{Attention}(Q,K,V) = \text{softmax}\Big(\dfrac{QK^\top}{\sqrt{d_{model}}}\Big)V
```

On divise par $\sqrt{d_{model}}$ (scaling) car le produit scalaire $QK^\top$ (somme de $d_{model}$ multiplications) devient vite très grand, ce qui déstabiliserait l'entraînement une fois passé au softmax.

> [!WARNING]
> ⚠️ Le coût de calcul de l'attention croît QUADRATIQUEMENT avec la longueur de la séquence (matrice sequence_length × sequence_length) — contrairement au nombre de poids appris ($W_Q, W_K, W_V$), qui n'en dépend PAS.
