---
title: Métriques de classification
subgroup: Métriques
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Matrice de confusion
Syntaxe:
```
pd.**crosstab**(index=y_true, columns=y_pred)
# ou : from sklearn.metrics import confusion_matrix
confusion_matrix(y_true, y_pred)
```
Params: TP/TN/FP/FN
Explication: base de toutes les métriques ci-dessous — définitions TP/TN/FP/FN : cf. page Modélisation ▸ [Métriques de classification](#ml-metrics-classification)

## Visualiser la matrice de confusion
Syntaxe:
```
from sklearn.metrics import ConfusionMatrixDisplay
**ConfusionMatrixDisplay**.from_estimator(model, X_test, y_test)
# ou : ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
```
Params: normalize='true' : proportions au lieu des comptages bruts
Explication: from_estimator = modèle + X à prédire ; from_predictions = prédictions déjà calculées (ex: via cross_val_predict)

## Toutes les métriques d'un coup, par classe
Syntaxe:
```
from sklearn.metrics import classification_report
print(**classification_report**(y_true, y_pred))
```
Params: -
Explication: tableau récapitulatif precision/recall/f1-score/support pour chaque classe — pratique pour un premier coup d'œil sans appeler chaque fonction séparément

## Accuracy
Syntaxe:
```
from sklearn.metrics import accuracy_score
**accuracy_score**(y_true, y_pred)
```
Params: -
Explication: cf. page Modélisation ▸ [Métriques de classification](#ml-metrics-classification)

## Recall
Syntaxe:
```
from sklearn.metrics import recall_score
**recall_score**(y_true, y_pred)
```
Params: -
Explication: cf. page Modélisation ▸ [Métriques de classification](#ml-metrics-classification), et Precision-Recall Tradeoff ci-dessous

## Precision
Syntaxe:
```
from sklearn.metrics import precision_score
**precision_score**(y_true, y_pred)
```
Params: -
Explication: cf. page Modélisation ▸ [Métriques de classification](#ml-metrics-classification), et Precision-Recall Tradeoff ci-dessous

## F1 score
Syntaxe:
```
from sklearn.metrics import f1_score
**f1_score**(y_true, y_pred)
```
Params: -
Explication: cf. page Modélisation ▸ [Métriques de classification](#ml-metrics-classification)
