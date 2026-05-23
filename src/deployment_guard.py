"""HC:// deployment hardening guard."""

from __future__ import annotations

REQUIRED_DEPLOYMENT_FIELDS = {
    "deployment_id",
    "source_ref",
    "artifact_hash",
    "environment",
}

ALLOWED_ENVIRONMENTS = {"dev", "staging", "production"}


def deployment_manifest_valid(manifest: dict) -> bool:
    return REQUIRED_DEPLOYMENT_FIELDS.issubset(manifest.keys())


def environment_allowed(environment: str) -> bool:
    return environment.strip().lower() in ALLOWED_ENVIRONMENTS


def build_deployment_decision(manifest: dict) -> dict:
    env = str(manifest.get("environment", "")).strip().lower()
    allowed = deployment_manifest_valid(manifest) and environment_allowed(env)
    return {
        "deployment_id": manifest.get("deployment_id", ""),
        "environment": env,
        "allowed": allowed,
        "reason": "deployment manifest accepted" if allowed else "deployment manifest rejected",
    }
