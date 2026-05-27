"""Public-safe advisory response builders for HC:// runtime verification routes."""

from __future__ import annotations

from typing import Any


def _build_response(
    *,
    status: str,
    message: str,
    warnings: list[str] | None = None,
    record_id: str | None = None,
) -> dict[str, Any]:
    response: dict[str, Any] = {
        "status": status,
        "advisory_only": True,
        "public_safe": True,
        "message": message,
        "warnings": warnings or [],
        "traceable": True,
        "truth_guarantee": False,
    }

    if record_id is not None:
        response["record_id"] = record_id

    return response


def advisory_response(record_id: str, message: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="ADVISORY",
        message=message,
        warnings=warnings,
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


def not_found_response(record_id: str | None = None, warnings: list[str] | None = None) -> dict[str, Any]:
    return _build_response(
        record_id=record_id,
        status="NOT_FOUND",
        message="Requested verification record was not found in this advisory runtime scope.",
        warnings=warnings or ["Record lookup returned no canonical record within local advisory boundaries."],
    )
