#!/usr/bin/env python3
"""PR scope boundary guard for HC-TRUST-LAYER pull requests."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

PROTECTED_PREFIXES = (
    "schema/",
    "validators/",
    "federation/",
    "signatures/",
    "canonical/",
    "policy/",
)

DOCS_ONLY_ALLOWED_PREFIXES = (
    "docs/",
    "scripts/check_pr_scope.py",
)


def run_git_diff(base_ref: str, head_ref: str) -> list[str]:
    cmd = ["git", "diff", "--name-only", f"{base_ref}...{head_ref}"]
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def is_prefix_match(path: str, prefix: str) -> bool:
    return path == prefix or path.startswith(prefix)


def in_any_prefix(path: str, prefixes: tuple[str, ...]) -> bool:
    return any(is_prefix_match(path, prefix) for prefix in prefixes)


def render_list(title: str, items: list[str]) -> None:
    print(title)
    if not items:
        print("  - none")
        return
    for item in items:
        print(f"  - {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Advisory PR scope boundary checker.")
    parser.add_argument("--base-ref", default="origin/main", help="Base git ref for PR diff.")
    parser.add_argument("--head-ref", default="HEAD", help="Head git ref for PR diff.")
    parser.add_argument("--docs-only", action="store_true", help="Enforce docs-only boundary policy.")
    args = parser.parse_args()

    changed_files = run_git_diff(args.base_ref, args.head_ref)
    protected_files = sorted([path for path in changed_files if in_any_prefix(path, PROTECTED_PREFIXES)])

    allowed_scope = list(PROTECTED_PREFIXES)
    violations: list[str] = []

    if args.docs_only:
        allowed_scope = list(DOCS_ONLY_ALLOWED_PREFIXES)
        violations = sorted(
            [
                path
                for path in changed_files
                if not any(path == allowed or path.startswith(allowed) for allowed in DOCS_ONLY_ALLOWED_PREFIXES)
            ]
        )
    elif protected_files:
        violations = protected_files

    print("HC-TRUST-LAYER PR scope boundary report")
    print(f"base_ref: {args.base_ref}")
    print(f"head_ref: {args.head_ref}")
    print(f"docs_only_mode: {args.docs_only}")
    render_list("changed protected files:", protected_files)
    render_list("allowed scope:", sorted(allowed_scope))
    render_list("unexpected scope violations:", violations)

    if violations:
        print("ADVISORY: scope boundary violations detected; preserve human-supervised validation and reviewer authority.")
        return 1

    print("ADVISORY: no scope boundary violations detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
