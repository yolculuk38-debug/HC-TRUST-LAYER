from typing import Dict, List


SUPPORTED_WITNESS_TYPES = {"ai", "human", "system", "institution"}


def build_witness_summary(witnesses: List[Dict]) -> Dict:
    """Build a compact witness summary for HC:// verification displays."""

    if witnesses is None:
        witnesses = []

    if not isinstance(witnesses, list):
        raise ValueError("witnesses must be a list")

    type_counts = {witness_type: 0 for witness_type in SUPPORTED_WITNESS_TYPES}
    invalid_count = 0

    for witness in witnesses:
        if not isinstance(witness, dict):
            invalid_count += 1
            continue

        witness_type = str(witness.get("type", "")).lower()
        if witness_type in SUPPORTED_WITNESS_TYPES:
            type_counts[witness_type] += 1
        else:
            invalid_count += 1

    total_valid = sum(type_counts.values())

    return {
        "witness_count": total_valid,
        "witness_types": type_counts,
        "invalid_witness_count": invalid_count,
        "has_human_witness": type_counts["human"] > 0,
        "has_ai_witness": type_counts["ai"] > 0,
        "has_independent_mix": type_counts["human"] > 0 and type_counts["ai"] > 0,
        "experimental": True,
    }
