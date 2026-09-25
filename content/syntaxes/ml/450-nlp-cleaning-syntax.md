---
title: Cleaning — Python core + RegEx
subgroup: NLP
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Retirer les espaces en début/fin
Syntaxe: text.**strip**()
Params: -
Explication: -

## Remplacer un mot
Syntaxe: text.**replace**("koala", "panda")
Params: -
Explication: -

## Découper une chaîne
Syntaxe: text.**split**("/")
Params: -
Explication: liste de sous-chaînes

## Mettre en minuscules
Syntaxe: text.**lower**()
Params: -
Explication: obligatoire avant tokenizing/vectorizing — sinon "Football" ≠ "football"

## Retirer les chiffres
Syntaxe: ''.join(c for c in text if not c.**isdigit**())
Params: -
Explication: -

## Retirer ponctuation et symboles
Syntaxe:
```
import string
for p in string.punctuation:
    text = text.**replace**(p, '')
```
Params: -
Explication: string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

## Retirer les accents
Syntaxe:
```
from unidecode import unidecode
text = **unidecode**(text)  # pip install unidecode
```
Params: -
Explication: indispensable AVANT un regex `[^a-z]` sur du texte accentué (ex: français/portugais) — sinon 'ã'/'é' sont juste supprimés ("não" → "n o") au lieu de devenir 'a'/'e', ce qui casse la détection de mots

## Extraire un pattern (ex: e-mails) par RegEx
Syntaxe:
```
import re
**re.findall**(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
```
Params: -
Explication: liste des correspondances trouvées
