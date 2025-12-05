# tools/summary_tool.py
import requests
from typing import List, Dict

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  # change if using another model

def summarize_findings(findings: List[Dict]) -> str:
    """
    Compose a prompt that asks the local LLM to summarize validation findings.
    """
    prompt_lines = ["You are an assistant that summarizes validation findings."]
    prompt_lines.append("Summarize the following findings:\n")
    for i, f in enumerate(findings, 1):
        prompt_lines.append(f"{i}. {f}")
    prompt = "\n".join(prompt_lines)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "max_tokens": 400,
        "temperature": 0.1
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        if "text" in data:
            return data["text"]
        elif "content" in data:
            return data["content"]

        return str(data)
    except Exception as e:
        return f"LLM summarization failed: {e}"
