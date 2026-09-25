---
title: 'Appeler une API LLM (ex: Gemini)'
subgroup: Fondamentaux
type: syntax
---

## Instancier un client API
Syntaxe:
```
from google import genai
client = genai.**Client**()
```
Résultat: nécessite une clé API (variable d'environnement, ex: GOOGLE_API_KEY)

## Générer du texte
Syntaxe:
```
response = client.models.**generate_content**(
    model="gemini-2.5-flash-lite",
    contents=prompt,
)
response.text
```
Résultat: équivalent d'un .predict() — le modèle est choisi par son nom (string)

## Configurer la génération
Syntaxe:
```
config=genai.types.GenerateContentConfig(
    system_instruction=system_prompt,
    max_output_tokens=200,
    **temperature**=1.2,
)
```
Résultat: system_instruction = rôle/consignes globales ; temperature/max_output_tokens — cf. page Modélisation ▸ Contrôler la génération (groupe Transformers)
