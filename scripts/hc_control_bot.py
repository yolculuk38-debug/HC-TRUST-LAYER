#!/usr/bin/env python3
"""Deterministic advisory scanner for HC Control Bot v0.1.

This module intentionally avoids network calls, LLM calls, semantic PR review,
workflow actions, labels, and repository writes. It only classifies changed file
paths against a small protected-surface map and returns a public-safe advisory
result.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
from dataclasses import dataclass
from typing import Iterable


PROTECTED_PATTERNS: tuple[str, ...] = (
    ".github/workflows/**",
    "schema/**",
    "validators/**",
    "src/hc_runtime/**",
    "records/**",
    "signatures/**",
    "policy/**",
    "federation/**",
    "docs/governance/**",
    "docs/project-control/**",
    "scripts/hc_control_bot.py",
)

GOVERNANCE_ADJACENT_PATTERNS: tuple[str, ...] = (
    "AGENTS.md",
    "HC_BOOTSTRAP.md",
    "CODEOWNERS",
    ".github/CODEOWNERS",
    "docs/branch-protection.md",
    "docs/START_HERE.md",
    "README.md",
)

GENERATED_ARTIFACT_PATTERNS: tuple[str, ...] = (
    "generated/**",
    "records/**/explorer_index.json",
    "**/explorer_index.json",
    "**/*manifest*.json",
    "**/*cache*.json",
    "**/*export*.json",
)

REVIEW_ROUTE_PATTERNS: tuple[tuple[str, str], ...] = (
    (".github/workflows/**", "workflow-automation-review"),
    ("src/hc_runtime/**", "runtime-contract-review"),
    ("validators/**", "validator-review"),
    ("schema/**", "schema-compatibility-review"),
    ("records/**", "record-boundary-review"),
    ("docs/governance/**", "governance-review"),
    ("docs/project-control/**", "project-control-review"),
    ("policy/**", "policy-review"),
    ("federation/**", "federation-review"),
    ("generated/**", "generated-artifact-review"),
)


@dataclass(frozen=True)
class ScanResult:
    """Machine-readable advisory result for changed path scanning."""

    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    human_review_required: bool
    protected_paths_touched: list[str]
    governance_adjacent_paths_touched: list[str]
    generated_artifacts_observed: list[str]
    warnings: list[str]
    evidence_prompts: list[str]
    review_routes: list[str]
    evidence_source: str

    def to_dict(self) -> dict[str, object]:
        return {
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "human_review_required": self.human_review_required,
            "protected_paths_touched": self.protected_paths_touched,
            "governance_adjacent_paths_touched": self.governance_adjacent_paths_touched,
            "generated_artifacts_observed": self.generated_artifacts_observed,
            "warnings": self.warnings,
            "evidence_prompts": self.evidence_prompts,
            "review_routes": self.review_routes,
            "evidence_source": self.evidence_source,
        }


def _normalize_path(path: str) -> str:
    return path.strip().replace("\\", "/").lstrip("/")


def _matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def _dedupe_sorted(values: Iterable[str]) -> list[str]:
    return sorted(set(values))


def _build_review_routes(paths: Iterable[str]) -> list[str]:
    routes: list[str] = []
    for path in paths:
        for pattern, route in REVIEW_ROUTE_PATTERNS:
            if fnmatch.fnmatch(path, pattern):
                routes.append(route)
    return _dedupe_sorted(routes)


def _build_evidence_prompts(
    protected_paths: list[str],
    governance_adjacent_paths: list[str],
    generated_artifacts: list[str],
) -> list[str]:
    prompts: list[str] = []

    if protected_paths:
        prompts.append("Provide reviewer evidence for protected or trust-kernel-adjacent paths.")
    if governance_adjacent_paths:
        prompts.append("Provide maintainer rationale for governance-adjacent changes.")
    if generated_artifacts:
        prompts.append("Identify the canonical source and reproduction method for generated artifacts.")
    if any(path.startswith(".github/workflows/") for path in protected_paths):
        prompts.append("Confirm workflow changes do not run untrusted PR branch code.")
    if any(path.startswith("src/hc_runtime/") for path in protected_paths):
        prompts.append("Provide runtime test output or response-contract examples.")
    if any(path.startswith("validators/") for path in protected_paths):
        prompts.append("Provide validator test output including malformed-input behavior.")
    if any(path.startswith("schema/") for path in protected_paths):
        prompts.append("Provide schema compatibility notes and example records.")

    return _dedupe_sorted(prompts)


def scan_changed_paths(changed_paths: Iterable[str]) -> ScanResult:
    """Classify changed paths without reading PR text or file contents."""

    normalized_paths = sorted(
        {
            normalized
            for raw_path in changed_paths
            if (normalized := _normalize_path(raw_path))
        }
    )

    protected_paths = [
        path for path in normalized_paths if _matches_any(path, PROTECTED_PATTERNS)
    ]
    governance_adjacent_paths = [
        path for path in normalized_paths if _matches_any(path, GOVERNANCE_ADJACENT_PATTERNS)
    ]
    generated_artifacts = [
        path for path in normalized_paths if _matches_any(path, GENERATED_ARTIFACT_PATTERNS)
    ]

    warnings: list[str] = []
    if protected_paths:
        warnings.append("Protected or trust-kernel-adjacent path observed.")
    if governance_adjacent_paths:
        warnings.append("Governance-adjacent path observed.")
    if generated_artifacts:
        warnings.append("Generated artifact path observed; do not treat as canonical record by default.")

    evidence_prompts = _build_evidence_prompts(
        protected_paths,
        governance_adjacent_paths,
        generated_artifacts,
    )
    review_routes = _build_review_routes(normalized_paths)

    return ScanResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=bool(protected_paths or governance_adjacent_paths),
        protected_paths_touched=protected_paths,
        governance_adjacent_paths_touched=governance_adjacent_paths,
        generated_artifacts_observed=generated_artifacts,
        warnings=warnings,
        evidence_prompts=evidence_prompts,
        review_routes=review_routes,
        evidence_source="changed file path metadata only",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run deterministic HC Control Bot path scanning."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Changed repository paths to classify.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = scan_changed_paths(args.paths).to_dict()
    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
