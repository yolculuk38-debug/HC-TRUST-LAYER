"""HC:// task queue core."""

from __future__ import annotations


def build_task(*, task_id: str, title: str, priority: str = "MEDIUM") -> dict:
    return {
        "task_id": task_id.strip(),
        "title": title.strip(),
        "priority": priority.strip().upper(),
        "status": "QUEUED",
    }


def mark_task_done(task: dict) -> dict:
    updated = dict(task)
    updated["status"] = "DONE"
    return updated
