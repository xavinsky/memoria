---
title: Precision-Recall Tradeoff
subgroup: Métriques
type: syntax
---

## Explorer tous les seuils
Syntaxe:
```
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = **precision_recall_curve**(y_true, y_proba)
```
Résultat: y_proba : probabilités prédites de la classe positive, via model.predict_proba(X)[:,1] — donne precision et recall pour chaque seuil possible

## Trouver le seuil garantissant un recall minimum
Syntaxe:
```
scores = pd.DataFrame({'threshold':thresholds,'precision':precision[:-1],'recall':recall[:-1]})
scores[scores['recall'] >= 0.8].**tail**(1)
```
Résultat: parmi les seuils qui garantissent le recall visé, prendre le plus élevé maximise la precision associée à ce recall

## Appliquer le nouveau seuil pour reclasser
Syntaxe: preds = (y_proba >= **seuil_choisi**).astype(int)  # au lieu du seuil 0.5 par défaut
Résultat: une fois le seuil optimal trouvé, reclasse les probabilités manuellement plutôt que d'utiliser model.predict() (seuil fixe à 0.5)
