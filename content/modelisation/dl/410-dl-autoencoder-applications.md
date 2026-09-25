---
title: Applications — compression, génération, débruitage
subgroup: LLM
subsubgroup: Autoencoder
---

:::compare
- **Compression** : l'espace latent EST une version compressée de l'input (ex: une image de 784 pixels réduite à 2 valeurs) — bien plus compact, au prix d'une perte d'information
- **Génération** : le décodeur SEUL devient un générateur — n'importe quel point de l'espace latent (même jamais vu à l'entraînement) produit une nouvelle image plausible
- **Débruitage (Denoising)** : entraîner avec une entrée BRUITÉE mais une target PROPRE — le modèle apprend à retirer le bruit plutôt qu'à le reproduire
:::

> [!WARNING]
> ⚠️ Choisir la taille de l'espace latent est un compromis (méthode du coude, cf. PCA groupe ml) : trop petite → perte d'info excessive (reconstruction dégradée) ; trop grande (proche de la dimension d'origine) → aucune vraie compression, pas d'intérêt.
