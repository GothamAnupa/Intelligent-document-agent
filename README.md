# Intelligent Document Agent

A Python-based pipeline for validating structured data and processing documents with vector search.  
This project allows you to:

- Validate sample data rows for quality and geocode issues.
- Summarize validation findings.
- Optionally, process PDF documents into a FAISS vectorstore for similarity search (when PDFs are added).
- Run a demo pipeline without any PDFs using mock validation.

---

## Features

- **Data Validation**: Check row quality and geocode correctness.
- **Summarization**: Aggregate findings into a readable summary.
- **PDF Processing**: Convert PDFs into a searchable vectorstore (optional).
- **Flexible Demo**: Works with or without PDFs.
- **Mock Mode**: Test pipeline functionality without real PDFs or external APIs.

---

## Getting Started

### Prerequisites

- Python 3.9+
- Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Intelligent-document-agent.git
cd intelligent-document-agent

2. Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3. Install dependencies:

pip install -r requirements.txt

