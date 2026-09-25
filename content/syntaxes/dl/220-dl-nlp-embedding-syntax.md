---
title: Couche d'embedding — layers.Embedding
subgroup: LLM
subsubgroup: NLP
type: syntax
---

## Ajouter une couche d'embedding apprise
Syntaxe:
```
model.add(layers.**Embedding**(
    input_dim=vocab_size+1,
    output_dim=embedding_dim,
    mask_zero=True,
))
```
Résultat: input_dim = taille du vocabulaire +1 (pour le 0 du padding) ; output_dim = dimension de l'espace d'embedding (30 à 300 typiquement) ; mask_zero=True = Masking intégré (ignore le padding automatiquement)
