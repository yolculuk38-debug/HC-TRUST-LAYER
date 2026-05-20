from datetime import datetime, timezone
from typing import Dict, Optional

from .trust_engine import TrustResult


FORMAT_VERSION = "hc-trust-result-v1-experimental"


def format_trust_result(
    record_id: str,
    trust_result: TrustResult,
    *,
    verification_id: Optional[str] = None,
    verified_at: Optional[str] = None,
) -> Dict:
    """Format a TrustResult into an API-ready HC:// verification response."""

    if not record_id:
        raise ValueError("record_id is required")

    timestamp = verified_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    return {
        "format_version": FORMAT_VERSION,
        "verification_id": verification_id or f"VR-{record_id}",
        "record_id": record_id,
        "trust_score": trust_result.score,
        "trust_level": trust_result.level,
        "indicators": list(trust_result.indicators),
        "verified_at": timestamp,
        "experimental": True,
    }
