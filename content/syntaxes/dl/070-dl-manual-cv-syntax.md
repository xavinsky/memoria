---
title: Cross-Validation manuelle (K-Fold)
subgroup: Keras
type: syntax
---

## Découper les INDICES en K folds
Syntaxe:
```
from sklearn.model_selection import KFold
kf = **KFold**(n_splits=5, shuffle=True, random_state=0)
for train_idx, val_idx in kf.split(X):
    ...
```
Résultat: contrairement à cross_val_score (Sklearn only), un modèle Keras se boucle à la main — cf. page Modélisation ▸ [Cross-Validation manuelle en Deep Learning](#dl-manual-cv)

## Boucle complète (1 fold)
Syntaxe:
```
X_tr, X_va = X[train_idx], X[val_idx]
y_tr, y_va = y[train_idx], y[val_idx]
preproc = create_preproc(X_tr)   # refait à zéro CHAQUE fold
X_tr_p, X_va_p = preproc.fit_transform(X_tr, y_tr), preproc.transform(X_va)
model = **initialize_model**(X_tr_p.shape[1])   # modèle NEUF chaque fold
h = model.fit(X_tr_p, y_tr, validation_data=(X_va_p, y_va), epochs=150)
```
Résultat: score du fold : min(h.history['val_loss']) ou sa dernière valeur, selon ce qu'on veut comparer
