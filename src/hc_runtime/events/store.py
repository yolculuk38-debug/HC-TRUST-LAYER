"""Append-only advisory runtime event store for HC:// reference runtime flows."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from hc_runtime.redaction import redact_public_payload, redact_secret_like_text


@dataclass(slots=True)
class RuntimeEventStore:
    """Lightweight append-only in-memory event storage with public-safe payloads."""

    _events: list[dict[str, Any]] = field(default_factory=list)

    def append_runtime_event(
        self,
        *,
        event_type: str,
        record_id: str,
        details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        event = {
            "event_type": event_type,
            "record_id": redact_secret_like_text(record_id),
            "occurred_at": datetime.now(tz=timezone.utc).isoformat(),
            "advisory_only": True,
            "public_safe": True,
            "details": redact_public_payload(details or {}),
        }
        self._events.append(event)
        return event

    def append_trust_transition(self, *, record_id: str, trust_state: str, warnings: list[str]) -> dict[str, Any]:
        return self.append_runtime_event(
            event_type="trust_state_transition",
            record_id=record_id,
            details={"trust_state": trust_state, "warnings": warnings},
        )

    def append_continuity_checkpoint(self, *, record_id: str, continuity_ok: bool, warnings: list[str]) -> dict[str, Any]:
        return self.append_runtime_event(
            event_type="continuity_checkpoint",
            record_id=record_id,
            details={"continuity_ok": continuity_ok, "warnings": warnings},
        )

    def append_replay_warning(self, *, record_id: str, reason: str) -> dict[str, Any]:
        return self.append_runtime_event(
            event_type="replay_warning",
            record_id=record_id,
            details={"reason": reason},
        )

    def history(self, record_id: str) -> list[dict[str, Any]]:
        return [event for event in self._events if event["record_id"] == record_id]
