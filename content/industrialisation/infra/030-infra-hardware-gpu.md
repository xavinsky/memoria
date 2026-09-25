---
title: Configuration Hardware — GPU NVIDIA vs AMD
subgroup: Local
---

Entraîner ou faire tourner un modèle DL/LLM en local dépend fortement du GPU disponible — la **VRAM** (mémoire vidéo) est souvent le facteur limitant AVANT la puissance de calcul pure : charger un modèle + ses activations doit tenir en VRAM.

:::compare
- **NVIDIA (CUDA)** : écosystème dominant en Deep Learning — quasi tous les frameworks (PyTorch, TensorFlow) et outils d'optimisation (TensorRT, vLLM) sont d'abord conçus pour CUDA ; le choix par défaut le plus sûr
- **AMD (ROCm)** : alternative open-source à CUDA — support croissant mais encore partiel selon les frameworks, à vérifier au cas par cas avant de s'y engager
:::

> [!WARNING]
> ⚠️ Pour un LLM en local, la taille du modèle (nombre de paramètres × précision, cf. [Quantization](#dl-model-compression), page MLOps) doit tenir en VRAM — ex: un modèle 7B en 16-bit demande environ 14 Go, réductible via la quantization (8-bit ≈ 7 Go, 4-bit ≈ 3.5 Go).
