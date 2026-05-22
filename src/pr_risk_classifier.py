"""HC:// PR risk classifier core."""

from __future__ import annotations

HIGH_RISK_PATH_PREFIXES = (
    ".github/workflows/",
    "secrets/",
    "keys/",
    "deploy/",
)

HIGH_RISK_KEYWORDS = (
    "token",
    "secret",
    "password",
    "private_key",
    "permission",
    "workflow",
)


def classify_changed_files(paths: list[str]) -> dict:
    """Classify PR risk from changed file paths."""

    risk = "LOW"
    reasons: list[str] = []

    for path in paths:
        normalized = path.strip().lower()
        if normalized.startswith(HIGH_RISK_PATH_PREFIXES):
            risk = "HIGH"
            reasons.append("high_risk_path")
        if any(keyword in normalized for keyword in HIGH_RISK_KEYWORDS):
            risk = "HIGH"
            reasons.append("high_risk_keyword")

    return {
        "risk_level": risk,
        "reasons": sorted(set(reasons)),
        "changed_file_count": len(paths),
    }
