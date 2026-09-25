---
title: Naive Bayes — classification de texte
subgroup: NLP
type: syntax
---

## Pipeline vectorizer + Naive Bayes
Syntaxe:
```
from sklearn.naive_bayes import MultinomialNB
pipeline = make_pipeline(TfidfVectorizer(), **MultinomialNB**())
```
Résultat: cf. page Modélisation ▸ Naive Bayes pour la formule et l'hypothèse d'indépendance

## Lisser (éviter les probabilités nulles)
Syntaxe: MultinomialNB(**alpha**=0.1)
Résultat: alpha = paramètre de smoothing (cf. page Modélisation)

## Tuner vectorizer + modèle simultanément
Syntaxe:
```
grid = {
    'tfidfvectorizer__ngram_range': ((1,1),(2,2)),
    'multinomialnb__alpha': (0.1,1)
}
**GridSearchCV**(pipeline, grid, scoring='recall', cv=5)
```
Résultat: syntaxe `étape__param`, comme n'importe quel pipeline (cf. Model Tuning, groupe ml)
