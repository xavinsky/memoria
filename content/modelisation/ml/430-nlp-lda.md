---
title: LDA (Topic Modeling non supervisé)
subgroup: Modèles
subsubgroup: NLP
---

[[P:LatentDirichletAllocation]]

**Latent Dirichlet Allocation** — algorithme NON supervisé qui découvre des "topics" (thèmes) cachés (latents) dans un corpus de documents, sans labels fournis à l'avance.

Un document = mélange de topics ; un topic = mélange de mots (distribution de type Dirichlet pour les deux).

1. Choisir le nombre de topics à détecter (n_components)
2. Assigner aléatoirement chaque mot de chaque document à un topic
3. Pour chaque document : calculer p(topic t | document d) — le "document mixture"
4. Pour chaque topic : calculer p(mot w | topic t) — le "topic mixture"
5. Mettre à jour p(mot w avec topic t) = p(t|d) × p(w|t), répéter sur plusieurs itérations

> [!TIP]
> 👉 Les topics obtenus peuvent s'interpréter comme des "composantes principales non-linéaires" des documents du corpus (cf. PCA, groupe ml) — sortie utilisable pour explorer un corpus sans labels préexistants.

> [!WARNING]
> ⚠️ Vectoriser avec `CountVectorizer`, PAS `TfidfVectorizer` — LDA modélise des COMPTAGES bruts (loi multinomiale) ; passer du Tf-idf casse cette hypothèse (perplexité nettement dégradée, vérifié empiriquement).
