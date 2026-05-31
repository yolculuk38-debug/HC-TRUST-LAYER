"""Read-only HC:// public verification explorer helpers.

The helpers in this module use generated/explorer_index.json as an advisory
navigation source. They do not modify records, make automatic decisions, write to
federation surfaces, or calculate trust scoring.
"""

from __future__ import annotations

import html
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_EXPLORER_INDEX = ROOT / "generated" / "explorer_index.json"
EXPLORER_RECORD_ROUTE = "/explorer/record/{record_id}"
SHORT_RECORD_ROUTE = "/record/{record_id}"

ADVISORY_BOUNDARY = {
    "advisory_only": True,
    "read_only": True,
    "human_supervised": True,
    "automatic_decision": False,
    "record_modification": False,
    "federation_write": False,
}


def load_explorer_index(index_path: Path | str = DEFAULT_EXPLORER_INDEX) -> dict[str, Any]:
    """Load generated explorer index data from disk."""

    path = Path(index_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Explorer index must be a JSON object.")
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("Explorer index must contain a records list.")
    return data


def normalize_record(entry: dict[str, Any]) -> dict[str, Any]:
    """Return the public read-only shape used by the Explorer MVP."""

    content_hash = str(entry.get("content_hash") or entry.get("hash") or "")
    witness_information = entry.get("witness_information") or entry.get("witnesses") or []
    if not isinstance(witness_information, list):
        witness_information = []
    verification_history = entry.get("verification_history") or []
    if not isinstance(verification_history, list):
        verification_history = []

    return {
        **ADVISORY_BOUNDARY,
        "record_id": str(entry.get("record_id") or entry.get("id") or "").strip(),
        "verification_status": str(entry.get("verification_status") or entry.get("status") or "unavailable").strip(),
        "timestamp": str(entry.get("timestamp") or "").strip(),
        "content_hash": content_hash.strip(),
        "qr_reference": str(entry.get("qr_reference") or entry.get("qr_url") or entry.get("qr") or "").strip(),
        "witness_count": int(entry.get("witness_count") or len(witness_information) or 0),
        "source_path": str(entry.get("source_path") or entry.get("source_file") or "").strip(),
        "metadata": deepcopy(entry.get("metadata") if isinstance(entry.get("metadata"), dict) else {}),
        "verification_history": deepcopy(verification_history),
        "witness_information": deepcopy(witness_information),
        "archive_status": str(entry.get("archive_status") or "not_specified").strip(),
    }


def build_record_detail_response(index: dict[str, Any], record_id: str) -> dict[str, Any]:
    """Return a structured read-only detail response for a record route."""

    response = lookup_record(index, record_id)
    normalized_id = (record_id or "").strip()
    if not response.get("found"):
        return {
            "route": EXPLORER_RECORD_ROUTE.format(record_id=normalized_id),
            "alternate_route": SHORT_RECORD_ROUTE.format(record_id=normalized_id),
            "found": False,
            "record_id": normalized_id,
            "message": "Record detail is unavailable because the Record ID was not found in generated/explorer_index.json.",
            "error": {
                "code": "record_not_found",
                "human_message": "No generated explorer detail is available for this Record ID.",
            },
            **ADVISORY_BOUNDARY,
        }

    record = deepcopy(response["record"])
    return {
        "route": EXPLORER_RECORD_ROUTE.format(record_id=record["record_id"]),
        "alternate_route": SHORT_RECORD_ROUTE.format(record_id=record["record_id"]),
        "found": True,
        "record_id": record["record_id"],
        "verification_summary": {
            "verification_status": record["verification_status"],
            "timestamp": record["timestamp"],
            "advisory_only": True,
            "human_supervised": True,
        },
        "record_metadata": {
            "record_id": record["record_id"],
            "source_path": record["source_path"],
            "qr_reference": record["qr_reference"],
            "metadata": deepcopy(record["metadata"]),
        },
        "hash_information": {
            "content_hash": record["content_hash"],
        },
        "witness_information": {
            "witness_count": record["witness_count"],
            "witnesses": deepcopy(record["witness_information"]),
        },
        "record": record,
        **ADVISORY_BOUNDARY,
    }


def render_record_detail_html(index: dict[str, Any], record_id: str) -> str:
    """Render deterministic human-readable HTML for one explorer record detail."""

    response = build_record_detail_response(index, record_id)

    def esc(value: Any) -> str:
        if isinstance(value, (dict, list)):
            value = json.dumps(value, indent=2, sort_keys=True)
        return html.escape(str(value or ""))

    if not response["found"]:
        return (
            '<section class="record-detail record-detail--missing">'
            '<h1>Record Detail Unavailable</h1>'
            f'<p>{esc(response["message"])}</p>'
            f'<pre>{esc(response)}</pre>'
            '</section>'
        )

    record = response["record"]
    witnesses = record["witness_information"] or []
    witness_items = "".join(f"<li>{esc(witness)}</li>" for witness in witnesses) or "<li>Not present in the generated explorer index entry.</li>"
    qr_reference = record["qr_reference"] or "Not present in the generated explorer index entry."
    return (
        '<article class="record-detail">'
        f'<h1>Record Detail: {esc(record["record_id"])}</h1>'
        '<section><h2>Verification Summary</h2>'
        f'<dl><dt>Record ID</dt><dd>{esc(record["record_id"])}</dd>'
        f'<dt>Verification Status</dt><dd>{esc(record["verification_status"])}</dd>'
        f'<dt>Timestamp</dt><dd>{esc(record["timestamp"])}</dd></dl></section>'
        '<section><h2>Record Metadata</h2>'
        f'<dl><dt>Source path</dt><dd>{esc(record["source_path"])}</dd>'
        f'<dt>QR reference</dt><dd>{esc(qr_reference)}</dd>'
        f'<dt>Metadata</dt><dd><pre>{esc(record["metadata"])}</pre></dd></dl></section>'
        '<section><h2>Hash Information</h2>'
        f'<dl><dt>Content Hash</dt><dd><code>{esc(record["content_hash"])}</code></dd></dl></section>'
        '<section><h2>Witness Information</h2>'
        f'<dl><dt>Witness count</dt><dd>{esc(record["witness_count"])}</dd></dl>'
        f'<ul>{witness_items}</ul></section>'
        '</article>'
    )


def list_records(index: dict[str, Any]) -> list[dict[str, Any]]:
    """List normalized explorer records without changing the source index."""

    return [normalize_record(entry) for entry in index.get("records", []) if isinstance(entry, dict)]


def search_records(index: dict[str, Any], query: str, *, search_by: str = "record_id") -> list[dict[str, Any]]:
    """Search by record ID or content hash within the generated explorer index."""

    normalized_query = (query or "").strip().lower()
    if not normalized_query:
        return []
    if search_by not in {"record_id", "hash"}:
        raise ValueError("Explorer search supports record_id or hash only.")

    field = "record_id" if search_by == "record_id" else "content_hash"
    return [
        record
        for record in list_records(index)
        if normalized_query in str(record.get(field, "")).lower()
    ]


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
    "EXPLORER_RECORD_ROUTE",
    "SHORT_RECORD_ROUTE",
    "build_record_detail_response",
    "list_records",
    "load_explorer_index",
    "lookup_record",
    "normalize_record",
    "render_record_detail_html",
    "search_records",
]
