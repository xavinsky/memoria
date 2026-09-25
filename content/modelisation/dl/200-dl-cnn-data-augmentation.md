---
title: Data Augmentation
subgroup: Modèles de base
subsubgroup: CNN
---

[[P:RandomFlip]] · [[P:RandomRotation]] · [[P:RandomZoom]]

La **Data Augmentation** génère des variantes des images d'entraînement (rotation, décalage, zoom, miroir...) pour donner plus de diversité au modèle SANS dupliquer physiquement le dataset — les variantes sont générées à la volée, batch par batch, jamais stockées en RAM.

> [!WARNING]
> ⚠️ Avec de la Data Augmentation, `validation_split` (cf. [Early Stopping & jeu de validation](#dl-early-stopping), ci-dessus) n'est plus utilisable — une image et sa version augmentée pourraient se retrouver l'une en train, l'autre en validation (fuite de données). Il faut définir `validation_data=` manuellement, à partir d'un split fait AVANT d'augmenter quoi que ce soit.

> [!TIP]
> 👉 La Data Augmentation n'améliore pas automatiquement les performances — son effet dépend fortement de l'architecture, du learning rate et du type d'augmentation choisi ; elle peut même dégrader le résultat sur certains problèmes. À tester, pas à supposer utile par défaut.
