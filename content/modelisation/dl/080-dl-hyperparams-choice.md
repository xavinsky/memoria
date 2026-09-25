---
title: Hyperparamètres — comprendre les réglages clés
subgroup: Fondamentaux
---

Tous les hyperparamètres Deep Learning vus jusqu'ici, regroupés au même endroit.

**Entraînement — communs à toute architecture** (cf. [Hyperparamètres — learning rate, batch size, epochs](#dl-hyperparameters), [Early Stopping](#dl-early-stopping))

:::compare
- **learning_rate** : contrôle l'amplitude du changement de θ à chaque update — un scheduler (ex: ExponentialDecay) le fait décroître automatiquement pendant l'entraînement (grands pas au début, petits vers la fin).
- **batch_size** : petit = plus stochastique, converge potentiellement plus vite mais généralise moins bien ; grand = meilleure généralisation, plus coûteux par update. En pratique : 16 ou 32 pour des données réelles.
- **epochs** : pas besoin de fixer un nombre à l'avance — en mettre "autant que possible" et laisser l'Early Stopping arrêter au bon moment.
- **patience (EarlyStopping)** : nombre d'epochs sans amélioration de la loss de validation tolérées avant d'arrêter l'entraînement (la loss étant stochastique, il en faut plusieurs pour ne pas s'arrêter trop tôt).
:::

**Optimizer** (`model.compile`, cf. [Choisir un optimizer](#dl-optimizer-choice))

:::compare
- **optimizer='adam'** : combine Momentum + RMSProp — le choix par défaut pour démarrer ; passer une INSTANCE (`optimizers.Adam(learning_rate=...)`) plutôt qu'un string pour personnaliser ses réglages.
- **loss (model.compile)** : façon de comparer y_true à y_pred — ex: 'mse' (régression), 'binary_crossentropy' (classification binaire) ; cf. [Entraînement — loss & optimizer](#dl-training-loss-optim).
:::

**Régularisation** (cf. [Régularisation par couche](#dl-regularization-layers), [Dropout](#dl-dropout))

:::compare
- **kernel_regularizer / bias_regularizer / activity_regularizer** : L1/L2 appliquée respectivement aux poids W, aux biais b, ou à la sortie de la couche — même principe que Ridge/Lasso (cf. groupe ml), mais couche par couche.
- **rate (Dropout)** : fraction des neurones "tués" (=0) à chaque itération d'entraînement — force le réseau à répartir l'information plutôt que de sur-spécialiser un neurone.
:::

**CNN** (cf. [Convolution](#dl-cnn-convolution), [Hyperparamètres de la convolution](#dl-cnn-hyperparams))

:::compare
- **filters / kernel_size** : nombre de filtres appris en parallèle par la couche, et taille du kernel (ex: 3×3) — petits kernels/peu de filtres en début de réseau, l'inverse en fin (Transfer Learning).
- **strides** : pas de déplacement du kernel — 1 (défaut) glisse pixel par pixel ; 2 saute un pixel sur deux (feature map deux fois plus petite).
- **padding** : 'valid' (défaut, la feature map rétrécit) ou 'same' (ajoute des 0 aux bords pour garder la même taille).
- **pooling (MaxPooling/AveragePooling)** : réduit la taille de la feature map sans paramètre entraînable — une couche MaxPooling2D après chaque Conv2D est la pratique courante.
:::

**RNN** (cf. [Sous le capot d'une couche RNN](#dl-rnn-mechanics), [SimpleRNN, LSTM, GRU](#dl-rnn-zoology))

:::compare
- **units (n_h)** : taille de l'état interne h — indépendante de la longueur des séquences, contrairement au nombre d'observations temporelles.
- **return_sequences** : False (défaut) : une seule sortie par séquence (le dernier état) ; True : une sortie à chaque pas de temps — nécessaire pour empiler une autre couche RNN ou prédire une séquence complète.
- **cellule — SimpleRNN / LSTM / GRU** : SimpleRNN = rapide mais mémoire courte ; LSTM = mémoire longue, plus de paramètres ; GRU = variante plus légère du LSTM.
:::

**NLP / Embedding** (cf. [Embedding appris pour la tâche](#dl-nlp-embedding-layer), [CNN pour du texte — Conv1D](#dl-nlp-conv1d))

:::compare
- **embedding_dim** : dimension du vecteur dense représentant chaque mot (typiquement 30 à 300) — plus grand = plus de paramètres à apprendre, epochs plus lents.
- **vocab_size / max_length** : taille du vocabulaire (via la Tokenization) et longueur de séquence après padding — déterminent le nombre de paramètres de la couche Embedding : (vocab_size + 1) × embedding_dim.
- **kernel_size (Conv1D)** : nombre de mots consécutifs considérés à la fois par le filtre — analogue à une fenêtre Word2Vec.
:::

**Transformers** (cf. [Multi-Head Attention](#dl-transformer-multihead), [Contrôler la génération](#dl-transformer-generation-params))

:::compare
- **d_model / n_heads** : dimension totale des embeddings, divisée entre les têtes d'attention (d_head = d_model / n_heads) — chaque tête peut se spécialiser sur un aspect différent.
- **Temperature** : contrôle le hasard du choix du prochain token — basse = déterministe, haute = créatif/aléatoire.
- **Top-k / Top-p** : restreignent les tokens candidats aux k plus probables, ou au plus petit ensemble cumulant une probabilité p (nucleus sampling).
- **Max tokens** : longueur maximale de la génération, quitte à arrêter en plein milieu d'une phrase.
:::

**Autoencoder** (cf. [Applications — compression, génération, débruitage](#dl-autoencoder-applications))

:::compare
- **dimension de l'espace latent** : trop petite = perte d'info excessive (reconstruction dégradée) ; trop grande = aucune vraie compression — compromis choisi via la méthode du coude, comme pour k en PCA.
:::

**Diffusion** (cf. [Modèles de diffusion](#dl-diffusion-models))

:::compare
- **num_inference_steps** : nombre d'étapes de débruitage — plus haut = image plus nette, mais génération plus lente.
- **guidance_scale** : fidélité au prompt texte — plus haut = suit le texte plus strictement, au prix d'images moins naturelles/variées.
:::
