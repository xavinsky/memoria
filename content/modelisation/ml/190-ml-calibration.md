---
title: Calibration de probabilités
subgroup: Métriques
---

`predict_proba()` renvoie un NOMBRE entre 0 et 1, mais rien ne garantit que ce nombre soit une vraie probabilité fiable. Un modèle est **bien calibré** si, parmi toutes les prédictions autour de 0.9, environ 90% des observations sont RÉELLEMENT positives — l'accuracy seule ne dit rien de cela.

> [!WARNING]
> ⚠️ Certains modèles calibrent mal par construction — ex: `predict_proba()` d'un arbre de décision n'est que la proportion de classes dans la feuille atteinte, pas une vraie probabilité (cf. Arbre de décision, ci-dessus).

1. Tracer une **courbe de calibration** (proportion réelle de positifs vs probabilité prédite, par bucket) sur un jeu de TEST dédié — une diagonale parfaite = modèle bien calibré
2. Si le modèle est mal calibré, le RECALIBRER : entraîner un mapping supplémentaire (souvent une régression logistique ou une régression isotonique) qui corrige les probabilités brutes vers de vraies fréquences observées

> [!TIP]
> 👉 Important seulement quand la VALEUR de la probabilité compte (ex: risque de défaut de paiement, probabilité météo) — si seule la classe prédite (via un seuil) importe, la calibration ne change rien à l'accuracy/au F1.
