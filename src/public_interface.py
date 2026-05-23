"""HC:// public interface package.

Provides deterministic public-facing verifier and explorer interface models.
"""

from __future__ import annotations

from typing import Any, Iterable


PUBLIC_VERIFIED = "PUBLIC_VERIFIED"
PUBLIC_REVIEW = "PUBLIC_REVIEW"



def verifier_card(record: dict[str, Any]) -> dict[str, Any]:
    """Build normalized public verifier card."""

    trust_score = max(0, min(int(record.get("trust_score", 0)), 100))

    return {
        "record_id": str(record.get("record_id", "")).strip(),
        "status": str(record.get("status", "UNKNOWN")).strip().upper(),
        "trust_score": trust_score,
        "public_state": PUBLIC_VERIFIED if trust_score >= 70 else PUBLIC_REVIEW,
    }



def explorer_panel(item: dict[str, Any]) -> dict[str, Any]:
    """Build explorer visibility panel."""

    witnesses = sorted(set(item.get("witnesses", [])))
    federation_nodes = sorted(set(item.get("federation_nodes", [])))

    return {
        "record_id": str(item.get("record_id", "")).strip(),
        "witness_count": len(witnesses),
        "federation_nodes": federation_nodes,
        "visibility": bool(witnesses or federation_nodes),
    }



def trust_visualization(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic public trust visualization snapshot."""

    cards = [verifier_card(record) for record in records]

    return sorted(
        cards,
        key=lambda item: (
            -item["trust_score"],
            item["record_id"],
        ),
    )


__all__ = [
    "PUBLIC_VERIFIED",
    "PUBLIC_REVIEW",
    "verifier_card",
    "explorer_panel",
    "trust_visualization",
]
