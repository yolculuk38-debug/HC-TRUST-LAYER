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
            "evidence_source": self.evidence_source,
        }


def _normalize_path(path: str) -> str:
    return path.strip().replace("\\", "/").lstrip("/")


def _matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


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

    return ScanResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=bool(protected_paths or governance_adjacent_paths),
        protected_paths_touched=protected_paths,
        governance_adjacent_paths_touched=governance_adjacent_paths,
        generated_artifacts_observed=generated_artifacts,
        warnings=warnings,
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
