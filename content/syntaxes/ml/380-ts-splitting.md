---
title: Train/test split contigu & features autorégressives
subgroup: Time Series
type: syntax
columns:
  Objectif: col-objectif
  Syntaxe: col-syntaxe
  Params: col-params
  Explication: col-explication
---

## Split contigu (pas de shuffle)
Syntaxe:
```
train_size = 0.6
index = round(train_size * df.shape[0])
df_train = df.**iloc**[:index]
df_test = df.**iloc**[index:]
```
Params: -
Explication: JAMAIS train_test_split classique — data leakage temporel (cf. page Modélisation ▸ Modèles ▸ Time Series ▸ [Décomposition](#ts-decomposition))

## Créer des features autorégressives (lags)
Syntaxe:
```
for i in range(1, 13):
    df[f't-{i}'] = df['value'].**shift**(i)
df.**dropna**(inplace=True)
```
Params: -
Explication: 1 colonne par lag ; dropna() retire les premières lignes incomplètes

## Moyenne mobile (lisser, isoler la tendance)
Syntaxe: df['roll_12'] = df['value'].**rolling**(12).mean()
Params: fenêtre = nb de points glissants
Explication: moyenne des N derniers points — lisse le bruit court terme, fait ressortir la tendance

## Moyenne mobile exponentielle
Syntaxe: df['ewm_3'] = df['value'].**ewm**(halflife=3).mean()
Params: halflife : le poids d'un point est divisé par 2 tous les halflife pas
Explication: pondère les points récents plus fort que rolling() (poids décroissant exponentiellement) — réagit plus vite à un changement récent

## Baseline TS (prédire la valeur précédente)
Syntaxe: y_pred = df_test['value'].**shift**(1)
Params: -
Explication: modèle le plus simple possible — point de comparaison minimal (cf. [Baseline Score](#ml-baseline), groupe ml)

## Encoder une variable cyclique (angle, heure, jour...)
Syntaxe:
```
radians = df['angle_deg'] * np.pi / 180
df['x'] = np.**cos**(radians)
df['y'] = np.**sin**(radians)
```
Params: -
Explication: une valeur brute (359° proche de 0°, 23h proche de 0h) trompe un modèle qui ne voit qu'un nombre — sin/cos replace la valeur sur un cercle, où le début et la fin de la période sont bien voisins
