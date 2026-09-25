---
title: Choisir un optimizer — Momentum, AdaGrad, RMSProp, Adam
subgroup: Optimisation
---

[[P:SGD]] · [[P:RMSprop]] · [[P:Adagrad]] · [[P:Adam]]

Une descente de gradient simple (cf. groupe ml) ne suffit pas en Deep Learning : la Loss est beaucoup plus complexe (non convexe), et l'optimizer reste facilement bloqué dans un minimum local.

:::compare
- **Momentum** : ajoute de l'inertie au déplacement — accumule les gradients précédents pour continuer sur sa lancée et franchir les minima locaux peu profonds
- **AdaGrad** : learning rate adaptatif PAR paramètre — priorise les poids peu souvent mis à jour
- **RMSProp** : ajoute une décroissance (decay) — seuls les gradients récents comptent vraiment
- **Adam** : combine Momentum + RMSProp — le choix par défaut pour démarrer
:::

> [!TIP]
> 👉 En pratique : commencer avec `optimizer='adam'` (cf. page Syntaxes) avant d'explorer les autres.

> [!TIP]
> 💡 Le string `'adam'` utilise ses hyperparamètres par défaut — pour personnaliser le `learning_rate` (ou tout autre réglage), passer une INSTANCE de l'optimizer plutôt qu'un string (`optimizers.Adam(learning_rate=0.01)`, cf. page Syntaxes).
