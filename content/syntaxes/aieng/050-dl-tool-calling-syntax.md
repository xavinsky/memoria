---
title: Tool Calling — déclarer et appeler une fonction
subgroup: Agents
type: syntax
---

## Décrire la fonction pour le LLM
Syntaxe:
```
tool_declaration = {
    "name": "get_matches",
    "description": "...",
    "parameters": {"type": "object", "properties": {...}, "required": [...]},
}
```
Résultat: schéma JSON standard (nom, description, paramètres attendus) — cf. page Industrialisation ▸ Tool Calling

## Attacher le tool à la requête
Syntaxe:
```
tools = genai.types.**Tool**(function_declarations=[tool_declaration])
response = client.models.generate_content(
    ..., config=genai.types.GenerateContentConfig(tools=[tools])
)
```
Résultat: le LLM choisit d'appeler (ou non) la fonction décrite

## Récupérer les arguments extraits
Syntaxe:
```
args = response.candidates[0].content.parts[0].function_call.args
my_function(**args)
```
Résultat: le LLM ne fait qu'EXTRAIRE les arguments — c'est votre code qui appelle réellement la fonction

## Convertir une fonction Python en tool (LangChain)
Syntaxe:
```
from langchain.tools import tool

@**tool**
def get_recipes_tool(ingredient: str, max_prep_time: int = 0) -> pd.DataFrame:
    """Scrape recipes for a given ingredient."""
    return recipe.get_recipes(ingredient, max_prep_time)
```
Résultat: LangChain déduit le schéma JSON (nom, description, paramètres) directement des type hints + du docstring — évite d'écrire ce schéma à la main comme sur la 1ère ligne

## Inspecter le schéma déduit
Syntaxe:
```
get_recipes_tool.name
get_recipes_tool.description
get_recipes_tool.args
get_recipes_tool.args_schema.**model_json_schema**()
```
Résultat: utile pour vérifier ce que "voit" le LLM avant de l'utiliser

## Lier le(s) tool(s) à un chat model LangChain
Syntaxe: model_with_tools = model.**bind_tools**([get_recipes_tool])
Résultat: le binding est local (pas d'appel réseau) — le LLM ne "connaît" le tool qu'au moment de .invoke()

## Extraire l'appel de tool proposé (LangChain)
Syntaxe:
```
response = model_with_tools.invoke(query)
args = response.**tool_calls**[0]['args']
get_recipes_tool.**invoke**(args)
```
Résultat: tool_calls = liste (plusieurs tools possibles) ; même principe que ci-dessus, le LLM extrait juste les arguments

## Détailler chaque paramètre du schéma
Syntaxe:
```
@tool(**parse_docstring**=True)
def ma_fonction(x: int) -> ...:
    """Résumé court.

    Args:
        x: description du paramètre x.
    """
```
Résultat: répartit le docstring entre description générale et description par paramètre (extraite de la section Args:), au lieu d'un seul bloc de texte

## Énumérer les valeurs acceptées par un paramètre
Syntaxe:
```
from typing import Literal
difficulty_levels: list[**Literal**["Easy", "Moderate", "Hard"]] = []
```
Résultat: ajoute un enum au schéma JSON du paramètre — le LLM est bien plus fiable pour renvoyer exactement les valeurs attendues (plutôt que deviner une valeur proche mais fausse)
