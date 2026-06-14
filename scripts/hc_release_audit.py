#!/usr/bin/env python3
"""Deterministic local release audit reporter for HC-TRUST-LAYER.

The audit is report-only. It inspects local files and git metadata when
available. It does not publish releases, create tags, modify changelogs, or
claim release readiness without human review.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

RELEASE_EVIDENCE_FILES = ["CHANGELOG.md", "VERSION", "docs/project-control/task-ledger.md"]
RELEASE_PATH_PATTERNS = ("CHANGELOG.md", "VERSION", "docs/project-control/", ".github/workflows/release")


def _run_git(repo_root: Path, args: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", *args], cwd=repo_root, check=False, capture_output=True, text=True, timeout=10
        )
    except (OSError, subprocess.TimeoutExpired):
        return []
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def _changed_files(repo_root: Path) -> list[str]:
    files = set(_run_git(repo_root, ["diff", "--name-only", "HEAD"]))
    files.update(_run_git(repo_root, ["diff", "--cached", "--name-only"]))
    return sorted(files)


def _read_text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def build_report(repo_root: Path) -> dict[str, Any]:
    changed = _changed_files(repo_root)
    release_files_changed = [
        path for path in changed if path in RELEASE_PATH_PATTERNS or any(path.startswith(prefix) for prefix in RELEASE_PATH_PATTERNS)
    ]
    changelog_text = _read_text(repo_root / "CHANGELOG.md")
    task_ledger_text = _read_text(repo_root / "docs/project-control/task-ledger.md")
    combined = changelog_text + "\n" + task_ledger_text + "\n" + "\n".join(changed)

    changelog_evidence = bool(changelog_text.strip())
    task_ledger_evidence = bool(task_ledger_text.strip())
    pr_reference_evidence = bool(re.search(r"#\d+|pull/\d+", combined))

    missing_evidence = []
    for evidence_file in RELEASE_EVIDENCE_FILES:
        if not (repo_root / evidence_file).is_file():
            missing_evidence.append(evidence_file)
    if not changelog_evidence:
        missing_evidence.append("changelog_evidence")
    if not task_ledger_evidence:
        missing_evidence.append("task_ledger_evidence")
    if release_files_changed and not pr_reference_evidence:
        missing_evidence.append("pr_reference_evidence")

    evidence_complete = not missing_evidence and (not release_files_changed or pr_reference_evidence)
    return {
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "publishes_release": False,
        "creates_tags": False,
        "modifies_changelog": False,
        "release_files_changed": release_files_changed,
        "changelog_evidence": changelog_evidence,
        "task_ledger_evidence": task_ledger_evidence,
        "pr_reference_evidence": pr_reference_evidence,
        "missing_evidence": missing_evidence,
        "human_review_required": True,
        "evidence_complete": evidence_complete,
        "merge_ready": False,
        "note": "Release audit evidence is advisory and cannot establish release readiness without human final authority.",
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# HC Release Audit Report",
        "",
        f"- advisory_only={str(report['advisory_only']).lower()}",
        f"- public_safe={str(report['public_safe']).lower()}",
        f"- truth_guarantee={str(report['truth_guarantee']).lower()}",
        f"- human_review_required={str(report['human_review_required']).lower()}",
        f"- merge_ready={str(report['merge_ready']).lower()}",
        "",
        "## Evidence",
        "",
        f"- changelog_evidence={str(report['changelog_evidence']).lower()}",
        f"- task_ledger_evidence={str(report['task_ledger_evidence']).lower()}",
        f"- pr_reference_evidence={str(report['pr_reference_evidence']).lower()}",
        "",
        "## Release files changed",
        "",
    ]
    lines.extend(f"- `{path}`" for path in report["release_files_changed"] or ["none"])
    lines.extend(["", "## Missing evidence", ""])
    lines.extend(f"- `{item}`" for item in report["missing_evidence"] or ["none"])
    lines.extend(["", report["note"]])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local HC release audit.")
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
