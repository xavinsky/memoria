---
title: ROC-AUC
subgroup: Métriques
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Courbe ROC
Syntaxe:
```
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = **roc_curve**(y_true, y_proba)
```
Params:
```
fpr (False Positive Rate) = FP/(FP+TN)
tpr (True Positive Rate) = recall
```
Explication: contrairement à precision_recall_curve, les deux axes se basent sur la matrice de confusion complète — cf. page Modélisation ▸ [ROC-AUC](#ml-roc-auc)

## AUC (Area Under Curve)
Syntaxe:
```
from sklearn.metrics import roc_auc_score
**roc_auc_score**(y_true, y_proba)
```
Params: -
Explication: cf. page Modélisation ▸ [ROC-AUC](#ml-roc-auc)

## PR-AUC (Average Precision)
Syntaxe:
```
from sklearn.metrics import average_precision_score
**average_precision_score**(y_true, y_proba)
# ou : cross_validate(model, X, y, scoring='average_precision')
```
Params: -
Explication: cf. page Modélisation ▸ [ROC-AUC](#ml-roc-auc)

## Visualiser la courbe precision-recall
Syntaxe:
```
from sklearn.metrics import PrecisionRecallDisplay
**PrecisionRecallDisplay**.from_estimator(model, X_test, y_test)
# ou : .from_predictions(y_test, y_proba)
```
Params: -
Explication: équivalent "tout-en-un" de precision_recall_curve + plt.plot (cf. [Precision-Recall Tradeoff](#ml-precision-recall-tradeoff), ci-dessus)
