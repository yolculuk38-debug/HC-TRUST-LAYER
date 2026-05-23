"""HC:// protocol analytics core."""

from __future__ import annotations

from collections import Counter


def count_categories(entries: list[dict]) -> dict:
    categories = [entry.get("category", "GENERAL") for entry in entries]
    return dict(Counter(categories))


def calculate_validation_rate(total: int, passed: int) -> float:
    if total <= 0:
        return 0.0
    return round((passed / total) * 100, 2)


def build_protocol_metrics(*, total_records: int, verified_records: int, failed_records: int) -> dict:
    validation_rate = calculate_validation_rate(total_records, verified_records)

    return {
        "total_records": total_records,
        "verified_records": verified_records,
        "failed_records": failed_records,
        "validation_rate": validation_rate,
        "protocol_health": "STABLE" if validation_rate >= 90 else "WARNING",
    }
