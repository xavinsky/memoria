---
title: Hugging Face — charger tokenizer/modèle séparément & fine-tuner
subgroup: LLM
subsubgroup: Transformers
type: syntax
---

## Charger le tokenizer d'un modèle précis
Syntaxe:
```
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.**from_pretrained**("prajjwal1/bert-tiny")
```
Résultat: le tokenizer DOIT correspondre exactement au modèle choisi (même vocabulaire) — sinon les tokens ne veulent plus rien dire pour lui

## Tokeniser un batch de textes pour Keras
Syntaxe:
```
tokens = tokenizer(
    df['text'].tolist(),
    max_length=500, truncation=True, padding='max_length',
    return_tensors='**tf**',
)
```
Résultat: renvoie un dict avec input_ids/attention_mask/token_type_ids, chacun un tf.Tensor (return_tensors='tf', sinon simples listes Python)

## Charger le modèle pré-entraîné (poids figés)
Syntaxe:
```
from transformers import TFAutoModel
model = TFAutoModel.**from_pretrained**("prajjwal1/bert-tiny", from_pt=True)
```
Résultat: from_pt=True convertit des poids PyTorch en TensorFlow — nécessaire pour la plupart des modèles du hub, entraînés en PyTorch à l'origine

## Récupérer les embeddings contextuels
Syntaxe:
```
output = model.predict(tokens['input_ids'])
cls_embedding = output.**last_hidden_state**[:, 0, :]
```
Résultat: last_hidden_state a pour shape (n_phrases, n_tokens, hidden_size) ; le token [CLS] (index 0) résume toute la phrase — utilisable comme feature pour un petit classifieur Dense séparé (BERT gelé)

## Fine-tuner le modèle en entier pour une tâche précise
Syntaxe:
```
from transformers import TFAutoModelForSequenceClassification
model = TFAutoModelForSequenceClassification.from_pretrained(
    "prajjwal1/bert-tiny", from_pt=True, **num_labels**=2,
)
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
model.fit(tokens['input_ids'], y, validation_data=(...), epochs=3, batch_size=16)
```
Résultat: ajoute une tête de classification et RÉENTRAÎNE tous les poids (contrairement à l'extraction de features ci-dessus) — from_logits=True indispensable, ce modèle renvoie des logits bruts ; peu d'epochs (3-5), beaucoup de poids à mettre à jour d'un coup
