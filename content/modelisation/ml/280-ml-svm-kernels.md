---
title: Kernel Trick — rendre les données linéairement séparables
subgroup: Modèles
---

Si les classes ne sont pas linéairement séparables dans l'espace d'origine, une solution est d'ajouter des features transformées (ex: $Z = X^2+Y^2$) pour les rendre séparables dans un espace de dimension supérieure — une fonction de **feature mapping** φ.

> [!WARNING]
> ⚠️ Problème : cette transformation explicite augmente la dimensionnalité du problème, ce qui peut rendre l'entraînement d'un SVM très coûteux.

**Le kernel trick** : au lieu de transformer explicitement chaque point, on calcule directement une **similarité** K(a,b) entre chaque paire de points — cette similarité simule le produit scalaire qu'on aurait obtenu dans l'espace transformé, sans jamais le calculer explicitement. Beaucoup plus efficace.

| Kernel | Formule | Usage |
|---|---|---|
| linear | K(a,b) = aᵀb | cas linéairement séparable (pas de feature mapping) |
| poly (degré d) | K(a,b) = (aᵀb + c)ᵈ | frontières polynomiales — utilisable aussi en régression (SVR) |
| rbf (gaussien) | K(a,b) = exp(−γ‖a−b‖²) | similarité qui décroît exponentiellement avec la distance — γ (gamma) = facteur de myopie, γ grand → overfitting |
| sigmoid | \- | coefficient gamma également |

```
SVC(**kernel**='rbf', C=1, gamma='scale')
```

> [!TIP]
> 👉 Chaque kernel correspond à un feature mapping φ implicite différent — `linear` = pas de mapping, `rbf` = un mapping de dimension infinie.

> [!TIP]
> 💡 **PolynomialFeatures** applique la même idée (ajouter des termes polynomiaux/croisés : a², b², a·b...) mais de façon EXPLICITE plutôt qu'implicite — utilisable avec n'importe quel modèle linéaire (LinearRegression, Ridge...), pas seulement un SVM ; combiner avec une régularisation (cf. Régularisation, ci-dessus) pour éviter l'overfitting que ces termes supplémentaires peuvent causer.
