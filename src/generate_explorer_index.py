"""Generate a lightweight explorer index from canonical record directories."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL_RECORD_DIRS = (
    ROOT / "records" / "pending",
    ROOT / "records" / "verified",
    ROOT / "records" / "archived",
)
OUTPUT = ROOT / "generated" / "explorer_index.json"


def _safe_str(value: object) -> str:
    return value if isinstance(value, str) else ""


def _content_hash_prefix(content_hash: object, length: int = 12) -> str:
    value = _safe_str(content_hash).strip()
    return value[:length] if value else ""


def load_index_entries() -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []

    for directory in CANONICAL_RECORD_DIRS:
        if not directory.exists():
            continue

        for file_path in sorted(directory.glob("*.json")):
            try:
                record = json.loads(file_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue

            entries.append(
                {
                    "record_id": _safe_str(record.get("record_id")),
                    "verification_status": _safe_str(record.get("verification_status")),
                    "timestamp": _safe_str(record.get("timestamp")),
                    "author": _safe_str(record.get("author")),
                    "content_hash_prefix": _content_hash_prefix(record.get("content_hash")),
                    "source_file": file_path.relative_to(ROOT).as_posix(),
                }
            )

    return sorted(entries, key=lambda item: (item["timestamp"], item["record_id"]))


def build_explorer_index() -> dict[str, object]:
    return {
        "generated_by": "src/generate_explorer_index.py",
        "advisory_only": True,
        "records": load_index_entries(),
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    explorer_index = build_explorer_index()
    OUTPUT.write_text(json.dumps(explorer_index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote explorer index: {OUTPUT}")


if __name__ == "__main__":
    main()
