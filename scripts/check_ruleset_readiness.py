#!/usr/bin/env python3
"""Local, advisory GitHub ruleset readiness reporter for HC-TRUST-LAYER."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_CHECK_CANDIDATES = [
    {"name": "terminology", "workflow": ".github/workflows/terminology.yml"},
    {"name": "docs-drift", "workflow": ".github/workflows/docs-drift.yml"},
    {"name": "canonical-artifacts", "workflow": ".github/workflows/canonical-artifacts.yml"},
    {"name": "governance-preflight", "workflow": ".github/workflows/governance-preflight.yml"},
]

NOT_REQUIRED_READY_CHECKS = [
    {"name": "validate", "workflow": ".github/workflows/validate.yml", "status": "path_filtered"},
    {"name": "pr-scope-guard", "workflow": ".github/workflows/pr-scope-guard.yml", "status": "advisory_continue_on_error"},
]

PROTECTED_SURFACES = [
    ".github/CODEOWNERS",
    "CODEOWNERS",
    "protocol-graph.json",
    "verification-map.json",
    "trust-kernel-index.json",
    ".github/workflows/",
    "docs/project-control/",
    "docs/governance/",
    "scripts/",
    "src/",
    "tests/",
    "records/",
    "schema/",
    "validators/",
    "policy/",
    "signatures/",
    "federation/",
]


def _workflow_entries(repo_root: Path, checks: list[dict[str, str]]) -> list[dict[str, Any]]:
    return [
        {
            "name": check["name"],
            "workflow": check["workflow"],
            "workflow_exists": (repo_root / check["workflow"]).is_file(),
            **({"status": check["status"]} if "status" in check else {}),
        }
        for check in checks
    ]


def build_report(repo_root: Path) -> dict[str, Any]:
    required_candidates = _workflow_entries(repo_root, REQUIRED_CHECK_CANDIDATES)
    not_required_ready = _workflow_entries(repo_root, NOT_REQUIRED_READY_CHECKS)
    return {
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": True,
        "settings_verified_locally": False,
        "github_api_called": False,
        "mutates_repository_settings": False,
        "required_check_candidates": required_candidates,
        "not_required_ready_checks": not_required_ready,
        "protected_surfaces": PROTECTED_SURFACES,
        "missing_workflow_files": [item["workflow"] for item in required_candidates if not item["workflow_exists"]],
        "note": "GitHub branch protection and ruleset enforcement cannot be verified or changed by this local checker.",
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# HC GitHub Ruleset Readiness Report",
        "",
        f"- advisory_only={str(report['advisory_only']).lower()}",
        f"- public_safe={str(report['public_safe']).lower()}",
        f"- truth_guarantee={str(report['truth_guarantee']).lower()}",
        f"- human_review_required={str(report['human_review_required']).lower()}",
        f"- settings_verified_locally={str(report['settings_verified_locally']).lower()}",
        "",
        "## Required-check candidates",
        "",
        "| Check | Workflow | Exists |",
        "| --- | --- | --- |",
    ]
    for item in report["required_check_candidates"]:
        lines.append(f"| {item['name']} | `{item['workflow']}` | {str(item['workflow_exists']).lower()} |")
    lines.extend(["", "## Not required-ready checks", "", "| Check | Workflow | Status |", "| --- | --- | --- |"])
    for item in report["not_required_ready_checks"]:
        lines.append(f"| {item['name']} | `{item['workflow']}` | {item['status']} |")
    lines.extend(["", "## Protected surfaces", ""])
    lines.extend(f"- `{surface}`" for surface in report["protected_surfaces"])
    if report["missing_workflow_files"]:
        lines.extend(["", "## Missing workflow files", ""])
        lines.extend(f"- `{path}`" for path in report["missing_workflow_files"])
    lines.extend(["", report["note"]])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Report local HC GitHub ruleset readiness.")
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    args = parser.parse_args()
    report = build_report(Path(args.repo).resolve())
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_markdown(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())