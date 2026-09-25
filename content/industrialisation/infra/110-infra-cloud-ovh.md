---
title: OVHcloud
subgroup: Cloud
---

Contrairement aux 3 hyperscalers ci-dessus (GCP/AWS/Azure), **OVHcloud** est un acteur européen (français), avec un catalogue IA/ML plus resserré — équivalences GCP indiquées quand elles existent, sinon signalé explicitement.

:::category Données & Analytics {#cat-ovh-data}
stocker, interroger et gouverner la donnée EN AMONT d'un modèle.
:::

:::compare
- **Data Platform** : lakehouse construit sur Object Storage + Apache Iceberg + Trino (stack open-source) — équivalent PARTIEL de BigQuery/BigLake, sur une base ouverte plutôt qu'un moteur propriétaire — [doc officielle](https://docs.ovhcloud.com/en/guides/public-cloud/data-platform/general-what-is-the-data-platform)
- **Analytics Manager** : requêtage SQL + dashboards (compatible Power BI/Tableau) sur le Data Platform — équivalent PARTIEL de BigQuery côté requêtage/visualisation — [doc officielle](https://www.ovhcloud.com/en/public-cloud/analytics-manager/)
- **Data Processing** : traitement Apache Spark managé — équivalent OVHcloud de Dataproc/EMR — [doc officielle](https://www.ovhcloud.com/en/public-cloud/data-processing-engine/)
- **Managed Databases** : catalogue de bases managées (Kafka, PostgreSQL, MySQL, Cassandra, OpenSearch...) — briques individuelles, pas un service de gouvernance unifié comme Dataplex/Lake Formation — [doc officielle](https://www.ovhcloud.com/en/public-cloud/databases/)
:::

> [!TIP]
> 👉 Pas d'équivalent trouvé chez OVHcloud pour **BigQuery ML** (entraîner un modèle directement en SQL) ni pour **Cloud Composer/MWAA** (orchestration de pipelines managée) — à combiner soi-même (Airflow auto-hébergé, ou orchestration via le Managed Kubernetes ci-dessous).

---

:::category Plateforme MLOps & Compute {#cat-ovh-mlops}
entraîner, déployer et monitorer VOS modèles.
:::

:::compare
- **AI Training** : entraîne un modèle sur un ou plusieurs nœuds CPU/GPU (PyTorch, TensorFlow, Scikit-learn) — équivalent PARTIEL (côté training) de la plateforme MLOps de GCP/AWS — [doc officielle](https://www.ovhcloud.com/en/public-cloud/ai-training/)
- **AI Deploy** : déploie un modèle en production avec un point d'accès API — équivalent PARTIEL (côté hosting/serving) de la plateforme MLOps de GCP/AWS — [doc officielle](https://www.ovhcloud.com/en/public-cloud/ai-deploy/)
- **AI Notebooks** : notebooks Jupyter/VS Code managés, démarrage instantané — équivalent OVHcloud de Vertex AI Workbench/SageMaker Studio — [doc officielle](https://www.ovhcloud.com/en/public-cloud/ai-notebooks/)
:::

👉 Compute :

:::compare
- **Public Cloud — instances GPU** : instances GPU NVIDIA à la demande, généralement moins chères que chez les hyperscalers américains — équivalent OVHcloud de Compute Engine/EC2 + GPU — [doc officielle](https://www.ovhcloud.com/en/public-cloud/gpu/)
- **Managed Kubernetes Service (MKS)** : cluster Kubernetes managé — équivalent OVHcloud de GKE/EKS, utilisé par ex. pour déployer un moteur d'inférence (vLLM) à grande échelle — [doc officielle](https://www.ovhcloud.com/en/public-cloud/kubernetes/)
:::

> [!TIP]
> 👉 Pas d'accélérateur IA propriétaire chez OVHcloud (aucun équivalent au TPU/Trainium-Inferentia) — uniquement du GPU NVIDIA. Pas d'équivalent trouvé non plus pour un **Feature Store** managé (cf. Feast en open-source, [Feature Store](#aieng-feature-store), page MLOps, pour combler ce manque soi-même).

:::compare
- **Managed OpenSearch** : moteur vectoriel managé — équivalent OVHcloud de Vector Search/OpenSearch Service, pour un RAG (cf. [Vector Databases & recherche avancée](#aieng-rag-vectordb-strategies), page AI Engineering) — [doc officielle](https://docs.ovhcloud.com/en/guides/public-cloud/databases/opensearch-getting-started)
:::

---

:::category Modèles & Agents {#cat-ovh-models-agents}
partir d'un modèle/agent DÉJÀ construit plutôt que de zéro.
:::

:::compare
- **AI Endpoints** : catalogue de 40+ modèles open-source managés, servis en serverless (Llama, Mistral, Qwen, DeepSeek, Whisper...) — équivalent OVHcloud de Model Garden/Bedrock — [doc officielle](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/)
:::

> [!TIP]
> 👉 Pas d'équivalent trouvé chez OVHcloud pour la construction d'agents (pas de pendant à Agent Studio/ADK/Bedrock AgentCore) ni pour un RAG managé packagé (pas de pendant à Bedrock Knowledge Bases) — à construire soi-même sur AI Endpoints + AI Deploy avec un framework comme LangGraph (cf. [Agents LLM](#dl-agents), page AI Engineering).

---

:::category APIs IA pré-entraînées {#cat-ovh-apis}
appeler un modèle DÉJÀ entraîné pour une tâche standard (perception).
:::

Contrairement à GCP/AWS, OVHcloud ne propose pas de suite d'API spécialisées par tâche de perception (pas de pendant direct à Document AI/Vision AI ou Textract/Rekognition) — le même catalogue **AI Endpoints** (ci-dessus) couvre ces besoins via des modèles génériques :

:::compare
- **Speech-to-Text** : Whisper (large-v3, large-v3-turbo) disponible dans le catalogue AI Endpoints — équivalent OVHcloud de Speech-to-Text/Transcribe
- **OCR / compréhension de document** : pas de service dédié — se fait via un modèle vision-langage du catalogue (ex: Qwen 2.5 VL) plutôt qu'une API spécialisée comme Document AI/Textract
- **Vision par ordinateur (labellisation, détection d'objets)** : pas d'équivalent trouvé — même limite que l'OCR ci-dessus, à combler via un modèle vision-langage générique du catalogue
:::

> [!TIP]
> 👉 OVHcloud mise sur un catalogue UNIQUE de modèles génériques (texte, vision, audio) plutôt que sur des API spécialisées par tâche — plus simple à maintenir pour eux, mais moins clé-en-main pour un besoin de perception précis (facture, image) qu'un service dédié comme Document AI/Textract.

> [!TIP]
> 👉 L'argument différenciant d'OVHcloud n'est pas la richesse fonctionnelle mais la **souveraineté numérique** (données hébergées en Europe, hors Cloud Act américain) — pertinent pour des projets IA soumis à des contraintes réglementaires (RGPD, secteur public, santé...).
