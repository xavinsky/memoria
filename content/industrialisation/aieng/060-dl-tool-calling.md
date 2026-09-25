---
title: Tool Calling (Function Calling)
subgroup: Agents
---

Le **Tool Calling** permet à un LLM de traduire une requête en langage naturel en appel à UNE FONCTION précise, avec les bons arguments — ex: "les matchs joués en Italie dans les années 80-90" → `get_matches(country="Italy", start_year=1980, end_year=1999)`.

1. Décrire la fonction au LLM (nom, description, paramètres attendus — schéma JSON)
2. Envoyer cette description + la requête utilisateur au LLM
3. Le LLM renvoie le nom de la fonction à appeler ET les arguments extraits du langage naturel

> [!WARNING]
> ⚠️ Le LLM n'EXÉCUTE PAS la fonction lui-même — il se contente d'identifier QUELLE fonction appeler et avec QUELS arguments. C'est votre code qui appelle réellement la fonction avec ces arguments.

> [!TIP]
> 👉 Écrire le schéma JSON à la main (ci-dessus) ou le laisser être déduit automatiquement des type hints + docstring d'une fonction Python (ex: décorateur `@tool` de LangChain) revient au même pour le LLM — la seconde option évite juste de dupliquer l'information. Plus le schéma est précis (docstring détaillé, valeurs énumérées pour un paramètre catégoriel), plus les arguments extraits sont fiables. Pour exposer cet outil de façon RÉUTILISABLE par n'importe quel agent plutôt que de le recoder à chaque intégration, cf. [MCP](#dl-mcp) ci-dessous.
