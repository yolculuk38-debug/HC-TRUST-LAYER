#!/usr/bin/env python3
"""Report-only stale baseline scanner for HC-TRUST-LAYER documentation."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

ADVISORY_FLAGS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
    "issue_comment_automation": False,
    "label_reviewer_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
}

STALE_PATTERNS = (
    "Python 3.11",
    "Python 3.9",
    'requires-python = ">=3.9"',
    "pytest==9.0.3",
    "fastapi==0.115.14",
    "jsonschema==4.17.3",
    "qrcode[pil]==7.4.2",
    "uvicorn==0.35.0",
)

BOUNDARY_PATTERNS = (
    re.compile(r"Historical/report-only boundary", re.IGNORECASE),
    re.compile(r"historical/report-only", re.IGNORECASE),
    re.compile(r"should not be read as the current", re.IGNORECASE),
    re.compile(r"not\s+(?:be\s+)?read\s+as\s+(?:the\s+)?current", re.IGNORECASE),
    re.compile(r"not\s+(?:the\s+)?current\s+(?:active\s+)?(?:baseline|package baseline|CI baseline|runtime)", re.IGNORECASE),
)

DEPENDENCY_RE = re.compile(r'["\']?([A-Za-z0-9_.-]+(?:\[[A-Za-z0-9_,.-]+\])?)==([^"\'\s;,]+)')
REQUIRES_PYTHON_RE = re.compile(r'requires-python\s*=\s*["\']([^"\']+)["\']')
WORKFLOW_PYTHON_RE = re.compile(r"python-version\s*:\s*[\"']?([^\"'\n#]+)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_requires_python(pyproject_text: str) -> str | None:
    match = REQUIRES_PYTHON_RE.search(pyproject_text)
    return match.group(1) if match else None


def parse_dependency_pins(text: str) -> dict[str, str]:
    pins: dict[str, str] = {}
    for name, version in DEPENDENCY_RE.findall(text):
        pins[name] = version
    return dict(sorted(pins.items()))


def parse_workflow_python_versions(workflow_text: str) -> list[str]:
    versions = [match.strip() for match in WORKFLOW_PYTHON_RE.findall(workflow_text)]
    return sorted(dict.fromkeys(versions))


def iter_existing(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.exists():
            yield path


def discover_files(root: Path) -> dict[str, list[Path]]:
    workflows = []
    workflow_root = root / ".github" / "workflows"
    if workflow_root.exists():
        workflows = sorted([*workflow_root.glob("**/*.yml"), *workflow_root.glob("**/*.yaml")])
    docs_root = root / "docs"
    docs = sorted(docs_root.glob("**/*.md")) if docs_root.exists() else []
    return {
        "pyproject": list(iter_existing([root / "pyproject.toml"])),
        "requirements": list(iter_existing([root / "requirements.txt"])),
        "workflows": workflows,
        "docs": docs,
    }


def has_historical_boundary(text: str) -> bool:
    return any(pattern.search(text) for pattern in BOUNDARY_PATTERNS)


def find_stale_matches(path: Path, text: str, root: Path) -> list[dict[str, object]]:
    matches = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in STALE_PATTERNS:
            if pattern in line:
                matches.append({
                    "file": str(path.relative_to(root)),
                    "line": line_number,
                    "match": pattern,
                })
    return matches


def build_report(root: Path) -> dict[str, object]:
    root = root.resolve()
    files = discover_files(root)
    warnings: list[str] = []
    scanned_files: list[str] = []

    pyproject_text = read_text(files["pyproject"][0]) if files["pyproject"] else ""
    if not pyproject_text:
        warnings.append("pyproject.toml was not found; current package baseline is incomplete.")

    requirement_pins = {}
    if files["requirements"]:
        requirement_pins = parse_dependency_pins(read_text(files["requirements"][0]))
    else:
        warnings.append("requirements.txt was not found; current requirements baseline is incomplete.")

    workflow_versions: dict[str, list[str]] = {}
    for workflow in files["workflows"]:
        workflow_versions[str(workflow.relative_to(root))] = parse_workflow_python_versions(read_text(workflow))

    historical_safe: list[dict[str, object]] = []
    missing_boundary: list[dict[str, object]] = []
    for doc in files["docs"]:
        text = read_text(doc)
        scanned_files.append(str(doc.relative_to(root)))
        matches = find_stale_matches(doc, text, root)
        if not matches:
            continue
        target = historical_safe if has_historical_boundary(text) else missing_boundary
        target.append({"file": str(doc.relative_to(root)), "matches": matches})

    return {
        **ADVISORY_FLAGS,
        "current_baseline": {
            "requires_python": parse_requires_python(pyproject_text),
            "pyproject_dependency_pins": parse_dependency_pins(pyproject_text),
            "requirements_dependency_pins": requirement_pins,
            "workflow_python_versions": workflow_versions,
        },
        "scanned_files": scanned_files,
        "historical_safe_matches": historical_safe,
        "missing_boundary_matches": missing_boundary,
        "warnings": warnings,
    }


def markdown_report(report: dict[str, object]) -> str:
    baseline = report["current_baseline"]
    assert isinstance(baseline, dict)
    lines = [
        "# HC Stale Baseline Scanner Report",
        "",
        "Advisory notice: this local report is advisory/report-only, public-safe, and requires human review. It provides no truth, security, legal, identity, approval, or merge guarantee.",
        "",
        "## Current observed baseline",
        f"- requires-python: `{baseline.get('requires_python')}`",
        f"- requirements pins: `{baseline.get('requirements_dependency_pins')}`",
        f"- workflow Python versions: `{baseline.get('workflow_python_versions')}`",
        "",
        "## Files with historical-safe matches",
    ]
    for item in report["historical_safe_matches"]:  # type: ignore[index]
        lines.append(f"- {item['file']}")
    if not report["historical_safe_matches"]:  # type: ignore[index]
        lines.append("- None")
    lines += ["", "## Files with missing-boundary matches"]
    for item in report["missing_boundary_matches"]:  # type: ignore[index]
        lines.append(f"- {item['file']}")
    if not report["missing_boundary_matches"]:  # type: ignore[index]
        lines.append("- None")
    lines += ["", "Reminder: CI/checks are evidence, not trust authority; human review remains final."]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report stale-looking HC baseline references in documentation.")
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--markdown", action="store_true", help="print a short Markdown report instead of JSON")
    parser.add_argument("--fail-on-missing-boundary", action="store_true", help="exit 1 when missing-boundary matches are present")
    args = parser.parse_args(argv)

    report = build_report(args.repo_root)
    if args.markdown:
        sys.stdout.write(markdown_report(report))
    else:
        json.dump(report, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    if args.fail_on_missing_boundary and report["missing_boundary_matches"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
