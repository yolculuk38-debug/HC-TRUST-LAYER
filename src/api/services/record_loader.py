"""Experimental record loader for runtime verification API.

Security properties:
- Safe path handling via strict record-id allowlist and resolved-path validation.
- Replay-safe lookup behavior by searching canonical directories in a fixed order.
- Malformed request protection via explicit record_id validation.
- Non-canonical artifact rejection by excluding generated and unsupported file types.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ALLOWED_RECORD_ID = re.compile(r"^[A-Za-z0-9._-]+$")
ALLOWED_EXTENSIONS = {".json", ".md", ".txt"}
REJECTED_SUFFIXES = {".sha256", ".sig", ".tmp", ".bak"}
CANONICAL_STATES = ("pending", "verified", "archived")


class RecordLoaderError(ValueError):
    """Raised when a record cannot be safely loaded."""


def _safe_candidates(record_id: str) -> list[str]:
    if not record_id or not ALLOWED_RECORD_ID.fullmatch(record_id):
        raise RecordLoaderError("Malformed record_id; only [A-Za-z0-9._-] are accepted.")
    return [record_id, f"{record_id}.json", f"{record_id}.md", f"{record_id}.txt"]


def load_record(record_id: str, base_dir: str | Path = "records") -> dict[str, Any]:
    """Load a record from pending/verified/archived with canonical validation."""

    root = Path(base_dir).resolve()
    state_dirs = {
        "pending": root / "pending",
        "verified": root / "verified",
        "archived": root / "archived",
    }

    # Backward compatibility for pre-archived directory naming.
    if not state_dirs["archived"].exists() and (root / "archive").exists():
        state_dirs["archived"] = root / "archive"

    for state in CANONICAL_STATES:
        directory = state_dirs[state]
        for candidate in _safe_candidates(record_id):
            path = (directory / candidate).resolve()

            if directory not in path.parents:
                continue

            if path.suffix.lower() in REJECTED_SUFFIXES:
                continue

            if path.suffix.lower() and path.suffix.lower() not in ALLOWED_EXTENSIONS:
                continue

            if not path.exists() or not path.is_file():
                continue

            payload = path.read_text(encoding="utf-8")
            if not payload.strip():
                raise RecordLoaderError("Record exists but is empty.")

            if path.suffix.lower() == ".json":
                try:
                    record_data = json.loads(payload)
                except json.JSONDecodeError as exc:
                    raise RecordLoaderError("Record JSON is malformed.") from exc
            else:
                record_data = {"raw": payload}

            return {
                "record_id": record_id,
                "state": state,
                "path": str(path.relative_to(root)),
                "record": record_data,
            }

    raise RecordLoaderError("Record not found in canonical directories.")
