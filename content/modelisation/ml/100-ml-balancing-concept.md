---
title: Balancing — pourquoi équilibrer les classes
subgroup: Data Preparation
---

Une classe sous-représentée est mal apprise par le modèle — un split 70/30 est déjà considéré déséquilibré en classification binaire.

:::compare
- **Oversampling** : augmenter le nombre d'observations de la classe minoritaire (par duplication, ou génération synthétique via SMOTE, cf. ci-dessous)
- **Undersampling** : sous-échantillonner (retirer des observations de) la classe majoritaire
:::

**SMOTE** (Synthetic Minority Oversampling Technique) — au lieu de dupliquer des points existants (qui n'ajoute aucune information nouvelle), génère de nouveaux points synthétiques de la classe minoritaire par interpolation : pour chaque point minoritaire, prend un de ses plus proches voisins (de la même classe) et crée un nouveau point sur le segment qui les relie.

> [!WARNING]
> ⚠️ **Où appliquer le balancing** : seulement sur le train set, après le split — jamais sur le test set qui doit rester représentatif du monde réel.
