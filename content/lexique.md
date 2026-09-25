# Lexique

Un terme par titre `## Terme` ; la définition renvoie vers la section qui le détaille.

## A/B Test

nom donné en pratique (produit/data) à un test d'hypothèse appliqué à une expérience : control group vs treatment group. [Maths ▸ Test d'hypothèse](#test-hypothese)

## Accuracy

proportion de prédictions correctes sur l'ensemble des prédictions. [Modélisation ▸ Métriques de classification](#ml-metrics-classification)

## ACF (Autocorrelation Function)

mesure la corrélation entre une Time Series et ses versions décalées (lags) — sert à estimer l'ordre q d'un processus MA. [Modélisation ▸ Modèles ▸ Time Series ▸ Autocorrélation (ACF & PACF)](#ts-autocorrelation)

## AdaBoost

boosting qui repondère les observations mal classées à chaque itération, pour que le weak learner suivant s'y concentre davantage. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Adam

optimizer de réseau de neurones combinant Momentum et RMSProp — le choix par défaut pour démarrer un entraînement Keras. [Modélisation ▸ Choisir un optimizer](#dl-optimizer-choice)

## ADF (Augmented Dickey-Fuller)

test de stationnarité d'une Time Series : p-value proche de 0 (< 0.05) → série stationnaire. [Modélisation ▸ Stationnarité & test ADF](#ts-stationarity)

## Agent (LLM)

utilise un LLM pour prendre des actions vers un objectif (boucle Observe → Think → Act → Repeat), typiquement avec des outils (Tool Calling) et de la mémoire. [Industrialisation ▸ Agents LLM — de répondeur à exécutant](#dl-agents)

## Agent (RL)

le décideur qui interagit avec un environnement — observe un état, choisit une action, reçoit une récompense, et met à jour sa stratégie. [Modélisation ▸ Reinforcement Learning — composants & boucle](#dl-rl-foundations)

## Apprentissage non supervisé (Unsupervised Learning)

aucun label fourni — le modèle trouve des structures/patterns dans les données seules (ex: clustering, réduction de dimension). [Modélisation ▸ Qu'est-ce que la Modélisation](#intro-overview)

## Apprentissage semi-supervisé (Semi-supervised Learning)

un petit nombre d'exemples labellisés + beaucoup de données non labellisées — utile quand labelliser coûte cher. [Modélisation ▸ Qu'est-ce que la Modélisation](#intro-overview)

## Apprentissage supervisé (Supervised Learning)

chaque exemple d'entraînement a une bonne réponse connue (label) — le modèle apprend à la reproduire (ex: régression, classification). [Modélisation ▸ Qu'est-ce que la Modélisation](#intro-overview)

## AR (AutoRegressive)

modèle de Time Series qui régresse Y sur ses propres valeurs passées — un choc se propage loin dans le futur. [Modélisation ▸ AR & MA](#ts-ar-ma)

## Arbre de décision (Decision Tree)

modèle hiérarchique qui sépare les données par une suite de décisions binaires (feature, seuil), en minimisant le Gini Index à chaque coupure. [Modélisation ▸ Arbre de décision](#ml-decision-tree)

## ARIMA

modèle de Time Series combinant AutoRegressive (AR), Integrated (differencing) et Moving Average (MA), noté ARIMA(p,d,q). [Modélisation ▸ ARMA, ARIMA & SARIMA](#ts-arima)

## ARMA

combine AR et MA : modélise Y à la fois par ses valeurs passées et par ses erreurs passées. [Modélisation ▸ ARMA, ARIMA & SARIMA](#ts-arima)

## Attention (Self-Attention)

mécanisme qui permet à chaque token d'une séquence de "regarder" tous les autres pour calculer sa propre représentation, contextualisée par toute la phrase. [Modélisation ▸ Self-Attention — Query, Key, Value](#dl-transformer-attention)

## AUC (Area Under Curve)

aire sous la courbe ROC — mesure la capacité d'un classifieur à distinguer les classes, indépendamment du seuil choisi. [Modélisation ▸ ROC-AUC](#ml-roc-auc)

## Autoencoder

réseau encodeur+décodeur entraîné à reconstruire son propre input via un espace latent compressé — compression, génération, débruitage. [Modélisation ▸ Autoencoder — encoder, décodeur, espace latent](#dl-autoencoder)

## AutoTokenizer

classe Hugging Face qui charge le tokenizer EXACTEMENT associé à un modèle pré-entraîné (from_pretrained) — doit toujours correspondre au modèle utilisé, sous peine de tokens incohérents. [Modélisation ▸ Tokenization — du texte aux entiers](#dl-tokenization)

## Average Precision (PR-AUC)

aire sous la courbe precision-recall — préférée à l'AUC-ROC sur un dataset fortement déséquilibré (l'AUC-ROC reste optimiste, écrasée par les nombreux vrais négatifs). [Modélisation ▸ ROC-AUC](#ml-roc-auc)

## Backpropagation (rétropropagation)

calcule le gradient de la Loss d'un réseau de neurones en repartant de la sortie vers l'entrée, via la règle de la chaîne — bien plus rapide qu'un calcul terme à terme. [Modélisation ▸ Forward & Backward Propagation](#dl-backpropagation)

## Bag-of-Words (BoW)

représentation vectorielle d'un texte par comptage des occurrences de chaque mot, sans tenir compte de l'ordre. [Modélisation ▸ Vectorizing](#nlp-vectorizing)

## Bagging (Bootstrap Aggregating)

entraîne plusieurs weak learners EN PARALLÈLE sur des échantillons bootstrap, puis moyenne/vote leurs prédictions — réduit la variance. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Baseline (Baseline Score)

score d'un modèle trivial (ex: `DummyRegressor`, `DummyClassifier`), utilisé comme point de comparaison minimal avant tout modèle réel. [Modélisation ▸ Baseline — pourquoi comparer avant de complexifier](#ml-baseline-concept)

## Batch Size

taille du sous-ensemble de données utilisé à chaque mise à jour des paramètres pendant l'entraînement d'un réseau de neurones. [Modélisation ▸ Entraînement — loss & optimizer](#dl-training-loss-optim)

## Bayes (Théorème de)

relie la probabilité a posteriori d'une hypothèse à sa probabilité a priori et à la vraisemblance des données observées. [Maths ▸ Théorème de Bayes](#bayes-naive-bayes)

## Bellman Equation

formule de mise à jour du Q-Learning — combine la récompense immédiate et la meilleure valeur future estimée, pondérées par learning rate et discount factor. [Modélisation ▸ Q-Learning — apprendre la valeur d'une action](#dl-rl-q-learning)

## BERT (Bidirectional Encoder Representations from Transformers)

Transformer encoder-only pré-entraîné avec attention bidirectionnelle — produit des embeddings contextuels, réutilisables pour classification, NER... [Modélisation ▸ Encoder-only, Decoder-only, Encoder-Decoder](#dl-transformer-families)

## Bias (biais)

écart systématique entre les prédictions du modèle et la vraie valeur — un biais élevé signale un modèle trop simple (underfitting). [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## Bias-Variance Tradeoff

compromis fondamental entre un modèle trop simple (bias élevé) et un modèle trop complexe (variance élevée). [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## BLEU (Bilingual Evaluation Understudy)

mesure la proportion de n-grammes du texte généré présents dans la référence (proche d'une precision), pénalisée si le texte est trop court — utilisé en traduction. [Modélisation ▸ Évaluer un LLM — BLEU, ROUGE, Perplexité](#dl-transformer-evaluation)

## Boosting

entraîne les weak learners EN SÉQUENCE, chacun corrigeant les erreurs du précédent — réduit le biais. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Box-Jenkins Method

démarche complète de modélisation ARIMA : stationnariser, lire p/q sur ACF/PACF, fitter, inspecter les résidus, itérer. [Modélisation ▸ ARMA, ARIMA & SARIMA](#ts-arima)

## Calibration (probabilités)

un modèle est bien calibré si, parmi les prédictions autour de p, environ p% des observations sont réellement positives — l'accuracy seule ne le garantit pas. [Modélisation ▸ Calibration de probabilités](#ml-calibration)

## Chaîne de Markov (Markov Chain)

modélise un système qui change d'état selon des probabilités de transition fixes — seul l'état actuel compte (propriété de Markov), pas l'historique. [Maths ▸ Chaînes de Markov](#chaines-markov)

## Checkpointer (LangGraph)

donne une mémoire persistante à un agent — conserve l'historique de conversation entre plusieurs appels, identifié par un thread_id. [Industrialisation ▸ Agents LLM — de répondeur à exécutant](#dl-agents)

## Chunking (RAG)

découpe un document long en morceaux (chunks) avec un léger chevauchement, avant de les embedder — un chunk trop long dépasse la limite d'entrée de l'embedder, trop court perd le contexte. [Industrialisation ▸ Pipeline RAG — Embedding, Vector Database, Retrieval](#dl-rag-pipeline)

## Classification

tâche de prédiction d'une catégorie parmi un nombre fini de classes connues (target discrète). [Modélisation ▸ Choisir sa famille de modèle](#ml-model-selection)

## CLS (token BERT)

token spécial placé au début de toute séquence pour BERT — son embedding en sortie résume l'information de la phrase entière, réutilisable comme feature. [Modélisation ▸ Encoder-only, Decoder-only, Encoder-Decoder](#dl-transformer-families)

## Clustering

regroupement d'observations similaires entre elles, sans labels connus au départ. [Modélisation ▸ Choisir sa famille de modèle](#ml-model-selection)

## CNN (Convolutional Neural Network)

réseau de neurones spécialisé dans les images, qui empile des couches de convolution (au lieu de couches Dense) pour préserver la structure spatiale de l'input. [Modélisation ▸ Pourquoi pas un réseau Dense pour les images](#dl-cnn-why-not-dense)

## ColumnTransformer

applique en parallèle un traitement différent selon le type de colonne (numérique vs catégorielle) dans une Pipeline. [Modélisation ▸ Workflow Scikit-learn — avec pipeline (usage réel)](#ml-workflow-pipeline)

## Concept Drift

la relation entre features et cible change dans le temps (P(y|X) évolue) — un modèle entraîné sur l'ancienne relation devient FAUX, même si la distribution des features reste stable. [Industrialisation ▸ Data Drift vs Concept Drift](#infra-drift)

## Confusion Matrix

tableau croisant prédictions et réalité (TP/TN/FP/FN), base de toutes les métriques de classification. [Modélisation ▸ Métriques de classification](#ml-metrics-classification)

## Conv1D

convolution 1D pour du texte — fait glisser le kernel uniquement le long de l'axe des mots (jamais sur l'axe de l'embedding). [Modélisation ▸ CNN pour du texte — Conv1D](#dl-nlp-conv1d)

## Conv2DTranspose

couche qui fait l'inverse d'une convolution — agrandit la taille spatiale au lieu de la réduire (strides=2 double la taille) ; brique de base d'un décodeur d'images. [Modélisation ▸ Conv2DTranspose — l'inverse d'une convolution](#dl-conv2d-transpose)

## Convolution

opération qui fait glisser un kernel sur une image, en multipliant terme à terme puis en sommant à chaque position, pour produire une feature map. [Modélisation ▸ Convolution — kernel, filtre, feature map](#dl-cnn-convolution)

## Corrélation de Pearson

mesure la dépendance LINÉAIRE entre deux variables (r∈[-1,1]) — r=0 n'implique pas indépendance, seulement l'absence de lien linéaire. [Maths ▸ Statistiques descriptives](#stats-descriptives)

## Cosine Similarity

mesure la similarité entre deux vecteurs via l'angle qui les sépare — métrique la plus utilisée pour la recherche de documents en RAG. [Industrialisation ▸ Pipeline RAG — Embedding, Vector Database, Retrieval](#dl-rag-pipeline)

## Cross-Attention

dans le décodeur d'un Transformer : la query vient du décodeur, mais les keys/values viennent de la sortie de l'encodeur — relie les deux blocs. [Modélisation ▸ Architecture — Positional Encoding, blocs, masquage](#dl-transformer-architecture)

## Cross-Entropy

voir Log Loss. [Modélisation ▸ Log Loss](#ml-log-loss)

## Cross-Validation

validation d'un modèle sur K sous-échantillons du train set, plus robuste qu'un simple train/test split — pas toujours du K-Fold classique (StratifiedKFold, TimeSeriesSplit, GroupKFold... selon le contexte). [Modélisation ▸ Cross-Validation](#ml-cross-validation-concept)

## Curse of Dimensionality (fléau de la dimension)

dégradation de la capacité de généralisation d'un modèle quand le nombre de features augmente — plus de features nécessite exponentiellement plus de données. [Modélisation ▸ Feature Selection](#ml-feature-selection-concept)

## darts (librairie)

librairie Python de séries temporelles qui unifie de nombreux modèles (naïf, ARIMA, Prophet, TBATS...) sous une même API .fit()/.predict(), avec gestion native des covariables. [Modélisation ▸ Modèles ▸ Time Series ▸ ARMA, ARIMA & SARIMA](#ts-arima)

## Data Augmentation

génère des variantes des images d'entraînement (rotation, zoom, miroir...) à la volée, pour plus de diversité sans dupliquer le dataset. [Modélisation ▸ Data Augmentation](#dl-cnn-data-augmentation)

## Data Drift

la distribution des features en entrée change dans le temps (nouveaux profils, saisonnalité...) — le modèle reste valide en théorie mais s'applique à des données différentes de son entraînement. [Industrialisation ▸ Data Drift vs Concept Drift](#infra-drift)

## Data Leakage

fuite d'information du test set (ou du futur) dans l'entraînement, qui fausse l'évaluation à la hausse. [Modélisation ▸ Data Leakage](#ml-data-leakage-concept)

## Décomposition (Time Series)

sépare une série en Trend + Seasonal + Résidus (additive) ou Trend × Seasonal × Résidus (multiplicative). [Modélisation ▸ Modèles ▸ Time Series ▸ Décomposition](#ts-decomposition)

## Deep Learning

réseau de neurones avec BEAUCOUP de layers — pas pertinent sur toute donnée : voir quand le choisir plutôt qu'un modèle ML classique. [Modélisation ▸ ML, DL ou RL ?](#ml-dl-choice)

## Dendrogramme

arbre des fusions successives d'un clustering hiérarchique — la hauteur d'une branche = la distance à laquelle deux clusters ont été unis ; couper l'arbre à une hauteur donnée fixe le nombre de clusters. [Modélisation ▸ Clustering Hiérarchique — dendrogramme](#ml-hierarchical-clustering)

## Densité de probabilité (pdf)

hauteur de la courbe d'une loi continue en un point x — ce n'est pas directement une probabilité (contrairement à la pmf discrète). [Maths ▸ Loi normale, LGN & TCL](#loi-normale)

## Déterminant

scalaire caractérisant une matrice carrée — déterminant = 0 ⇔ matrice NON inversible (colonnes colinéaires), même information que rang < nb de colonnes. [Maths ▸ Résoudre un système linéaire par inversion de matrice](#systeme-lineaire-matriciel)

## Discretizing

transformer une variable continue en catégories (ex: prix → Low/High), pour passer d'une tâche de régression à une tâche de classification. [Modélisation ▸ Discretizing — pourquoi/quand discrétiser](#ml-discretizing-concept)

## Distillation (Model Compression)

entraîne un petit modèle "élève" à imiter la distribution de probabilité d'un grand modèle "professeur" — pas seulement ses labels finaux. [Industrialisation ▸ Compresser un modèle — Quantization & Distillation](#dl-model-compression)

## DQN (Deep Q-Network)

remplace la Q-table par un réseau de neurones qui prédit les Q-values à partir d'un état — passe à l'échelle sur des espaces d'états grands ou continus. [Modélisation ▸ Deep Q-Network (DQN) — dépasser la Q-table](#dl-rl-dqn)

## Dropout

à chaque itération d'entraînement, désactive aléatoirement une fraction des neurones d'une couche — empêche le réseau de sur-dépendre d'un neurone particulier, améliore la généralisation. [Modélisation ▸ Dropout](#dl-dropout)

## Écart interquartile (IQR)

Q3-Q1 ; un point est considéré outlier hors de [Q1-1.5·IQR, Q3+1.5·IQR] — règle utilisée par les moustaches d'un boxplot. [Maths ▸ Statistiques descriptives](#stats-descriptives)

## Écart-type

ramène la variance (dispersion autour de la moyenne) dans l'unité des données ; sur un échantillon, diviser par n-1 (correction de Bessel) plutôt que n. [Maths ▸ Statistiques descriptives](#stats-descriptives)

## Early Stopping

arrête l'entraînement d'un réseau de neurones quand la loss de validation cesse de s'améliorer — évite l'overfitting sans fuite de données vers le test set. [Modélisation ▸ Early Stopping & jeu de validation](#dl-early-stopping)

## ElasticNet

régularisation combinant Ridge (L2) et Lasso (L1), pondérée par l'hyperparamètre `l1_ratio`. [Modélisation ▸ Régularisation](#ml-regularization)

## Embedding

représentation d'un mot par un vecteur dense (30 à 300 dimensions typiquement) — deux mots proches sémantiquement sont proches mathématiquement dans cet espace. [Modélisation ▸ Représenter les mots — pourquoi un Embedding](#dl-nlp-word-representation)

## Encodage cyclique (sin/cos)

transforme une variable cyclique (angle, heure, jour de l'année) en deux colonnes sin/cos, pour que le début et la fin de la période soient bien voisins pour le modèle. [Modélisation ▸ Encodage cyclique — variables périodiques](#ml-cyclical-encoding)

## Ensemble Learning

combine plusieurs modèles de base (souvent des arbres de décision) pour obtenir une prédiction plus robuste qu'un seul modèle. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Epoch

un passage complet sur l'ensemble du dataset d'entraînement pendant le fitting d'un réseau de neurones. [Modélisation ▸ Entraînement — loss & optimizer](#dl-training-loss-optim)

## Error Analysis

examen des erreurs individuelles du modèle (sous-groupes, classes, erreurs extrêmes), au-delà d'un score global unique. [Modélisation ▸ Error analysis](#ml-error-analysis)

## Espace latent (Latent Space)

représentation compressée de l'input produite par l'encodeur d'un Autoencoder — dimension bien plus faible que l'input d'origine. [Modélisation ▸ Autoencoder — encoder, décodeur, espace latent](#dl-autoencoder)

## Espérance (E[X])

moyenne théorique des valeurs d'une variable aléatoire, pondérée par leur probabilité. [Maths ▸ Lois de probabilité discrètes](#lois-discretes)

## Exploration vs Exploitation

compromis en RL entre essayer de nouvelles actions (exploration) et réutiliser les actions déjà connues pour bien performer (exploitation). [Modélisation ▸ Exploration vs Exploitation, récompenses différées](#dl-rl-exploration-exploitation)

## F-statistic

teste si un modèle de régression dans son ensemble est significatif (au moins un β≠0) ; Prob(F-statistic) = p-value associée, à regarder avant les coefficients individuels. [Maths ▸ Régression linéaire (OLS) — R² et diagnostic](#ols-theorie-r2)

## F1 Score

moyenne harmonique de precision et recall, utile quand aucune des deux n'est clairement prioritaire. [Modélisation ▸ Métriques de classification](#ml-metrics-classification)

## Feature Map

sortie d'un filtre de convolution appliqué à une image — plus on avance dans les couches d'un CNN, plus les feature maps sont petites et abstraites. [Modélisation ▸ Convolution — kernel, filtre, feature map](#dl-cnn-convolution)

## Feature Scaling

mise à l'échelle des features numériques (StandardScaler, MinMaxScaler, RobustScaler) avant d'entraîner un modèle sensible aux échelles. [Modélisation ▸ Feature Scaling — quel scaler choisir](#ml-scaling-choice)

## Feature Selection

réduction du nombre de features utilisées par le modèle, pour limiter l'overfitting et améliorer l'interprétabilité. [Modélisation ▸ Feature Selection](#ml-feature-selection-concept)

## FeatureUnion

applique plusieurs transformers EN PARALLÈLE sur le même jeu de colonnes puis concatène les résultats — utile pour ajouter une feature calculée en plus du preprocessing existant. [Modélisation ▸ Transformers personnalisés](#ml-custom-transformer-choice)

## Fenêtrage (Windowing)

transforme une série temporelle brute en paires (séquence d'entrée, cible) via des fenêtres glissantes — étape de préparation des données avant un RNN. [Modélisation ▸ Pourquoi un RNN — la dimension temporelle](#dl-rnn-input-shape)

## FFT (Fast Fourier Transform)

convertit un signal du domaine temporel (amplitude vs. temps) vers le domaine fréquentiel (amplitude vs. fréquence) — fait ressortir les fréquences dominantes d'un signal complexe (son, etc.), une étape de feature engineering courante avant ML/DL sur de l'audio. [Maths ▸ Transformée de Fourier (FFT)](#fourier-transform)

## Filtre (CNN)

ensemble de kernels (1 par channel de l'input) dont les sorties sont sommées pour produire UNE feature map — une couche de convolution applique plusieurs filtres en parallèle. [Modélisation ▸ Convolution — kernel, filtre, feature map](#dl-cnn-convolution)

## Fine-tuning

repart d'un modèle pré-entraîné et l'ajuste pour le spécialiser — moins coûteux qu'un entraînement from scratch, mais redevient obsolète dès que les données changent. [Industrialisation ▸ Adapter un LLM — Training, Fine-tuning, Grounding](#dl-llm-adapt)

## from_logits

argument d'une loss Keras (ex: SparseCategoricalCrossentropy) — à True si la dernière couche renvoie des logits bruts (pas de softmax), pour que la loss applique elle-même la normalisation. [Modélisation ▸ Entraînement — loss & optimizer](#dl-training-loss-optim)

## Functional API (Keras)

alternative à Sequential pour construire un modèle : on appelle les couches comme des fonctions (Input → ... → Model(inputs, outputs)) — nécessaire dès qu'il y a plusieurs entrées/sorties ou des branches parallèles. [Modélisation ▸ Construire l'architecture — règles de choix](#dl-architecture-rules)

## FunctionTransformer

encapsule une transformation STATELESS (qui n'apprend rien pendant le fit) dans un objet compatible Pipeline, sans écrire de classe. [Modélisation ▸ Transformers personnalisés](#ml-custom-transformer-choice)

## Gini Index

mesure l'impureté d'un nœud d'arbre de décision (0 = nœud pur) ; la coupure retenue minimise le Gini pondéré des nœuds enfants. [Modélisation ▸ Arbre de décision](#ml-decision-tree)

## GPT (Generative Pre-trained Transformer)

Transformer decoder-only, génère du texte de façon autorégressive (un token à la fois) à partir d'un prompt. [Modélisation ▸ Encoder-only, Decoder-only, Encoder-Decoder](#dl-transformer-families)

## Gradient Boosting

chaque arbre prédit le résidu (l'erreur) du précédent, au lieu de repondérer comme AdaBoost — généralement plus performant. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Gradient Descent (descente de gradient)

algorithme itératif qui minimise une Loss Function en suivant la pente inverse de son gradient. [Modélisation ▸ Gradient Descent](#ml-gradient-descent)

## Grid Search

recherche exhaustive des meilleurs hyperparamètres en testant toutes les combinaisons d'une grille de valeurs. [Modélisation ▸ Model Tuning — Grid Search vs Random Search](#ml-model-tuning)

## Grounding

connecte un LLM à des données externes AU MOMENT DE L'USAGE (typiquement via RAG), sans ré-entraîner le modèle. [Industrialisation ▸ Adapter un LLM — Training, Fine-tuning, Grounding](#dl-llm-adapt)

## GRU (Gated Recurrent Unit)

couche récurrente plus légère que le LSTM (moins de paramètres) — entraînement plus rapide, potentiellement moins de données nécessaires. [Modélisation ▸ SimpleRNN, LSTM, GRU](#dl-rnn-zoology)

## Guidance Scale

hyperparamètre d'un modèle de diffusion — contrôle la fidélité de l'image générée au prompt texte (haut = plus fidèle mais moins naturel/varié). [Modélisation ▸ Modèles de diffusion — génération d'images (Stable Diffusion)](#dl-diffusion-models)

## Gymnasium

librairie (ex-OpenAI Gym) qui fournit des environnements RL prêts à l'emploi (make, reset, step, close) pour développer et comparer des algorithmes. [Modélisation ▸ Reinforcement Learning — composants & boucle](#dl-rl-foundations)

## Hétéroscédasticité

variance des résidus non constante (motif en "entonnoir") — invalide l'hypothèse de variance constante de l'OLS ; le R² reste valide, mais p-values et IC des coefficients ne sont plus fiables. [Maths ▸ Régression linéaire (OLS) — R² et diagnostic](#ols-theorie-r2)

## Hidden State (état interne)

vecteur maintenu par une couche RNN, mis à jour à chaque pas de temps — résume ce que la séquence a "vu" jusque-là. [Modélisation ▸ Sous le capot d'une couche RNN](#dl-rnn-mechanics)

## Hinge Loss

loss linéaire d'un SVM en Soft Margin — pénalité proportionnelle à l'enfoncement d'un point dans la marge, sans jamais exploser. [Modélisation ▸ SVM — marge maximale](#ml-svm-margin)

## History (Keras)

objet retourné par model.fit() — history.history est un dict {"loss": [...], "accuracy": [...]} avec une valeur par epoch, exploitable pour tracer les courbes d'entraînement. [Modélisation ▸ Early Stopping & jeu de validation](#dl-early-stopping)

## Holdout Method

méthode de validation la plus simple : un seul split train/test. [Modélisation ▸ Workflow ML — Séparer train/test](#wf0-split)

## Huber Loss

mélange MSE (proche du minimum) et MAE (loin du minimum, peu sensible aux outliers), avec bascule à un seuil δ. [Modélisation ▸ Loss Functions — régression](#ml-loss-functions)

## Hugging Face

entreprise/communauté open-source ; sa librairie `transformers` donne accès en quelques lignes à des modèles pré-entraînés (BERT, GPT, T5...) via des pipelines. [Industrialisation ▸ Adapter un LLM — Training, Fine-tuning, Grounding](#dl-llm-adapt)

## Hyperparamètre

réglage du modèle choisi manuellement avant l'entraînement (ex: alpha, K, C) — par opposition aux paramètres (β), appris automatiquement par `.fit()`. [Modélisation ▸ Hyperparamètres](#ml-hyperparams-choice)

## Inférence bayésienne

mise à jour d'une croyance (prior → posterior) à partir de données observées, via le théorème de Bayes. [Maths ▸ Théorème de Bayes](#bayes-naive-bayes)

## Intervalle de confiance

plage de valeurs plausibles pour un paramètre estimé, à un niveau de confiance donné (ex: 95%). [Maths ▸ Intervalle de confiance](#intervalle-confiance)

## K-Means

algorithme de clustering non supervisé : assigne chaque point au centroïde le plus proche, recalcule les centroïdes, répète jusqu'à convergence. [Modélisation ▸ K-Means — Clustering](#ml-kmeans)

## Keras

API Deep Learning de haut niveau, exécutée au-dessus de TensorFlow, pour définir et entraîner des réseaux de neurones. [Modélisation ▸ Neurone, Layer, Réseau de neurones](#dl-neuron-network)

## Kernel (CNN)

petite matrice (ex: 3×3) glissée sur une image pendant une convolution — ses poids sont appris pendant l'entraînement, comme ceux d'un neurone Dense. [Modélisation ▸ Convolution — kernel, filtre, feature map](#dl-cnn-convolution)

## Kernel Trick

calcule une similarité entre deux points qui simule une transformation vers un espace de dimension supérieure, sans jamais la calculer explicitement. [Modélisation ▸ Kernel Trick](#ml-svm-kernels)

## KNN (K-Nearest Neighbors)

modèle non-paramétrique qui prédit à partir des K plus proches voisins d'un point (moyenne en régression, vote majoritaire en classification). [Modélisation ▸ KNN — K-Nearest Neighbors](#ml-knn)

## LangChain

framework Python qui fournit une interface commune pour appeler différents LLM (Google, OpenAI, Anthropic...), plus des briques pour du RAG, des agents, des chaînes de prompts. [Industrialisation ▸ Agents LLM — de répondeur à exécutant](#dl-agents)

## Lasso

régularisation L1 — peut ramener des coefficients exactement à 0, ce qui en fait un outil de sélection de features. [Modélisation ▸ Régularisation](#ml-regularization)

## LDA (Latent Dirichlet Allocation)

algorithme non supervisé de topic modeling — découvre des thèmes cachés dans un corpus de documents. [Modélisation ▸ Modèles ▸ NLP ▸ LDA (Topic Modeling)](#nlp-lda)

## Learning Curve (courbe d'apprentissage)

évolution des scores train/test selon la taille du training set — diagnostique underfitting, overfitting ou besoin de plus de données. [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## Learning Rate (η)

taille du pas de la descente de gradient à chaque itération — trop petit : convergence lente ; trop grand : risque de ne jamais converger. [Modélisation ▸ Gradient Descent](#ml-gradient-descent)

## Lemmatisation

ramène chaque mot à sa racine ("running" → "run") pour regrouper les mots par sens plutôt que par forme exacte. [Modélisation ▸ Text Preprocessing](#nlp-preprocessing)

## Log Loss (Cross-Entropy)

fonction de perte de la classification binaire, dérivée de la maximisation de la log-vraisemblance — pénalise sévèrement une prédiction confiante et fausse. [Modélisation ▸ Log Loss](#ml-log-loss)

## Log-Likelihood (log-vraisemblance)

logarithme de la vraisemblance des données observées sous un modèle — maximisé lors du MLE. [Maths ▸ Régression logistique — MLE](#logit-theorie)

## Loi Binomiale

probabilité d'obtenir exactement k succès sur n essais indépendants de même probabilité p. [Maths ▸ Lois de probabilité discrètes](#lois-discretes)

## Loi de Bernoulli

expérience à 2 issues complémentaires (succès/échec), de probabilité p. [Maths ▸ Lois de probabilité discrètes](#lois-discretes)

## Loi de Student (T)

loi utilisée pour un test statistique sur petit échantillon (t-test) — plus "lourde aux extrémités" que la loi normale. [Maths ▸ t-test](#t-test)

## Loi des probabilités totales

reconstruit P(B) à partir des probabilités conditionnelles par scénario, quand P(B) n'est pas mesurable directement — c'est le dénominateur du théorème de Bayes. [Maths ▸ Théorie des ensembles & probabilités](#ensembles-base)

## Loi Géométrique

probabilité de réussir pour la première fois au n-ième essai. [Maths ▸ Lois de probabilité discrètes](#lois-discretes)

## Lois de De Morgan

réécrit une condition niée sur une combinaison d'événements (ou un filtre DataFrame) : ¬(A∩B) = ¬A∪¬B et ¬(A∪B) = ¬A∩¬B. [Maths ▸ Théorie des ensembles & probabilités](#ensembles-base)

## LoRA (Low-Rank Adaptation)

technique de PEFT — ajoute une petite matrice entraînable EN PARALLÈLE des blocs existants d'un modèle gelé, au lieu de ré-entraîner tous ses poids. [Industrialisation ▸ Adapter un LLM — Training, Fine-tuning, Grounding](#dl-llm-adapt)

## Loss Function

fonction que `.fit()` minimise pour trouver les meilleurs paramètres d'un modèle — le choix de la Loss définit ce que "meilleur modèle" veut dire. [Modélisation ▸ Que fait .fit() ?](#ml-fit-hood)

## LSTM (Long Short-Term Memory)

couche récurrente introduite pour corriger le vanishing gradient d'un SimpleRNN — plus de paramètres, mémoire plus longue. [Modélisation ▸ SimpleRNN, LSTM, GRU](#dl-rnn-zoology)

## Machine Learning

modèles statistiques/algorithmiques sur données structurées (régression, arbres, SVM, clustering, PCA...) — par opposition au Deep Learning, réservé aux données non-structurées. [Modélisation ▸ Qu'est-ce que la Modélisation](#intro-overview)

## MAE (Mean Absolute Error)

moyenne des erreurs absolues — pénalise chaque erreur proportionnellement à sa taille. [Modélisation ▸ Métriques de régression](#ml-metrics-regression)

## make_scorer

transforme une fonction métrique maison (y_true, y_pred) -> score en un "scorer" sklearn valide, utilisable dans scoring= (cross_validate, GridSearchCV...). [Modélisation ▸ Model Tuning — Grid Search vs Random Search](#ml-model-tuning)

## MAP (Maximum a Posteriori)

estimation qui maximise la probabilité a posteriori, combinant la vraisemblance des données et un a priori sur le paramètre. [Maths ▸ Théorème de Bayes](#bayes-naive-bayes)

## Masking (Keras)

couche placée en tête d'un modèle RNN pour ignorer, pendant l'entraînement, les pas de temps factices ajoutés par le padding. [Modélisation ▸ Séquences de longueurs différentes](#dl-rnn-padding)

## Max Error

borne l'erreur individuelle la plus grave d'un modèle de régression — utile quand une seule erreur extrême est inacceptable (ex: sécurité). [Modélisation ▸ Métriques de régression](#ml-metrics-regression)

## MCP (Model Context Protocol)

protocole standard (Anthropic) pour exposer un outil/une source de données à N'IMPORTE QUEL agent compatible, sans code de connexion sur-mesure par paire agent-outil. [Industrialisation ▸ MCP (Model Context Protocol) — standardiser l'accès aux outils](#dl-mcp)

## Médiane

sépare les données triées en deux moitiés égales — contrairement à la moyenne, robuste aux outliers. [Maths ▸ Statistiques descriptives](#stats-descriptives)

## Minimum local / global

un minimum local minimise une fonction au voisinage d'un point, sans être forcément le minimum absolu (global) sur tout le domaine — un optimiseur parti d'un mauvais point de départ peut y rester bloqué si la fonction n'est pas convexe. [Modélisation ▸ Gradient Descent](#ml-gradient-descent)

## MLE (Maximum Likelihood Estimation)

estimation qui maximise la vraisemblance des données observées sous le modèle. [Maths ▸ Régression logistique — MLE](#logit-theorie)

## Mode (statistique)

valeur la plus fréquente d'une distribution — il peut y en avoir plusieurs (distribution bimodale). [Maths ▸ Statistiques descriptives](#stats-descriptives)

## ModelCheckpoint

callback Keras qui sauvegarde automatiquement le modèle sur disque à chaque amélioration de la métrique surveillée pendant l'entraînement. [Modélisation ▸ Early Stopping & jeu de validation](#dl-early-stopping)

## Modèle de diffusion (Diffusion Model)

génère une image en débruitant progressivement du bruit pur, guidé par un prompt texte — principe derrière Stable Diffusion. [Modélisation ▸ Modèles de diffusion — génération d'images (Stable Diffusion)](#dl-diffusion-models)

## Moyenne

somme des valeurs divisée par leur nombre — notée µ sur toute la population, x̄ sur un échantillon extrait de cette population. [Maths ▸ Statistiques descriptives](#stats-descriptives)

## MSE (Mean Squared Error)

moyenne des erreurs au carré — pénalise fortement les grosses erreurs, très sensible aux outliers. [Modélisation ▸ Métriques de régression](#ml-metrics-regression)

## MSLE (Mean Squared Log Error)

MSE calculé sur le log de la prédiction/target — pénalise l'erreur RELATIVE plutôt que l'écart absolu, adapté à une target positive très étalée (ex: prix). [Modélisation ▸ Loss Functions — régression](#ml-loss-functions)

## Multi-Agent System

plusieurs agents LLM spécialisés collaborent sur une tâche complexe (ex: recherche, résumé, rédaction) — spécialisation, parallélisme, délégation. [Industrialisation ▸ Agents LLM — de répondeur à exécutant](#dl-agents)

## Multi-Head Attention

exécute plusieurs mécanismes d'attention en parallèle (têtes), chacune spécialisée sur un aspect différent — les sorties sont concaténées. [Modélisation ▸ Multi-Head Attention](#dl-transformer-multihead)

## Multicolinéarité

redondance entre plusieurs features, au-delà des simples paires détectées par une matrice de corrélation classique. [Maths ▸ Multicolinéarité — VIF](#ml-multicollinearity)

## N-gram

séquence de n mots consécutifs (bigram, trigram...), utilisée en vectorizing pour restaurer une partie du contexte perdu par le Bag-of-Words. [Modélisation ▸ Vectorizing](#nlp-vectorizing)

## Naive Bayes

classifieur de texte basé sur le théorème de Bayes, sous l'hypothèse (naïve) que les mots d'un document sont conditionnellement indépendants. [Modélisation ▸ Naive Bayes](#nlp-naive-bayes)

## NearestNeighbors

version non supervisée de KNN — indexe un jeu de données et renvoie les k plus proches voisins d'un point, sans classer ni prédire (base d'un système de recommandation par similarité). [Modélisation ▸ KNN — K-Nearest Neighbors](#ml-knn)

## Neurone (Deep Learning)

brique de base d'un réseau de neurones — une régression linéaire suivie d'une fonction d'activation non-linéaire. [Modélisation ▸ Neurone, Layer, Réseau de neurones](#dl-neuron-network)

## No Free Lunch Theorem

aucun modèle n'est optimal pour tous les problèmes — le choix dépend des hypothèses faites sur les données. [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## Non-paramétrique (modèle)

modèle dont le nombre de paramètres appris dépend des données elles-mêmes (ex: KNN, kernel-SVM) — aucune hypothèse a priori sur leur structure. [Modélisation ▸ Choisir sa famille de modèle](#ml-model-selection)

## One-Hot Encoding

encodage d'une variable catégorielle sans ordre en une colonne binaire par catégorie. [Modélisation ▸ Encoding — quel encodage choisir](#ml-encoding-choice)

## One-vs-Rest / One-vs-One (OvR / OvO)

stratégies pour étendre un classifieur binaire à k classes — OvR : un modèle par classe vs le reste ; OvO : un modèle par paire de classes. [Modélisation ▸ Stratégies multiclasse (One-vs-Rest vs One-vs-One)](#ml-multiclass-strategies)

## Opérations sur les ensembles (Union, Intersection, Complémentaire)

Union : P(A∪B)=P(A)+P(B)-P(A∩B) ; Intersection d'événements indépendants : P(A∩B)=P(A)·P(B) ; Complémentaire : P(Ā)=1-P(A). [Maths ▸ Théorie des ensembles & probabilités](#ensembles-base)

## Overfitting (surapprentissage)

le modèle capte le bruit des données d'entraînement en plus du signal — score train haut, score test bas. [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## p-value

probabilité d'observer un résultat au moins aussi extrême que celui obtenu, sous l'hypothèse nulle. [Maths ▸ Test d'hypothèse](#test-hypothese)

## PACF (Partial Autocorrelation Function)

corrélation entre une Time Series et un lag donné, en retirant l'effet des lags intermédiaires — sert à estimer l'ordre p d'un processus AR. [Modélisation ▸ Modèles ▸ Time Series ▸ Autocorrélation (ACF & PACF)](#ts-autocorrelation)

## Padding (CNN)

remplissage à 0 ajouté autour d'une image avant une convolution — 'same' garde la feature map à la taille de l'input, 'valid' (défaut) laisse la feature map rétrécir. [Modélisation ▸ Hyperparamètres de la convolution](#dl-cnn-hyperparams)

## Padding (RNN)

complète les séquences plus courtes que la plus longue du batch avec une valeur factice absente des données réelles, de préférence en fin de séquence (padding='post'). [Modélisation ▸ Séquences de longueurs différentes](#dl-rnn-padding)

## Paramétrique (modèle)

modèle à nombre fixe de paramètres, indépendant de n (ex: LinearRegression, LogisticRegression). [Modélisation ▸ Choisir sa famille de modèle](#ml-model-selection)

## PCA (Principal Component Analysis)

cherche la meilleure combinaison linéaire des features existantes pour résumer le dataset dans moins de dimensions. [Modélisation ▸ PCA — Réduction de dimension](#ml-pca)

## PEFT (Parameter-Efficient Fine-Tuning)

gèle un LLM pré-entraîné et n'entraîne que quelques couches supplémentaires légères — ex: LoRA. [Industrialisation ▸ Adapter un LLM — Training, Fine-tuning, Grounding](#dl-llm-adapt)

## Perplexité

mesure à quel point un modèle de langage est "surpris" par les données — probabilité qu'il assigne à chaque token suivant, utilisée surtout pendant l'entraînement. [Modélisation ▸ Évaluer un LLM — BLEU, ROUGE, Perplexité](#dl-transformer-evaluation)

## Pipeline

enchaînement d'étapes de preprocessing puis de modélisation en un seul objet Sklearn. [Modélisation ▸ Workflow Scikit-learn — avec pipeline (usage réel)](#ml-workflow-pipeline)

## PMF (Probability Mass Function)

probabilité P(X=xᵢ) qu'une variable aléatoire DISCRÈTE prenne une valeur précise — équivalent discret de la pdf (densité) d'une variable continue. [Maths ▸ Variable aléatoire](#variable-aleatoire)

## Policy (RL)

stratégie de l'agent — associe à chaque état la ou les actions à prendre, pour maximiser la récompense cumulée sur le long terme. [Modélisation ▸ Reinforcement Learning — composants & boucle](#dl-rl-foundations)

## PolynomialFeatures

ajoute les termes polynomiaux et croisés (a², b², a·b...) d'un feature set — permet à un modèle linéaire de capturer des relations non-linéaires/des interactions. [Modélisation ▸ Kernel Trick — rendre les données linéairement séparables](#ml-svm-kernels)

## Pooling (Max/Average)

réduit la taille d'une feature map sans aucun paramètre entraînable, en gardant le max (MaxPooling, le plus courant) ou la moyenne (AveragePooling) de chaque sous-région. [Modélisation ▸ Hyperparamètres de la convolution](#dl-cnn-hyperparams)

## Positional Encoding

ajouté à l'embedding de chaque token pour réintroduire l'information de position, perdue quand le Transformer traite toute la séquence en parallèle. [Modélisation ▸ Architecture — Positional Encoding, blocs, masquage](#dl-transformer-architecture)

## PPO (Proximal Policy Optimization)

algorithme RL policy-based — ajuste directement la policy (au lieu d'une Q-table/Q-network), seul choix pour des actions continues, avec un clipping qui limite l'ampleur de chaque mise à jour. [Modélisation ▸ Deep Q-Network (DQN) — dépasser la Q-table](#dl-rl-dqn)

## Precision

fiabilité d'une prédiction positive — à privilégier quand une fausse alerte coûte cher. [Modélisation ▸ Métriques de classification](#ml-metrics-classification)

## Precision-Recall Tradeoff

compromis entre precision et recall selon le seuil de décision choisi. [Modélisation ▸ Choisir sa métrique](#ml-choose-metric)

## Probabilité conditionnelle

restreint l'univers à B, puis regarde la part de A dedans : P(A|B) = P(A∩B)/P(B). [Maths ▸ Théorie des ensembles & probabilités](#ensembles-base)

## Prompt Engineering

formuler soigneusement l'instruction donnée à un LLM (zero-shot, few-shot, exemples...) pour obtenir de meilleurs résultats, sans changer les poids du modèle. [Modélisation ▸ Prompt Engineering — principes](#dl-prompt-engineering)

## Prophet (Facebook)

librairie de prévision de séries temporelles, alternative à ARIMA — gère nativement tendance et saisonnalité(s) sans passer par ACF/PACF/differencing, format imposé (colonnes ds/y). [Modélisation ▸ Modèles ▸ Time Series ▸ ARMA, ARIMA & SARIMA](#ts-arima)

## Pseudo R²

indicateur de qualité d'ajustement pour la régression logistique, basé sur le rapport des log-vraisemblances. [Maths ▸ Régression logistique — MLE](#logit-theorie)

## Puissance (test statistique)

probabilité de détecter un effet réel quand il existe vraiment (1-β) — plus elle est grande, mieux c'est. [Maths ▸ Test d'hypothèse](#test-hypothese)

## Q-Learning

algorithme RL model-free qui apprend, dans une Q-table, la valeur de chaque paire (état, action), mise à jour via l'équation de Bellman. [Modélisation ▸ Q-Learning — apprendre la valeur d'une action](#dl-rl-q-learning)

## Q-Value (Q(s,a))

estime à quel point il est bon de prendre l'action a dans l'état s — le Q-Learning choisit toujours l'action de plus haut Q. [Modélisation ▸ Q-Learning — apprendre la valeur d'une action](#dl-rl-q-learning)

## Quantization

remplace les poids d'un modèle par une précision plus faible (16-bit float, 8-bit int...) — modèle plus petit et plus rapide, perte de précision minime. [Industrialisation ▸ Compresser un modèle — Quantization & Distillation](#dl-model-compression)

## Query/Key/Value (Q/K/V)

les 3 vecteurs projetés à partir de chaque token pour calculer l'attention — query = "que cherche-t-il ?", key = "qui est-il ?", value = "quelle info apporte-t-il ?". [Modélisation ▸ Self-Attention — Query, Key, Value](#dl-transformer-attention)

## R² (coefficient de détermination)

proportion de la variance de y expliquée par le modèle. [Modélisation ▸ Métriques de régression](#ml-metrics-regression)

## RAG (Retrieval-Augmented Generation)

récupère les documents pertinents pour une question (Information Retrieval) puis les injecte dans le prompt avant génération, au lieu de fine-tuner le modèle. [Industrialisation ▸ Pourquoi le RAG — les limites d'un LLM figé](#dl-rag-why)

## Random Forest

bagging d'arbres de décision — cas particulier du Bagging optimisé spécifiquement pour les arbres. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Random Search

recherche aléatoire d'hyperparamètres dans un espace de valeurs, plus scalable que Grid Search sur un grand espace. [Modélisation ▸ Model Tuning](#ml-model-tuning)

## Recall

capacité à détecter les occurrences réelles d'une classe — à privilégier quand rater un positif coûte cher. [Modélisation ▸ Métriques de classification](#ml-metrics-classification)

## ReduceLROnPlateau

callback Keras qui réduit le learning rate quand une métrique surveillée stagne pendant plusieurs epochs — alternative/complément à un scheduler fixe. [Modélisation ▸ Early Stopping & jeu de validation](#dl-early-stopping)

## return_sequences (Keras)

argument d'une couche RNN — renvoie la sortie à CHAQUE pas de temps (au lieu du seul dernier état), nécessaire pour prédire une séquence ou empiler un autre RNN. [Modélisation ▸ Sortie d'une couche RNN](#dl-rnn-return-sequences)

## Règle du produit (chain rule, probabilités)

P(A∩B) = P(A|B)·P(B) = P(B|A)·P(A) — reste valable même si A et B ne sont PAS indépendants. [Maths ▸ Théorie des ensembles & probabilités](#ensembles-base)

## Régression

tâche de prédiction d'une quantité continue (target numérique). [Modélisation ▸ Choisir sa famille de modèle](#ml-model-selection)

## Régression linéaire (LinearRegression)

modèle de référence en régression — combine linéairement les features, solution exacte en une étape ($\hat\beta=(X^\top X)^{-1}X^\top y$), aucune régularisation par défaut. [Modélisation ▸ Régression linéaire & logistique](#ml-linear-logistic)

## Régression logistique (LogisticRegression)

modèle de référence en classification binaire — sortie = probabilité via la sigmoïde, coefficients estimés par MLE (pas de solution fermée), régularisée L2 PAR DÉFAUT (hyperparamètre C). [Modélisation ▸ Régression linéaire & logistique](#ml-linear-logistic)

## Régularisation

pénalité ajoutée à la Loss Function pour limiter la complexité du modèle et réduire l'overfitting. [Modélisation ▸ Régularisation](#ml-regularization)

## Reinforcement Learning

un agent apprend par essai-erreur à maximiser une récompense en interagissant avec un environnement — pas de label, seulement une récompense reçue après une séquence d'actions. [Modélisation ▸ Reinforcement Learning — composants & boucle](#dl-rl-foundations)

## ReLU

fonction d'activation $f(x)=\max(0,x)$, choix par défaut pour les couches cachées d'un réseau de neurones. [Modélisation ▸ Fonctions d'activation](#dl-activation)

## Ridge

régularisation L2 — rétrécit les coefficients vers 0 sans jamais les annuler. [Modélisation ▸ Régularisation](#ml-regularization)

## RLHF (Reinforcement Learning from Human Feedback)

fine-tuning dont le signal de récompense vient d'évaluations humaines — à la base des modèles "chat" grand public. [Industrialisation ▸ Adapter un LLM — Training, Fine-tuning, Grounding](#dl-llm-adapt)

## RMSE (Root Mean Squared Error)

racine du MSE — ramène l'erreur dans l'unité de la target. [Modélisation ▸ Métriques de régression](#ml-metrics-regression)

## RNN (Recurrent Neural Network)

réseau de neurones spécialisé dans les séquences temporelles, qui maintient un état interne mis à jour à chaque pas de temps. [Modélisation ▸ Pourquoi un RNN — la dimension temporelle](#dl-rnn-input-shape)

## ROC Curve

trace le compromis recall (TPR) vs taux de faux positifs (FPR) pour tous les seuils possibles. [Modélisation ▸ ROC-AUC](#ml-roc-auc)

## ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

mesure la proportion de l'information de la référence retrouvée dans le texte généré (proche d'un recall) — utilisé en résumé. [Modélisation ▸ Évaluer un LLM — BLEU, ROUGE, Perplexité](#dl-transformer-evaluation)

## SARIMA

extension d'ARIMA avec 3 hyperparamètres supplémentaires (P,D,Q)[S] pour modéliser la saisonnalité directement. [Modélisation ▸ ARMA, ARIMA & SARIMA](#ts-arima)

## Scheduler (Learning Rate)

fait décroître automatiquement le learning rate pendant l'entraînement (ex: ExponentialDecay) — grands pas au début, petits pas vers la fin. [Modélisation ▸ Hyperparamètres — learning rate, batch size, epochs](#dl-hyperparameters)

## Score-z (z-score)

nombre d'écarts-types séparant une observation de la moyenne — permet de comparer des valeurs mesurées sur des échelles différentes. [Maths ▸ Loi normale, LGN & TCL](#loi-normale)

## SGD (Stochastic Gradient Descent)

mini-batch de taille 1 — moins stable qu'un Gradient Descent classique mais beaucoup plus rapide sur les gros datasets, permet de sortir d'un minimum local. [Modélisation ▸ Variantes de la descente de gradient](#ml-solvers)

## SimpleRNN

couche récurrente la plus simple et la plus rapide à entraîner, mais à mémoire courte (vanishing gradient marqué à travers le temps). [Modélisation ▸ SimpleRNN, LSTM, GRU](#dl-rnn-zoology)

## Smoothing (NLP)

ajoute un paramètre α>0 aux fréquences de mots pour éviter les probabilités nulles en Naive Bayes, quand un mot n'a jamais été vu dans une classe. [Modélisation ▸ Naive Bayes](#nlp-naive-bayes)

## SMOTE (Synthetic Minority Oversampling Technique)

génère de nouveaux points synthétiques de la classe minoritaire par interpolation entre plus proches voisins, au lieu de dupliquer des points existants. [Modélisation ▸ Balancing](#ml-balancing-concept)

## Soft Margin (SVM)

autorise certains points à être à l'intérieur de la marge, voire du mauvais côté, moyennant une pénalité (Hinge Loss). [Modélisation ▸ SVM — marge maximale](#ml-svm-margin)

## Softmax

fonction d'activation de la dernière couche en classification multi-classe — transforme k scores en probabilités qui somment à 1. [Modélisation ▸ Fonctions d'activation](#dl-activation)

## Solver

méthode utilisée pour minimiser la Loss Function pendant `.fit()` — résolution exacte ou itérative (Gradient Descent, Newton...). [Modélisation ▸ Que fait .fit() ?](#ml-fit-hood)

## Stable Baselines3 (sb3)

librairie d'implémentations fiables d'algorithmes RL (DQN, PPO, A2C...) — entraîner un agent tient en quelques lignes (DQN, .learn(), .predict()). [Modélisation ▸ Reinforcement Learning — composants & boucle](#dl-rl-foundations)

## Stacking

entraîne des modèles DIFFÉRENTS qui capturent chacun une structure différente des données, puis agrège leurs prédictions (vote/moyenne, ou modèle final entraîné sur leurs prédictions). [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)

## Stationnarité

propriété d'une Time Series dont les caractéristiques statistiques (moyenne, variance, autocorrélation) ne dépendent pas du temps. [Modélisation ▸ Stationnarité & test ADF](#ts-stationarity)

## Stopwords

mots très fréquents porteurs de peu d'information ("the", "is"...), souvent retirés en preprocessing NLP — sauf en analyse de sentiment. [Modélisation ▸ Text Preprocessing](#nlp-preprocessing)

## Stratify (train_test_split)

répartit chaque classe de y dans les mêmes proportions entre train et test — indispensable sur une target déséquilibrée. [Modélisation ▸ Workflow ML — Séparer train/test](#wf0-split)

## Strides (CNN)

pas de déplacement du kernel pendant une convolution — strides=2 saute un pixel sur deux et divise par ~2 la taille de la feature map en sortie. [Modélisation ▸ Hyperparamètres de la convolution](#dl-cnn-hyperparams)

## Support Vector Machine (SVM)

modèle qui cherche l'hyperplan maximisant la marge entre les classes. [Modélisation ▸ SVM — marge maximale](#ml-svm-margin)

## Support Vectors

points d'entraînement situés sur la frontière de la marge d'un SVM — ce sont eux qui déterminent l'hyperplan. [Modélisation ▸ SVM — marge maximale](#ml-svm-margin)

## Système linéaire (Xθ=y)

système de n équations à n inconnues résolu par inversion de matrice (θ=X⁻¹y) — quand il y a plus d'observations que d'inconnues (surdéterminé), plus de solution exacte : c'est le problème que la régression linéaire (OLS) résout par approximation. [Maths ▸ Résoudre un système linéaire par inversion de matrice](#systeme-lineaire-matriciel)

## t-test

test statistique comparant une moyenne observée à une hypothèse, adapté aux petits échantillons. [Maths ▸ t-test](#t-test)

## T5 (Text-to-Text Transfer Transformer)

Transformer encoder-decoder qui traite toute tâche NLP comme une transformation texte→texte (traduction, résumé, classification...). [Modélisation ▸ Encoder-only, Decoder-only, Encoder-Decoder](#dl-transformer-families)

## Temperature (génération)

contrôle le hasard du choix du prochain token d'un LLM — basse = déterministe/répétitif, haute = créatif/aléatoire. [Modélisation ▸ Contrôler la génération — Temperature, Top-k, Top-p](#dl-transformer-generation-params)

## TensorBoard

interface de suivi/comparaison d'entraînements en direct, à partir de logs écrits dans un dossier — via un callback Keras ([Modélisation ▸ Early Stopping & jeu de validation](#dl-early-stopping)) ou le paramètre tensorboard_log d'un modèle Stable Baselines3 ([Modélisation ▸ Reinforcement Learning — composants & boucle](#dl-rl-foundations)).

## TensorFlow

librairie de calcul sur tensors développée par Google, sur laquelle Keras s'appuie — à utiliser (fonctions `tf.*`) à la place de Numpy/Pandas dans toute fonction exécutée à l'intérieur du graphe Keras. [Modélisation ▸ Pourquoi tf.* et pas Numpy/Pandas](#dl-tf-ops-required)

## TextVectorization

couche Keras qui combine Tokenizer + pad_sequences en une seule étape intégrée au modèle — même logique que Normalization pour du numérique. [Modélisation ▸ Tokenization — du texte aux entiers](#dl-tokenization)

## Tf-idf

pondère le comptage Bag-of-Words par l'inverse document frequency, pour donner plus de poids aux mots rares dans le corpus. [Modélisation ▸ Vectorizing](#nlp-vectorizing)

## tf.data.Dataset

objet Keras qui charge un gros dataset (ex: images) batch par batch, sans tout mettre en RAM d'un coup — se passe directement à model.fit(ds, ...). [Modélisation ▸ Pourquoi tf.* et pas Numpy/Pandas dans un modèle Keras](#dl-tf-ops-required)

## Théorème Central Limite (TCL)

la moyenne d'échantillons tend vers une loi normale quand la taille d'échantillon augmente, quelle que soit la distribution d'origine. [Maths ▸ Loi normale, LGN & TCL](#loi-normale)

## Time Series

suite d'observations prises à intervalles de temps réguliers — deux objectifs : comprendre (décomposer) ou prévoir (forecaster). [Modélisation ▸ Modèles ▸ Time Series ▸ Décomposition](#ts-decomposition)

## Tokenizer (Keras)

construit un dictionnaire mot→entier à partir d'un corpus (`fit_on_texts`), puis convertit des phrases en séquences d'entiers (`texts_to_sequences`). [Modélisation ▸ Tokenization — du texte aux entiers](#dl-tokenization)

## Tool Calling (Function Calling)

traduit une requête en langage naturel en appel de fonction avec les bons arguments — le LLM identifie QUOI appeler, il n'exécute rien lui-même. [Industrialisation ▸ Tool Calling (Function Calling)](#dl-tool-calling)

## Top-k / Top-p

limitent les tokens candidats à la génération suivante — Top-k = les k plus probables ; Top-p (nucleus sampling) = les plus probables jusqu'à cumuler une probabilité p. [Modélisation ▸ Contrôler la génération — Temperature, Top-k, Top-p](#dl-transformer-generation-params)

## TPU (Tensor Processing Unit)

accélérateur de calcul propriétaire Google, spécifique à GCP, optimisé pour le calcul matriciel massif du Deep Learning (surtout TensorFlow/JAX) — alternative au GPU, écosystème logiciel plus restreint. [Industrialisation ▸ GCP](#infra-cloud-gcp)

## Train/Test Split

séparation des données en un ensemble d'entraînement et un ensemble de test, pour évaluer la capacité de généralisation. [Modélisation ▸ Workflow ML — Séparer train/test](#wf0-split)

## Transfer Learning

réutilise les couches de convolution d'un modèle pré-entraîné (freezées) pour un nouveau problème, en ne ré-entraînant que de nouvelles couches Dense adaptées à la tâche. [Modélisation ▸ Architecture typique & Transfer Learning](#dl-cnn-transfer-learning)

## Transformer

architecture qui traite toute une séquence EN PARALLÈLE via un mécanisme d'attention, sans état interne séquentiel — à la base des LLM actuels. [Modélisation ▸ Pourquoi remplacer le RNN — les limites du traitement séquentiel](#dl-transformer-why)

## TruncatedSVD

réduction de dimension équivalente à PCA mais SANS centrer les données — utilisable directement sur une matrice creuse (comptage de mots, notes utilisateurs). [Modélisation ▸ Systèmes de recommandation](#ml-recommender-systems)

## Underfitting (sous-apprentissage)

le modèle est trop simple pour capter les patterns des données — scores train ET test bas. [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## Universal Approximation Theorem

un réseau dense avec une seule couche cachée peut en théorie approximer n'importe quelle fonction continue — ne garantit PAS qu'on puisse facilement trouver ces paramètres optimaux. [Modélisation ▸ Entraînement — loss & optimizer](#dl-training-loss-optim)

## Vanishing Gradient

lors de la backpropagation, le gradient rétrécit à mesure qu'il remonte vers les premières couches — celles-ci apprennent donc plus lentement que les dernières. [Modélisation ▸ Forward & Backward Propagation](#dl-backpropagation)

## Variable aléatoire

formalise le passage d'une issue qualitative (ex: "pile") à une valeur numérique manipulable (ex: 1). [Maths ▸ Variable aléatoire](#variable-aleatoire)

## Variance

sensibilité du modèle au bruit des données d'entraînement — une variance élevée signale un modèle trop complexe (overfitting). [Modélisation ▸ Bias/Variance tradeoff](#ml-bias-variance)

## Variance (dispersion statistique)

mesure la dispersion des données autour de la moyenne, en unités au carré — à ne pas confondre avec la Variance du Bias/Variance tradeoff (overfitting d'un modèle). [Maths ▸ Statistiques descriptives](#stats-descriptives)

## Vector Database

base de données spécialisée qui stocke des embeddings (vecteurs) et leurs métadonnées, interrogeable par similarité — ex: Chroma. [Industrialisation ▸ Pipeline RAG — Embedding, Vector Database, Retrieval](#dl-rag-pipeline)

## Vectorizing (NLP)

conversion de texte préprocessé en représentation numérique (Bag-of-Words, Tf-idf...), seule forme exploitable par un modèle ML. [Modélisation ▸ Vectorizing](#nlp-vectorizing)

## VIF (Variance Inflation Factor)

mesure de multicolinéarité entre features, détecte les redondances qu'une simple matrice de corrélation ne voit pas. [Maths ▸ Multicolinéarité — VIF](#ml-multicollinearity)

## Word2Vec

entraîne un embedding indépendant de la tâche, en prédisant un mot à partir de ses voisins (la fenêtre) — rapide à entraîner, à privilégier sur un petit corpus. [Modélisation ▸ Embedding indépendant de la tâche — Word2Vec](#dl-nlp-word2vec)

## XGBoost

implémentation dédiée et très optimisée du gradient boosting, avec early stopping via un jeu de validation dédié. [Modélisation ▸ Ensemble Methods](#ml-ensemble-methods)
