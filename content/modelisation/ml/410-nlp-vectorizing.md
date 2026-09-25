---
title: Vectorizing (Bag-of-Words, Tf-idf, N-grams)
subgroup: Modèles
subsubgroup: NLP
---

[[P:CountVectorizer]] · [[P:TfidfVectorizer]]

**Vectorizing** — convertir du texte préprocessé en représentation numérique, seule forme exploitable par un modèle ML.

**Bag-of-Words (BoW)** — compte les occurrences de chaque mot du vocabulaire dans chaque document ; chaque mot devient une feature (une colonne).

:::compare
- **Ne capture PAS la longueur du document** : un mot répété 5 fois dans un texte long pèse autant qu'un mot répété 5 fois dans un texte court → Tf-idf corrige ça
- **Ne capture PAS le contexte/ordre** : "j'aime les acteurs mais pas le film" et "j'aime le film mais pas les acteurs" ont EXACTEMENT la même représentation BoW → N-grams corrige ça
:::

```math
TF_{x,d} = \dfrac{\text{occurrences de } x \text{ dans } d}{\text{nombre total de mots de } d}
```

**Term Frequency (tf)** — fréquence relative d'un mot x dans un document d, normalisée par la longueur du document (contrairement au simple comptage du BoW).

```math
w_{x,d} = \underbrace{tf_{x,d}}_{\text{tf}} \times \underbrace{\left[\log\!\left(\dfrac{N+1}{df_x+1}\right)+1\right]}_{\text{idf}}
```

**Tf-idf** — pondère tf par l'**inverse document frequency (idf)** : un mot rare dans le corpus (petit $df_x$, ex: "concussion") pèse plus lourd qu'un mot omniprésent (grand $df_x$, ex: "football" dans un journal sportif) — l'idée étant qu'un mot présent partout n'aide pas à distinguer les documents entre eux.

**N-grams** — au lieu de compter des mots isolés (unigrams), compter des séquences de n mots consécutifs (bigrams n=2, trigrams n=3...) — restaure une partie du contexte perdu par le BoW/Tf-idf.

> [!TIP]
> 👉 **Contrôler la taille du vocabulaire** (curse of dimensionality, cf. Feature Selection ci-dessus) : `min_df`/`max_df` retirent les mots trop rares/trop fréquents, `max_features` garde les k mots les plus fréquents, `ngram_range` fixe la longueur des séquences capturées (cf. page Syntaxes pour la syntaxe exacte).
