---
title: Multi-Head Attention
subgroup: LLM
subsubgroup: Transformers
---

[[P:MultiHeadAttention]]

Le **Multi-Head Attention** exécute PLUSIEURS mécanismes d'attention en parallèle (des "têtes"), chacune sur une portion de l'espace d'embedding — chaque tête peut ainsi se spécialiser sur un aspect différent (ex: relations sémantiques vs syntaxiques).

```math
d_{head} = d_{model} / n_{heads}
```

Ex: $d_{model}=512$ avec 8 têtes → chaque tête traite des vecteurs de taille 64. Les sorties des têtes sont concaténées puis repassées dans une couche linéaire — même dimension de sortie ($d_{model}$) qu'avec une seule tête, mais le modèle apprend mieux.
