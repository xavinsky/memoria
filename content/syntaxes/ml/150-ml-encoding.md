---
title: Encoding (variables catégorielles)
subgroup: Transformation
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## OrdinalEncoder — catégories avec un ordre
Syntaxe:
```
from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder(categories=[['bad','average','good']])
enc.**fit**(df[['col']])
enc.**categories_**
df[['col_encoded']] = enc.**transform**(df[['col']])
```
Params: categories : ordre explicite à préciser, sinon ordre alphabétique par défaut
Explication: à utiliser seulement si la variable a un vrai ordre — sinon crée une fausse relation numérique entre catégories

## OneHotEncoder — catégories sans ordre
Syntaxe:
```
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)
ohe.**fit**(df[['col']])
df[ohe.**get_feature_names_out**()] = ohe.**transform**(df[['col']])
df = df.**drop**(columns=['col'])
```
Params: drop="if_binary" : une seule colonne si la feature n'a que 2 catégories
Explication: crée une colonne binaire par catégorie — attention à la cardinalité (curse of dimensionality) sur les colonnes à beaucoup de catégories

## OneHotEncoder — limiter la cardinalité & gérer l'inconnu
Syntaxe: OneHotEncoder(**max_categories**=10, **handle_unknown**='ignore')
Params: max_categories : regroupe les catégories les moins fréquentes au-delà de N ; handle_unknown='ignore' : ne plante pas si le test set contient une catégorie absente du train (met 0 partout au lieu d'une erreur)
Explication: fit() reste sur le TRAIN uniquement — indispensable pour ne pas planter au .transform() du test set

## LabelEncoder — encoder la target (classification)
Syntaxe:
```
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder().fit(y)
y_encoded = le.**transform**(y)
le.**inverse_transform**(y_encoded)  # retour aux labels d'origine
```
Params: -
Explication: souvent inutile : la plupart des modèles Sklearn gèrent une target texte directement — à réserver aux cas où l'encodage/décodage est explicitement nécessaire
