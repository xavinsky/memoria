---
title: LangChain — interface de chat agnostique du fournisseur
subgroup: Fondamentaux
type: syntax
---

## Instancier un modèle sans coder en dur son fournisseur
Syntaxe:
```
from langchain.chat_models import init_chat_model
model = **init_chat_model**("gemini-2.5-flash-lite", model_provider="google_genai")
```
Résultat: au lieu d'une classe spécifique (ex: ChatGoogleGenerativeAI) — changer de fournisseur (OpenAI, Anthropic...) ne demande alors que de changer ces deux arguments, pas de réécrire le code

## Appeler le modèle
Syntaxe:
```
response = model.**invoke**("What is the capital of France?")
response.text
```
Résultat: interface commune quel que soit le fournisseur choisi à l'instanciation

## Ajuster les hyperparamètres après coup
Syntaxe:
```
model.temperature = 1.0
model.max_output_tokens = 200
```
Résultat: exposés comme de simples attributs de l'objet modèle — alternative à les passer à la création

## Conversation à plusieurs messages (système + utilisateur)
Syntaxe:
```
from langchain_core.messages import SystemMessage, HumanMessage
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain attention in one sentence."),
]
response = model.invoke(messages)
```
Résultat: SystemMessage = consigne de comportement donnée une fois ; HumanMessage = message utilisateur ; AIMessage = une réponse du modèle (pour repasser un historique multi-tours)
