"""HC:// batch task planner core."""

from __future__ import annotations

MAX_TASKS_PER_BATCH = 20
DEFAULT_BATCH_SIZE = 10


def create_batch_plan(*, batch_id: str, tasks: list[dict], batch_size: int = DEFAULT_BATCH_SIZE) -> dict:
    """Create a bounded plan for grouped development tasks."""

    safe_size = max(1, min(int(batch_size), MAX_TASKS_PER_BATCH))
    planned_tasks = tasks[:safe_size]

    return {
        "batch_id": batch_id.strip(),
        "batch_size": safe_size,
        "planned_count": len(planned_tasks),
        "tasks": planned_tasks,
        "status": "PLANNED",
    }


def split_into_batches(tasks: list[dict], batch_size: int = DEFAULT_BATCH_SIZE) -> list[list[dict]]:
    """Split tasks into bounded chunks."""

    safe_size = max(1, min(int(batch_size), MAX_TASKS_PER_BATCH))
    return [tasks[index : index + safe_size] for index in range(0, len(tasks), safe_size)]
