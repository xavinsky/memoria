---
title: Prompt Engineering — patterns concrets
subgroup: Fondamentaux
type: syntax
---

## Format Instruction/Sortie (réponse structurée)
Syntaxe: f"Instruct: {question}\n**Output**:"
Résultat: pousse le modèle à répondre directement plutôt qu'à continuer/paraphraser la question — surtout utile sur un petit modèle (SLM) pas fine-tuné par RLHF

## Forcer un raisonnement étape par étape
Syntaxe: question + " **Solve step by step.**"
Résultat: sur un petit modèle, ce raisonnement n'est pas toujours implicite (contrairement à un gros LLM) — à demander explicitement

## Forcer une réponse concise (1 mot/1 label)
Syntaxe: f"Classify the sentiment as Positive/Negative:\n{text}\n\n**Sentiment:**"
Résultat: terminer le prompt par le début du format de réponse attendu (ici juste avant le label) pousse le modèle à continuer directement par ce mot, au lieu de répéter toute la consigne

## Guider une génération de code
Syntaxe: code_start + '\n    """**Docstring décrivant précisément le comportement attendu**"""'
Résultat: une docstring précise (API à utiliser, comportement des paramètres) donne beaucoup plus de matière au modèle qu'une simple signature de fonction
