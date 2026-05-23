"""HC:// orchestration recovery state."""

from __future__ import annotations

VALID_STATES = {
    "PENDING",
    "RUNNING",
    "FAILED",
    "RECOVERED",
}


def build_state(*, task_id: str, state: str = "PENDING") -> dict:
    normalized = state.strip().upper()
    if normalized not in VALID_STATES:
        normalized = "PENDING"

    return {
        "task_id": task_id.strip(),
        "state": normalized,
    }


def recovery_required(task: dict) -> bool:
    return task.get("state") == "FAILED"


def mark_recovered(task: dict) -> dict:
    updated = dict(task)
    updated["state"] = "RECOVERED"
    return updated
