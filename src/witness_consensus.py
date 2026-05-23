"""HC:// witness consensus rules."""

from __future__ import annotations

MINIMUM_WITNESSES = 3


def witness_threshold_met(witnesses: list[str]) -> bool:
    unique_witnesses = {item.strip().lower() for item in witnesses if item.strip()}
    return len(unique_witnesses) >= MINIMUM_WITNESSES


def consensus_strength(witnesses: list[str]) -> str:
    count = len({item.strip().lower() for item in witnesses if item.strip()})

    if count >= 7:
        return "HIGH"
    if count >= MINIMUM_WITNESSES:
        return "MEDIUM"
    return "LOW"
