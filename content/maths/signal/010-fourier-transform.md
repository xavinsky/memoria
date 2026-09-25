---
title: Transformée de Fourier (FFT) — du temporel au fréquentiel
---

Un son (ou tout signal) est stocké comme une suite de nombres dans le **domaine temporel** — l'amplitude à chaque instant, échantillonnée à un taux R (Hz). Tracé brut, un signal complexe donne un nuage illisible : peu d'information exploitable telle quelle.

```math
y(t) = A \cdot \sin(2\pi f t)
```

Une onde sinusoïdale pure de fréquence **f** (Hz) et d'amplitude A — la brique de base : n'importe quel signal peut être vu comme une somme de sinusoïdes de fréquences/amplitudes différentes (superposer plusieurs `note(f)` = un accord).

La **Fast Fourier Transform (FFT)** convertit un signal du **domaine temporel** (amplitude vs. temps) vers le **domaine fréquentiel** (amplitude vs. fréquence) — elle décompose le signal en ses fréquences constitutives et leurs poids respectifs. Un signal complexe (accord, instrument, son animal...) devient un spectre avec un ou plusieurs pics nets aux fréquences dominantes, bien plus interprétable que la forme d'onde brute.

> [!TIP]
> 👉 **Feature engineering courant avant ML/DL sur de l'audio** : passer du signal brut à son spectre FFT (ou à un spectrogramme, FFT glissante dans le temps) fait ressortir des motifs reconnaissables par un modèle — un peu comme PCA réduit des features corrélées à des axes plus informatifs (cf. PCA, page Modélisation).
