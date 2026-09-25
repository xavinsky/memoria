---
title: Forward & Backward Propagation
subgroup: Optimisation
---

Entraîner un réseau applique la même mécanique que Gradient Descent (cf. groupe ml) à θ = TOUS les poids/biais du réseau — mais calculer $\nabla L$ pour des millions de paramètres demande une méthode spécifique : la **backpropagation**.

1. **Forward propagation** : le batch traverse le réseau couche par couche, produit $\hat y = f_{\theta^{(k)}}(X_{batch})$ puis la Loss $L(\theta^{(k)})$ — les calculs intermédiaires de chaque couche sont gardés en mémoire
2. **Backward propagation** : le gradient $\nabla L$ est calculé en repartant de la sortie vers l'entrée, couche par couche, via la règle de la chaîne (dérivées composées)
3. Mise à jour des poids : $\theta^{(k+1)} \leftarrow \text{Update}(\theta^{(k)}, \nabla L)$ — cf. [Gradient Descent](#ml-gradient-descent), groupe ml

Calculer chaque dérivée partielle $\partial L/\partial\theta_i$ séparément demanderait un forward pass PAR paramètre. En repartant de la sortie, la règle de la chaîne permet de **réutiliser** les termes déjà calculés à la couche suivante — une seule passe backward donne TOUTES les dérivées, pour un coût proche d'un simple forward pass.

> [!TIP]
> 💡 Popularisée en 1987, cette astuce de calcul est à l'origine de l'essor des réseaux de neurones : elle rend entraînable un modèle à des millions de paramètres.

> [!WARNING]
> ⚠️ **Vanishing gradient** — en repartant de la sortie, chaque multiplication de la règle de la chaîne peut réduire la magnitude du gradient. Les poids des PREMIÈRES couches (les plus loin de la sortie) reçoivent donc un gradient plus faible et sont plus difficiles à mettre à jour que ceux des dernières couches.
