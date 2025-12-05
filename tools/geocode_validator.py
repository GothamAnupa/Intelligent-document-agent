# tools/geocode_validator.py
from typing import Dict, Any

def validate_geocode_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate a single row's geocode fields.
    row expected to have 'latitude' and 'longitude' keys (floats or strings).
    Returns dictionary with results.
    """
    results = {"valid": True, "errors": []}
    try:
        lat = float(row.get("latitude", None))
        lon = float(row.get("longitude", None))
    except (TypeError, ValueError):
        results["valid"] = False
        results["errors"].append("invalid_latlon_format")
        return results

    # Basic range checks
    if not (-90 <= lat <= 90):
        results["valid"] = False
        results["errors"].append("latitude_out_of_range")
    if not (-180 <= lon <= 180):
        results["valid"] = False
        results["errors"].append("longitude_out_of_range")

    # Check for suspicious zero coordinates
    if abs(lat) < 1e-6 and abs(lon) < 1e-6:
        results["valid"] = False
        results["errors"].append("suspicious_zero_coordinates")

    return results
