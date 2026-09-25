---
title: Séquences de longueurs différentes — padding & masking
subgroup: Modèles de base
subsubgroup: RNN
---

[[P:Masking]]

Un tensor Keras impose que toutes les séquences d'un même batch aient la MÊME longueur — or des séquences réelles ont souvent des longueurs différentes (ex: historiques de villes commençant à des dates différentes).

1. **Padding** : compléter les séquences courtes avec une valeur factice, absente des données réelles (ex: -1000), jusqu'à la longueur de la plus longue séquence — de préférence à LA FIN (`padding='post'`), pour ne pas perturber l'état interne dès les premiers pas de temps
2. **Masking** : ajouter une couche `Masking(mask_value=...)` en tout début de modèle, pour que la couche RNN ignore ces pas de temps factices pendant le forward/backward pass

> [!WARNING]
> ⚠️ Ne JAMAIS padder avec une valeur qui existe réellement dans les données (ex: 0 si le dataset contient de vrais zéros) — le modèle ne pourrait plus distinguer un vrai 0 d'un pas de temps factice à ignorer.
