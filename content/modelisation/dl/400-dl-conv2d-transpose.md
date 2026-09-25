---
title: Conv2DTranspose — l'inverse d'une convolution
subgroup: LLM
subsubgroup: Autoencoder
---

[[P:Conv2DTranspose]]

Un décodeur d'images doit faire l'inverse d'un CNN classique : partir d'un vecteur compressé et AGRANDIR progressivement l'image jusqu'à retrouver sa taille d'origine, plutôt que la réduire (Conv2D + MaxPooling, cf. groupe CNN).

**Conv2DTranspose** fait cela : avec `strides > 1`, elle DOUBLE (ou plus) la taille spatiale à chaque couche, au lieu de la réduire.

> [!TIP]
> 👉 Architecture typique d'un décodeur : une couche Dense "déplie" le vecteur latent vers une petite grille (ex: 7×7×8), un `Reshape` lui redonne une forme d'image, puis plusieurs `Conv2DTranspose` (strides=2) doublent la taille à chaque couche jusqu'à retrouver les dimensions de l'image d'origine (7→14→28).
