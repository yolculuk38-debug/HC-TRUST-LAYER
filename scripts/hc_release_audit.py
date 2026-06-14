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
PR_REFERENCE_RE = re.compile(r"#\d+|pull/\d+")
PR_REFERENCE_EVIDENCE_PATHS = ("CHANGELOG.md", "docs/project-control/task-ledger.md")


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


def _changed_files(repo_root: Path, base_ref: str | None = None, head_ref: str | None = None) -> list[str]:
    if base_ref and head_ref:
        return sorted(set(_run_git(repo_root, ["diff", "--name-only", f"{base_ref}...{head_ref}"])))

    files = set(_run_git(repo_root, ["diff", "--name-only", "HEAD"]))
    files.update(_run_git(repo_root, ["diff", "--cached", "--name-only"]))
    return sorted(files)


def _diff_lines(repo_root: Path, base_ref: str | None = None, head_ref: str | None = None) -> list[str]:
    if base_ref and head_ref:
        return _run_git(repo_root, ["diff", "--unified=0", f"{base_ref}...{head_ref}"])
    diff_lines = _run_git(repo_root, ["diff", "--unified=0", "HEAD"])
    diff_lines.extend(_run_git(repo_root, ["diff", "--cached", "--unified=0"]))
    return diff_lines


def _release_evidence_added_lines(repo_root: Path, base_ref: str | None = None, head_ref: str | None = None) -> str:
    added_lines: list[str] = []
    current_path: str | None = None
    for line in _diff_lines(repo_root, base_ref=base_ref, head_ref=head_ref):
        if line.startswith("+++ b/"):
            current_path = line.removeprefix("+++ b/")
            continue
        if line.startswith("+++ "):
            current_path = None
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        if current_path in PR_REFERENCE_EVIDENCE_PATHS:
            added_lines.append(line[1:])
    return "\n".join(added_lines)


def _read_text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _is_release_path(path: str) -> bool:
    return path in RELEASE_PATH_PATTERNS or any(path.startswith(prefix) for prefix in RELEASE_PATH_PATTERNS)


def build_report(
    repo_root: Path,
    base_ref: str | None = None,
    head_ref: str | None = None,
    pr_number: str | None = None,
) -> dict[str, Any]:
    changed = _changed_files(repo_root, base_ref=base_ref, head_ref=head_ref)
    release_files_changed = [path for path in changed if _is_release_path(path)]
    changelog_text = _read_text(repo_root / "CHANGELOG.md")
    task_ledger_text = _read_text(repo_root / "docs/project-control/task-ledger.md")
    release_evidence_added_lines = _release_evidence_added_lines(repo_root, base_ref=base_ref, head_ref=head_ref)

    changelog_evidence = bool(changelog_text.strip())
    task_ledger_evidence = bool(task_ledger_text.strip())
    pr_reference_evidence = bool(pr_number) or bool(PR_REFERENCE_RE.search(release_evidence_added_lines))

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
        "base_ref": base_ref,
        "head_ref": head_ref,
        "pr_number": pr_number,
        "diff_mode": "ref_range" if base_ref and head_ref else "worktree",
        "pr_reference_evidence_paths": list(PR_REFERENCE_EVIDENCE_PATHS),
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
        f"- diff_mode={report['diff_mode']}",
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
    parser.add_argument("--base-ref", default=None, help="Optional base ref/SHA for committed PR diff evidence.")
    parser.add_argument("--head-ref", default=None, help="Optional head ref/SHA for committed PR diff evidence.")
    parser.add_argument("--pr-number", default=None, help="Optional current PR number supplied by CI.")
    args = parser.parse_args()
    report = build_report(Path(args.repo).resolve(), base_ref=args.base_ref, head_ref=args.head_ref, pr_number=args.pr_number)
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_markdown(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
