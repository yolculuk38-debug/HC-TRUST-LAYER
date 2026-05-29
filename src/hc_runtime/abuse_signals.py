"""Public-safe advisory abuse signal helpers for HC:// runtime flows."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from hc_runtime.qr_spoof_protection import QRRiskLevel
from hc_runtime.redaction import redact_public_payload


class AbuseSignalLevel(StrEnum):
    """Deterministic advisory abuse signal bands for repeated runtime patterns."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(frozen=True, slots=True)
class AbuseSignalResult:
    """Public-safe advisory abuse-pattern visibility result."""

    warnings: list[str] = field(default_factory=list)
    signal_level: AbuseSignalLevel = AbuseSignalLevel.LOW
    reasons: list[str] = field(default_factory=list)
    pattern_counts: dict[str, int] = field(default_factory=dict)
    advisory_only: bool = True
    public_safe: bool = True
    truth_guarantee: bool = False
    request_denied: bool = False
    human_final_authority: bool = True

    def summary(self) -> dict[str, Any]:
        """Return a deterministic public-safe summary for runtime responses."""

        return redact_public_payload(
            {
                "advisory_only": self.advisory_only,
                "public_safe": self.public_safe,
                "truth_guarantee": self.truth_guarantee,
                "request_denied": self.request_denied,
                "human_final_authority": self.human_final_authority,
                "signal_level": self.signal_level.value,
                "reasons": list(self.reasons),
                "pattern_counts": dict(sorted(self.pattern_counts.items())),
                "warnings": list(self.warnings),
            }
        )


@dataclass(slots=True)
class AdvisoryAbuseSignalTracker:
    """In-memory advisory-only repeated-pattern tracker.

    The tracker is intentionally local and non-authoritative: it does not deny
    requests, quarantine inputs, mutate canonical records, or change validators.
    It only creates public-safe warnings so operators can apply external,
    human-supervised rate limiting guidance when repeated malformed, spoof-risk,
    replay-risk, or degraded validation patterns are visible.
    """

    malformed_inputs: dict[str, set[str]] = field(default_factory=dict)
    spoof_risk_inputs: dict[str, set[str]] = field(default_factory=dict)
    replay_markers: dict[str, set[str]] = field(default_factory=dict)
    degraded_states: dict[str, set[str]] = field(default_factory=dict)

    def reset(self) -> None:
        """Clear local advisory counters for isolated tests or runtime restart."""

        self.malformed_inputs.clear()
        self.spoof_risk_inputs.clear()
        self.replay_markers.clear()
        self.degraded_states.clear()

    def inspect(
        self,
        *,
        record_id: str,
        schema_valid: bool,
        qr_risk_level: QRRiskLevel,
        qr_risk_reasons: list[str],
        qr_risk_group_keys: list[str],
        replay_warning: bool,
        degraded_mode: bool,
    ) -> AbuseSignalResult:
        """Record visible risk patterns and return advisory warnings only."""

        counters = {
            "malformed_input": 0,
            "spoof_risk": 0,
            "replay_marker": 0,
            "degraded_state": 0,
        }
        reasons: list[str] = []
        warnings: list[str] = []

        if not schema_valid:
            key = _record_family(record_id)
            counters["malformed_input"] = _increment_unique(self.malformed_inputs, key, record_id)
            if counters["malformed_input"] > 1:
                reasons.append("repeated_malformed_input")
                warnings.append(
                    "Repeated malformed HC:// runtime input pattern observed; advisory warning only, no request denial applied."
                )

        if qr_risk_level in {QRRiskLevel.HIGH, QRRiskLevel.INCIDENT}:
            key = _first_or_default(qr_risk_group_keys, _record_family(record_id))
            counters["spoof_risk"] = _increment_unique(self.spoof_risk_inputs, key, record_id)
            if counters["spoof_risk"] > 1:
                reasons.append("repeated_spoof_risk_qr")
                warnings.append(
                    "Repeated spoof-risk QR pattern observed; advisory warning only with human-supervised validation retained."
                )

        if replay_warning:
            key = _record_family(record_id)
            counters["replay_marker"] = _increment_unique(self.replay_markers, key, record_id)
            if counters["replay_marker"] > 1:
                reasons.append("repeated_replay_marker")
                warnings.append(
                    "Repeated replay marker pattern observed; advisory warning only, no autonomous blocking applied."
                )

        if degraded_mode:
            key = _record_family(record_id)
            counters["degraded_state"] = _increment_unique(self.degraded_states, key, record_id)
            if counters["degraded_state"] > 1:
                reasons.append("repeated_degraded_validator_state")
                warnings.append(
                    "Repeated degraded validator state observed; degraded visibility remains public-safe and advisory."
                )

        if qr_risk_level is QRRiskLevel.MEDIUM and qr_risk_reasons:
            reasons.append("medium_qr_risk_visible")

        signal_level = _signal_level(reasons=reasons, qr_risk_level=qr_risk_level)
        pattern_counts = {key: value for key, value in counters.items() if value}

        return AbuseSignalResult(
            warnings=warnings,
            signal_level=signal_level,
            reasons=_dedupe(reasons),
            pattern_counts=pattern_counts,
        )


def _increment_unique(counters: dict[str, set[str]], key: str, record_id: str) -> int:
    counters.setdefault(key, set()).add(record_id)
    return len(counters[key])


def _record_family(record_id: str) -> str:
    return record_id.rsplit("-", 1)[0] if "-" in record_id else record_id


def _first_or_default(values: list[str], default: str) -> str:
    return values[0] if values else default


def _dedupe(values: list[str]) -> list[str]:
    deduped: list[str] = []
    for value in values:
        if value not in deduped:
            deduped.append(value)
    return deduped


def _signal_level(*, reasons: list[str], qr_risk_level: QRRiskLevel) -> AbuseSignalLevel:
    if any(reason in reasons for reason in {"repeated_spoof_risk_qr", "repeated_replay_marker"}):
        return AbuseSignalLevel.HIGH
    if reasons or qr_risk_level in {QRRiskLevel.MEDIUM, QRRiskLevel.HIGH, QRRiskLevel.INCIDENT}:
        return AbuseSignalLevel.MEDIUM
    return AbuseSignalLevel.LOW
