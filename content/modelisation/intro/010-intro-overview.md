---
title: Qu'est-ce que la Modélisation
---

Un **modèle** est mathématiquement une **fonction**. Il est produit par un **algorithme** lors de la phase d'**entraînement** (basée sur un grand volume de données), et sert ensuite à transformer une entrée en nouvelles données (prédiction, classification, génération, ...).

> [!TIP]
> 👉 La modélisation est utile dès que la relation entrée→sortie est trop complexe ou trop coûteuse à coder explicitement (ex: reconnaître un chat sur une photo, prédire un prix), mais qu'on dispose d'exemples passés pour l'apprendre.

On classe les modèles en 3 familles — Machine Learning classique / Deep Learning / Reinforcement Learning — et par **type d'apprentissage**.

![](../../diagrams/intro-overview-1.svg)

:::compare
- **Machine Learning classique** : modèles statistiques/algorithmiques sur des données structurées
- **Deep Learning** : réseaux de neurones à plusieurs couches — apprentissage de représentations directement à partir de données brutes (image, texte, audio)
- **Reinforcement Learning** : un agent apprend par essai-erreur à maximiser une récompense en interagissant avec un environnement
:::

:::compare
- **Apprentissage supervisé** : chaque exemple d'entraînement a une bonne réponse connue (label) — le modèle apprend à la reproduire (ex: régression, classification)
- **Apprentissage non supervisé** : aucun label fourni — le modèle trouve des structures/patterns dans les données seules (ex: clustering, réduction de dimension)
- **Apprentissage semi-supervisé** : un petit nombre d'exemples labellisés + beaucoup de données non labellisées — utile quand labelliser coûte cher, le modèle généralise à partir des deux
- **Apprentissage par essai-erreur (récompense)** : pas de label — seulement une récompense reçue après une séquence d'actions, l'agent apprend par essai-erreur — propre au Reinforcement Learning
:::
