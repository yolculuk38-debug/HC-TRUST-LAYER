"""HC:// immutable audit chain core."""

from __future__ import annotations


def build_chain_entry(*, entry_id: str, current_hash: str, previous_hash: str = "") -> dict:
    return {
        "entry_id": entry_id.strip(),
        "current_hash": current_hash.strip(),
        "previous_hash": previous_hash.strip(),
    }


def is_genesis_entry(entry: dict) -> bool:
    return not bool(entry.get("previous_hash"))


def verify_chain_link(*, previous_entry: dict, current_entry: dict) -> bool:
    return current_entry.get("previous_hash") == previous_entry.get("current_hash")


def verify_chain(entries: list[dict]) -> bool:
    if len(entries) <= 1:
        return True
    return all(
        verify_chain_link(previous_entry=entries[index - 1], current_entry=entries[index])
        for index in range(1, len(entries))
    )
