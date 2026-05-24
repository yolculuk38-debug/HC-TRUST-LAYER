#!/usr/bin/env python3
"""Advisory-only policy evaluator for HC-TRUST-LAYER merge risk classification."""

from __future__ import annotations

import argparse
import sys
from fnmatch import fnmatchcase
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

POLICY_FILE = Path("policy/hc-policy-v1.yml")
RISK_LEVELS = ("low", "medium", "high", "blocked")
BLOCKED_KEY = "blocked_unless_explicitly_reviewed"


class PolicyParseError(Exception):
    """Raised when policy rules cannot be parsed safely."""


def _parse_list(lines: List[str], start_index: int, base_indent: int) -> Tuple[List[str], int]:
    values: List[str] = []
    i = start_index
    while i < len(lines):
        raw = lines[i]
        if not raw.strip() or raw.strip().startswith("#"):
            i += 1
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent < base_indent:
            break
        stripped = raw.strip()
        if not stripped.startswith("- "):
            break
        values.append(stripped[2:].strip().strip('"').strip("'"))
        i += 1
    return values, i


def load_path_risk_rules(policy_path: Path) -> Dict[str, List[str]]:
    """Load path risk rules from the repository policy file without external deps."""
    if not policy_path.exists():
        raise PolicyParseError(f"policy file not found: {policy_path}")

    lines = policy_path.read_text(encoding="utf-8").splitlines()
    path_rules: Dict[str, List[str]] = {"low": [], "medium": [], "high": [], "blocked": []}

    in_path_rules = False
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        indent = len(raw) - len(raw.lstrip(" "))
        if stripped == "path_risk_rules:":
            in_path_rules = True
            i += 1
            continue

        if in_path_rules and indent == 0:
            break

        if in_path_rules and indent == 2 and stripped.endswith(":"):
            key = stripped[:-1]
            values, next_i = _parse_list(lines, i + 1, base_indent=4)
            if key == BLOCKED_KEY:
                path_rules["blocked"] = values
            elif key in ("low", "medium", "high"):
                path_rules[key] = values
            i = next_i
            continue

        i += 1

    if not any(path_rules.values()):
        raise PolicyParseError("no path_risk_rules entries were parsed")

    return path_rules


def _pattern_matches(path: str, pattern: str) -> bool:
    normalized = path.replace("\\", "/")
    if fnmatchcase(normalized, pattern):
        return True
    if "**/" in pattern and fnmatchcase(normalized, pattern.replace("**/", "")):
        return True
    return False


def match_risk(path: str, rules: Dict[str, List[str]]) -> str:
    for risk in RISK_LEVELS:
        for pattern in rules[risk]:
            if _pattern_matches(path, pattern):
                return risk
    return "unknown"


def evaluate_paths(paths: Iterable[str], rules: Dict[str, List[str]]) -> Tuple[Dict[str, List[str]], str]:
    grouped: Dict[str, List[str]] = {"low": [], "medium": [], "high": [], "blocked": [], "unknown": []}
    for path in paths:
        grouped[match_risk(path, rules)].append(path)

    if grouped["blocked"]:
        outcome = "blocked"
    elif grouped["high"] or grouped["unknown"]:
        outcome = "human_review_required"
    elif grouped["medium"]:
        outcome = "conditional_merge"
    else:
        outcome = "auto_merge_allowed"

    return grouped, outcome


def print_summary(grouped: Dict[str, List[str]], outcome: str) -> None:
    print("HC-TRUST-LAYER policy evaluator (advisory-only)")
    print("Policy rules classification for merge risk:\n")
    for category in ("blocked", "high", "medium", "low", "unknown"):
        paths = grouped[category]
        print(f"- {category}: {len(paths)}")
        for path in paths:
            print(f"    - {path}")
    print("\nRecommended merge outcome:")
    print(f"- {outcome}")
    print("\nNote: This output is advisory-only for human-supervised validation in the trust kernel.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate changed paths against HC:// policy rules and return merge risk guidance."
    )
    parser.add_argument("paths", nargs="+", help="Changed file paths to evaluate.")
    parser.add_argument(
        "--policy",
        default=str(POLICY_FILE),
        help="Path to policy file (default: policy/hc-policy-v1.yml)",
    )
    args = parser.parse_args()

    try:
        rules = load_path_risk_rules(Path(args.policy))
    except Exception as exc:
        print("HC-TRUST-LAYER policy evaluator (advisory-only)")
        print(f"Policy parse failure: {exc}")
        print("Recommended merge outcome:")
        print("- human_review_required")
        print("Fail-closed behavior engaged for human-supervised validation.")
        return 2

    grouped, outcome = evaluate_paths(args.paths, rules)
    print_summary(grouped, outcome)
    return 0


if __name__ == "__main__":
    sys.exit(main())
