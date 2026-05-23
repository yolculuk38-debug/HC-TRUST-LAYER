"""HC:// recovery registry core."""

from __future__ import annotations


def register_checkpoint(*, checkpoint_id: str, commit_sha: str, reason: str) -> dict:
    return {
        "checkpoint_id": checkpoint_id.strip(),
        "commit_sha": commit_sha.strip(),
        "reason": reason.strip(),
        "status": "REGISTERED",
    }


def find_checkpoint(registry: list[dict], checkpoint_id: str) -> dict | None:
    target = checkpoint_id.strip()
    for checkpoint in registry:
        if checkpoint.get("checkpoint_id") == target:
            return checkpoint
    return None


def build_recovery_manifest(*, checkpoint: dict, target_branch: str = "main") -> dict:
    return {
        "checkpoint_id": checkpoint.get("checkpoint_id", ""),
        "checkpoint_commit_sha": checkpoint.get("commit_sha", ""),
        "target_branch": target_branch.strip(),
        "status": "READY",
    }
