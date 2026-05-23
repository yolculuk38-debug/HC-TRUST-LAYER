"""Generate deterministic explorer indexes from local HC:// records."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORD_DIRS = [ROOT / "records" / "pending", ROOT / "records" / "verified"]
OUTPUT = ROOT / "records" / "explorer_index.json"


def load_records() -> list[dict]:
    records: list[dict] = []
    for directory in RECORD_DIRS:
        if not directory.exists():
            continue
        for file_path in sorted(directory.glob("*.json")):
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            data["_source"] = str(file_path.relative_to(ROOT))
            records.append(data)
    return sorted(records, key=lambda item: item.get("record_id", ""))


def build_index(records: list[dict]) -> dict:
    searchable = []
    provenance_graph = []
    witness_relations = []
    trust_lookup = []

    for record in records:
        record_id = record.get("record_id")
        if not record_id:
            continue

        searchable.append(
            {
                "record_id": record_id,
                "title": record.get("title"),
                "tags": record.get("tags", []),
                "status": record.get("verification_status", "unverified"),
                "created_at": record.get("created_at"),
                "source": record.get("_source"),
            }
        )

        if record.get("supersedes"):
            provenance_graph.append(
                {
                    "from": record.get("supersedes"),
                    "to": record_id,
                    "type": "revision",
                }
            )

        witness_relations.append(
            {
                "record_id": record_id,
                "witness_type": record.get("witness_type"),
                "author": record.get("author"),
            }
        )

        trust_lookup.append(
            {
                "record_id": record_id,
                "status": record.get("verification_status", "unverified"),
            }
        )

    return {
        "searchable_index": searchable,
        "provenance_graph": provenance_graph,
        "witness_relations": witness_relations,
        "federation_map": [],
        "trust_score_lookup": trust_lookup,
        "audit_chain_lookup": [],
    }


def main() -> None:
    records = load_records()
    index = build_index(records)
    OUTPUT.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote explorer index: {OUTPUT}")


if __name__ == "__main__":
    main()
