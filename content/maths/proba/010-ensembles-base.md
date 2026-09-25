---
title: Théorie des ensembles & probabilités (base)
---

:::compare
- **Épreuve (trial)** : une réalisation de l'expérience
- **Issue (outcome)** : un résultat possible
- **Univers ($\Omega$)** : l'ensemble de toutes les issues possibles
- **Événement** : un sous-ensemble de $\Omega$
:::

Ex: lancer un dé = expérience, un lancer = épreuve, "3" = issue, {1,2,3,4,5,6} = univers $\Omega$, "obtenir un nombre pair" = événement.

```math
P(A \cup B) = P(A) + P(B) - P(A \cap B)
```

**Union** de deux événements — on retire $P(A\cap B)$ car sinon la zone commune serait comptée deux fois. Cas particulier : si $A\cap B=\emptyset$ (événements **incompatibles/disjoints**), $P(A\cup B)=P(A)+P(B)$.

```math
P(\overline{A}) = 1 - P(A)
```

**Complémentaire** — toute la probabilité restante hors de A.

```math
\overline{A \cup B} = \overline{A} \cap \overline{B} \qquad \overline{A \cap B} = \overline{A} \cup \overline{B}
```

**Lois de De Morgan** — utile pour réécrire une condition niée sur un DataFrame : `df[~((df.col1>10)&(df.col2=="A"))]` devient `df[(df.col1<=10)|(df.col2!="A")]`.

```math
P(A \cap B) = P(A) \cdot P(B)
```

**Intersection** de deux événements **indépendants** (A n'influence pas B) — ex: deux jets de dé.

```math
P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)
```

**Règle du produit (chain rule)** — reste valable même si A et B ne sont PAS indépendants, contrairement à la formule précédente. Ex: deux tirages de carte sans remise sont dépendants.

```math
P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}
```

**Probabilité conditionnelle** — restreint l'univers à B, puis regarde la part de A dedans ($P(B)>0$).

```math
P(B) = \sum_i P(B \mid A_i)\,P(A_i)
```

**Loi des probabilités totales** — sert à calculer P(B) quand on ne peut pas le mesurer directement, en le reconstruisant à partir des probas conditionnelles par scénario ($\{A_i\}$ = partition de l'univers, ex: malade/sain — sous-ensembles disjoints dont l'union couvre tout $\Omega$).

> [!TIP]
> 👉 C'est précisément le dénominateur utilisé dans le théorème de Bayes (page suivante).

```math
A \setminus B = A \cap \overline{B}
```

**Différence de deux ensembles** — à ne pas confondre avec le complémentaire $\overline A$ (qui retire tout A, sans référence à B) : $A\setminus B$ ne retire de A que la partie commune avec B.
