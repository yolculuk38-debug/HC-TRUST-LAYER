"""HC:// reviewer policy engine."""

from __future__ import annotations


PROTECTED_PATHS = {
    ".github/workflows/",
    "schema/",
    "security/",
}


DEFAULT_REVIEWERS = {
    "LOW": ["automation-review"],
    "MEDIUM": ["protocol-review"],
    "HIGH": ["security-review", "manual-review"],
}


def detect_protected_change(paths: list[str]) -> bool:
    return any(
        any(path.startswith(prefix) for prefix in PROTECTED_PATHS)
        for path in paths
    )


def select_reviewers(*, risk_level: str, changed_paths: list[str]) -> list[str]:
    normalized_risk = risk_level.strip().upper()

    if detect_protected_change(changed_paths):
        return ["security-review", "manual-review"]

    return DEFAULT_REVIEWERS.get(normalized_risk, ["protocol-review"])
