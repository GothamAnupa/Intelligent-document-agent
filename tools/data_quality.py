# tools/data_quality.py
from typing import Dict, Any, List

def check_row_quality(row: Dict[str, Any], required_fields: List[str]=None) -> Dict[str,Any]:
    if required_fields is None:
        required_fields = ["address", "city", "postal_code", "latitude", "longitude"]

    issues = []
    for f in required_fields:
        val = row.get(f, None)
        if val is None or (isinstance(val, str) and val.strip() == ""):
            issues.append(f"missing_{f}")

    # Postal code format validation
    postal = row.get("postal_code", "")
    if postal and not str(postal).strip().isdigit():
        issues.append("invalid_postal_format")

    return {"row_id": row.get("id"), "issues": issues, "ok": len(issues)==0}
