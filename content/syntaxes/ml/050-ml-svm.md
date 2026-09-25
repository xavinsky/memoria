---
title: SVM — Support Vector Machines (SVC / SVR)
subgroup: Choix du modèle
type: syntax
columns:
  Nom: col-nom
  Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## SVC — classification à marge maximale
Syntaxe:
```
from sklearn.svm import SVC
model = **SVC**(kernel='linear', C=10)
```
Params: kernel : linear/poly/rbf/sigmoid — C : force de la pénalité sur les points mal classés
Explication: toujours scaler les features avant (cf. Feature Scaling) — cf. page Modélisation ▸ SVM pour le détail marge/kernel

## SVR — régression à marge maximale
Syntaxe:
```
from sklearn.svm import SVR
model = **SVR**(kernel='rbf', C=1, epsilon=0.1)
```
Params: epsilon : largeur de la "rue" dans laquelle les points ne sont pas pénalisés
Explication: même principe que SVC, inversé : fitter le plus de points possible DANS la marge plutôt qu'en dehors

## Équivalent SGD (kernel linéaire uniquement)
Syntaxe:
```
from sklearn.linear_model import SGDClassifier
model = **SGDClassifier**(loss='hinge', penalty='l2', alpha=1/C)
```
Params: -
Explication: solver SGD au lieu d'une résolution exacte — beaucoup plus rapide sur un gros dataset, mais uniquement kernel linéaire (pas de kernel trick)

## Analyser le modèle entraîné
Syntaxe:
```
model.**n_support_**       # nb de vecteurs de support par classe
model.**decision_function**(X)  # distance signée à l'hyperplan
```
Params: -
Explication: n_support_ élevé = frontière complexe (beaucoup de points proches de la marge) ; decision_function() renvoie la distance AVANT application du seuil (contrairement à predict())

## ⚠️ Éviter un blocage du solveur (kernel linéaire + C élevé)
Syntaxe: SVC(kernel='linear', C=100, **max_iter**=10_000)
Params: -
Explication: sur des données pas parfaitement séparables, libsvm peut ne JAMAIS converger (bloqué indéfiniment, pas juste lent) — max_iter force un arrêt propre (ConvergenceWarning) au lieu d'un blocage
