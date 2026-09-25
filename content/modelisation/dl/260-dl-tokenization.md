---
title: Tokenization — du texte aux entiers
subgroup: LLM
subsubgroup: NLP
---

[[P:TextVectorization]] · [[P:AutoTokenizer]]

Avant même de choisir COMMENT représenter un mot (cf. Embedding, ci-dessous), il faut d'abord le transformer en NOMBRE — un réseau ne lit que ça. La **Tokenization** construit un **vocabulaire** (mot → entier unique) à partir d'un corpus, puis convertit chaque phrase en séquence d'entiers.

1. **Construire le vocabulaire** : parcourir le corpus, attribuer un entier à chaque mot rencontré (souvent trié par fréquence décroissante) — un token spécial (ex: `<OOV>`) reçoit tout mot ABSENT du vocabulaire au moment de l'usage
2. **Convertir** chaque phrase en séquence de ces entiers
3. **Uniformiser la longueur** (padding) : les phrases n'ont pas toutes le même nombre de mots, or un batch doit être un tableau rectangulaire — compléter les séquences courtes avec un token `<PAD>` (cf. Séquences de longueurs différentes, groupe RNN)

:::compare
- **Vocabulaire construit sur SON PROPRE corpus** : Tokenizer / TextVectorization (Keras) — le vocabulaire dépend entièrement des données d'entraînement fournies
- **Vocabulaire figé du modèle pré-entraîné** : AutoTokenizer (Hugging Face) — DOIT correspondre exactement au modèle choisi (même vocabulaire, même découpage) ; en changer casse le modèle, les entiers ne veulent plus rien dire pour lui
:::

> [!TIP]
> 👉 Étape purement mécanique — elle ne dit rien du SENS des mots (deux entiers voisins ne sont pas forcément des mots proches en signification), c'est le rôle de l'Embedding qui suit (cf. ci-dessous).
