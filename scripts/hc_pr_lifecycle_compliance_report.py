#!/usr/bin/env python3
"""Report-only HC PR lifecycle compliance evidence generator."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

PROTECTED_PREFIXES: tuple[str, ...] = (
    ".github/",
    "validators/",
    "src/hc_runtime/",
    "records/",
    "docs/project-control/",
    "schema/",
    "policy/",
    "federation/",
    "signing/",
    "signatures/",
    "canonical/",
    "generated/",
)

PROTECTED_FILES: tuple[str, ...] = (
    "CODEOWNERS",
    ".github/CODEOWNERS",
    "protocol-graph.json",
    "verification-map.json",
    "trust-kernel-index.json",
)

DEPENDENCY_FILES: tuple[str, ...] = (
    "package.json",
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "requirements.txt",
    "requirements-dev.txt",
    "pyproject.toml",
    "poetry.lock",
    "Pipfile",
    "Pipfile.lock",
)

CANONICAL_ROOT_FILES: tuple[str, ...] = (
    "protocol-graph.json",
    "verification-map.json",
    "trust-kernel-index.json",
)


@dataclass(frozen=True)
class LifecycleReport:
    report_name: str
    report_version: str
    advisory_only: bool
    report_only: bool
    public_safe: bool
    truth_guarantee: bool
    human_review_required: bool
    approval_authority: bool
    merge_authority: bool
    label_authority: bool
    reviewer_request_authority: bool
    assignment_authority: bool
    issue_mutation_authority: bool
    thread_resolution_authority: bool
    governance_mutation_authority: bool
    changed_file_count: int
    evidence_missing: bool
    protected_path_touched: bool
    workflow_or_bot_surface_touched: bool
    validator_surface_touched: bool
    runtime_surface_touched: bool
    records_surface_touched: bool
    codeowners_touched: bool
    project_control_surface_touched: bool
    canonical_root_artifact_touched: bool
    generated_or_canonical_surface_touched: bool
    dependency_surface_touched: bool
    blockers_for_human_review: list[str]
    not_evaluated: list[str]
    changed_files: list[str]


def _normalize_path(path: str) -> str:
    return path.strip().replace("\\", "/").lstrip("./")


def _under(path: str, prefix: str) -> bool:
    return path == prefix.rstrip("/") or path.startswith(prefix)


def _any_under(path: str, prefixes: Iterable[str]) -> bool:
    return any(_under(path, prefix) for prefix in prefixes)


def is_dependency_path(path: str) -> bool:
    name = Path(path).name
    return path in DEPENDENCY_FILES or name in DEPENDENCY_FILES


def is_protected_path(path: str) -> bool:
    return path in PROTECTED_FILES or _any_under(path, PROTECTED_PREFIXES) or is_dependency_path(path)


def read_changed_files(path: Path) -> tuple[list[str], bool]:
    if not path.exists():
        return [], True
    files = sorted({_normalize_path(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()})
    return files, False


def build_report(changed_files: list[str], *, evidence_missing: bool = False) -> LifecycleReport:
    protected = any(is_protected_path(path) for path in changed_files)
    workflow_or_bot = any(path.startswith(".github/") or "bot" in path.lower() for path in changed_files)
    validators = any(path.startswith("validators/") for path in changed_files)
    runtime = any(path.startswith("src/hc_runtime/") for path in changed_files)
    records = any(path.startswith("records/") for path in changed_files)
    codeowners = any(path in {"CODEOWNERS", ".github/CODEOWNERS"} for path in changed_files)
    project_control = any(path.startswith("docs/project-control/") for path in changed_files)
    canonical_root = any(path in CANONICAL_ROOT_FILES for path in changed_files)
    generated_or_canonical = any(path.startswith(("canonical/", "generated/")) for path in changed_files) or canonical_root
    dependency = any(is_dependency_path(path) for path in changed_files)

    blockers: list[str] = []
    if evidence_missing:
        blockers.append("changed file evidence is missing; human review should evaluate PR scope")
    if protected:
        blockers.append("protected_path_touched=true; human review should evaluate the protected surface")

    not_evaluated = []
    if evidence_missing:
        not_evaluated.append("changed_files")

    return LifecycleReport(
        report_name="HC Control Bot PR Lifecycle Compliance Report",
        report_version="1.0",
        advisory_only=True,
        report_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=evidence_missing or protected,
        approval_authority=False,
        merge_authority=False,
        label_authority=False,
        reviewer_request_authority=False,
        assignment_authority=False,
        issue_mutation_authority=False,
        thread_resolution_authority=False,
        governance_mutation_authority=False,
        changed_file_count=len(changed_files),
        evidence_missing=evidence_missing,
        protected_path_touched=protected or evidence_missing,
        workflow_or_bot_surface_touched=workflow_or_bot,
        validator_surface_touched=validators,
        runtime_surface_touched=runtime,
        records_surface_touched=records,
        codeowners_touched=codeowners,
        project_control_surface_touched=project_control,
        canonical_root_artifact_touched=canonical_root,
        generated_or_canonical_surface_touched=generated_or_canonical,
        dependency_surface_touched=dependency,
        blockers_for_human_review=blockers,
        not_evaluated=not_evaluated,
        changed_files=changed_files,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate advisory PR lifecycle compliance report evidence.")
    parser.add_argument("--changed-files", type=Path, default=Path("changed-files.txt"))
    parser.add_argument("--output", type=Path, default=Path("hc-pr-lifecycle-compliance-report.json"))
    args = parser.parse_args()

    changed_files, missing = read_changed_files(args.changed_files)
    report = build_report(changed_files, evidence_missing=missing)
    args.output.write_text(json.dumps(asdict(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(asdict(report), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
