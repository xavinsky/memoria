---
title: LangGraph — construire un agent (create_agent)
subgroup: Agents
type: syntax
---

## Créer un agent (LLM + tools)
Syntaxe:
```
from langchain.agents import create_agent
agent_executor = **create_agent**(model, tools)
```
Résultat: tools = liste d'objets Tool (cf. Tool Calling ci-dessus) — combine le cerveau (model) et la boîte à outils ; contrairement au tool calling seul, l'agent EXÉCUTE lui-même les tools nécessaires

## Appeler l'agent
Syntaxe:
```
from langchain_core.messages import HumanMessage
response = agent_executor.**invoke**({"messages": [HumanMessage(content=query)]})
response["messages"][-1].content
```
Résultat: l'état de l'agent est une liste de messages ; le dernier contient la réponse finale, après tous les appels de tools intermédiaires

## Suivre les étapes intermédiaires en streaming
Syntaxe:
```
for step in agent_executor.**stream**(
    {"messages": [HumanMessage(content=query)]}, stream_mode="values",
):
    step["messages"][-1].pretty_print()
```
Résultat: affiche chaque étape (appel de tool, résultat, réponse) au fur et à mesure plutôt que d'attendre la fin — utile pour vérifier que le LLM n'hallucine pas

## Gérer les erreurs d'un tool sans planter l'agent
Syntaxe:
```
from langchain.agents.middleware import wrap_tool_call

@**wrap_tool_call**
def handle_tool_errors(request, handler):
    try:
        return handler(request)
    except Exception as e:
        return ToolMessage(content=f"Tool error: {e}", tool_call_id=request.tool_call["id"])

agent_executor = create_agent(model, tools, middleware=[handle_tool_errors])
```
Résultat: middleware = intercepte les appels de tool ; sans ça, une erreur d'un tool (ex: accès API refusé) fait planter tout l'agent au lieu de laisser le LLM s'adapter

## Donner une mémoire à l'agent (conversation multi-tours)
Syntaxe:
```
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
agent_executor = create_agent(model, tools, **checkpointer**=memory)
```
Résultat: sans checkpointer, chaque .invoke() repart de zéro — avec, l'historique de conversation est conservé automatiquement, identifié par un thread_id (ligne suivante)

## Poursuivre une conversation existante
Syntaxe:
```
config = {"configurable": {"**thread_id**": "abc123"}}
agent_executor.invoke({"messages": [...]}, config=config)
```
Résultat: même thread_id = même fil de conversation (mémoire partagée) ; changer de thread_id démarre une conversation vierge

## Orienter le comportement de l'agent
Syntaxe:
```
agent_executor = create_agent(
    model, tools, **system_prompt**="...instructions de comportement...",
)
```
Résultat: ex: "si l'accès au prix courant échoue, utilise le dernier prix de clôture disponible" — LangGraph n'ajoute AUCUN system prompt par défaut
