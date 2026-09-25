---
title: Systèmes de recommandation — TruncatedSVD & similarité
subgroup: Unsupervised Learning
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Réduire une matrice CREUSE (comptage de mots, notes...)
Syntaxe:
```
from sklearn.decomposition import TruncatedSVD
svd = **TruncatedSVD**(n_components=25, random_state=42)
latent = svd.fit_transform(count_matrix)
```
Params: n_components : dimensions gardées
Explication: équivalent de PCA mais NE CENTRE PAS les données — utilisable directement sur une matrice creuse (Bag-of-Words, pivot de notes), contrairement à PCA qui exige un centrage préalable

## Calculer une similarité item-à-tous
Syntaxe:
```
from sklearn.metrics.pairwise import cosine_similarity
sims = **cosine_similarity**(latent_df.loc[['item_cible']], latent_df)[0]
```
Params: -
Explication: angle entre vecteurs — proche de 1 = très similaire, indépendant de la norme des vecteurs (cf. Modélisation ▸ [Systèmes de recommandation](#ml-recommender-systems))
