---
title: Text Preprocessing
subgroup: Modèles
subsubgroup: NLP
---

Un modèle ML ne peut pas traiter du texte brut — comme pour toute donnée, un preprocessing est nécessaire, mais les étapes diffèrent du preprocessing numérique.

1. Cleaning de base : minuscules, retirer chiffres/ponctuation/symboles (opérateurs Python natifs : `.strip()`, `.lower()`, `.replace()`, RegEx)
2. Tokenizing : découper le texte en mots individuels (tokens)
3. Retirer les stopwords : mots très fréquents porteurs de peu d'information ("the", "is"...)
4. Lemmatizing : ramener chaque mot à sa racine ("running" → "run") pour regrouper les mots par SENS plutôt que par forme exacte

> [!WARNING]
> ⚠️ **Retirer les stopwords est dangereux pour l'analyse de sentiment et l'attribution d'auteur** — "not" est considéré comme un stopword, or il inverse totalement le sens d'une phrase ("not going to the party"). Utile en revanche pour le topic modeling.

> [!TIP]
> 👉 La lemmatisation dépend de la nature grammaticale du mot (`pos='v'` pour un verbe, `pos='n'` pour un nom) — un mot peut se lemmatiser différemment selon qu'on le traite comme verbe ou nom.
