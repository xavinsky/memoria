---
title: Scraper une page HTML & choisir un format
subgroup: Import / export données
type: syntax
---

## Parser le HTML d'une page
Syntaxe:
```
from bs4 import BeautifulSoup
soup = **BeautifulSoup**(response.text, "html.parser")
```
Résultat: objet navigable dans l'arbre HTML

## Extraire des balises
Syntaxe: soup.**find_all**("a", class_="result-link")
Résultat: liste de balises correspondant au sélecteur (tag + attributs)

## Format de sauvegarde pour un gros dataset
Syntaxe: df.**to_parquet**("fichier.parquet")  # vs. df.to_csv(...)
Résultat: Parquet : binaire, compressé, types préservés (int/float/date), bien plus rapide à lire/écrire qu'un CSV — à préférer dès que le dataset devient volumineux ou est réutilisé souvent
