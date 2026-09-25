---
title: Embedding indépendant de la tâche — Word2Vec
subgroup: LLM
subsubgroup: NLP
---

[[P:Word2Vec]]

Option 2 : apprendre (ou charger) un embedding INDÉPENDANT de la tâche, entraîné une fois pour toutes sur un grand corpus, puis le réutiliser tel quel (Transfer Learning, cf. groupe CNN).

**Word2Vec** entraîne ce type d'embedding en prédisant un mot à partir de ses voisins immédiats dans la phrase (la **fenêtre**, ou window) — la couche cachée de ce réseau auxiliaire, une fois entraînée, EST l'embedding : chaque mot y est représenté par son vecteur de poids appris.

:::compare
- **layers.Embedding — spécifique à la tâche** : représentation optimale pour LE problème posé, mais plus de paramètres à apprendre → entraînement plus lent
- **Word2Vec — indépendant de la tâche** : entraînement très rapide, moins de paramètres pour le RNN en aval — mais représentation potentiellement sous-optimale pour la tâche précise
:::

> [!TIP]
> 👉 En pratique : préférer Word2Vec sur un petit corpus (avec ses poids pré-entraînés, en Transfer Learning) — `layers.Embedding` a besoin de beaucoup de données pour apprendre une bonne représentation from scratch.
