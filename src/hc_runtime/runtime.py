"""Advisory-only HC:// runtime service components for minimal operational flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any


class TrustState(StrEnum):
    """Advisory trust-state values for the reference runtime."""

    ADVISORY = "ADVISORY"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    DEGRADED = "DEGRADED"
    UNRESOLVED = "UNRESOLVED"


@dataclass(slots=True)
class RuntimeEventStore:
    """Append-only in-memory runtime event storage placeholder."""

    _events: list[dict[str, Any]] = field(default_factory=list)

    def append_event(self, *, event_type: str, record_id: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
        event = {
            "event_type": event_type,
            "record_id": record_id,
            "occurred_at": datetime.now(tz=timezone.utc).isoformat(),
            "details": details or {},
        }
        self._events.append(event)
        return event

    def append_trust_state_transition(self, *, record_id: str, trust_state: str, warnings: list[str]) -> dict[str, Any]:
        return self.append_event(
            event_type="trust_state_transition",
            record_id=record_id,
            details={"trust_state": trust_state, "warnings": warnings},
        )

    def append_continuity_checkpoint(self, *, record_id: str, continuity_ok: bool) -> dict[str, Any]:
        return self.append_event(
            event_type="continuity_checkpoint",
            record_id=record_id,
            details={"continuity_ok": continuity_ok},
        )

    def append_replay_warning(self, *, record_id: str, reason: str) -> dict[str, Any]:
        return self.append_event(
            event_type="replay_warning",
            record_id=record_id,
            details={"reason": reason},
        )

    def history(self, record_id: str) -> list[dict[str, Any]]:
        return [event for event in self._events if event["record_id"] == record_id]


class ValidatorPipeline:
    """Validator runtime pipeline hooks for advisory-only verification flow."""

    def run(self, *, record_id: str, qr_input: str) -> dict[str, Any]:
        schema_result = self._schema_validation_hook(qr_input=qr_input)
        hash_result = self._hash_verification_hook(qr_input=qr_input)
        trust_assignment = self._trust_state_assignment_hook(schema_result=schema_result, hash_result=hash_result)
        escalation_result = self._escalation_routing_hook(warnings=trust_assignment["warnings"])

        return {
            "record_id": record_id,
            "schema_result": schema_result,
            "hash_result": hash_result,
            "trust_assignment": trust_assignment,
            "escalation": escalation_result,
        }

    def _schema_validation_hook(self, *, qr_input: str) -> dict[str, Any]:
        return {"checked": True, "placeholder": True, "valid": bool(qr_input.strip())}

    def _hash_verification_hook(self, *, qr_input: str) -> dict[str, Any]:
        hash_verified = "hash:" in qr_input.lower()
        return {"checked": True, "placeholder": True, "hash_verified": hash_verified}

    def _trust_state_assignment_hook(self, *, schema_result: dict[str, Any], hash_result: dict[str, Any]) -> dict[str, Any]:
        warnings: list[str] = []
        if not schema_result["valid"]:
            warnings.append("Schema validation placeholder flagged invalid QR input.")
        if not hash_result["hash_verified"]:
            warnings.append("Hash verification placeholder could not confirm QR input hash marker.")
        return {"warnings": warnings}

    def _escalation_routing_hook(self, *, warnings: list[str]) -> dict[str, Any]:
        return {
            "route": "human-supervised-validation" if warnings else "none",
            "required": bool(warnings),
            "placeholder": True,
        }


class TrustStateDecisionEngine:
    """Minimal advisory trust-state classifier and warning generator."""

    def classify(self, pipeline_result: dict[str, Any]) -> tuple[TrustState, list[str]]:
        warnings = list(pipeline_result["trust_assignment"]["warnings"])
        schema_valid = pipeline_result["schema_result"]["valid"]
        hash_verified = pipeline_result["hash_result"]["hash_verified"]

        if not schema_valid:
            state = TrustState.UNRESOLVED
        elif not hash_verified:
            state = TrustState.REVIEW_REQUIRED
        elif "degraded" in pipeline_result["record_id"].lower():
            state = TrustState.DEGRADED
            warnings.append("Runtime is operating in advisory degraded placeholder mode for this record.")
        else:
            state = TrustState.ADVISORY

        if state is not TrustState.ADVISORY:
            warnings.append("Human-supervised validation is required before trust interpretation.")

        return state, self.public_safe_warnings(warnings)

    def public_safe_warnings(self, warnings: list[str]) -> list[str]:
        return [warning for warning in warnings if "private" not in warning.lower()]
