---
title: Workflow Deep Learning
subgroup: Workflow
---

![](../../diagrams/dl-lifecycle-1.html)

Contrairement au workflow Scikit-learn (cf. [Workflow ML](#ml-lifecycle), groupe Machine Learning), pas de distinction "avec/sans Pipeline" — Keras impose déjà une séquence unique **définir → compiler → fit**. Chaque étape ci-dessous renvoie vers sa carte détaillée plutôt que de la ré-expliquer.

1. **Prétraiter** — scaler le numérique (même logique que pour un modèle classique, cf. [Feature Scaling](#ml-scaling-choice)), tokeniser le texte (cf. [Tokenization](#dl-tokenization)), redimensionner/augmenter les images (cf. [Data Augmentation](#dl-cnn-data-augmentation))
2. **Séparer train / validation / test** — le jeu de VALIDATION (distinct du test) est indispensable dès qu'on utilise l'Early Stopping (cf. [Early Stopping & jeu de validation](#dl-early-stopping))
3. **Charger en batches** — `tf.data.Dataset` si le dataset ne tient pas en RAM (cf. [Pourquoi tf.* et pas Numpy/Pandas](#dl-tf-ops-required))
4. **Choisir la famille d'architecture** selon le type de donnée : CNN pour une image (cf. [Pourquoi pas un réseau Dense pour les images](#dl-cnn-why-not-dense)), RNN/LSTM/GRU pour une séquence (cf. [Pourquoi un RNN](#dl-rnn-input-shape)), Transformer pour du texte long/LLM (cf. [Pourquoi remplacer le RNN](#dl-transformer-why)), Dense pour du tabulaire
5. **Définir l'architecture** — Sequential (séquentiel simple) ou Functional API (plusieurs entrées/sorties, branches parallèles) (cf. [Construire l'architecture](#dl-architecture-rules))
6. **Compiler** — loss + optimizer + metrics (cf. [Entraînement — loss & optimizer](#dl-training-loss-optim), [Choisir un optimizer](#dl-optimizer-choice))
7. **Entraîner** (`.fit()`) avec les callbacks utiles — Early Stopping, ModelCheckpoint, ReduceLROnPlateau (cf. [Early Stopping & jeu de validation](#dl-early-stopping))
8. **Régulariser si overfitting** — Dropout, pénalité L1/L2 par couche (cf. [Dropout](#dl-dropout), [Régularisation par couche](#dl-regularization-layers))
9. **Ajuster les hyperparamètres** — learning rate, batch size, epochs (cf. [Hyperparamètres](#dl-hyperparameters))
10. **Évaluer** sur le TEST set (jamais vu pendant l'entraînement) — comparer à une [Baseline](#ml-baseline-concept) ; un K-fold reste possible mais coûteux en Deep Learning (cf. [Cross-Validation manuelle en Deep Learning](#dl-manual-cv))
11. **Prédire** sur une donnée nouvelle une fois le modèle validé

> [!TIP]
> 👉 Déploiement (API de prédiction, monitoring en production, outils comme MLflow) : pas encore couvert dans ce mémo — hors périmètre tant que ce n'est pas vu en cours.
