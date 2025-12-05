# retriever/vector_store.py
import os
from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from retriever.embedder import get_embeddings
import pdfplumber

def load_text_from_pdf(path: str) -> str:
    """Read text from a PDF file."""
    print("Reading PDF:", path)
    with pdfplumber.open(path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def create_vectorstore_from_docs(doc_paths: List[str], index_path: str = "faiss_index", embed_model: str = None) -> FAISS:
    """Create a FAISS vectorstore from PDF documents."""
    texts = []
    metadatas = []

    for p in doc_paths:
        text = load_text_from_pdf(p)
        texts.append(text)
        metadatas.append({"source": os.path.basename(p)})

    emb = get_embeddings(model_name=embed_model) if embed_model else get_embeddings()
    docs = [Document(page_content=t, metadata=m) for t, m in zip(texts, metadatas)]
    vectorstore = FAISS.from_documents(docs, emb)
    vectorstore.save_local(index_path)
    return vectorstore

def load_vectorstore(index_path: str = "faiss_index", embed_model: str = None) -> FAISS:
    """Load an existing FAISS vectorstore."""
    emb = get_embeddings(model_name=embed_model) if embed_model else get_embeddings()
    return FAISS.load_local(index_path, emb)
