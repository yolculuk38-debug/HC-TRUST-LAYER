"""Read-only HC:// public verification explorer helpers.

The helpers in this module use generated/explorer_index.json as an advisory
navigation source. They do not modify records, make automatic decisions, write to
federation surfaces, or calculate trust scoring.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_EXPLORER_INDEX = ROOT / "generated" / "explorer_index.json"

ADVISORY_BOUNDARY = {
    "advisory_only": True,
    "read_only": True,
    "human_supervised": True,
    "automatic_decision": False,
    "record_modification": False,
    "federation_write": False,
}


def load_explorer_index(
    index_path: Path | str = DEFAULT_EXPLORER_INDEX,
) -> dict[str, Any]:
    """Load generated explorer index data from disk."""

    path = Path(index_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Explorer index must be a JSON object.")
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("Explorer index must contain a records list.")
    return data


def _list_or_empty(value: Any) -> list[Any]:
    """Return list values used for public detail rendering, or an empty list."""

    return value if isinstance(value, list) else []


def _first_list(*values: Any) -> list[Any]:
    """Return the first list value without treating an explicit empty list as missing."""

    for value in values:
        if isinstance(value, list):
            return value
    return []


def _witness_count(entry: dict[str, Any], witness_information: list[Any]) -> int:
    """Return explicit witness_count values without treating zero as missing."""

    if "witness_count" in entry and entry["witness_count"] is not None:
        return int(entry["witness_count"])
    return len(witness_information)


def normalize_record(entry: dict[str, Any]) -> dict[str, Any]:
    """Return the public read-only shape used by the Explorer MVP."""

    content_hash = str(entry.get("content_hash") or entry.get("hash") or "")
    witness_information = _first_list(
        entry.get("witness_information"), entry.get("witnesses")
    )
    verification_history = _list_or_empty(entry.get("verification_history"))

    return {
        **ADVISORY_BOUNDARY,
        "record_id": str(entry.get("record_id") or entry.get("id") or "").strip(),
        "verification_status": str(
            entry.get("verification_status") or entry.get("status") or "unavailable"
        ).strip(),
        "timestamp": str(entry.get("timestamp") or "").strip(),
        "content_hash": content_hash.strip(),
        "content_hash_prefix": str(
            entry.get("content_hash_prefix") or content_hash[:12]
        ).strip(),
        "witness_count": _witness_count(entry, witness_information),
        "source_path": str(
            entry.get("source_path") or entry.get("source_file") or ""
        ).strip(),
        "qr_reference": str(entry.get("qr_reference") or "").strip(),
        "metadata": deepcopy(
            entry.get("metadata") if isinstance(entry.get("metadata"), dict) else {}
        ),
        "verification_history": deepcopy(verification_history),
        "witness_information": deepcopy(witness_information),
        "archive_status": str(entry.get("archive_status") or "not_specified").strip(),
    }


def list_records(index: dict[str, Any]) -> list[dict[str, Any]]:
    """List normalized explorer records without changing the source index."""

    return [
        normalize_record(entry)
        for entry in index.get("records", [])
        if isinstance(entry, dict)
    ]


SEARCH_FIELD_ALIASES = {
    "record_id": "record_id",
    "content_hash": "content_hash",
    "hash": "content_hash",
    "verification_status": "verification_status",
    "status": "verification_status",
    "source_path": "source_path",
}


def search_records(
    index: dict[str, Any], query: str, *, search_by: str = "record_id"
) -> list[dict[str, Any]]:
    """Search generated Explorer records without changing canonical records.

    Supported search fields are record_id, content_hash, verification_status,
    and source_path. The legacy ``hash`` and ``status`` aliases remain accepted
    for compatibility with the first Explorer MVP helper tests.
    """

    normalized_query = (query or "").strip().lower()
    if not normalized_query:
        return []

    field = SEARCH_FIELD_ALIASES.get((search_by or "").strip())
    if field is None:
        supported = ", ".join(sorted(SEARCH_FIELD_ALIASES))
        raise ValueError(f"Explorer search supports these fields only: {supported}.")

    return [
        record
        for record in list_records(index)
        if normalized_query in str(record.get(field, "")).lower()
    ]


def render_search_results(records: list[dict[str, Any]]) -> str:
    """Render advisory search matches as simple human-readable text."""

    if not records:
        return (
            "No matching generated explorer index entry was found. "
            "Absence from this index is not a trust-kernel decision."
        )

    lines = [
        "HC:// Public Verification Explorer search results",
        "Advisory-only, read-only generated index view.",
    ]
    for position, record in enumerate(records, start=1):
        lines.extend(
            [
                f"{position}. record_id: {record.get('record_id', '')}",
                f"   content_hash: {record.get('content_hash', '')}",
                f"   verification_status: {record.get('verification_status', '')}",
                f"   source_path: {record.get('source_path', '')}",
            ]
        )
    return "\n".join(lines)


def lookup_record(index: dict[str, Any], record_id: str) -> dict[str, Any]:
    """Return one record detail payload, or a safe missing-record response."""

    normalized_id = (record_id or "").strip()
    for record in list_records(index):
        if record["record_id"] == normalized_id:
            return {"found": True, "record": record, **ADVISORY_BOUNDARY}

    return {
        "found": False,
        "record_id": normalized_id,
        "message": "Record ID was not found in generated/explorer_index.json.",
        **ADVISORY_BOUNDARY,
    }


__all__ = [
    "ADVISORY_BOUNDARY",
    "DEFAULT_EXPLORER_INDEX",
    "SEARCH_FIELD_ALIASES",
    "list_records",
    "load_explorer_index",
    "lookup_record",
    "normalize_record",
    "render_search_results",
    "search_records",
]
