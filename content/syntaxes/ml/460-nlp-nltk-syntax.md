---
title: NLTK — tokenizing, stopwords, lemmatizing
subgroup: NLP
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Tokenizer un texte
Syntaxe:
```
from nltk.tokenize import word_tokenize
**word_tokenize**(text)
```
Params: -
Explication: liste de tokens (mots)

## Charger les stopwords
Syntaxe:
```
from nltk.corpus import stopwords
stop_words = set(**stopwords.words**('english'))
```
Params: -
Explication: set de mots à filtrer — attention en sentiment analysis (cf. page Modélisation)

## Retirer les stopwords d'une liste de tokens
Syntaxe: [w for w in tokens if not w in stop_words]
Params: -
Explication: -

## Lemmatiser (verbes / noms)
Syntaxe:
```
from nltk.stem import WordNetLemmatizer
**WordNetLemmatizer**().lemmatize(word, pos='v')  # verbes
WordNetLemmatizer().lemmatize(word, pos='n')  # noms
```
Params: -
Explication: pos= précise la nature grammaticale (cf. page Modélisation) — 'n' (nom) par défaut si omis

## Détecter automatiquement le pos= de chaque mot
Syntaxe:
```
from nltk import pos_tag
from nltk.corpus import wordnet
tag = pos_tag([word])[0][1][0].upper()  # ex: 'V'
pos_map = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
lemmatizer.lemmatize(word, pos=pos_map.get(tag, wordnet.NOUN))
```
Params: -
Explication: évite de lemmatiser tout un texte avec un seul pos= fixe — chaque mot garde sa vraie nature grammaticale (pos_tag renvoie un tag détaillé type 'VBG', on ne garde que sa 1ère lettre)
