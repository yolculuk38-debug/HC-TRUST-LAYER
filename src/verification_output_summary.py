"""HC:// verification output summary."""

from __future__ import annotations

from typing import Any


OUTPUT_SUMMARY_VERSION = "HC-OUTPUT-SUMMARY-V1"


def build_output_summary(
    *,
    record_id: str,
    decision: str,
    trusted: bool,
    trust_score: int | None = None,
    risk_level: str | None = None,
    reasons: list[str] | None = None,
) -> dict[str, Any]:
    """Build portable verification output summary."""

    return {
        "output_summary_version": OUTPUT_SUMMARY_VERSION,
        "record_id": record_id,
        "decision": decision,
        "trusted": bool(trusted),
        "trust_score": trust_score,
        "risk_level": risk_level,
        "reasons": sorted(set(reasons or [])),
        "portable": True,
        "machine_readable": True,
    }


def validate_output_summary(summary: dict[str, Any]) -> dict[str, Any]:
    """Validate output summary shape."""

    if not isinstance(summary, dict):
        return _result(False, ["invalid_summary_structure"])

    reasons: list[str] = []

    for field in ["output_summary_version", "record_id", "decision", "trusted"]:
        if field not in summary:
            reasons.append(f"missing_{field}")

    if summary.get("output_summary_version") != OUTPUT_SUMMARY_VERSION:
        reasons.append("unsupported_output_summary_version")

    return _result(not reasons, reasons)


def _result(valid: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "output_summary_version": OUTPUT_SUMMARY_VERSION,
        "valid": valid,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "OUTPUT_SUMMARY_VERSION",
    "build_output_summary",
    "validate_output_summary",
]
