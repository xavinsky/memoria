---
title: Format d'inférence & moteurs — ONNX, TensorRT, vLLM
subgroup: Déploiement & Optimisation Hardware
---

Un modèle brut sorti d'un script PyTorch de Data Scientist est souvent une horreur en termes de performance pure pour de la prod à grande échelle — trop lent, trop gourmand en mémoire.

:::compare
- **ONNX (Open Neural Network Exchange)** : format de sérialisation neutre pour exporter un modèle et l'exécuter de manière optimisée (CPU ou GPU), hors de l'écosystème Python pur
- **TensorRT** : optimiseur/moteur d'inférence bas niveau spécifique aux GPU NVIDIA — fusionne les couches, quantize automatiquement pour un débit maximal sur ce matériel
:::

> [!WARNING]
> ⚠️ Faire tourner un LLM en prod avec du code PyTorch classique est intenable en mémoire. Les **moteurs d'inférence LLM** (**vLLM**, **TGI** — Text Generation Inference) gèrent l'optimisation de la mémoire VRAM (via le **PagedAttention**) pour multiplier le débit par 2 à 4.

> [!TIP]
> 👉 Combinable avec la Quantization/Distillation ci-dessus : un modèle déjà quantizé exporté en ONNX/TensorRT cumule les deux gains.
