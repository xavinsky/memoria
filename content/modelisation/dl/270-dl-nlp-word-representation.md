---
title: Représenter les mots — pourquoi un Embedding
subgroup: LLM
subsubgroup: NLP
---

Une phrase est une séquence de mots (une observation à chaque pas de temps, cf. groupe RNN ci-dessus) — mais un réseau de neurones n'accepte que des nombres. Deux fausses bonnes idées avant d'arriver à la solution :

:::compare
- **❌ Tokenisation naïve (1 entier par mot)** : ex: {"this":9, "is":8, "good":1...} — fait croire au modèle à un ORDRE entre les mots (9 > 8 n'a aucun sens linguistique)
- **❌ One-Hot Encoding** : un corpus dépasse facilement 10 000 mots uniques — vecteur beaucoup trop grand et creux (sparse) pour être exploitable
:::

✅ Un **Embedding** représente chaque mot par un vecteur DENSE de dimension choisie (typiquement 30 à 300) — deux mots proches sémantiquement ("chat"/"chien") sont proches mathématiquement dans cet espace.

```math
V(\text{Reine}) - V(\text{Roi}) \approx V(\text{Femme}) - V(\text{Homme})
```

> [!TIP]
> 👉 Illustration classique : dans un bon espace d'embedding, des opérations arithmétiques sur les vecteurs de mots correspondent à des relations de sens (cf. formule ci-dessus).
