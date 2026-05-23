"""HC:// AI task planner core."""

from __future__ import annotations

RISK_KEYWORDS = {
    "workflow": "HIGH",
    "secret": "HIGH",
    "token": "HIGH",
    "deploy": "HIGH",
    "docs": "LOW",
    "test": "LOW",
}


def plan_task(*, task_id: str, title: str, description: str) -> dict:
    """Plan one AI-assisted engineering task."""

    text = f"{title} {description}".lower()
    risk_level = "MEDIUM"

    for keyword, risk in RISK_KEYWORDS.items():
        if keyword in text:
            risk_level = risk
            break

    return {
        "task_id": task_id.strip(),
        "title": title.strip(),
        "description": description.strip(),
        "risk_level": risk_level,
        "status": "PLANNED",
    }


def plan_tasks(tasks: list[dict]) -> list[dict]:
    return [
        plan_task(
            task_id=str(index + 1),
            title=str(task.get("title", "")),
            description=str(task.get("description", "")),
        )
        for index, task in enumerate(tasks)
    ]
