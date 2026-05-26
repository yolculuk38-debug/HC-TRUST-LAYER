#!/usr/bin/env python3
"""Generate append-only audit snapshot metadata from canonical record directories."""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRECTORIES = [
    ROOT / "records" / "pending",
    ROOT / "records" / "verified",
    ROOT / "records" / "archived",
]
OUTPUT_PATH = ROOT / "generated" / "audit_snapshot.json"


def _timestamp() -> str:
    source_date_epoch = os.getenv("SOURCE_DATE_EPOCH")
    if source_date_epoch:
        try:
            epoch = int(source_date_epoch)
            return datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def generate_snapshot() -> dict:
    files: list[Path] = []
    for directory in SCAN_DIRECTORIES:
        if directory.exists():
            files.extend(p for p in directory.rglob("*") if p.is_file())

    files = sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())

    record_ids = sorted({file_path.stem for file_path in files})
    manifest_entries = []
    for file_path in files:
        rel = file_path.relative_to(ROOT).as_posix()
        manifest_entries.append(f"{rel}:{_file_sha256(file_path)}")

    manifest_hash = hashlib.sha256("\n".join(manifest_entries).encode("utf-8")).hexdigest()

    return {
        "snapshot_timestamp": _timestamp(),
        "source_directories": [path.relative_to(ROOT).as_posix() + "/" for path in SCAN_DIRECTORIES],
        "file_count": len(files),
        "record_ids": record_ids,
        "sha256_manifest_hash": manifest_hash,
    }


def main() -> None:
    snapshot = generate_snapshot()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote audit snapshot: {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
