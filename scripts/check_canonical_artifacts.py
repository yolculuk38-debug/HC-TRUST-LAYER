#!/usr/bin/env python3
"""Canonical artifact boundary guard for HC-TRUST-LAYER."""

from __future__ import annotations

import fnmatch
from pathlib import Path

CANONICAL_DIRS = [
    Path("records/pending"),
    Path("records/verified"),
    Path("records/archived"),
]

LEGACY_QR_BRIDGE_EXCEPTIONS = {
    Path("records/verified/HC-TEST-2026-0001.md"),
}

NON_CANONICAL_PATTERNS = [
    "explorer_index.json",
    "index.json",
    "*_index.json",
    "*manifest*.json",
    "*cache*.json",
    "exports/**",
    "generated/**",
    "docs/generated/**",
    "records/**/*.tmp",
    "records/**/cache/**",
    "records/**/generated/**",
]

DOC_GLOBS = ["docs/canonical-record-boundary.md", "docs/ai-collaboration-workflow.md", "docs/capability-status.md"]
ARTIFACT_TOKENS = ("index", "manifest", "cache", "export", "generated", "explorer_index.json")
POSITIVE_CANONICAL_MARKERS = ("canonical verification record", "canonical verification records", "treated as canonical record")
NEGATION_MARKERS = ("non-canonical", "not canonical", "must not", "never", "skip", "skipped")
ASSERTION_MARKERS = (" is ", " are ", "treated as", "considered", "authoritative")


def is_non_canonical(path: Path) -> bool:
    norm = path.as_posix()
    if path.name == "explorer_index.json":
        return True
    return any(fnmatch.fnmatch(norm, pat) for pat in NON_CANONICAL_PATTERNS)


def is_legacy_qr_bridge_exception(path: Path) -> bool:
    return path in LEGACY_QR_BRIDGE_EXCEPTIONS


def in_canonical_dir(path: Path) -> bool:
    norm = path.as_posix()
    return any(norm == d.as_posix() or norm.startswith(f"{d.as_posix()}/") for d in CANONICAL_DIRS)


def main() -> int:
    repo = Path.cwd()
    errors = 0

    all_files: list[Path] = []
    for p in repo.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(repo)
        if ".git" in rel.parts:
            continue
        all_files.append(rel)

    for rel in sorted(all_files):
        if in_canonical_dir(rel):
            if is_legacy_qr_bridge_exception(rel):
                print(f"SKIP: {rel} (explicitly non-canonical legacy QR compatibility bridge)")
            elif is_non_canonical(rel):
                print(f"ERROR: non-canonical artifact inside canonical record boundary: {rel}")
                errors += 1
            else:
                print(f"CANONICAL: {rel}")
        elif is_non_canonical(rel):
            if rel.name == "explorer_index.json":
                print(f"SKIP: {rel} (explicitly non-canonical explorer_index.json)")
            else:
                print(f"SKIP: {rel}")

    for pattern in DOC_GLOBS:
        for doc in sorted(repo.glob(pattern)):
            lines = doc.read_text(encoding="utf-8").splitlines()
            for lineno, line in enumerate(lines, start=1):
                low = line.lower()
                has_artifact = any(token in low for token in ARTIFACT_TOKENS)
                has_canonical_claim = any(marker in low for marker in POSITIVE_CANONICAL_MARKERS)
                has_assertion = any(marker in low for marker in ASSERTION_MARKERS)
                has_negation = any(marker in low for marker in NEGATION_MARKERS)

                if has_artifact and has_canonical_claim and has_assertion and not has_negation:
                    print(
                        f"ERROR: docs canonical-boundary violation {doc.relative_to(repo)}:{lineno}: "
                        "generated/index/export/cache artifact described as canonical verification record"
                    )
                    errors += 1

    if errors:
        print(f"Canonical artifact guard failed with {errors} error(s).")
        return 1

    print("Canonical artifact guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
