---
title: Chain rule appliquée à la SSR — pas à pas
intro: Pourquoi ŷᵢ reste tel quel à une étape de la dérivation, puis se retrouve remplacé par β₀+β₁X₁ juste après — sans que ce soit une incohérence.
---

::::derivation

:::step Rappel — la règle de la chaîne, en plus simple

Avant de revenir à la SSR, posons la règle sur une fonction à une seule variable, sans aucun β ni Σ pour l'instant. Si une fonction se compose de deux étages, un extérieur f et un intérieur g :

```math
h(x) = f(g(x))
```

alors sa dérivée est le produit des deux dérivées, chacune évaluée à son propre niveau :

```math
h'(x) = f'(g(x)) \cdot g'(x)
```

Exemple concret : $h(x) = (5-x^2)^2$. On pose $g(x) = 5-x^2$ et $f(u) = u^2$ :

```math
h'(x) = \textcolor{#2E6F82}{2(5-x^2)}\cdot\textcolor{#9C3B31}{(-2x)}
```

> [!TIP]
> 👉 Dans $\textcolor{#2E6F82}{2(5-x^2)}$, on garde $g(x)$ tel quel — c'est juste "2 fois la valeur de g", pas besoin de la ré-écrire autrement. Dans $\textcolor{#9C3B31}{(-2x)}$, en revanche, on a bien dû utiliser la formule explicite $5-x^2$ pour calculer sa dérivée. C'est exactement le même mécanisme qu'on va retrouver avec la SSR — juste avec ŷᵢ à la place de g(x).

:::

:::step Le terme qu'on cherche à dériver

La SSR (Sum of Squared Residuals) additionne, pour chaque observation i, le carré de l'écart entre la vraie valeur et la valeur prédite :

```math
SSR(\beta) = \sum_{i=1}^n (y_i-\hat y_i)^2 = \sum_{i=1}^n \big(y_i-(\beta_0+\beta_1 X_1^{(i)})\big)^2
```

On veut $\partial SSR/\partial\beta_0$ : de combien la SSR change quand on bouge β₀ d'un tout petit pas. Pour un seul terme de la somme, c'est encore une composition f(g(β₀)), exactement comme à l'étape 0.

:::

:::step Qui est l'extérieur, qui est l'intérieur ?

Pour appliquer la règle de la chaîne, il faut d'abord décider ce qu'on appelle f et ce qu'on appelle g :

:::compare
- {outer} **Extérieur — f** : f(u) = u² — "mettre au carré". Elle ne sait rien de β₀, elle prend juste un nombre u et le met au carré.
- {inner} **Intérieur — g** : g(β₀) = yᵢ − ŷᵢ — le résidu. C'est LUI qui dépend de β₀, puisque ŷᵢ est la prédiction du modèle.
:::

Autrement dit : u = g(β₀), et le terme de la SSR c'est f(g(β₀)). On va dériver chacune séparément, dans l'ordre.

:::

:::step Dériver l'extérieur — f par rapport à u

f(u) = u² se dérive en f'(u) = 2u. On réinjecte u = g(β₀) = yᵢ−ŷᵢ :

```math
f'(g(\beta_0)) = 2\,\textcolor{#2E6F82}{(y_i - \hat y_i)}
```

> [!TIP]
> 👉 ŷᵢ reste tel quel — à cette étape, on ne dérive PAS ŷᵢ, on l'utilise juste comme une valeur. On n'a aucune raison de la remplacer par sa formule ici, parce qu'on n'est pas en train de calculer "comment ŷᵢ varie" — on calcule juste la pente de la fonction "carré", évaluée à l'endroit où se trouve le résidu actuel.

:::

:::step Dériver l'intérieur — g par rapport à β₀

Ici, en revanche, on doit calculer g'(β₀), c'est-à-dire : de combien yᵢ−ŷᵢ varie quand β₀ varie. Pour répondre, il faut forcément savoir ce qu'est ŷᵢ **en fonction de β₀** — donc on la remplace par sa formule :

```math
\dfrac{\partial}{\partial\beta_0}(y_i-\hat y_i) = \dfrac{\partial}{\partial\beta_0}\big(y_i-\textcolor{#9C3B31}{(\beta_0+\beta_1 X_1^{(i)})}\big)
```

c'est seulement maintenant qu'on explicite ŷᵢ = β₀ + β₁X₁⁽ⁱ⁾. Une fois développé, yᵢ est une constante par rapport à β₀ (dérivée nulle), β₁X₁⁽ⁱ⁾ est aussi constant par rapport à β₀ (dérivée nulle), et −β₀ se dérive en −1 :

```math
g'(\beta_0) = 0 - 1 - 0 = -1
```

:::

:::step Pourquoi la substitution arrive exactement là, et pas avant

C'est la réponse directe à la question "pourquoi on mélange ŷᵢ et β" : ce ne sont pas les mêmes ŷᵢ. Il y en a deux occurrences dans le calcul, avec deux rôles totalement différents.

:::compare
- {outer} **Étape 3 — ŷᵢ = une valeur** : On multiplie par le résidu actuel. Sa formule interne (β₀+β₁X₁) ne joue aucun rôle dans ce facteur — seul son résultat numérique compte.
- {inner} **Étape 4 — ŷᵢ = un objet à dériver** : On demande "comment ŷᵢ réagit à β₀ ?". Pour répondre, il faut absolument sa formule explicite — impossible de dériver quelque chose dont on ignore la définition.
:::

> [!TIP]
> 💡 **En une phrase** : on garde ŷᵢ en notation compacte partout où on ne fait que l'utiliser, et on la déplie en β₀+β₁X₁⁽ⁱ⁾ uniquement à l'endroit précis où on la dérive. Le "mélange" apparent, c'est juste ces deux rôles qui coexistent dans la même ligne de calcul.

:::

:::step Recombiner les deux facteurs

La règle de la chaîne dit f'(g)·g'. On multiplie le résultat de l'étape 3 par celui de l'étape 4 :

```math
\dfrac{\partial}{\partial\beta_0}(y_i-\hat y_i)^2 = 2(y_i-\hat y_i)\cdot(-1) = -2(y_i-\hat y_i)
```

Le signe change simplement parce que g'(β₀) = −1 ; la structure "2 fois le résidu" de l'étape 3 ne bouge pas.

:::

:::step Sommer sur toutes les observations

La SSR est une somme sur n observations, et la dérivée d'une somme est la somme des dérivées — on répète donc le résultat de l'étape 6 pour chaque i :

```math
\dfrac{\partial SSR}{\partial\beta_0} = \sum_{i=1}^n -2(y_i-\hat y_i)
```

c'est la formule finale utilisée par la descente de gradient pour mettre à jour β₀.

:::

:::step Exactement le même raisonnement pour β₁

Seule différence : à l'étape 4, on dérive (yᵢ−(β₀+β₁X₁⁽ⁱ⁾)) par rapport à β₁ au lieu de β₀. Cette fois β₀ est la constante, et −β₁X₁⁽ⁱ⁾ se dérive en −X₁⁽ⁱ⁾ (au lieu de −1) :

```math
\dfrac{\partial SSR}{\partial\beta_1} = \sum_{i=1}^n 2(y_i-\hat y_i)\cdot(-X_1^{(i)}) = \sum_{i=1}^n -2X_1^{(i)}(y_i-\hat y_i)
```

Le facteur X₁⁽ⁱ⁾ apparaît uniquement parce que β₁ est multiplié par X₁ dans ŷᵢ — dériver "par rapport à β₁" fait ressortir son coefficient, exactement comme dériver 3x par rapport à x donne 3.

En écriture vectorielle, les deux dérivées ci-dessus (et celles de tous les autres β) se rangent dans le vecteur gradient :

```math
\nabla SSR(\beta) = -2X^T(y-\hat y) = -2X^T(y-X\beta)
```

:::

:::step Vérification avec l'exemple numérique du cours

Le cours reprend cette formule sur l'exemple taille/poids, avec β₁ fixé à 0.64 et β₀ initialisé à 0 :

```
b1 = 0.64
b0_epoch0 = 0

# dérivée = Σ −2(y − ŷ), avec ŷ = h(X, b0) = b0 + b1·X
derivative = np.sum(-2 * (y - h(X, b0_epoch0)))
# → -5.448

# mise à jour : β₀ ← β₀ − η · dérivée  (η = 0.1)
b0_epoch1 = b0_epoch0 - (eta * derivative)
# → 0.5448
```

C'est la formule de l'étape 7 appliquée telle quelle : on calcule le résidu (y−ŷ) pour chaque point avec le β₀ courant, on multiplie par −2, on somme — et on obtient la dérivée qui pilote le pas suivant de la descente de gradient.

:::

:::step Carte résumé

```math
\dfrac{\partial SSR}{\partial\beta_0} = \sum_{i=1}^n -2(y_i-\hat y_i) \qquad \dfrac{\partial SSR}{\partial\beta_1} = \sum_{i=1}^n -2X_1^{(i)}(y_i-\hat y_i)
```

**Règle à retenir** : ŷᵢ garde sa forme compacte tant qu'on ne fait que l'évaluer ; ŷᵢ se déplie en β₀+β₁X₁⁽ⁱ⁾ uniquement à l'instant précis où on dérive par rapport à un β.

:::

::::
