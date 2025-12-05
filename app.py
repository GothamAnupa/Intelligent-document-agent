# app.py
import os
import json
from retriever.vector_store import create_vectorstore_from_docs, load_vectorstore

# -------------------------------
# Mock validation functions
# -------------------------------
# Mock validation functions
def check_row_quality(row):
    return {"ok": False, "issues": ["Mock issue detected"]}

def validate_geocode_row(row):
    return {"valid": False, "errors": ["Mock geocode error"]}


def summarize_findings(findings):
    return f"Summary: {len(findings)} issues found"

# -------------------------------
# Validation pipeline
# -------------------------------
def run_validation_pipeline(sample_rows: list):
    findings = []
    for r in sample_rows:
        dq = check_row_quality(r)
        g = validate_geocode_row(r)

        if not dq.get("ok", True):
            findings.append(f"Row {r['id']}: Data issues - {dq.get('issues')}")
        if not g.get("valid", True):
            findings.append(f"Row {r['id']}: Geocode errors - {g.get('errors')}")

    summary = summarize_findings(findings)
    return {"findings": findings, "summary": summary}

# -------------------------------
# Demo function
# -------------------------------
def demo():
    print("Demo started!")

    index_path = "faiss_index"

    # Check if vectorstore exists
    if not os.path.exists(index_path):
        pdfs = []
        docs_folder = "docs"
        if os.path.exists(docs_folder):
            # Only include PDFs that are not empty
            for f in os.listdir(docs_folder):
                if f.endswith(".pdf"):
                    path = os.path.join(docs_folder, f)
                    if os.path.getsize(path) > 0:
                        pdfs.append(path)
                    else:
                        print(f"Skipping empty PDF: {f}")

        if pdfs:
            print(f"Creating vectorstore from PDFs: {pdfs}")
            create_vectorstore_from_docs(pdfs, index_path)
        else:
            print("No valid PDFs found. Skipping vectorstore creation.")

    # Sample rows for validation
    sample_rows = [
        {"id": 1, "address": "12 Baker St", "city": "London", "postal_code": "NW1", "latitude": "51.5237", "longitude": "-0.1585"},
        {"id": 2, "address": "", "city": "Hyderabad", "postal_code": "500081", "latitude": "17.3850", "longitude": "78.4867"},
        {"id": 3, "address": "Unknown", "city": "Nowhere", "postal_code": "abc", "latitude": "200", "longitude": "400"},
        {"id": 4, "address": "Null Island", "city": "Ocean", "postal_code": "00000", "latitude": "0", "longitude": "0"},
    ]

    result = run_validation_pipeline(sample_rows)
    print("\nFindings:")
    print(json.dumps(result["findings"], indent=2))
    print("\nSummary:")
    print(result["summary"])


if __name__ == "__main__":
    demo()

