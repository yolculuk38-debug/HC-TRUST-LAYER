"""HC:// realtime verification session core."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any

REALTIME_VERIFICATION_VERSION = "HC-REALTIME-VERIFICATION-V1"
SESSION_DURATION_MINUTES = 15


def _utc_now() -> datetime:
    return datetime.now(UTC).replace(microsecond=0)


def create_verification_session(
    *,
    session_id: str,
    record_id: str,
    validator_node_id: str,
) -> dict[str, Any]:
    created = _utc_now()
    expires = created + timedelta(minutes=SESSION_DURATION_MINUTES)

    return {
        "realtime_verification_version": REALTIME_VERIFICATION_VERSION,
        "session_id": session_id.strip(),
        "record_id": record_id.strip(),
        "validator_node_id": validator_node_id.strip(),
        "created_at": created.isoformat().replace("+00:00", "Z"),
        "expires_at": expires.isoformat().replace("+00:00", "Z"),
        "status": "ACTIVE",
    }


def is_session_active(session: dict[str, Any]) -> bool:
    return session.get("status") == "ACTIVE"
