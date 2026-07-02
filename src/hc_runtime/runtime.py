"""Advisory-only HC:// runtime service components for operational prototype flow."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Mapping

from hc_runtime.canonical_record_loader import MALFORMED_RECORD, CanonicalRecordLoader
from hc_runtime.decision_engine import TrustState, TrustStateDecisionEngine
from hc_runtime.events import RuntimeEventStore
from hc_runtime.contracts.redaction import redact_public_payload, redact_secret_like_text


class ValidatorPipeline:
    """Validator runtime pipeline hooks for advisory-only verification flow."""

    def __init__(
        self,
        *,
        canonical_records: Mapping[str, object] | None = None,
        canonical_loader: CanonicalRecordLoader | None = None,
    ) -> None:
        self._canonical_records = canonical_records
        self._canonical_loader = canonical_loader

    def run(self, *, record_id: str, qr_input: str) -> dict[str, Any]:
        bridge_result = self._canonical_bridge_hook(record_id=record_id)
        schema_result = self._schema_validation_hook(qr_input=qr_input, bridge_result=bridge_result)
        hash_result = self._hash_verification_hook(qr_input=qr_input, bridge_result=bridge_result)
        trust_assignment = self._trust_state_assignment_hook(
            schema_result=schema_result,
            hash_result=hash_result,
            bridge_result=bridge_result,
        )
        escalation_result = self._escalation_routing_hook(warnings=trust_assignment["warnings"])

        return {
            "record_id": record_id,
            "canonical_bridge": bridge_result,
            "schema_result": schema_result,
            "hash_result": hash_result,
            "trust_assignment": trust_assignment,
            "escalation": escalation_result,
        }

    def _canonical_bridge_hook(self, *, record_id: str) -> dict[str, Any]:
        warnings: list[str] = []
        result: dict[str, Any] = {
            "checked": True,
            "placeholder": True,
            "lookup_performed": self._canonical_records is not None or self._canonical_loader is not None,
            "found": False,
            "record_id_match": False,
            "malformed": False,
            "schema_valid": False,
            "content_hash_present": False,
            "hash_verified": False,
            "lookup_status": "not_configured",
            "warnings": warnings,
        }

        if self._canonical_records is None and self._canonical_loader is None:
            warnings.append("Canonical record lookup is not configured for this advisory runtime boundary.")
            return result

        if self._canonical_loader is not None:
            canonical_record = self._canonical_loader.get(record_id)
        else:
            canonical_record = self._canonical_records.get(record_id)
        if canonical_record is None:
            result["lookup_status"] = "missing"
            warnings.append("Canonical record lookup returned no record for this HC:// runtime request.")
            return result

        result["found"] = True
        result["lookup_status"] = "found"
        if canonical_record is MALFORMED_RECORD or not isinstance(canonical_record, dict):
            result["malformed"] = True
            result["lookup_status"] = "malformed"
            warnings.append("Canonical record is malformed and cannot be schema-validated in the advisory runtime.")
            return result

        record_snapshot = copy.deepcopy(canonical_record)
        result["record_id_match"] = record_snapshot.get("record_id") == record_id
        result["content_hash_present"] = isinstance(record_snapshot.get("content_hash"), str) and bool(
            record_snapshot.get("content_hash", "").strip()
        )
        result["schema_valid"] = self._canonical_record_schema_valid(record_id=record_id, record=record_snapshot)

        if not result["record_id_match"]:
            warnings.append("Canonical record id does not match the advisory runtime lookup id.")
        if not result["schema_valid"]:
            result["lookup_status"] = "schema_invalid"
            warnings.append("Canonical record schema validation failed within advisory-only runtime boundaries.")

        if not result["content_hash_present"]:
            result["lookup_status"] = "hash_missing"
            warnings.append("Canonical record content_hash is missing; SHA-256 verification remains unresolved.")
            return result

        calculated_hash = self._canonical_record_content_hash(record_snapshot.get("content"))
        result["hash_verified"] = calculated_hash == record_snapshot["content_hash"]
        if not result["hash_verified"]:
            result["lookup_status"] = "hash_mismatch"
            warnings.append("Canonical record content_hash mismatch detected during advisory SHA-256 verification.")
        elif result["schema_valid"]:
            result["lookup_status"] = "verified"

        return result

    def _schema_validation_hook(self, *, qr_input: str, bridge_result: dict[str, Any]) -> dict[str, Any]:
        if bridge_result["lookup_performed"]:
            return {
                "checked": True,
                "placeholder": True,
                "valid": bool(qr_input.strip()) and bridge_result["schema_valid"],
                "canonical_lookup_status": bridge_result["lookup_status"],
                "warnings": list(bridge_result["warnings"]),
            }
        return {
            "checked": True,
            "placeholder": True,
            "valid": bool(qr_input.strip()),
            "canonical_lookup_status": bridge_result["lookup_status"],
            "warnings": [],
        }

    def _hash_verification_hook(self, *, qr_input: str, bridge_result: dict[str, Any]) -> dict[str, Any]:
        if bridge_result["lookup_performed"]:
            return {
                "checked": True,
                "placeholder": True,
                "hash_verified": bridge_result["hash_verified"],
                "canonical_lookup_status": bridge_result["lookup_status"],
                "warnings": list(bridge_result["warnings"]),
            }
        hash_verified = "hash:" in qr_input.lower()
        return {
            "checked": True,
            "placeholder": True,
            "hash_verified": hash_verified,
            "canonical_lookup_status": bridge_result["lookup_status"],
            "warnings": [],
        }

    def _trust_state_assignment_hook(
        self,
        *,
        schema_result: dict[str, Any],
        hash_result: dict[str, Any],
        bridge_result: dict[str, Any],
    ) -> dict[str, Any]:
        warnings: list[str] = []
        if bridge_result["lookup_performed"]:
            warnings.extend(bridge_result["warnings"])
        elif not schema_result["valid"]:
            warnings.append("Schema validation placeholder flagged invalid QR input.")
        if not hash_result["hash_verified"] and not bridge_result["lookup_performed"]:
            warnings.append("Hash verification placeholder could not confirm QR input hash marker.")
        return {"warnings": warnings}

    def _canonical_record_schema_valid(self, *, record_id: str, record: dict[str, Any]) -> bool:
        return (
            record.get("record_id") == record_id
            and "content" in record
            and isinstance(record.get("content_hash"), str)
            and bool(record.get("content_hash", "").strip())
        )

    def _canonical_record_content_hash(self, content: object) -> str:
        if isinstance(content, str):
            canonical_content = content
        else:
            canonical_content = json.dumps(content, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical_content.encode("utf-8")).hexdigest()

    def _escalation_routing_hook(self, *, warnings: list[str]) -> dict[str, Any]:
        return {
            "route": "human-supervised-validation" if warnings else "none",
            "required": bool(warnings),
            "placeholder": True,
        }


@dataclass(slots=True)
class RuntimeQueueStore:
    verification_queue: list[dict[str, Any]] = field(default_factory=list)
    escalation_queue: list[dict[str, Any]] = field(default_factory=list)
    replay_warning_queue: list[dict[str, Any]] = field(default_factory=list)

    def enqueue_verification(self, item: dict[str, Any]) -> None:
        self.verification_queue.append(redact_public_payload(item))

    def enqueue_escalation(self, item: dict[str, Any]) -> None:
        self.escalation_queue.append(redact_public_payload(item))

    def enqueue_replay_warning(self, item: dict[str, Any]) -> None:
        self.replay_warning_queue.append(redact_public_payload(item))


@dataclass(slots=True)
class RuntimePolicyEngine:
    def evaluate(
        self,
        *,
        trust_state: TrustState,
        replay_warning: bool,
        degraded_mode: bool,
    ) -> dict[str, Any]:
        warnings: list[str] = []
        public_exposure = "standard"

        if trust_state is not TrustState.ADVISORY:
            warnings.append("Advisory downgrade active for non-advisory trust-state response.")

        if replay_warning:
            warnings.append("Replay-warning escalation policy routed to human-supervised validation queue.")
            public_exposure = "restricted"

        if degraded_mode:
            warnings.append("Degraded runtime restriction policy applied to runtime response scope.")
            public_exposure = "restricted"

        return {
            "advisory_downgrade": trust_state is not TrustState.ADVISORY,
            "replay_warning_escalation": replay_warning,
            "degraded_runtime_restriction": degraded_mode,
            "public_exposure": public_exposure,
            "warnings": warnings,
            "advisory_only": True,
        }


@dataclass(slots=True)
class FederationRelay:
    def review(self, *, record_id: str, degraded_mode: bool, replay_warning: bool) -> dict[str, Any]:
        warnings: list[str] = []
        if degraded_mode:
            warnings.append("Degraded federation visibility is active in this advisory relay placeholder.")
        if replay_warning:
            warnings.append("Federation warning propagation includes replay-warning visibility.")
        return {
            "record_id": redact_secret_like_text(record_id),
            "relay_mode": "local-placeholder",
            "advisory_only": True,
            "warnings": warnings,
        }
