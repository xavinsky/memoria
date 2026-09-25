---
title: Autoencoder — encoder, décodeur, espace latent
subgroup: LLM
subsubgroup: Autoencoder
---

Un **Autoencoder** est un réseau à deux parties : un **encodeur** qui compresse l'input dans un espace de faible dimension (l'**espace latent**, ou bottleneck), et un **décodeur** qui tente de RECONSTRUIRE l'input original à partir de cette représentation compressée.

```math
X \xrightarrow{\text{Encoder}} z\ (\text{latent},\ \dim(z) \ll \dim(X)) \xrightarrow{\text{Decoder}} \hat X
```

Entraînement NON supervisé dans sa forme : pas de label externe — la target EST l'input lui-même ($y = X$). La loss compare $X$ à sa reconstruction $\hat X$ (MSE, comparaison pixel par pixel pour des images).

> [!TIP]
> 👉 Contrairement à une PCA (cf. groupe ml), qui trouve la meilleure combinaison LINÉAIRE des features, un Autoencoder peut apprendre une compression NON-LINÉAIRE — plus flexible, mais sans les garanties mathématiques de la PCA (composantes non orthogonales, pas de % de variance expliquée directement lisible).
