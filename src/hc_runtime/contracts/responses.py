"""Public-safe advisory response builders for HC:// runtime verification routes."""

from __future__ import annotations

from typing import Any

from hc_runtime.redaction import redact_public_payload, redact_secret_like_text

PUBLIC_RESPONSE_BASE_KEYS: tuple[str, ...] = (
    "status",
    "advisory_only",
    "runtime_stage",
    "verification_mode",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "human_review_required",
)

PUBLIC_RESPONSE_RECORD_KEYS: tuple[str, ...] = (*PUBLIC_RESPONSE_BASE_KEYS, "record_id")

QR_VERIFICATION_RESPONSE_KEYS: tuple[str, ...] = (
    *PUBLIC_RESPONSE_RECORD_KEYS,
    "trust_state",
    "replay_warning",
    "continuity_warning",
    "degraded_runtime",
    "recovery_mode",
    "public_exposure",
    "qr_risk_level",
    "qr_risk_reasons",
    "human_review_recommended",
    "escalation_queued",
    "incident_summary",
    "canonical_lookup_status",
    "schema_valid",
    "hash_verified",
    "qr_scan_summary",
)

MALFORMED_INPUT_RESPONSE_KEYS: tuple[str, ...] = (
    *PUBLIC_RESPONSE_RECORD_KEYS,
    "malformed_input",
    "public_exposure",
)


def _build_response(
    *,
    status: str,
    message: str,
    warnings: list[str] | None = None,
    record_id: str | None = None,
    escalation_required: bool = False,
) -> dict[str, Any]:
    public_warnings = redact_public_payload(warnings or [])
    response: dict[str, Any] = {
        "status": status,
        "advisory_only": True,
        "runtime_stage": "prototype",
        "verification_mode": "advisory",
        "public_safe": True,
        "message": redact_secret_like_text(message),
        "warnings": public_warnings,
        "traceable": True,
        "truth_guarantee": False,
        "human_review_required": bool(public_warnings) or escalation_required,
    }

    if record_id is not None:
        response["record_id"] = redact_secret_like_text(record_id)

    return response


def advisory_response(
    record_id: str,
    message: str,
    warnings: list[str] | None = None,
    *,
    escalation_required: bool = False,
) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="ADVISORY",
        message=message,
        warnings=warnings,
        escalation_required=escalation_required,
    )


def verified_placeholder_response(record_id: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="VERIFIED_PLACEHOLDER",
        message=(
            "HC:// verification remains advisory-only in the reference runtime. "
            "No production readiness or truth guarantee is asserted."
        ),
        warnings=warnings or ["Verification outcome is a placeholder pending human-supervised validation."],
    )


def disputed_response(record_id: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="DISPUTED",
        message="Verification record is disputed and requires human-supervised validation.",
        warnings=warnings or ["Dispute prevents conclusive trust interpretation in this advisory runtime."],
    )


def unresolved_response(record_id: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="UNRESOLVED",
        message="Verification could not be resolved within advisory runtime boundaries.",
        warnings=warnings or ["Provide additional evidence for human-supervised validation."],
    )


def continuity_warning_response(record_id: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="CONTINUITY_WARNING",
        message="Provenance continuity warning detected in the advisory verification map.",
        warnings=warnings or ["Audit trail continuity should be reviewed by a human supervisor."],
    )


def degraded_runtime_response(record_id: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="DEGRADED_RUNTIME",
        message="HC:// reference runtime is in degraded advisory mode.",
        warnings=warnings or ["Runtime degradation may limit verification map completeness."],
    )


def malformed_input_response(record_id: str | None = None, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="MALFORMED_INPUT",
        message=(
            "Malformed HC:// validator input was rejected within advisory runtime boundaries. "
            "Human-supervised validation is required before trust interpretation."
        ),
        warnings=warnings
        or [
            "Validator input was malformed, incomplete, or not processable as a public-safe QR verification request.",
            "No hidden fallback behavior was applied; warning routing remains explicit.",
        ],
    )


def not_found_response(record_id: str | None = None, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="NOT_FOUND",
        message="Requested verification record was not found in this advisory runtime scope.",
        warnings=warnings or ["Record lookup returned no canonical record within local advisory boundaries."],
    )
