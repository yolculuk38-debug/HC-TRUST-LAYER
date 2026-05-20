from typing import Dict


API_RESPONSE_VERSION = "hc-verify-api-v1-experimental"


REQUIRED_VERIFY_RESPONSE_FIELDS = {
    "api_version",
    "record_id",
    "verification_id",
    "trust_score",
    "trust_level",
    "indicators",
    "verified_at",
    "experimental",
}


def validate_verify_response(payload: Dict) -> bool:
    """Validate the minimal HC:// API-ready verification response shape."""

    missing = REQUIRED_VERIFY_RESPONSE_FIELDS - set(payload.keys())
    if missing:
        return False

    if payload.get("api_version") != API_RESPONSE_VERSION:
        return False

    if not isinstance(payload.get("record_id"), str) or not payload["record_id"]:
        return False

    if not isinstance(payload.get("verification_id"), str) or not payload["verification_id"]:
        return False

    if not isinstance(payload.get("trust_score"), int):
        return False

    if not 0 <= payload["trust_score"] <= 100:
        return False

    if not isinstance(payload.get("trust_level"), str) or not payload["trust_level"]:
        return False

    if not isinstance(payload.get("indicators"), list):
        return False

    if not isinstance(payload.get("verified_at"), str) or not payload["verified_at"]:
        return False

    if payload.get("experimental") is not True:
        return False

    return True


def to_api_response(payload: Dict) -> Dict:
    """Add HC:// API response metadata to a formatted trust result payload."""

    response = dict(payload)
    response["api_version"] = API_RESPONSE_VERSION
    return response
