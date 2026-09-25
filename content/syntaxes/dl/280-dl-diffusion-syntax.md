---
title: Génération d'image — diffusers (Stable Diffusion)
subgroup: Génération
type: syntax
---

## Charger un pipeline de diffusion pré-entraîné
Syntaxe:
```
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.**from_pretrained**(model_id, torch_dtype=torch.float32)
pipe = pipe.to("cpu")
```
Résultat: même logique qu'un pipeline Hugging Face (cf. page Syntaxes ▸ Hugging Face) mais pour l'image ; torch_dtype=torch.float16 sur GPU pour accélérer, float32 sur CPU

## Générer une image à partir d'un prompt
Syntaxe:
```
image = pipe(prompt, **num_inference_steps**=25, **guidance_scale**=7.5).images[0]
image.save("out.png")
```
Résultat: cf. page Modélisation ▸ Modèles de diffusion pour le rôle de ces deux hyperparamètres

## Accéder à un modèle à accès restreint (gated)
Syntaxe:
```
from huggingface_hub import login
login()
```
Résultat: nécessite d'avoir accepté la licence du modèle sur sa page Hugging Face au préalable — sinon from_pretrained() lève une GatedRepoError (401), avant même de télécharger le moindre poids
