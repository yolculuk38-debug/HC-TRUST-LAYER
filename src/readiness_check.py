"""HC:// readiness check core."""

from __future__ import annotations


def build_readiness_report(*, requirements: dict[str, bool]) -> dict:
    passed = sum(1 for value in requirements.values() if value)
    total = len(requirements)

    return {
        "ready": total > 0 and passed == total,
        "passed_requirements": passed,
        "total_requirements": total,
        "requirements": requirements,
    }
