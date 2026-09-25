---
title: Pipeline RAG avec LangChain
subgroup: RAG
type: syntax
---

## Charger un document
Syntaxe:
```
from langchain_community.document_loaders import PyPDFLoader
data = PyPDFLoader("book.pdf").**load**()
```
Résultat: découpe déjà 1 Document par page — mais des frontières de page arbitraires (souvent en plein milieu d'une phrase) ; pour un vrai découpage en chunks, cf. ligne suivante

## Découper en chunks avec chevauchement
Syntaxe:
```
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = **RecursiveCharacterTextSplitter**(chunk_size=2000, chunk_overlap=400)
chunks = splitter.**split_documents**(data)
```
Résultat: chunk_overlap = chevauchement entre chunks consécutifs, pour ne pas perdre le contexte à une frontière de coupe — le splitter essaie d'abord de couper aux frontières naturelles (paragraphes, phrases)

## Indexer les chunks dans une Vector Database
Syntaxe:
```
from langchain_chroma import Chroma
vector_db = Chroma.**from_documents**(
    documents=chunks,
    embedding=embeddings,
)
```
Résultat: embedding = un modèle d'embedding (ex: GoogleGenerativeAIEmbeddings) — calcule et stocke un vecteur par chunk ; vit en RAM, perdu à la fermeture (cf. ligne suivante pour la persistance)

## Vector Database PERSISTANTE (stockée sur disque)
Syntaxe:
```
vector_db = Chroma(
    collection_name="mes_docs",
    embedding_function=embeddings,
    **persist_directory**="./chroma_db",
)
vector_db.**add_documents**(chunks)
```
Résultat: évite de re-payer l'embedding de tous les documents à chaque redémarrage — construction en 2 temps (instancier vide, puis add_documents) plutôt que from_documents() en une fois

## Récupérer les documents les plus pertinents
Syntaxe: docs = vector_db.**similarity_search**(query, k=5)
Résultat: k = nombre de chunks retournés — cf. page Industrialisation ▸ Pipeline RAG

## Filtrer la recherche par métadonnées
Syntaxe: vector_db.similarity_search(query, k=5, **filter**={"session_date": "2026-07-06"})
Résultat: restreint la recherche par similarité aux documents dont les metadata correspondent EXACTEMENT au filtre — utile pour combiner similarité sémantique et filtre exact (date, source...)

## Réutiliser un prompt RAG déjà éprouvé
Syntaxe:
```
from langchain_classic import hub
template = hub.**pull**("rlm/rag-prompt")
prompt = template.invoke({"context": docs_content, "question": query})
```
Résultat: évite d'écrire son prompt RAG à la main (concaténation de contexte+question) — bibliothèque de prompts partagés (LangSmith Hub)
