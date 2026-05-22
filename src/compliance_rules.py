"""HC:// compliance rules core."""

from __future__ import annotations


def build_compliance_rule(*, rule_id: str, export_allowed: bool) -> dict:
    return {
        "rule_id": rule_id.strip(),
        "export_allowed": bool(export_allowed),
    }
