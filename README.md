# Assistant RAG 100% local basé sur une bibliotheque des PDF's

## Stack Technique
- Langage: Python 3.12 (avec venv)
- LLM & Embeddings: Ollama (`llama3.2:3b` & `nomic-embed-text`)
- Base vectorielle: ChromaDB
- Interface & Tests: Streamlit, pytest, ruff, GitHub Actions

## Plan des phases
1. Ingestion et nettoyage du corpus PDF
2. Découpage (Chunking) et vectorisation (Embeddings)
3. Moteur de recherche vectorielle et génération guidée avec citations
4. Évaluation quantitative (Hit Rate, MRR, latence)
5. Interface Streamlit et CI/CD