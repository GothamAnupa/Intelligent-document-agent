# retriever/embedder.py
from langchain_community.embeddings import SentenceTransformerEmbeddings

def get_embeddings(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    return SentenceTransformerEmbeddings(model_name=model_name)
