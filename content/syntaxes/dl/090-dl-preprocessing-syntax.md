---
title: Preprocessing intégré au modèle — Normalization
subgroup: Keras
type: syntax
---

## Scaler en dehors du modèle (façon Sklearn)
Syntaxe:
```
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
```
Résultat: fonctionne, mais il faut refaire cette étape à chaque prédiction — le scaler vit en dehors du modèle sauvegardé

## Intégrer le scaling dans l'architecture
Syntaxe:
```
from tensorflow.keras.layers import Normalization
norm = **Normalization**()
norm.adapt(X_train)
model.add(norm)
```
Résultat: norm.adapt() calcule moyenne/écart-type sur X_train (équivalent d'un .fit()) ; ajoutée comme 1ère couche, elle scale automatiquement toute entrée du modèle (train, test, futures prédictions)

## Autres couches de preprocessing intégrables
Syntaxe: CategoryEncoding (OneHotEncoder), TextVectorization (NLP), Resizing (images)...
Résultat: même logique que Normalization : le preprocessing fait partie du modèle sauvegardé, plus besoin de le répéter manuellement à l'inférence
