#!/usr/bin/env python3
"""Advisory governance-aware PR validation preflight for HC-TRUST-LAYER."""

from __future__ import annotations

import argparse
import subprocess
from dataclasses import dataclass
from enum import Enum

PROTECTED_PREFIXES: tuple[str, ...] = (
    "schema/",
    "validators/",
    "signatures/",
    "policy/",
    "federation/",
    ".github/workflows/",
    "src/hc_runtime/",
    "records/",
)
PROTECTED_FILES: tuple[str, ...] = (
    "CODEOWNERS",
    "protocol-graph.json",
    "verification-map.json",
    "trust-kernel-index.json",
)

DOC_PREFIXES: tuple[str, ...] = ("docs/",)
DOC_FILES: tuple[str, ...] = ("README.md", "CHANGELOG.md", "GOVERNANCE.md")
TEST_PREFIXES: tuple[str, ...] = ("tests/",)
DEPENDENCY_FILES: tuple[str, ...] = (
    "requirements.txt",
    "requirements-dev.txt",
    "pyproject.toml",
    "poetry.lock",
    "Pipfile",
    "Pipfile.lock",
)


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(frozen=True)
class GovernanceSummary:
    risk: RiskLevel
    auto_merge_eligible: bool
    human_review_required: bool
    protected_paths_touched: bool
    docs_only: bool
    dependency_only: bool
    tests_only: bool
    override_reason: str | None


def run_git_diff(base_ref: str, head_ref: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...{head_ref}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def _is_in_prefix(path: str, prefix: str) -> bool:
    return path == prefix or path.startswith(prefix)


def _matches_any(path: str, prefixes: tuple[str, ...]) -> bool:
    return any(_is_in_prefix(path, prefix) for prefix in prefixes)


def is_protected_path(path: str) -> bool:
    return path in PROTECTED_FILES or _matches_any(path, PROTECTED_PREFIXES)


def is_doc_path(path: str) -> bool:
    return path in DOC_FILES or _matches_any(path, DOC_PREFIXES)


def is_dependency_path(path: str) -> bool:
    return path in DEPENDENCY_FILES


def is_test_path(path: str) -> bool:
    return _matches_any(path, TEST_PREFIXES)


def summarize_governance(changed_paths: list[str]) -> GovernanceSummary:
    if not changed_paths:
        return GovernanceSummary(
            risk=RiskLevel.LOW,
            auto_merge_eligible=True,
            human_review_required=False,
            protected_paths_touched=False,
            docs_only=True,
            dependency_only=False,
            tests_only=False,
            override_reason=None,
        )

    protected_paths_touched = any(is_protected_path(path) for path in changed_paths)
    docs_only = all(is_doc_path(path) for path in changed_paths)
    dependency_only = all(is_dependency_path(path) for path in changed_paths)
    tests_only = all(is_test_path(path) for path in changed_paths)

    low_risk_candidate = (docs_only or dependency_only or tests_only) and not protected_paths_touched

    if protected_paths_touched:
        risk = RiskLevel.HIGH
    elif low_risk_candidate:
        risk = RiskLevel.LOW
    else:
        risk = RiskLevel.MEDIUM

    auto_merge_eligible = risk == RiskLevel.LOW
    human_review_required = risk != RiskLevel.LOW

    return GovernanceSummary(
        risk=risk,
        auto_merge_eligible=auto_merge_eligible,
        human_review_required=human_review_required,
        protected_paths_touched=protected_paths_touched,
        docs_only=docs_only,
        dependency_only=dependency_only,
        tests_only=tests_only,
        override_reason=None,
    )


def apply_label_overrides(summary: GovernanceSummary, labels: set[str]) -> GovernanceSummary:
    normalized = {label.strip().lower() for label in labels if label.strip()}
    if not normalized:
        return summary

    override_reason: str | None = None
    if "manual-review" in normalized and "auto-merge" in normalized:
        override_reason = (
            "label-conflict: manual-review overrides auto-merge; "
            "auto-merge cancelled and human-supervised validation required"
        )
    elif "risk-high" in normalized and "auto-merge" in normalized:
        override_reason = (
            "label-conflict: risk-high is not eligible for auto-merge; "
            "human-supervised validation required"
        )
    elif "blocked-human-review" in normalized and "auto-merge" in normalized:
        override_reason = (
            "label-conflict: blocked-human-review disallows auto-merge; "
            "human-supervised validation required"
        )

    if override_reason is None:
        return summary

    return GovernanceSummary(
        risk=summary.risk,
        auto_merge_eligible=False,
        human_review_required=True,
        protected_paths_touched=summary.protected_paths_touched,
        docs_only=summary.docs_only,
        dependency_only=summary.dependency_only,
        tests_only=summary.tests_only,
        override_reason=override_reason,
    )


def _as_yes_no(value: bool) -> str:
    return "yes" if value else "no"


def render_summary(summary: GovernanceSummary, changed_paths: list[str]) -> None:
    protected_paths = [path for path in changed_paths if is_protected_path(path)]

    print("HC-TRUST-LAYER governance preflight (advisory)")
    print("HUMAN_READABLE_SUMMARY:")
    print(f"- Risk level: {summary.risk.value}")
    print(f"- Auto-merge eligible: {_as_yes_no(summary.auto_merge_eligible)}")
    print(f"- Human review required: {_as_yes_no(summary.human_review_required)}")
    print(f"- Protected paths touched: {_as_yes_no(summary.protected_paths_touched)}")
    if protected_paths:
        print("- Protected path list:")
        for path in protected_paths:
            print(f"  - {path}")
    else:
        print("- Protected path list: none")
    if summary.override_reason:
        print(f"- Override reason: {summary.override_reason}")
    else:
        print("- Override reason: none")

    print("MACHINE_READABLE_SUMMARY:")
    print(f"CHANGED_PATH_COUNT: {len(changed_paths)}")
    print(f"DOCS_ONLY: {_as_yes_no(summary.docs_only)}")
    print(f"DEPENDENCY_ONLY: {_as_yes_no(summary.dependency_only)}")
    print(f"TESTS_ONLY: {_as_yes_no(summary.tests_only)}")
    print(f"RISK: {summary.risk.value}")
    print(f"AUTO_MERGE_ELIGIBLE: {_as_yes_no(summary.auto_merge_eligible)}")
    print(f"HUMAN_REVIEW_REQUIRED: {_as_yes_no(summary.human_review_required)}")
    print(f"PROTECTED_PATHS_TOUCHED: {_as_yes_no(summary.protected_paths_touched)}")
    if summary.override_reason:
        print(f"OVERRIDE_REASON: {summary.override_reason}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Advisory governance PR preflight checker.")
    parser.add_argument("--base-ref", default="origin/main", help="Base git ref for PR diff.")
    parser.add_argument("--head-ref", default="HEAD", help="Head git ref for PR diff.")
    parser.add_argument(
        "--files",
        nargs="*",
        help="Optional explicit file list; when provided, git diff is skipped.",
    )
    parser.add_argument(
        "--labels",
        nargs="*",
        default=[],
        help="Optional PR labels used for advisory conflict handling.",
    )
    args = parser.parse_args()

    changed_paths = args.files if args.files is not None else run_git_diff(args.base_ref, args.head_ref)
    summary = summarize_governance(changed_paths)
    summary = apply_label_overrides(summary, set(args.labels))
    render_summary(summary, changed_paths)
    print(
        "ADVISORY: This preflight is a governance control-layer signal only; "
        "human-supervised validation retains merge authority."
    )
    if summary.human_review_required:
        print("REVIEW_REQUIRED: manual-only paths require human-supervised validation before merge.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
