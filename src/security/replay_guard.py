"""Replay-protection architecture placeholders.

This module defines foundations only and is not production hardened.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass(slots=True)
class ReplayGuardPolicy:
    """Replay policy placeholders for distributed verification entrypoints."""

    nonce_ttl_seconds: int = 300
    max_clock_skew_seconds: int = 30


def build_request_fingerprint(method: str, path: str, body_hash: str) -> str:
    """Return normalized fingerprint input for future signing and replay checks."""

    return f"{method.upper()}::{path}::{body_hash}"


def is_timestamp_within_skew(ts: datetime, policy: ReplayGuardPolicy | None = None) -> bool:
    """Validate request timestamp against accepted skew window."""

    active = policy or ReplayGuardPolicy()
    now = datetime.now(tz=timezone.utc)
    delta = timedelta(seconds=active.max_clock_skew_seconds)
    return now - delta <= ts <= now + delta


def detect_replay_placeholder(fingerprint: str, nonce: str | None = None) -> bool:
    """Replay detection placeholder.

    Always returns ``False`` until durable nonce/fingerprint storage is added.
    """

    _ = (fingerprint, nonce)
    return False
