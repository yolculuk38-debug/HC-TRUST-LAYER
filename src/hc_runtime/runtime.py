"""Advisory-only HC:// runtime service components for operational prototype flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hc_runtime.decision_engine import TrustState, TrustStateDecisionEngine
from hc_runtime.events import RuntimeEventStore


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


@dataclass(slots=True)
class RuntimeQueueStore:
    verification_queue: list[dict[str, Any]] = field(default_factory=list)
    escalation_queue: list[dict[str, Any]] = field(default_factory=list)
    replay_warning_queue: list[dict[str, Any]] = field(default_factory=list)

    def enqueue_verification(self, item: dict[str, Any]) -> None:
        self.verification_queue.append(item)

    def enqueue_escalation(self, item: dict[str, Any]) -> None:
        self.escalation_queue.append(item)

    def enqueue_replay_warning(self, item: dict[str, Any]) -> None:
        self.replay_warning_queue.append(item)


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
            "record_id": record_id,
            "relay_mode": "local-placeholder",
            "advisory_only": True,
            "warnings": warnings,
        }
