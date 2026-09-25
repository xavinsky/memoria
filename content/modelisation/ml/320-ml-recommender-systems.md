---
title: Systèmes de recommandation
subgroup: Modèles
---

Méthode **memory-based** : pas de modèle qui "apprend" au sens classique — on précalcule une matrice de similarités entre items (ou entre utilisateurs), réutilisée directement pour recommander.

:::compare
- **Content-based** : similarité calculée à partir des ATTRIBUTS des items (ex: genres/tags d'un film) — recommande des items similaires par leur contenu, même sans aucune interaction utilisateur
- **Collaborative filtering** : similarité calculée à partir des INTERACTIONS/notes des utilisateurs (ex: matrice films × utilisateurs) — capture des similarités "de goût" invisibles dans le contenu, mais nécessite un historique d'interactions
- **Hybrid** : combine les deux (ex: moyenne des deux similarités) — plus robuste que chacune seule : le contenu ancre la recommandation dans la thématique, le collaboratif ajoute la popularité/le goût réel des utilisateurs
:::

1. Construire une matrice **item × features** (content-based : Bag-of-Words sur du texte, cf. NLP) ou **item × utilisateurs** (collaborative : pivot des notes, 0 pour une note manquante)
2. Réduire sa dimension si elle est grande/creuse (cf. `TruncatedSVD`, page Syntaxes)
3. Calculer la **similarité cosinus** entre un item cible et tous les autres (cf. page Syntaxes) — ou utiliser `NearestNeighbors` (cf. Unsupervised Learning, page Syntaxes) pour ne récupérer que les k plus proches
4. Recommander les items les plus similaires (hors l'item cible lui-même)
