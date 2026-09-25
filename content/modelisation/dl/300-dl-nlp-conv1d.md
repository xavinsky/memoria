---
title: CNN pour du texte — Conv1D
subgroup: LLM
subsubgroup: NLP
---

[[P:Conv1D]]

Une phrase embeddée est une matrice (mots × dimensions d'embedding) — on pourrait être tenté d'y appliquer un CNN comme sur une image (cf. groupe CNN), mais une convolution 2D classique n'a pas de sens ici.

> [!WARNING]
> ⚠️ Les dimensions de l'embedding n'ont AUCUN ordre spatial signifiant (contrairement aux pixels d'une image) — une convolution ne doit donc JAMAIS glisser le long de cet axe, seulement le long de l'axe des mots.

**Conv1D** (`layers.Conv1D`) ne fait glisser le kernel que le long de l'axe des mots — le `kernel_size` correspond alors au nombre de mots consécutifs considérés à la fois par le filtre (analogue à une fenêtre Word2Vec, ci-dessus).

> [!TIP]
> 👉 Conv1D peut remplacer un RNN (SimpleRNN/LSTM/GRU) après une couche d'Embedding OU Word2Vec — souvent plus rapide à entraîner (nettement plus rapide par epoch), pour un nombre de paramètres quasi identique (la couche d'Embedding domine largement dans les deux cas).

> [!WARNING]
> ⚠️ Conv1D ne supporte PAS le masking : le masque produit par `Embedding(mask_zero=True)` (cf. groupe RNN) est détruit dès qu'il traverse une couche Conv1D — le padding redevient une entrée comme une autre à partir de cette couche (Keras émet un warning, pas une erreur bloquante).
