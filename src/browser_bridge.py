"""HC:// browser verification bridge."""

from __future__ import annotations


def build_browser_verification_payload(*, url: str, verification_status: str) -> dict:
    return {
        "url": url.strip(),
        "verification_status": verification_status.strip().upper(),
    }
