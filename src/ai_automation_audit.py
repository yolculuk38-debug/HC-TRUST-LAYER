"""HC:// AI automation audit core.

Creates deterministic audit records for AI agents, workflows, and automated
execution chains. This module records metadata only and never executes agents.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


AI_AUDIT_VERSION = "HC-AI-AUTOMATION-AUDIT-V1"
SUPPORTED_AGENT_TYPES = {"llm_agent", "workflow", "scheduler", "automation", "review_agent"}


class AutomationAuditStatus:
    VERIFIED = "VERIFIED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    INVALID = "INVALID"


def canonical_json(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def audit_hash(record: dict[str, Any]) -> str:
    normalized = dict(record)
    normalized.pop("audit_hash", None)
    return hashlib.sha256(canonical_json(normalized).encode("utf-8")).hexdigest()


def create_automation_audit_record(
    audit_id: str,
    agent_type: str,
    workflow_name: str,
    observed_at: str,
    *,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    record = {
        "ai_audit_version": AI_AUDIT_VERSION,
        "audit_id": audit_id,
        "agent_type": agent_type,
        "workflow_name": workflow_name,
        "observed_at": observed_at,
        "metadata": metadata or {},
    }
    record["audit_hash"] = audit_hash(record)
    return record


def verify_automation_audit_record(record: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(record, dict):
        return {"status": AutomationAuditStatus.INVALID, "reason": "record must be an object"}

    required = {
        "ai_audit_version",
        "audit_id",
        "agent_type",
        "workflow_name",
        "observed_at",
        "audit_hash",
    }
    missing = required.difference(record)
    if missing:
        return {
            "status": AutomationAuditStatus.INVALID,
            "reason": f"missing required field(s): {', '.join(sorted(missing))}",
        }

    if record["ai_audit_version"] != AI_AUDIT_VERSION:
        return {"status": AutomationAuditStatus.INVALID, "reason": "unsupported audit version"}

    if record["agent_type"] not in SUPPORTED_AGENT_TYPES:
        return {"status": AutomationAuditStatus.INVALID, "reason": "unsupported agent type"}

    expected = audit_hash(record)
    if expected != record["audit_hash"]:
        return {"status": AutomationAuditStatus.INVALID, "reason": "audit hash mismatch"}

    flags = []
    metadata = record.get("metadata", {})

    if metadata.get("network_access"):
        flags.append("network_access")

    if metadata.get("filesystem_write"):
        flags.append("filesystem_write")

    if metadata.get("auto_execute"):
        flags.append("auto_execute")

    if metadata.get("external_tools"):
        flags.append("external_tools")

    if flags:
        return {
            "status": AutomationAuditStatus.REVIEW_REQUIRED,
            "review_flags": flags,
            "reason": "automation workflow requires additional review",
        }

    return {
        "status": AutomationAuditStatus.VERIFIED,
        "reason": "automation audit record verified",
    }


__all__ = [
    "AI_AUDIT_VERSION",
    "SUPPORTED_AGENT_TYPES",
    "AutomationAuditStatus",
    "create_automation_audit_record",
    "verify_automation_audit_record",
    "audit_hash",
]
