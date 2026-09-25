---
title: Encoding — quel encodage choisir
subgroup: Data Preparation
---

Les modèles Sklearn ne travaillent qu'avec des nombres — toute variable catégorielle doit être encodée avant `.fit()`.

:::compare
- **OrdinalEncoder** : la catégorie a un VRAI ordre (ex: bad < average < good) — encode en un seul entier respectant cet ordre. Mauvais choix sur une variable sans ordre : crée une fausse relation numérique entre catégories (ex: Paris=0, Lyon=1, Marseille=2 n'a pas de sens).
- **OneHotEncoder** : la catégorie n'a PAS d'ordre (ex: ville, couleur) — une colonne binaire par catégorie. Attention à la cardinalité : beaucoup de catégories distinctes → curse of dimensionality (cf. Feature Selection, ci-dessous).
- **LabelEncoder** : réservé à l'encodage de la TARGET en classification — pas des features. Souvent inutile : la plupart des modèles Sklearn acceptent une target texte directement.
:::

> [!TIP]
> 👉 **Repère rapide** : y a-t-il un ordre naturel entre les catégories ? Oui → OrdinalEncoder. Non → OneHotEncoder (cf. Encoding, page Syntaxes, pour la syntaxe).
