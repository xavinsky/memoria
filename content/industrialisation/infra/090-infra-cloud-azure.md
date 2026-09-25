---
title: Azure
subgroup: Cloud
---

:::category Données & Analytics {#cat-azure-data}
stocker, interroger et gouverner la donnée EN AMONT d'un modèle.
:::

:::compare
- **Microsoft Fabric** : plateforme d'analytics unifiée (SaaS) — Data Warehouse, Lakehouse, Data Factory et Power BI autour d'un stockage commun (OneLake) — remplace stratégiquement **Azure Synapse Analytics** (fin de vie prévue en 2026) ; équivalent Azure de BigQuery/BigLake combinés — [doc officielle](https://learn.microsoft.com/en-us/fabric/)
- **Azure Databricks** : plateforme Spark/lakehouse managée (partenariat Microsoft-Databricks) — équivalent Azure de Dataproc/EMR, très utilisée sur Azure spécifiquement — [doc officielle](https://learn.microsoft.com/en-us/azure/databricks/)
- **Azure Data Factory** : ETL managé + orchestration de pipelines (aussi intégré à Fabric) — équivalent Azure de Dataflow/Glue ET de Cloud Composer/MWAA côté orchestration — [doc officielle](https://learn.microsoft.com/en-us/azure/data-factory/)
- **Microsoft Purview** : gouvernance de données unifiée — catalogue, qualité, lignée, intégré nativement à Fabric — équivalent Azure de Dataplex/Lake Formation — [doc officielle](https://learn.microsoft.com/en-us/purview/)
:::

> [!TIP]
> 👉 Pas d'équivalent aussi direct que **BigQuery ML** (entraîner un modèle en SQL pur) — Fabric propose plutôt des notebooks Data Science intégrés (Spark) pour ce besoin.

---

:::category Plateforme MLOps & Compute {#cat-azure-mlops}
entraîner, déployer et monitorer VOS modèles.
:::

:::compare
- **Azure Machine Learning** : plateforme managée pour entraîner/déployer/monitorer VOS modèles — training, hosting/serving, Model Registry, pipelines, notebooks intégrés (studio) — équivalent Azure de la partie "MLOps classique" de Vertex AI/SageMaker AI — [doc officielle](https://learn.microsoft.com/en-us/azure/machine-learning/)
:::

👉 Compute :

:::compare
- **VM série NC/ND (GPU)** : instances à la demande avec GPU NVIDIA attaché, dédiées au calcul IA — équivalent Azure de Compute Engine+GPU/EC2+GPU — [doc officielle](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-family)
- **AKS (Azure Kubernetes Service)** : déploie du training/inference distribué dans un cluster Kubernetes — équivalent Azure de GKE/EKS — [doc officielle](https://learn.microsoft.com/en-us/azure/aks/)
:::

> [!TIP]
> 👉 Pas d'accélérateur IA propriétaire disponible en libre-service côté Azure pour l'instant — Microsoft développe ses propres puces (**Maia**, déployées en interne pour Copilot/Microsoft Foundry) mais pas encore un SKU Azure public sélectionnable, contrairement au TPU (GCP) ou Trainium/Inferentia (AWS). Azure reste donc 100% GPU NVIDIA côté client.

:::compare
- **Azure AI Search** : moteur de recherche + base vectorielle managée — équivalent Azure de Vector Search/OpenSearch Service, pour un RAG (cf. [Vector Databases & recherche avancée](#aieng-rag-vectordb-strategies), page AI Engineering) — [doc officielle](https://learn.microsoft.com/en-us/azure/search/)
- **Azure ML managed feature store** : feature store managé de la plateforme — équivalent Azure de Vertex AI Feature Store/Feast (cf. [Feature Store](#aieng-feature-store), page MLOps) — [doc officielle](https://learn.microsoft.com/en-us/azure/machine-learning/concept-what-is-managed-feature-store)
:::

---

:::category Modèles & Agents {#cat-azure-models-agents}
partir d'un modèle/agent DÉJÀ construit plutôt que de zéro.
:::

:::compare
- **Microsoft Foundry** : plateforme pour CONSOMMER des modèles et construire des applications/agents — **Foundry Models** (catalogue de 10 000+ modèles : Azure OpenAI, Anthropic Claude, Meta, Mistral, Cohere...) + **Foundry Agent Service** (construction d'agents) — équivalent Azure de Model Garden/Bedrock ET d'Agent Studio-ADK/Bedrock AgentCore réunis ; renommée 2 fois en 1 an (Azure AI Studio → Azure AI Foundry, nov. 2024 → Microsoft Foundry, nov. 2025) — [doc officielle](https://learn.microsoft.com/en-us/azure/foundry/)
:::

> [!TIP]
> 👉 L'**[Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** reste disponible comme SKU autonome (accès direct aux modèles OpenAI avec garanties d'entreprise) — Foundry l'englobe désormais sans l'obliger à disparaître. cf. [Agents LLM](#dl-agents), page AI Engineering, pour le pattern générique agentique.

---

:::category APIs IA pré-entraînées {#cat-azure-apis}
appeler un modèle DÉJÀ entraîné par Microsoft pour une tâche standard (perception).
:::

:::compare
- **Azure AI Document Intelligence** : OCR + extraction structurée de documents (anciennement **Form Recognizer**) — équivalent Azure de Document AI/Textract — [doc officielle](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- **Azure AI Speech** : reconnaissance ET synthèse vocale managées (audio ↔ texte) — équivalent Azure de Speech-to-Text/Transcribe (+ Text-to-Speech intégré) — [doc officielle](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)
- **Azure AI Vision** : vision par ordinateur managée — équivalent Azure de Vision AI/Rekognition — [doc officielle](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- **Azure AI Language** : analyse de texte managée (sentiment, entités, classification) — équivalent Azure de Comprehend — [doc officielle](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
:::

> [!TIP]
> 👉 Ces 4 API (regroupées sous la bannière **Foundry Tools**, ex-Azure AI Services, ex-Cognitive Services) sont des modèles DÉJÀ entraînés par Microsoft, appelés via API — pas de training/fine-tuning à faire, à l'opposé de la plateforme MLOps ci-dessus. Bon réflexe : les essayer en premier pour un besoin standard (facture, image, audio, texte) avant d'envisager d'entraîner un modèle custom.
