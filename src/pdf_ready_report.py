"""HC:// PDF-ready verification report structure."""

from __future__ import annotations

from typing import Any


PDF_READY_REPORT_VERSION = "HC-PDF-REPORT-V1"



def build_pdf_ready_report(
    *,
    report_title: str,
    record_id: str,
    decision: str,
    trust_score: int | None = None,
    risk_level: str | None = None,
    reasons: list[str] | None = None,
    audit_summary: str | None = None,
) -> dict[str, Any]:
    """Build printable verification report structure."""

    return {
        "pdf_ready_report_version": PDF_READY_REPORT_VERSION,
        "report_title": report_title,
        "record_id": record_id,
        "decision": decision,
        "trust_score": trust_score,
        "risk_level": risk_level,
        "reasons": sorted(set(reasons or [])),
        "audit_summary": audit_summary,
        "printable": True,
        "exportable": True,
    }



def validate_pdf_ready_report(report: dict[str, Any]) -> dict[str, Any]:
    """Validate printable report structure."""

    if not isinstance(report, dict):
        return _result(False, ["invalid_report_structure"])

    reasons: list[str] = []

    for field in ["report_title", "record_id", "decision"]:
        if field not in report:
            reasons.append(f"missing_{field}")

    if report.get("pdf_ready_report_version") != PDF_READY_REPORT_VERSION:
        reasons.append("unsupported_report_version")

    return _result(not reasons, reasons)



def _result(valid: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "pdf_ready_report_version": PDF_READY_REPORT_VERSION,
        "valid": valid,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "PDF_READY_REPORT_VERSION",
    "build_pdf_ready_report",
    "validate_pdf_ready_report",
]
