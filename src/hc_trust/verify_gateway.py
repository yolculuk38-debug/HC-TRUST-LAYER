from typing import Dict

from .api_schema import to_api_response
from .result_formatter import format_trust_result
from .trust_engine import ExperimentalTrustEngine


def build_verify_response(record_id: str, evidence: dict) -> Dict:
    """Build a single HC:// API-ready verification response from trust evidence."""

    if not isinstance(record_id, str) or not record_id:
        raise ValueError("record_id must be a non-empty string")

    if not isinstance(evidence, dict):
        raise ValueError("evidence must be a dict")

    engine = ExperimentalTrustEngine()
    trust_result = engine.calculate(evidence)
    formatted_result = format_trust_result(record_id, trust_result)
    return to_api_response(formatted_result)
