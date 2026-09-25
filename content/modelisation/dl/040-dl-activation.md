---
title: Fonctions d'activation
subgroup: Fondamentaux
---

**Pourquoi une activation NON-LINÉAIRE est indispensable** : sans elle, empiler des layers reviendrait à composer des fonctions linéaires — qui reste... une fonction linéaire. Un réseau de 100 layers sans activation équivaut mathématiquement à une seule régression linéaire.

```math
A(a_1x_1+a_2x_2)+B(b_1x_1+b_2x_2) = (Aa_1+Bb_1)x_1+(Aa_2+Bb_2)x_2
```

Toute combinaison de fonctions linéaires reste une fonction linéaire (démonstration ci-dessus) — la non-linéarité de $f$ est ce qui permet au réseau d'approximer des relations complexes.

:::compare
- **ReLU — hidden layers, choix par défaut** : $f(x)=\max(0,x)$ — rapide à calculer, quasi toujours le premier choix pour les couches cachées
- **Sigmoid — dernière couche, classification binaire** : écrase entre 0 et 1, interprétable comme une probabilité (1 neurone de sortie)
- **Softmax — dernière couche, classification multi-classe** : généralise sigmoid à k classes — transforme k scores en probabilités qui somment à 1 (softmax à 2 classes = sigmoid)
- **Linear (identité) — dernière couche, régression** : $f(x)=x$ — aucune borne sur la sortie, adapté à une target continue non bornée
:::

> [!TIP]
> 👉 **Règle empirique** : (presque) toujours ReLU pour les couches cachées, sauf la DERNIÈRE couche dont l'activation est dictée par la tâche (cf. [Construire l'architecture](#dl-architecture-rules), ci-dessous) — pas par préférence.
