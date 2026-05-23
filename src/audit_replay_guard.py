"""HC:// audit replay protection."""

from __future__ import annotations


def build_replay_token(*, entry_id: str, nonce: str, timestamp: str) -> dict:
    return {
        "entry_id": entry_id.strip(),
        "nonce": nonce.strip(),
        "timestamp": timestamp.strip(),
    }


def token_seen(token: dict, seen_nonces: set[str]) -> bool:
    return token.get("nonce") in seen_nonces


def replay_allowed(token: dict, seen_nonces: set[str]) -> bool:
    return bool(token.get("entry_id")) and bool(token.get("nonce")) and not token_seen(token, seen_nonces)


def build_replay_decision(token: dict, seen_nonces: set[str]) -> dict:
    allowed = replay_allowed(token, seen_nonces)
    return {
        "entry_id": token.get("entry_id", ""),
        "allowed": allowed,
        "reason": "fresh audit token" if allowed else "replay or invalid audit token",
    }
