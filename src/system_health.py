"""HC:// system health core."""

from __future__ import annotations

SYSTEM_HEALTH_VERSION = "HC-SYSTEM-HEALTH-V1"


def build_health_report(*, checks: dict[str, bool]) -> dict:
    passed = sum(1 for value in checks.values() if value)
    total = len(checks)
    status = "HEALTHY" if total > 0 and passed == total else "DEGRADED"

    return {
        "system_health_version": SYSTEM_HEALTH_VERSION,
        "status": status,
        "passed_checks": passed,
        "total_checks": total,
        "checks": checks,
    }
