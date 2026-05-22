"""HC:// automation orchestrator core."""

from __future__ import annotations


def build_automation_task(*, task_id: str, task_type: str, safety_level: str) -> dict:
    return {
        "task_id": task_id.strip(),
        "task_type": task_type.strip().upper(),
        "safety_level": safety_level.strip().upper(),
        "status": "PENDING",
    }


def mark_task_checked(task: dict) -> dict:
    updated = dict(task)
    updated["status"] = "CHECKED"
    return updated
