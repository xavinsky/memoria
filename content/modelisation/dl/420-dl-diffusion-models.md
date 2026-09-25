---
title: Modèles de diffusion — génération d'images (Stable Diffusion)
subgroup: Génération
---

Un **modèle de diffusion** génère une image en partant de BRUIT PUR et en le débruitant progressivement, guidé par un prompt texte — principe derrière Stable Diffusion, DALL-E, Midjourney...

1. **Forward diffusion** (entraînement uniquement) : ajouter progressivement du bruit gaussien à une image réelle, jusqu'à obtenir du bruit pur
2. Un réseau (UNet) apprend à PRÉDIRE ce bruit à chaque étape, conditionné par l'**embedding du prompt texte** (cf. Embedding, groupe NLP)
3. **Reverse diffusion** (génération) : partir de bruit aléatoire, puis retirer itérativement le bruit prédit par le réseau à chaque pas, jusqu'à obtenir une image nette

> [!TIP]
> 👉 Deux hyperparamètres clés : `num_inference_steps` = nombre d'étapes de débruitage (plus haut = image plus nette, mais plus lent) ; `guidance_scale` = fidélité au prompt (plus haut = suit le texte plus strictement, au prix d'images moins naturelles/variées).
