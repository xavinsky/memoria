---
title: Encodage cyclique — variables périodiques
subgroup: Data Preparation
---

Une variable **cyclique** (heure, jour de la semaine, mois, angle) pose un problème si on la laisse en valeur brute : sa valeur numérique masque la proximité entre la FIN et le DÉBUT du cycle. Ex: 23h et 0h sont voisines dans le temps, mais 23 et 0 sont numériquement aux deux extrêmes opposés pour le modèle.

```math
x_{sin} = \sin\!\left(\dfrac{2\pi \cdot x}{période}\right) \qquad x_{cos} = \cos\!\left(\dfrac{2\pi \cdot x}{période}\right)
```

Remplacer la variable par CE COUPLE de deux colonnes place chaque valeur sur un cercle plutôt que sur une droite — deux valeurs voisines sur le cercle restent numériquement voisines, même à cheval sur la frontière du cycle (23h → (sin≈-0.26, cos≈0.97) et 0h → (sin=0, cos=1), très proches).

> [!TIP]
> 👉 Une seule colonne (sin OU cos) ne suffit pas : plusieurs heures partagent le même sinus (ex: 6h et 18h) — il faut le COUPLE (sin, cos) pour identifier une position unique sur le cercle.
