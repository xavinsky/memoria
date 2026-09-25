---
title: Multicolinéarité — VIF
---

**Multicolinéarité** — redondance entre PLUSIEURS features, au-delà des simples paires détectées par une matrice de corrélation classique (deux features peuvent être peu corrélées entre elles individuellement, mais l'une être presque entièrement prédite par une COMBINAISON des autres).

> [!WARNING]
> ⚠️ Ce n'est PAS un problème de prédiction — le R² global reste correct. Le problème est l'INTERPRÉTATION : l'OLS ne sait plus "répartir" l'effet entre features redondantes, leurs coefficients deviennent instables (grande variance), parfois de signes contre-intuitifs (cf. Cond. No., ci-dessus).

```math
VIF_j = \dfrac{1}{1 - R_j^2}
```

Pour détecter laquelle des features pose problème (feature par feature, contrairement au Cond. No. qui est un signal global) : régresser la feature $j$ sur TOUTES les autres features, $R_j^2$ = variance de $j$ expliquée par les autres. Si $j$ est presque entièrement redondante avec les autres, $R_j^2 \to 1$ et $VIF_j \to +\infty$.

> [!TIP]
> 👉 **Repère pratique** : VIF > 5 (parfois 10 selon les sources) signale une multicolinéarité problématique — retirer une des features redondantes, ou régulariser (Ridge gère nativement les features corrélées, cf. Régularisation, groupe ML).
