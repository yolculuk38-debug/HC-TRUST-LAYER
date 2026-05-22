"""HC:// analysis report core."""

from __future__ import annotations


def build_analysis_report(*, report_id: str, target: str, risk_level: str) -> dict:
    return {
        "report_id": report_id.strip(),
        "target": target.strip(),
        "risk_level": risk_level.strip().upper(),
    }
