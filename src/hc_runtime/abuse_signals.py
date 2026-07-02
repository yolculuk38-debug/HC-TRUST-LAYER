"""Compatibility wrapper for HC:// advisory abuse signal helpers."""

from hc_runtime.contracts.abuse_signals import (
    AbuseSignalLevel,
    AbuseSignalResult,
    AdvisoryAbuseSignalTracker,
)

__all__ = [
    "AbuseSignalLevel",
    "AbuseSignalResult",
    "AdvisoryAbuseSignalTracker",
]
