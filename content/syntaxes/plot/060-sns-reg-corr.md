---
title: Seaborn — régression et corrélation
type: syntax
---

## Nuage de points + droite de régression + intervalle de confiance
Syntaxe: sns.**regplot**(x="col1", y="col2", data=df, y_jitter=0.3, ci=95)
Résultat: scatter + droite de régression linéaire, avec un cône ombré = intervalle de confiance (95% par défaut) — y_jitter ajoute du bruit vertical pour mieux voir la densité de points quand y est discret

## Matrice de corrélation entre toutes les colonnes numériques
Syntaxe: df.**corr**(numeric_only=True)
Résultat: DataFrame carré (n_cols x n_cols) des coefficients de corrélation de Pearson entre chaque paire de colonnes (cf. Corrélation de Pearson, page Maths)

## Visualiser la matrice de corrélation
Syntaxe: sns.**heatmap**(df.corr(numeric_only=True), cmap="coolwarm", annot=True)
Résultat: grille colorée : rouge = corrélation positive forte, bleu = corrélation négative forte ; annot=True affiche les valeurs numériques dans chaque case
