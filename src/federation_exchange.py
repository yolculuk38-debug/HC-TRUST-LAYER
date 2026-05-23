"""HC:// federation trust exchange."""

from __future__ import annotations


def build_exchange_packet(*, source_node: str, target_node: str, trust_level: str) -> dict:
    return {
        "source_node": source_node.strip(),
        "target_node": target_node.strip(),
        "trust_level": trust_level.strip().upper(),
    }


def exchange_allowed(packet: dict) -> bool:
    return bool(packet.get("source_node")) and bool(packet.get("target_node"))


def build_exchange_result(*, packet: dict, accepted: bool) -> dict:
    return {
        "packet": packet,
        "accepted": bool(accepted),
    }
