---
title: GCP
subgroup: Cloud
---

:::category Données & Analytics {#cat-gcp-data}
stocker, interroger et gouverner la donnée EN AMONT d'un modèle.
:::

:::compare
- **BigQuery** : data warehouse serverless interrogé en SQL — la source de données de référence sur GCP, à des volumes que Pandas ne gère plus — [doc officielle](https://cloud.google.com/bigquery/docs)
- **BigQuery ML** : entraîne un modèle ML DIRECTEMENT en SQL sur des données déjà dans BigQuery (régression, classification, clustering, forecasting) — pas d'export vers un notebook, pratique pour un premier modèle rapide — [doc officielle](https://cloud.google.com/bigquery/docs/bqml-introduction)
- **Dataproc** : clusters Spark/Hadoop managés — traitement big data PAR LOTS (ETL massif, feature engineering distribué) quand BigQuery seul ne suffit pas — [doc officielle](https://cloud.google.com/dataproc/docs)
- **Dataflow** : service managé Apache Beam — pipelines ETL en streaming ET par lots (contrairement à Dataproc, orienté Spark/Hadoop par lots) ; alimente typiquement un pipeline de features en temps réel — le service le plus central du data engineering sur GCP — [doc officielle](https://cloud.google.com/dataflow/docs)
- **Pub/Sub** : messagerie asynchrone managée, encaisse des événements à très grande échelle — brique d'ENTRÉE standard d'un pipeline streaming (Pub/Sub → Dataflow → BigQuery est l'architecture de référence GCP) — [doc officielle](https://cloud.google.com/pubsub/docs)
- **Cloud Data Fusion** : ETL no-code (interface visuelle drag & drop) — alternative à Dataflow/Dataproc pour des analystes qui ne codent pas ; a remplacé Dataprep (retiré) comme outil no-code de référence — [doc officielle](https://cloud.google.com/data-fusion/docs)
- **BigLake** : couche de stockage unifiée entre Cloud Storage (data lake, fichiers bruts) et BigQuery (entrepôt) — interroge des fichiers d'un data lake avec les mêmes performances/gouvernance qu'une table BigQuery, sans dupliquer la donnée (renommé **Lakehouse for Apache Iceberg** en avril 2026, API/CLI encore sous le nom BigLake) — [doc officielle](https://cloud.google.com/biglake)
- **Dataplex** : gouvernance de données unifiée — catalogue/métadonnées, qualité et lignée des données à travers BigQuery ET les data lakes (via BigLake) ; répond à "d'où vient cette donnée, est-elle fiable" plutôt qu'à un besoin de calcul (rebrandé **Knowledge Catalog** mi-2026 — l'exam guide et une partie de l'interface disent encore « Dataplex »/« policy tag », le nouveau nom pour ce dernier étant **Aspect**) — [doc officielle](https://cloud.google.com/dataplex/docs)
:::

> [!TIP]
> 👉 **[Cloud Composer](https://cloud.google.com/composer/docs)** (Airflow managé) orchestre ces briques entre elles (ex: Dataproc → BigQuery → déclenchement d'un ré-entraînement) — l'équivalent GCP d'un Airflow auto-hébergé.

:::compare
- **Analytics Hub** : partage/monétisation de datasets BigQuery en interne ou avec des partenaires externes — équivalent GCP d'un data marketplace, à ne pas confondre avec Dataplex/Knowledge Catalog (gouvernance INTERNE) — [doc officielle](https://cloud.google.com/bigquery/docs/analytics-hub-introduction)
- **Looker** : suite BI payante — modélise/abstrait des sources hétérogènes (LookML) derrière une interface unique pour l'analyste, partage de rapports en interne/externe à grande échelle — [doc officielle](https://cloud.google.com/looker/docs)
- **Data Studio** : outil de dashboard GRATUIT branché directement sur BigQuery/Sheets — plus léger que Looker (pas d'abstraction multi-sources) ; brièvement rebrandé "Looker Studio" (~2021-2026) puis re-rebrandé **Data Studio** mi-2026 — [doc officielle](https://cloud.google.com/looker-studio)
:::

> [!TIP]
> 👉 **Connected Sheets** connecte directement Google Sheets à BigQuery sans écrire de SQL — la solution la plus légère pour une équipe déjà à l'aise avec les tableurs. Les **éditions BigQuery** (Standard/Enterprise/Enterprise Plus) conditionnent certaines fonctionnalités : Standard (la moins chère) ne supporte ni BigQuery ML, ni les vues matérialisées en écriture, ni le chiffrement CMEK.

---

:::category Plateforme MLOps & Compute {#cat-gcp-mlops}
entraîner, déployer et monitorer VOS modèles.
:::

:::compare
- **Gemini Enterprise Agent Platform (ex-Vertex AI)** : plateforme managée qui centralise tout le cycle de vie ML — training (custom ou **AutoML**, sans code), hosting/serving, Model Registry, pipelines — renommée depuis **Vertex AI** lors du rebranding "agentic" de Google Cloud Next 2026 (avril 2026) ; les endpoints d'API existants restent inchangés, "Vertex AI" reste donc le nom que l'on croise dans la plupart des tutoriels/docs pas encore mis à jour — [doc officielle](https://cloud.google.com/vertex-ai/docs)
- **Vertex AI Workbench / Colab Enterprise** : notebooks Jupyter managés, intégrés nativement à BigQuery/Cloud Storage — le poste de travail du Data Scientist sur GCP — [doc Workbench](https://cloud.google.com/vertex-ai/docs/workbench/introduction) · [doc Colab Enterprise](https://cloud.google.com/colab/docs)
:::

👉 Plusieurs niveaux d'accès au calcul GPU/TPU, du plus géré au plus bas niveau :

:::compare
- **Compute Engine + GPU** : VM classique avec un GPU NVIDIA attaché — accès généraliste, pas spécifique à l'IA — [doc officielle](https://cloud.google.com/compute/docs)
- **Cloud TPU VMs** : accès DIRECT à la machine hôte d'un TPU — exécute TensorFlow/PyTorch/JAX sans couche d'orchestration intermédiaire — [doc officielle](https://cloud.google.com/tpu/docs)
- **GKE (Google Kubernetes Engine)** : déploie des TPU slices/pods (ou des GPU) DANS un cluster Kubernetes — training/inference distribué à grande échelle, pour une stack déjà orientée Kubernetes — [doc officielle](https://cloud.google.com/kubernetes-engine/docs)
:::

> [!TIP]
> 👉 Le **TPU** (Tensor Processing Unit) est spécifique à GCP (pas disponible chez les autres clouds) — accélérateur propriétaire Google pensé pour le calcul matriciel massif du Deep Learning, mais moins universel qu'un GPU (écosystème logiciel plus restreint, surtout hors TensorFlow/JAX). **[SkyPilot](https://docs.skypilot.co/en/latest/docs/)** (outil open-source, multi-cloud) simplifie le lancement de jobs sur ces différentes options d'accélérateurs (GPU comme TPU v4/v6e) sans écrire l'orchestration à la main.

:::compare
- **Vector Search** : base vectorielle managée (ScaNN) intégrée à la plateforme — équivalent GCP de Chroma/Qdrant pour un RAG (cf. [Vector Databases & recherche avancée](#aieng-rag-vectordb-strategies), page AI Engineering) — [doc officielle](https://cloud.google.com/vertex-ai/docs/vector-search/overview)
- **Vertex AI Feature Store** : feature store managé de la plateforme — équivalent GCP de Feast (cf. [Feature Store](#aieng-feature-store), page MLOps) — [doc officielle](https://cloud.google.com/vertex-ai/docs/featurestore)
:::

> [!TIP]
> 👉 **[Bigtable](https://cloud.google.com/bigtable/docs)** (NoSQL clé-valeur à très grande échelle) sert souvent de magasin de features en ligne à faible latence en complément du Feature Store managé — cas d'usage classique : séries temporelles/données éparses (fintech, IoT). Pour un job batch de plusieurs jours sans gestion d'infra (hors GPU/TPU), le service **[Batch](https://cloud.google.com/batch/docs)** est l'option la plus légère.

---

:::category Modèles & Agents {#cat-gcp-models-agents}
partir d'un modèle/agent DÉJÀ construit plutôt que de zéro.
:::

:::compare
- **Model Garden** : catalogue de 200+ modèles pré-entraînés dans la plateforme (Gemini, Claude, Llama, modèles open-source...) — parcourir et déployer un modèle en quelques clics plutôt que partir de zéro — [doc officielle](https://cloud.google.com/model-garden)
:::

> [!TIP]
> 👉 Depuis le rebranding d'avril 2026, la construction d'agents (**Agent Studio** — no-code, **[ADK](https://google.github.io/adk-docs/)** — Agent Development Kit pour du code, protocole **A2A** pour la communication inter-agents) est nativement intégrée à la plateforme ci-dessus plutôt qu'un produit séparé (ex-Agentspace) — cf. [Agents LLM](#dl-agents), page AI Engineering, pour le pattern générique.

---

:::category APIs IA pré-entraînées {#cat-gcp-apis}
appeler un modèle DÉJÀ entraîné par Google pour une tâche standard (perception).
:::

:::compare
- **Document AI** : OCR + extraction structurée de documents (factures, formulaires, contrats) — parsing spécialisé, au-delà d'un OCR générique — [doc officielle](https://cloud.google.com/document-ai/docs)
- **Speech-to-Text** : reconnaissance vocale managée (audio → texte) — [doc officielle](https://cloud.google.com/speech-to-text/docs)
- **Vision AI** : vision par ordinateur managée — labellisation d'image, détection d'objets, OCR sur image — [doc officielle](https://cloud.google.com/vision/docs)
:::

> [!TIP]
> 👉 Document AI/Speech-to-Text/Vision AI sont des modèles DÉJÀ entraînés par Google, appelés via API — pas de training/fine-tuning à faire, à l'opposé de la plateforme MLOps ci-dessus (qui entraîne/héberge VOS modèles). Bon réflexe : les essayer en premier pour un besoin standard (facture, image, audio) avant d'envisager d'entraîner un modèle custom.
