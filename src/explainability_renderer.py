"""HC:// explainability renderer."""

from __future__ import annotations

from typing import Any


EXPLAINABILITY_RENDERER_VERSION = "HC-EXPLAINABILITY-RENDERER-V1"


def render_explanation(
    *,
    decision: str,
    reasons: list[str] | None = None,
    trust_score: int | None = None,
    risk_level: str | None = None,
) -> dict[str, Any]:
    """Render human-readable verification explanation."""

    normalized_reasons = sorted(set(reasons or []))

    if decision in {"VERIFIED", "ALLOW"}:
        summary = "Verification passed with sufficient trusted evidence."
        action = "TRUST_PASSPORT_VISIBLE"
    elif decision in {"REVIEW_REQUIRED", "PARTIAL", "REVIEW"}:
        summary = "Verification needs human or additional review before trust."
        action = "SHOW_REVIEW_REQUIRED"
    elif decision in {"INVALID", "DENY", "REVOKED"}:
        summary = "Verification failed or trust was revoked."
        action = "BLOCK_TRUST"
    elif decision in {"CRITICAL_LOCK", "QUARANTINE"}:
        summary = "High-risk security gate activated. Trust display is locked."
        action = "SECURITY_LOCK"
    else:
        summary = "Current evidence is not enough to establish trust."
        action = "SHOW_UNTRUSTED"

    return {
        "explainability_renderer_version": EXPLAINABILITY_RENDERER_VERSION,
        "decision": decision,
        "summary": summary,
        "recommended_action": action,
        "trust_score": trust_score,
        "risk_level": risk_level,
        "reasons": normalized_reasons,
    }


__all__ = [
    "EXPLAINABILITY_RENDERER_VERSION",
    "render_explanation",
]
