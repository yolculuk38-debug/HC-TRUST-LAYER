"""HC:// label helper."""

from __future__ import annotations


def suggest_labels(paths: list[str]) -> list[str]:
    labels: set[str] = set()

    for path in paths:
        normalized = path.lower()

        if normalized.startswith("docs/"):
            labels.add("documentation")

        if normalized.startswith("tests/"):
            labels.add("tests")

        if normalized.startswith("src/"):
            labels.add("code")

        if ".github/workflows/" in normalized:
            labels.add("review-required")

    return sorted(labels)
