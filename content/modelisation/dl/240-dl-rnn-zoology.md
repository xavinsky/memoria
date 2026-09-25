---
title: SimpleRNN, LSTM, GRU — vanishing gradient dans le temps
subgroup: Modèles de base
subsubgroup: RNN
---

[[P:SimpleRNN]] · [[P:LSTM]] · [[P:GRU]]

Un RNN simple souffre du vanishing gradient (cf. Forward & Backward Propagation, ci-dessus) À TRAVERS LE TEMPS : en rétropropageant depuis le dernier pas de temps, le gradient s'atténue à mesure qu'il remonte vers les premiers pas de temps → mémoire courte, difficulté à apprendre des dépendances lointaines dans la séquence.

:::compare
- **SimpleRNN** : le plus simple et le plus rapide à entraîner, mais mémoire courte (vanishing gradient marqué)
- **LSTM (Long Short-Term Memory)** : introduit pour corriger le vanishing gradient — plus de paramètres, mémoire plus longue
- **GRU (Gated Recurrent Unit)** : variante plus légère du LSTM (moins de paramètres) — entraînement plus rapide, potentiellement moins de données nécessaires
:::

> [!TIP]
> 👉 `activation='tanh'` est le choix par défaut (quasi systématique) pour une couche récurrente — sa dérivée seconde reste non nulle sur une plage plus large que sigmoid/ReLU, ce qui limite le vanishing gradient.
