#!/usr/bin/env python3
"""Report-only ecosystem baseline scanner for HC-TRUST-LAYER docs."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

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

BOUNDARY_PATTERNS = (
    re.compile(r"Historical/report-only boundary", re.IGNORECASE),
    re.compile(r"historical/report-only", re.IGNORECASE),
    re.compile(r"should not be read as the current", re.IGNORECASE),
    re.compile(r"not\s+(?:be\s+)?read\s+as\s+(?:the\s+)?current", re.IGNORECASE),
    re.compile(
        r"not\s+(?:the\s+)?current\s+(?:active\s+)?"
        r"(?:baseline|package baseline|CI baseline|runtime)",
        re.IGNORECASE,
    ),
)

DEPENDENCY_RE = re.compile(r'["\']?([A-Za-z0-9_.-]+(?:\[[A-Za-z0-9_,.-]+\])?)==([^"\'\s;,]+)')
REQUIRES_PYTHON_RE = re.compile(r'requires-python\s*=\s*(["\'])([^"\']+)\1')
WORKFLOW_VALUE_RE_TEMPLATE = r"{key}\s*:\s*([\"']?)([^\"'\n#]+)\1"
PACKAGE_NODE_ENGINE_RE = re.compile(r'"node"\s*:\s*"([^"]+)"')
GO_MOD_RE = re.compile(r"^go\s+([^\s]+)", re.MULTILINE)
RUST_TOOLCHAIN_CHANNEL_RE = re.compile(r"^channel\s*=\s*([\"'])([^\"']+)\1", re.MULTILINE)
POM_JAVA_RE = re.compile(r"<(?:maven\.compiler\.(?:source|target|release)|java\.version)>([^<]+)</")
GRADLE_JAVA_RE = re.compile(r"(?:sourceCompatibility|targetCompatibility|languageVersion)\s*(?:=|\()\s*[\"']?([0-9][0-9._-]*)")


@dataclass(frozen=True)
class DeclarationPattern:
    label: str
    regex: re.Pattern[str]


@dataclass(frozen=True)
class EcosystemBaseline:
    ecosystem: str
    source_files: tuple[str, ...]
    current_observed: dict[str, object]
    stale_patterns: tuple[str, ...]
    declaration_patterns: tuple[DeclarationPattern, ...]


@dataclass(frozen=True)
class DetectedMatch:
    ecosystem: str
    pattern: str
    matched_text: str
    file_path: str
    line_number: int
    classification: str

    def as_dict(self) -> dict[str, object]:
        return {
            "ecosystem": self.ecosystem,
            "pattern": self.pattern,
            "matched_text": self.matched_text,
            "file": self.file_path,
            "line": self.line_number,
            "classification": self.classification,
        }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def iter_existing(root: Path, paths: Iterable[str]) -> list[Path]:
    return [root / path for path in paths if (root / path).exists()]


def workflow_files(root: Path) -> list[Path]:
    workflow_root = root / ".github" / "workflows"
    if not workflow_root.exists():
        return []
    return sorted([*workflow_root.glob("**/*.yml"), *workflow_root.glob("**/*.yaml")])


def docs_files(root: Path) -> list[Path]:
    docs_root = root / "docs"
    return sorted(docs_root.glob("**/*.md")) if docs_root.exists() else []


def parse_requires_python(pyproject_text: str) -> str | None:
    match = REQUIRES_PYTHON_RE.search(pyproject_text)
    return match.group(2) if match else None


def parse_dependency_pins(text: str) -> dict[str, str]:
    pins: dict[str, str] = {}
    for name, version in DEPENDENCY_RE.findall(text):
        pins[name] = version
    return dict(sorted(pins.items()))


def workflow_versions(workflows: list[Path], root: Path, key: str) -> dict[str, list[str]]:
    regex = re.compile(WORKFLOW_VALUE_RE_TEMPLATE.format(key=re.escape(key)))
    versions: dict[str, list[str]] = {}
    for workflow in workflows:
        found = [match.group(2).strip() for match in regex.finditer(read_text(workflow))]
        versions[relative(workflow, root)] = sorted(dict.fromkeys(found))
    return versions


def has_historical_boundary(text: str) -> bool:
    return any(pattern.search(text) for pattern in BOUNDARY_PATTERNS)


def line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def make_declaration(label: str, regex: str) -> DeclarationPattern:
    return DeclarationPattern(label=label, regex=re.compile(regex, re.IGNORECASE))


def source_paths(paths: Iterable[Path], root: Path) -> tuple[str, ...]:
    return tuple(relative(path, root) for path in paths)


def detect_python(root: Path, workflows: list[Path]) -> EcosystemBaseline:
    pyproject = iter_existing(root, ["pyproject.toml"])
    requirements = iter_existing(root, ["requirements.txt"])
    pyproject_text = read_text(pyproject[0]) if pyproject else ""
    requirements_text = read_text(requirements[0]) if requirements else ""
    return EcosystemBaseline(
        ecosystem="python",
        source_files=source_paths([*pyproject, *requirements, *workflows], root),
        current_observed={
            "requires_python": parse_requires_python(pyproject_text),
            "pyproject_dependency_pins": parse_dependency_pins(pyproject_text),
            "requirements_dependency_pins": parse_dependency_pins(requirements_text),
            "workflow_python_versions": workflow_versions(workflows, root, "python-version"),
        },
        stale_patterns=(
            "Python 3.11",
            "Python 3.9",
            "pytest==9.0.3",
            "fastapi==0.115.14",
            "jsonschema==4.17.3",
            "qrcode[pil]==7.4.2",
            "uvicorn==0.35.0",
        ),
        declaration_patterns=(
            make_declaration("python-version", r"python-version\s*:\s*([\"']?)(?:3\.11|3\.9)\1"),
            make_declaration("requires-python", r"requires-python\s*=\s*([\"'])(?:>=3\.11|>=3\.9)\1"),
        ),
    )


def detect_java(root: Path, workflows: list[Path]) -> EcosystemBaseline:
    files = iter_existing(root, ["pom.xml", "build.gradle", "build.gradle.kts", "gradle.properties", ".java-version"])
    observed: dict[str, object] = {"workflow_java_versions": workflow_versions(workflows, root, "java-version")}
    for path in files:
        text = read_text(path)
        if path.name == ".java-version":
            observed["java_version_file"] = text.strip()
        elif path.name == "pom.xml":
            observed["pom_java_versions"] = sorted(dict.fromkeys(match.strip() for match in POM_JAVA_RE.findall(text)))
        elif path.name.startswith("build.gradle"):
            observed[f"{path.name}_java_versions"] = sorted(dict.fromkeys(match.strip() for match in GRADLE_JAVA_RE.findall(text)))
        elif path.name == "gradle.properties":
            observed["gradle_properties_mentions"] = [line.strip() for line in text.splitlines() if "java" in line.lower()]
    return EcosystemBaseline(
        ecosystem="java",
        source_files=source_paths([*files, *workflows], root),
        current_observed=observed,
        stale_patterns=("Java 17",),
        declaration_patterns=(make_declaration("java-version", r"java-version\s*:\s*([\"']?)17\1"),),
    )


def detect_node(root: Path, workflows: list[Path]) -> EcosystemBaseline:
    files = iter_existing(root, ["package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock", ".nvmrc", ".node-version"])
    observed: dict[str, object] = {"workflow_node_versions": workflow_versions(workflows, root, "node-version")}
    for path in files:
        text = read_text(path)
        if path.name in {".nvmrc", ".node-version"}:
            observed[path.name.lstrip(".").replace("-", "_")] = text.strip()
        elif path.name == "package.json":
            match = PACKAGE_NODE_ENGINE_RE.search(text)
            observed["package_json_engines_node"] = match.group(1) if match else None
        else:
            observed[f"{path.name}_present"] = True
    return EcosystemBaseline(
        ecosystem="node",
        source_files=source_paths([*files, *workflows], root),
        current_observed=observed,
        stale_patterns=("Node 18",),
        declaration_patterns=(make_declaration("node-version", r"node-version\s*:\s*([\"']?)18\1"),),
    )


def detect_go(root: Path, workflows: list[Path]) -> EcosystemBaseline:
    files = iter_existing(root, ["go.mod"])
    go_version = None
    if files:
        match = GO_MOD_RE.search(read_text(files[0]))
        go_version = match.group(1) if match else None
    return EcosystemBaseline(
        ecosystem="go",
        source_files=source_paths([*files, *workflows], root),
        current_observed={
            "go_mod_version": go_version,
            "workflow_go_versions": workflow_versions(workflows, root, "go-version"),
        },
        stale_patterns=("Go 1.21",),
        declaration_patterns=(make_declaration("go-version", r"go-version\s*:\s*([\"']?)1\.21\1"),),
    )


def detect_rust(root: Path, workflows: list[Path]) -> EcosystemBaseline:
    del workflows
    files = iter_existing(root, ["Cargo.toml", "rust-toolchain", "rust-toolchain.toml"])
    observed: dict[str, object] = {}
    for path in files:
        text = read_text(path)
        if path.name == "rust-toolchain":
            observed["rust_toolchain"] = text.strip()
        elif path.name == "rust-toolchain.toml":
            match = RUST_TOOLCHAIN_CHANNEL_RE.search(text)
            observed["rust_toolchain_toml_channel"] = match.group(2) if match else None
        elif path.name == "Cargo.toml":
            observed["cargo_toml_present"] = True
    return EcosystemBaseline(
        ecosystem="rust",
        source_files=source_paths(files, root),
        current_observed=observed,
        stale_patterns=("Rust 1.75",),
        declaration_patterns=(make_declaration("rust-toolchain", r"(?:channel|rust-toolchain)\s*(?:=|:)\s*([\"']?)1\.75(?:\.\d+)?\1"),),
    )


def ecosystem_baselines(root: Path) -> list[EcosystemBaseline]:
    workflows = workflow_files(root)
    detectors: tuple[Callable[[Path, list[Path]], EcosystemBaseline], ...] = (
        detect_python,
        detect_java,
        detect_node,
        detect_go,
        detect_rust,
    )
    return [detector(root, workflows) for detector in detectors]


def detect_matches_for_doc(doc: Path, root: Path, baselines: list[EcosystemBaseline]) -> list[DetectedMatch]:
    text = read_text(doc)
    classification = "historical_safe" if has_historical_boundary(text) else "missing_boundary"
    file_path = relative(doc, root)
    matches: list[DetectedMatch] = []
    for baseline in baselines:
        for pattern in baseline.stale_patterns:
            start = 0
            while True:
                offset = text.find(pattern, start)
                if offset == -1:
                    break
                matches.append(DetectedMatch(baseline.ecosystem, pattern, pattern, file_path, line_number_for_offset(text, offset), classification))
                start = offset + len(pattern)
        for declaration in baseline.declaration_patterns:
            for match in declaration.regex.finditer(text):
                matched_text = match.group(0)
                matches.append(DetectedMatch(baseline.ecosystem, declaration.label, matched_text, file_path, line_number_for_offset(text, match.start()), classification))
    return sorted(matches, key=lambda item: (item.file_path, item.line_number, item.ecosystem, item.matched_text))


def group_matches(matches: list[DetectedMatch], classification: str) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for match in matches:
        if match.classification != classification:
            continue
        grouped.setdefault(match.ecosystem, []).append(match.as_dict())
    return grouped


def build_report(root: Path) -> dict[str, object]:
    root = root.resolve()
    baselines = ecosystem_baselines(root)
    docs = docs_files(root)
    all_matches: list[DetectedMatch] = []
    for doc in docs:
        all_matches.extend(detect_matches_for_doc(doc, root, baselines))

    return {
        **ADVISORY_FLAGS,
        "baseline_model": "repository_declared_ecosystem_baselines",
        "upstream_latest_version_check": False,
        "current_baseline": {
            baseline.ecosystem: {
                "source_files": baseline.source_files,
                "current_observed": baseline.current_observed,
                "stale_patterns": baseline.stale_patterns,
                "declaration_patterns": [pattern.label for pattern in baseline.declaration_patterns],
            }
            for baseline in baselines
        },
        "scanned_files": [relative(doc, root) for doc in docs],
        "historical_safe_matches": group_matches(all_matches, "historical_safe"),
        "missing_boundary_matches": group_matches(all_matches, "missing_boundary"),
        "matches": [match.as_dict() for match in all_matches],
        "warnings": [],
    }


def markdown_report(report: dict[str, object]) -> str:
    current = report["current_baseline"]
    assert isinstance(current, dict)
    lines = [
        "# HC Stale Baseline Scanner Report",
        "",
        "Advisory notice: this local report is advisory/report-only, public-safe, and requires human review. It provides no truth, security, legal, identity, approval, or merge guarantee.",
        "",
        "This scanner compares documentation against repository-declared ecosystem baselines. It does not fetch latest upstream versions.",
        "",
        "## Current observed repository baselines",
    ]
    for ecosystem, baseline in current.items():
        assert isinstance(baseline, dict)
        lines.extend([
            f"### {ecosystem}",
            f"- source files: `{baseline.get('source_files')}`",
            f"- observed: `{baseline.get('current_observed')}`",
            "",
        ])
    for title, key in (("Historical-safe matches", "historical_safe_matches"), ("Missing-boundary matches", "missing_boundary_matches")):
        lines.append(f"## {title}")
        grouped = report[key]
        assert isinstance(grouped, dict)
        if not grouped:
            lines.append("- None")
        for ecosystem, matches in grouped.items():
            lines.append(f"### {ecosystem}")
            assert isinstance(matches, list)
            for match in matches:
                assert isinstance(match, dict)
                lines.append(f"- {match['file']}:{match['line']} `{match['matched_text']}`")
        lines.append("")
    lines.append("Reminder: CI/checks are evidence, not trust authority; human review remains final.")
    return "\n".join(lines) + "\n"


def has_missing_boundary(report: dict[str, object]) -> bool:
    grouped = report["missing_boundary_matches"]
    return isinstance(grouped, dict) and any(grouped.values())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report stale-looking HC ecosystem baseline references in documentation.")
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
    if args.fail_on_missing_boundary and has_missing_boundary(report):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
