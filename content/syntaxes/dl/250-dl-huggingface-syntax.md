---
title: Hugging Face — pipeline pré-entraîné
subgroup: LLM
subsubgroup: Transformers
type: syntax
---

## Charger un pipeline pré-entraîné
Syntaxe:
```
from transformers import pipeline
pipe = **pipeline**("translation", model="Helsinki-NLP/opus-mt-en-fr")
```
Résultat: combine automatiquement le tokenizer ET le modèle adaptés à la tâche et au modèle choisis

## Exécuter le pipeline
Syntaxe:
```
result = pipe("I am a student")
result[0]['translation_text']
```
Résultat: sortie déjà post-traitée (texte lisible, pas des tokens/probabilités brutes)

## Sans préciser de modèle (défaut HuggingFace)
Syntaxe:
```
pipe = pipeline("sentiment-analysis")
pipe("Transformers are awesome!")
```
Résultat: pratique pour prototyper vite ; le modèle par défaut généralise parfois mal (vocabulaire différent du corpus d'entraînement) — préciser model= pour un domaine spécifique

## Autres tâches courantes (même interface)
Syntaxe:
```
pipeline("summarization", model="sshleifer/distilbart-xsum-12-6")
pipeline("question-answering", model="deepset/roberta-base-squad2")(question=q, context=texte)
pipeline("automatic-speech-recognition", model="openai/whisper-tiny")("audio.wav")
```
Résultat: même abstraction pipeline(tâche, model=...) pour résumé, question-réponse, reconnaissance vocale... — seuls le nom de la tâche et les arguments d'appel changent
