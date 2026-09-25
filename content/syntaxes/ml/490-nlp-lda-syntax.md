---
title: LDA — Topic Modeling
subgroup: NLP
type: syntax
---

## Instancier et fitter
Syntaxe:
```
from sklearn.decomposition import LatentDirichletAllocation
lda = **LatentDirichletAllocation**(n_components=2, max_iter=100)
lda.fit(X)
```
Résultat: X = matrice document-terme déjà vectorisée (CountVectorizer/TfidfVectorizer)

## Mixture de topics par document
Syntaxe: lda.**transform**(X)
Résultat: matrice (n_documents × n_topics) — poids de chaque topic dans chaque document

## Mixture de mots par topic
Syntaxe: lda.**components_**
Résultat: matrice (n_topics × n_mots) — poids de chaque mot dans chaque topic
