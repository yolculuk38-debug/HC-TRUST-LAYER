"""HC:// verification report renderer."""

from __future__ import annotations

from typing import Any


REPORT_RENDERER_VERSION = "HC-REPORT-RENDERER-V1"


def render_report_sections(report: dict[str, Any]) -> dict[str, Any]:
    """Render verification report into human-readable sections."""

    record_id = report.get("record_id", "UNKNOWN")
    decision = report.get("decision", "UNTRUSTED")
    trust_score = report.get("trust_score")
    risk_level = report.get("risk_level")
    reasons = report.get("reasons", []) or []
    audit_summary = report.get("audit_summary") or "No audit summary provided."

    return {
        "report_renderer_version": REPORT_RENDERER_VERSION,
        "title": report.get("report_title", "HC:// Verification Report"),
        "sections": [
            {
                "heading": "Record",
                "body": f"Record ID: {record_id}",
            },
            {
                "heading": "Verification Decision",
                "body": f"Decision: {decision}. Trust score: {trust_score}. Risk level: {risk_level}.",
            },
            {
                "heading": "Reasons",
                "body": ", ".join(reasons) if reasons else "No blocking reasons reported.",
            },
            {
                "heading": "Audit Summary",
                "body": audit_summary,
            },
        ],
        "printable": True,
    }


__all__ = [
    "REPORT_RENDERER_VERSION",
    "render_report_sections",
]
