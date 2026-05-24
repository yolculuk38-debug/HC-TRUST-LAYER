"""Verification receipt structures for exportable verification evidence."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from src.api.models.verification_models import VerificationState


@dataclass(slots=True)
class VerificationReceipt:
    """Experimental verification receipt summary."""

    receipt_id: str
    verification_timestamp: datetime
    verification_state: VerificationState
    federation_confirmations: int = 0
    witness_summary: dict[str, str] = field(default_factory=dict)
    integrity_summary: dict[str, str] = field(default_factory=dict)
    revision_summary: dict[str, str] = field(default_factory=dict)
