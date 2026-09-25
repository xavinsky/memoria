---
title: Pourquoi un RNN — la dimension temporelle
subgroup: Modèles de base
subsubgroup: RNN
---

Un **RNN (Recurrent Neural Network)** traite des données avec une dimension TEMPORELLE — des séquences d'observations répétées dans le temps — là où un CNN traite une dimension spatiale (image) et un Dense un simple vecteur de features.

```math
X.shape = (n_{séquences},\ n_{observations},\ n_{features})
```

Ex: prévoir la pollution du lendemain dans 16 villes, à partir de 100 jours d'historique (température, vent, pollution) → `X.shape = (16, 100, 3)`. Chaque séquence (ville) peut être uni- ou multivariée.

> [!TIP]
> 👉 Contrairement à un Dense ou un CNN, le nombre d'observations temporelles (la longueur des séquences) n'a AUCUN impact sur le nombre de paramètres entraînables d'une couche RNN — cf. [Sous le capot d'une couche RNN](#dl-rnn-mechanics), ci-dessous.

À partir d'UNE SEULE série temporelle brute (ex: 365 jours de température), on obtient ce format via le **fenêtrage** (windowing) : chaque fenêtre glissante de N observations consécutives devient une séquence d'entrée, et l'observation suivante devient sa cible — cf. page Syntaxes.

> [!WARNING]
> ⚠️ Le split train/test doit rester CHRONOLOGIQUE (jamais mélangé) pour une série temporelle — sinon des fenêtres du futur aideraient à prédire le passé, une fuite de données (cf. [Data Leakage](#ml-data-leakage-concept), groupe ml).
