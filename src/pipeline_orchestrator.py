"""HC:// pipeline orchestrator core."""

from __future__ import annotations

PIPELINE_GROUPS = {
    "CORE": ["validation", "security", "risk"],
    "OPTIONAL": ["pages", "docs", "analytics"],
    "AUTO": ["auto_merge", "labels", "queue"],
}


def build_pipeline_plan(*, changed_paths: list[str]) -> dict:
    groups: set[str] = {"CORE"}

    for path in changed_paths:
        normalized = path.lower()
        if normalized.startswith("docs/"):
            groups.add("OPTIONAL")
        if normalized.startswith("src/"):
            groups.add("AUTO")
        if normalized.startswith(".github/workflows/"):
            groups.add("CORE")

    return {
        "pipeline_groups": sorted(groups),
        "steps": {group: PIPELINE_GROUPS[group] for group in sorted(groups)},
    }


def should_run_auto_pipeline(plan: dict) -> bool:
    return "AUTO" in plan.get("pipeline_groups", [])
