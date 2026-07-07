#!/usr/bin/env python3
"""Deterministic local report-only runner for HC Multi-AI Council outputs.

This module intentionally avoids network calls, LLM calls, subprocess execution,
repository writes, labels, assignments, approvals, merges, and issue closure.
It turns local fixtures into public-safe advisory JSON suitable for hashing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

HASH_ALGORITHM = "sha256"
SCHEMA_VERSION = "0.1"


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _as_str_list(value: Any) -> list[str]:
    return sorted({str(item) for item in _as_list(value) if str(item).strip()})


def _as_optional_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _as_optional_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return None
    return parsed if parsed > 0 else None


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _canonical_json(value: dict[str, Any]) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _normalize_session(value: Any) -> dict[str, Any]:
    session = value if isinstance(value, dict) else {}
    source = str(session.get("source") or "local_fixture")
    allowed_sources = {
        "manual_command",
        "calendar_or_command",
        "calendar_event",
        "google_chat",
        "github_issue",
        "local_fixture",
    }
    if source not in allowed_sources:
        source = "local_fixture"
    return {
        "source": source,
        "meeting_link": _as_optional_str(session.get("meeting_link")),
        "started_at": _as_optional_str(session.get("started_at")),
    }


def _normalize_model_output(value: Any) -> dict[str, Any]:
    item = value if isinstance(value, dict) else {}
    role = str(item.get("role") or "unassigned_reviewer")
    provider = str(item.get("provider") or "local_fixture")
    model = str(item.get("model") or "unknown")
    output = str(item.get("output") or "")
    prompt = _as_optional_str(item.get("prompt"))
    uncertainty = str(item.get("uncertainty") or "unknown")
    if uncertainty not in {"low", "medium", "high", "unknown"}:
        uncertainty = "unknown"

    return {
        "role": role,
        "provider": provider,
        "model": model,
        "output": output,
        "evidence_refs": _as_str_list(item.get("evidence_refs", [])),
        "uncertainty": uncertainty,
        "prompt_sha256": None if prompt is None else _sha256_text(prompt),
        "output_sha256": _sha256_text(output),
    }


def _normalize_model_outputs(value: Any) -> list[dict[str, Any]]:
    return [_normalize_model_output(item) for item in _as_list(value)]


def _build_unsigned_run(fixture: dict[str, Any]) -> dict[str, Any]:
    synthesis = fixture.get("synthesis")
    if not isinstance(synthesis, dict):
        synthesis = {}

    return {
        "schema_version": SCHEMA_VERSION,
        "mode": "report_only",
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "operator": "human_supervised",
        "repository": str(fixture.get("repository") or ""),
        "session": _normalize_session(fixture.get("session", {})),
        "inputs": {
            "command": _as_optional_str(fixture.get("command")),
            "repo_ref": _as_optional_str(fixture.get("repo_ref")),
            "pr_number": _as_optional_int(fixture.get("pr_number")),
            "evidence_refs": _as_str_list(fixture.get("evidence_refs", [])),
        },
        "model_outputs": _normalize_model_outputs(fixture.get("model_outputs", [])),
        "synthesis": {
            "summary": _as_optional_str(synthesis.get("summary")),
            "risks": _as_str_list(synthesis.get("risks", [])),
            "next_safe_actions": _as_str_list(synthesis.get("next_safe_actions", [])),
            "blocked_items": _as_str_list(synthesis.get("blocked_items", [])),
        },
        "verification": {
            "output_sha256": None,
            "advisory_only": True,
            "truth_guarantee": False,
            "hash_algorithm": HASH_ALGORITHM,
        },
    }


def build_council_run(fixture: dict[str, Any]) -> dict[str, Any]:
    """Build a deterministic report-only council run from a local fixture."""

    run = _build_unsigned_run(fixture)
    unsigned = deepcopy(run)
    unsigned["verification"]["output_sha256"] = None
    run["verification"]["output_sha256"] = _sha256_text(_canonical_json(unsigned))
    return run


def verify_output_hash(run: dict[str, Any]) -> bool:
    """Verify the self-hash by excluding verification.output_sha256 itself."""

    expected = run.get("verification", {}).get("output_sha256")
    unsigned = deepcopy(run)
    if isinstance(unsigned.get("verification"), dict):
        unsigned["verification"]["output_sha256"] = None
    return expected == _sha256_text(_canonical_json(unsigned))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a deterministic HC Council report-only JSON bundle."
    )
    parser.add_argument("fixture", help="Path to a local HC Council JSON fixture.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    run = build_council_run(fixture)
    indent = 2 if args.pretty else None
    print(json.dumps(run, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
