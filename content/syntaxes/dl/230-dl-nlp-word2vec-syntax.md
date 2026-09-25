---
title: Word2Vec — embedding indépendant de la tâche (Gensim)
subgroup: LLM
subsubgroup: NLP
type: syntax
---

## Entraîner un Word2Vec sur son propre corpus
Syntaxe:
```
from gensim.models import Word2Vec
word2vec = **Word2Vec**(sentences=X_train, vector_size=100, window=5, min_count=5)
```
Résultat: vector_size = dimension de l'embedding ; window = nb de mots voisins utilisés pour la prédiction ; min_count = ignore les mots vus moins de N fois

## Récupérer le vecteur d'un mot
Syntaxe: word2vec.wv['movie']
Résultat: vecteur dense de taille vector_size

## Trouver les mots les plus proches
Syntaxe: word2vec.wv.**most_similar**('movie', topn=10)
Résultat: proximité = similarité cosinus dans l'espace d'embedding — cf. page Modélisation ▸ Représenter les mots

## Charger un Word2Vec pré-entraîné (Transfer Learning)
Syntaxe:
```
import gensim.downloader
model_wiki = gensim.downloader.**load**('glove-wiki-gigaword-50')
```
Résultat: à préférer sur un petit corpus — cf. page Modélisation ▸ Embedding indépendant de la tâche

## Voir le vocabulaire appris
Syntaxe: vocab_size = len(word2vec.wv.**key_to_index**)
Résultat: taille réellement retenue après filtrage par min_count — souvent bien plus petite que le nombre de mots distincts du corpus

## Embedder une phrase mot par mot (sans layers.Embedding)
Syntaxe:
```
def embed_sentence(word2vec, sentence):
    return np.array([word2vec.wv[w] for w in sentence if w in word2vec.wv])

X_train_embedded = [embed_sentence(word2vec, s) for s in X_train]
X_train_pad = pad_sequences(X_train_embedded, dtype='float32', padding='post')
```
Résultat: transforme chaque phrase en matrice (n_mots, vector_size) AVANT de la passer au RNN — alternative à layers.Embedding : le vecteur de chaque mot est déjà figé par Word2Vec, pas appris pendant model.fit() ; ignorer les mots absents du vocabulaire (min_count, ou mot inconnu du train)
