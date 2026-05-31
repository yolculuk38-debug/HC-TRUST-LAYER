"""Generate a lightweight read-only explorer index from record directories."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CANONICAL_RECORD_DIRS = (
    ROOT / "records" / "pending",
    ROOT / "records" / "verified",
    ROOT / "records" / "archived",
    ROOT / "records" / "archive",
)
OUTPUT = ROOT / "generated" / "explorer_index.json"


def _safe_str(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


def _content_hash_prefix(content_hash: object, length: int = 12) -> str:
    value = _safe_str(content_hash)
    return value[:length] if value else ""


def _safe_list(value: object) -> list[Any]:
    return value if isinstance(value, list) else []


def _witness_count(record: dict[str, Any]) -> int:
    witnesses = _safe_list(record.get("witnesses"))
    if witnesses:
        return len(witnesses)
    witness_summary = record.get("witness_summary")
    if isinstance(witness_summary, dict):
        count = witness_summary.get("count")
        try:
            return max(0, int(count))
        except (TypeError, ValueError):
            return 0
    return 0


def _verification_history(record: dict[str, Any]) -> list[dict[str, str]]:
    history = record.get("verification_history")
    if isinstance(history, list):
        return [item for item in history if isinstance(item, dict)]

    status = _safe_str(record.get("verification_status")) or _safe_str(record.get("status")) or "unavailable"
    timestamp = _safe_str(record.get("timestamp")) or _safe_str(record.get("created_at"))
    return [
        {
            "status": status,
            "timestamp": timestamp,
            "note": "Derived from generated explorer index metadata; advisory-only.",
        }
    ]


def _archive_status(record: dict[str, Any], file_path: Path) -> str:
    status = _safe_str(record.get("archive_status"))
    if status:
        return status
    if "pending" in file_path.parts:
        return "pending_archive"
    if "verified" in file_path.parts:
        return "verified_archive"
    if "archive" in file_path.parts or "archived" in file_path.parts:
        return "archived"
    return _safe_str(record.get("archive_ref")) or "not_specified"


def _json_entry(file_path: Path) -> dict[str, Any] | None:
    try:
        record = json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if not isinstance(record, dict):
        return None

    content_hash = _safe_str(record.get("content_hash")) or _safe_str(record.get("hash"))
    witnesses = _safe_list(record.get("witnesses"))
    return {
        "record_id": _safe_str(record.get("record_id")) or _safe_str(record.get("id")),
        "verification_status": _safe_str(record.get("verification_status")) or _safe_str(record.get("status")),
        "timestamp": _safe_str(record.get("timestamp")) or _safe_str(record.get("created_at")),
        "content_hash": content_hash,
        "content_hash_prefix": _content_hash_prefix(content_hash),
        "witness_count": _witness_count(record),
        "witness_information": witnesses,
        "witness_type": _safe_str(record.get("witness_type")),
        "source_path": file_path.relative_to(ROOT).as_posix(),
        "source_file": file_path.relative_to(ROOT).as_posix(),
        "archive_status": _archive_status(record, file_path),
        "verification_history": _verification_history(record),
        "metadata": {
            "author": _safe_str(record.get("author")),
            "record_type": _safe_str(record.get("record_type")),
            "source": _safe_str(record.get("source")),
            "title": _safe_str(record.get("title")),
            "created_at": _safe_str(record.get("created_at")),
            "archive_ref": _safe_str(record.get("archive_ref")),
        },
    }


def load_index_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []

    for directory in CANONICAL_RECORD_DIRS:
        if not directory.exists():
            continue

        for file_path in sorted(directory.glob("*.json")):
            entry = _json_entry(file_path)
            if entry is not None:
                entries.append(entry)

    return sorted(entries, key=lambda item: (item["timestamp"], item["record_id"]))


def build_explorer_index() -> dict[str, object]:
    return {
        "generated_by": "src/generate_explorer_index.py",
        "advisory_only": True,
        "read_only": True,
        "human_supervised": True,
        "records": load_index_entries(),
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    explorer_index = build_explorer_index()
    OUTPUT.write_text(json.dumps(explorer_index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote explorer index: {OUTPUT}")


if __name__ == "__main__":
    main()
