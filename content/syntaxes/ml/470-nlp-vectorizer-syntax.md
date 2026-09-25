---
title: CountVectorizer & TfidfVectorizer
subgroup: NLP
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Bag-of-Words
Syntaxe:
```
from sklearn.feature_extraction.text import CountVectorizer
X = **CountVectorizer**().fit_transform(texts)
```
Params: -
Explication: matrice sparse de comptages de mots — cf. page Modélisation ▸ Vectorizing

## Tf-idf
Syntaxe:
```
from sklearn.feature_extraction.text import TfidfVectorizer
X = **TfidfVectorizer**().fit_transform(texts)
```
Params: -
Explication: pondère par l'importance du mot dans le corpus (cf. page Modélisation)

## Récupérer le vocabulaire appris
Syntaxe: vectorizer.**get_feature_names_out**()
Params: -
Explication: array des mots correspondant à chaque colonne de X

## Filtrer les mots trop rares / trop fréquents
Syntaxe: CountVectorizer(**max_df**=0.8, **min_df**=2)
Params: max_df/min_df : float [0,1] (proportion) ou int (compte absolu)
Explication: construit des "stopwords" spécifiques au corpus

## Limiter le vocabulaire aux k mots les plus fréquents
Syntaxe: CountVectorizer(**max_features**=1000)
Params: max_features : int
Explication: lutte contre la curse of dimensionality (cf. Feature Selection, groupe ml)

## Capturer le contexte (bi/tri-grammes)
Syntaxe: CountVectorizer(**ngram_range**=(1,2))
Params: ngram_range=(min_n,max_n)
Explication: (1,1)=unigrams seuls (défaut) ; (1,2)=unigrams+bigrams ; (2,3)=bigrams+trigrams sans unigrams
