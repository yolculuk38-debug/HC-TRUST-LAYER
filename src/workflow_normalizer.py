"""HC:// workflow normalization layer."""

from __future__ import annotations

STANDARD_STAGES = [
    "validation",
    "security",
    "review",
    "deployment",
]


def normalize_stage(stage: str) -> str:
    value = stage.strip().lower()
    return value if value in STANDARD_STAGES else "validation"


def build_workflow_profile(stages: list[str]) -> dict:
    normalized = [normalize_stage(stage) for stage in stages]
    return {
        "stages": normalized,
        "normalized": True,
    }


def workflow_ready(profile: dict) -> bool:
    return bool(profile.get("normalized", False)) and bool(profile.get("stages"))
