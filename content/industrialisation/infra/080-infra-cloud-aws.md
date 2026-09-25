---
title: AWS
subgroup: Cloud
---

:::category Données & Analytics {#cat-aws-data}
stocker, interroger et gouverner la donnée EN AMONT d'un modèle.
:::

:::compare
- **Amazon Redshift** : data warehouse managé interrogé en SQL — équivalent AWS de BigQuery — [doc officielle](https://docs.aws.amazon.com/redshift/)
- **Redshift ML** : entraîne un modèle ML DIRECTEMENT en SQL sur des données déjà dans Redshift — équivalent AWS de BigQuery ML — [doc officielle](https://docs.aws.amazon.com/redshift/latest/dg/machine_learning.html)
- **Amazon Athena** : requêtage SQL serverless directement sur des fichiers S3, sans charger dans un warehouse — complète Redshift ; pas d'équivalent GCP aussi net (le plus proche : BigQuery en mode tables externes) — [doc officielle](https://docs.aws.amazon.com/athena/)
- **Amazon EMR** : clusters Spark/Hadoop managés — équivalent AWS de Dataproc — [doc officielle](https://docs.aws.amazon.com/emr/)
- **AWS Glue** : ETL managé (jobs Spark serverless) + Glue Data Catalog (métadonnées) — équivalent AWS combiné de Dataflow (ETL) et d'une partie de Dataplex (catalogue) — [doc officielle](https://docs.aws.amazon.com/glue/)
- **AWS Lake Formation** : gouvernance et permissions fines sur un data lake S3/Glue Catalog — équivalent AWS de Dataplex côté gouvernance — [doc officielle](https://docs.aws.amazon.com/lake-formation/)
:::

> [!TIP]
> 👉 **[Amazon MWAA](https://docs.aws.amazon.com/mwaa/)** (Managed Workflows for Apache Airflow) orchestre ces briques entre elles — équivalent AWS de Cloud Composer.

---

:::category Plateforme MLOps & Compute {#cat-aws-mlops}
entraîner, déployer et monitorer VOS modèles.
:::

:::compare
- **Amazon SageMaker AI** : plateforme managée qui centralise tout le cycle de vie ML — training, hosting/serving, Model Registry, pipelines — équivalent AWS de [Gemini Enterprise Agent Platform/ex-Vertex AI](#infra-cloud-gcp) ; renommée depuis "Amazon SageMaker" en décembre 2024 pour libérer ce nom (cf. ci-dessous) — [doc officielle](https://docs.aws.amazon.com/sagemaker/)
- **Amazon SageMaker (Unified Studio)** : environnement de développement UNIFIÉ qui regroupe Redshift/Athena/EMR/Glue/MWAA/Bedrock/SageMaker AI dans UNE seule interface — porte maintenant le nom "SageMaker" tout court ; pas d'équivalent GCP aussi intégré (le plus proche : BigQuery Studio, plus limité) — [doc officielle](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html)
:::

👉 Plusieurs niveaux d'accès au calcul GPU/accélérateur IA, du plus géré au plus bas niveau :

:::compare
- **EC2 + GPU** : instances à la demande avec GPU NVIDIA attaché — famille **P** (P4/P5, GPU haut de gamme A100/H100) pour l'entraînement lourd, famille **G** (G5, GPU A10G plus abordable) pour l'inférence — équivalent AWS de Compute Engine + GPU — [doc officielle](https://docs.aws.amazon.com/ec2/)
- **EC2 Trn/Inf (AWS Neuron)** : instances avec les accélérateurs propriétaires AWS — **Trainium** (entraînement, Trn) et **Inferentia** (inférence, Inf) — équivalent AWS du TPU — [doc officielle](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/what-is-neuron.html)
- **Amazon EKS** : déploie du training/inference distribué dans un cluster Kubernetes — équivalent AWS de GKE — [doc officielle](https://docs.aws.amazon.com/eks/)
:::

> [!TIP]
> 👉 Trainium/Inferentia sont une alternative moins chère au GPU NVIDIA mais, comme le TPU chez GCP, avec un écosystème logiciel plus restreint (SDK **AWS Neuron** dédié).

:::compare
- **Amazon OpenSearch Service (moteur vectoriel)** : base vectorielle managée — équivalent AWS de Vector Search, pour un RAG (cf. [Vector Databases & recherche avancée](#aieng-rag-vectordb-strategies), page AI Engineering) — [doc officielle](https://docs.aws.amazon.com/opensearch-service/)
- **SageMaker Feature Store** : feature store managé — équivalent AWS de Vertex AI Feature Store/Feast (cf. [Feature Store](#aieng-feature-store), page MLOps) — [doc officielle](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
:::

---

:::category Modèles & Agents {#cat-aws-models-agents}
partir d'un modèle/agent DÉJÀ construit plutôt que de zéro.
:::

:::compare
- **Amazon Bedrock** : catalogue de modèles pré-entraînés managés (Anthropic Claude, Meta Llama, Mistral, Amazon Nova/Titan...) — équivalent AWS de Model Garden — [doc officielle](https://docs.aws.amazon.com/bedrock/)
:::

> [!TIP]
> 👉 La construction d'agents passe par **[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/)** (équivalent AWS d'Agent Studio/ADK) et le RAG managé par **[Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)** — cf. [Agents LLM](#dl-agents), page AI Engineering, pour le pattern générique.

---

:::category APIs IA pré-entraînées {#cat-aws-apis}
appeler un modèle DÉJÀ entraîné par AWS pour une tâche standard (perception).
:::

:::compare
- **Amazon Textract** : OCR + extraction structurée de documents — équivalent AWS de Document AI — [doc officielle](https://docs.aws.amazon.com/textract/)
- **Amazon Transcribe** : reconnaissance vocale managée (audio → texte) — équivalent AWS de Speech-to-Text — [doc officielle](https://docs.aws.amazon.com/transcribe/)
- **Amazon Rekognition** : vision par ordinateur managée — équivalent AWS de Vision AI — [doc officielle](https://docs.aws.amazon.com/rekognition/)
- **Amazon Comprehend** : analyse de texte managée (sentiment, entités, classification) — pas d'équivalent listé côté GCP dans ce mémo — [doc officielle](https://docs.aws.amazon.com/comprehend/)
- **Amazon Polly** : synthèse vocale managée (texte → audio) — complément de Transcribe, pas d'équivalent listé côté GCP dans ce mémo — [doc officielle](https://docs.aws.amazon.com/polly/)
:::

> [!TIP]
> 👉 Ces 5 API sont des modèles DÉJÀ entraînés par AWS, appelés via API — pas de training/fine-tuning à faire, à l'opposé de la plateforme MLOps ci-dessus (qui entraîne/héberge VOS modèles). Bon réflexe : les essayer en premier pour un besoin standard (facture, image, audio, texte) avant d'envisager d'entraîner un modèle custom.
