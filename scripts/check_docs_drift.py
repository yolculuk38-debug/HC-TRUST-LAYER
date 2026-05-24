#!/usr/bin/env python3
"""Documentation drift checker for HC-TRUST-LAYER."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

DOCS = [
    Path("docs/implementation-map.md"),
    Path("docs/capability-status.md"),
    Path("docs/master-architecture.md"),
    Path("README.md"),
]

ALLOWED_STATUS = {"implemented", "partial", "planned", "research", "not implemented"}

SENSITIVE_PHRASES = [
    "production-ready",
    "fully decentralized",
    "bank-grade",
    "government integrated",
    "guaranteed",
]

REQUIRED_TERMS = [
    "hc-trust-layer",
    "hc://",
    "verification infrastructure",
    "provenance",
    "audit trail",
    "public verification",
    "human-supervised validation",
    "ai-assisted witness",
]

EVIDENCE_PATTERNS = {
    "src/": "src/**/*.py",
    "tests/": "tests/test_*.py",
    "docs/": "docs/**/*.md",
    "schema/": "schema/**/*",
    "examples/": "examples/**/*",
    ".github/workflows/": ".github/workflows/*.yml",
}

DISALLOWED_HYPE = ["truth guarantee", "guarantees truth", "ai authority", "proves truth"]


@dataclass
class Finding:
    severity: str  # WARNING or ERROR
    path: Path
    line: int
    message: str

    def render(self) -> str:
        return f"{self.severity}: {self.path}:{self.line}: {self.message}"


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def line_number(lines: list[str], text: str) -> int:
    for i, line in enumerate(lines, start=1):
        if text in line:
            return i
    return 1


def extract_statuses(path: Path, lines: list[str]) -> dict[str, str]:
    statuses: dict[str, str] = {}
    if path.name == "implementation-map.md":
        current = ""
        for i, line in enumerate(lines, start=1):
            if line.startswith("## ") and ") " in line:
                current = line.split(") ", 1)[1].strip().lower()
            m = re.match(r"\*\*Status:\*\*\s*(.+)$", line.strip(), flags=re.I)
            if m and current:
                statuses[current] = m.group(1).strip().lower()
    elif path.name == "master-architecture.md":
        in_table = False
        for line in lines:
            if line.strip().startswith("| Layer | Current status"):
                in_table = True
                continue
            if in_table and line.strip().startswith("|"):
                cols = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cols) >= 2 and cols[0].lower() != "---":
                    statuses[cols[0].lower()] = cols[1].lower()
            elif in_table and line.strip() and not line.strip().startswith("|"):
                break
    return statuses


def is_future_context(line: str) -> bool:
    low = line.lower()
    markers = ["planned", "future", "roadmap", "research", "not implemented", "pending"]
    return any(m in low for m in markers)


def main() -> int:
    repo = Path.cwd()
    findings: list[Finding] = []

    for doc in DOCS:
        if not (repo / doc).exists():
            findings.append(Finding("ERROR", doc, 1, "required document missing"))

    if findings:
        for f in findings:
            print(f.render())
        print("ERROR: broken required references")
        return 1

    doc_lines = {doc: read_lines(repo / doc) for doc in DOCS}
    doc_text = {doc: "\n".join(lines) for doc, lines in doc_lines.items()}

    # Required terminology presence across corpus.
    corpus = "\n".join(doc_text.values()).lower()
    for term in REQUIRED_TERMS:
        if term not in corpus:
            findings.append(Finding("WARNING", Path("docs"), 1, f"required terminology missing in inspected docs: '{term}'"))

    # Status vocabulary enforcement.
    for doc, lines in doc_lines.items():
        for i, line in enumerate(lines, start=1):
            status_match = re.search(r"\*\*status:\\*\*\s*`?([A-Za-z ]+)`?", line, flags=re.I)
            if status_match:
                status = status_match.group(1).strip().lower()
                if status not in ALLOWED_STATUS:
                    findings.append(Finding("ERROR", doc, i, f"invalid status label '{status_match.group(1).strip()}'"))

    # Contradictions between implementation-map and master-architecture layer states.
    impl = extract_statuses(Path("docs/implementation-map.md"), doc_lines[Path("docs/implementation-map.md")])
    arch = extract_statuses(Path("docs/master-architecture.md"), doc_lines[Path("docs/master-architecture.md")])
    for layer, impl_status in impl.items():
        if layer in arch and arch[layer] != impl_status:
            findings.append(Finding("ERROR", Path("docs/master-architecture.md"), 1, f"conflicting capability state for '{layer}': implementation-map={impl_status}, master-architecture={arch[layer]}"))

    # Implementation claim without evidence path.
    for doc, lines in doc_lines.items():
        for i, line in enumerate(lines, start=1):
            if "implemented" in line.lower() and "|" in line:
                paths = re.findall(r"`([^`]+)`", line)
                for p in paths:
                    if "/" in p and not (repo / p).exists():
                        findings.append(Finding("WARNING", doc, i, f"implemented claim references missing repo evidence '{p}'"))

    # Sensitive phrases warning unless future/planned context.
    for doc, lines in doc_lines.items():
        for i, line in enumerate(lines, start=1):
            low = line.lower()
            for phrase in SENSITIVE_PHRASES:
                if phrase in low and "not " + phrase not in low and not is_future_context(line):
                    findings.append(Finding("WARNING", doc, i, f"sensitive claim '{phrase}' should be explicitly marked future/planned"))

            for phrase in DISALLOWED_HYPE:
                if phrase in low:
                    findings.append(Finding("WARNING", doc, i, f"avoid exaggerated authority/guarantee phrasing '{phrase}'"))

    # Duplicate architecture naming.
    arch_lines = doc_lines[Path("docs/master-architecture.md")]
    headings = [line.strip().lower() for line in arch_lines if line.startswith("### ")]
    seen: set[str] = set()
    for h in headings:
        if h in seen:
            findings.append(Finding("WARNING", Path("docs/master-architecture.md"), line_number(arch_lines, h.replace("### ", "")), f"duplicate architecture section heading '{h}'"))
        seen.add(h)

    # Missing required cross references.
    required_refs = {
        Path("docs/implementation-map.md"): ["capability-status.md", "master-architecture.md"],
        Path("docs/capability-status.md"): ["implementation-map.md", "master-architecture.md"],
        Path("docs/master-architecture.md"): ["implementation-map.md", "capability-status.md"],
        Path("README.md"): ["docs/implementation-map.md", "docs/capability-status.md", "docs/master-architecture.md"],
    }
    for doc, refs in required_refs.items():
        text_low = doc_text[doc].lower()
        for ref in refs:
            if ref.lower() not in text_low:
                findings.append(Finding("ERROR", doc, 1, f"missing required reference to '{ref}'"))

    # Print results with clear warnings/errors.
    errors = 0
    warnings = 0
    for finding in findings:
        print(finding.render())
        if finding.severity == "ERROR":
            errors += 1
        else:
            warnings += 1

    if warnings:
        print(f"WARNING: {warnings} warning(s) found")
    if errors:
        print(f"ERROR: {errors} error(s) found")
        return 1

    print("Documentation drift check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
