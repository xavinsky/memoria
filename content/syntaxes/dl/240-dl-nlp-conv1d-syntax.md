---
title: Conv1D — convolution pour du texte
subgroup: LLM
subsubgroup: NLP
type: syntax
---

## Convolution 1D après un Embedding
Syntaxe: model.add(layers.**Conv1D**(filters=20, kernel_size=3))
Résultat: glisse uniquement le long de l'axe des mots (jamais sur l'axe de l'embedding) ; kernel_size = nb de mots consécutifs considérés — cf. page Modélisation ▸ [CNN pour du texte — Conv1D](#dl-nlp-conv1d)
