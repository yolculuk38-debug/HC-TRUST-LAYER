"""Local-only HC:// Public Validator record_id lookup MVP."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
ALLOWED_RECORD_PATTERNS: tuple[str, ...] = (
    "records/pending/*.json",
    "records/verified/*.json",
    "records/archived/*.json",
)
SAFETY_MARKERS: dict[str, bool] = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}
EXCLUDED_ARTIFACT_NAME_MARKERS: tuple[str, ...] = ("index", "manifest", "cache", "export")
_VALID_RECORD_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:_-]{0,199}$")


def _checked_paths() -> list[str]:
    return list(ALLOWED_RECORD_PATTERNS)


def _base_result(record_id: str, status: str, found: bool) -> dict[str, Any]:
    return {
        "record_id": record_id,
        "status": status,
        "found": found,
        "source_path": None,
        **SAFETY_MARKERS,
        "warnings": [],
        "errors": [],
        "checked_paths": _checked_paths(),
    }


def _is_valid_record_id(record_id: object) -> bool:
    if not isinstance(record_id, str):
        return False
    if record_id != record_id.strip():
        return False
    if "://" in record_id:
        return False
    return bool(_VALID_RECORD_ID.fullmatch(record_id))


def _relative_path(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _iter_allowed_json_paths(root: Path) -> list[Path]:
    resolved_root = root.resolve()
    paths: list[Path] = []
    for pattern in ALLOWED_RECORD_PATTERNS:
        relative_directory = Path(pattern).parent
        directory = (resolved_root / relative_directory).resolve()
        try:
            directory.relative_to(resolved_root)
        except ValueError:
            continue
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.json"), key=lambda candidate: candidate.as_posix()):
            resolved_path = path.resolve()
            try:
                resolved_path.relative_to(directory)
                resolved_path.relative_to(resolved_root)
            except ValueError:
                continue
            lowered_name = resolved_path.name.lower()
            if any(marker in lowered_name for marker in EXCLUDED_ARTIFACT_NAME_MARKERS):
                continue
            if resolved_path.is_file():
                paths.append(resolved_path)
    return paths


def lookup_public_validator_record(record_id: str, *, root: Path | str = ROOT) -> dict[str, Any]:
    """Resolve a record_id against allowed local canonical record directories only.

    The result is deterministic, public-safe, and advisory-only. It is not a
    production API response, truth verification, QR authenticity proof, signed
    payload verification, or schema/hash validation result.
    """

    requested_record_id = record_id if isinstance(record_id, str) else ""
    if not _is_valid_record_id(record_id):
        result = _base_result(requested_record_id, "invalid_record_id", False)
        result["errors"].append("Invalid record_id. Provide a non-empty record_id, not a path, URL, or query.")
        return result

    resolved_root = Path(root).resolve()
    result = _base_result(record_id, "not_found", False)
    matches: list[tuple[Path, dict[str, Any]]] = []

    try:
        for path in _iter_allowed_json_paths(resolved_root):
            try:
                with path.open(encoding="utf-8") as handle:
                    payload = json.load(handle)
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                if path.stem == record_id:
                    result["status"] = "lookup_error"
                    result["errors"].append(
                        f"Allowed record JSON could not be loaded from {_relative_path(resolved_root, path)}: {exc.__class__.__name__}."
                    )
                    return result
                continue

            if not isinstance(payload, dict):
                continue
            if payload.get("record_id") == record_id:
                matches.append((path, payload))
    except OSError as exc:
        result["status"] = "lookup_error"
        result["errors"].append(f"Local lookup failed: {exc.__class__.__name__}.")
        return result

    if not matches:
        result["warnings"].append(
            "No matching record_id was found in allowed canonical record directories; demo fixtures and generated artifacts were not checked."
        )
        return result

    if len(matches) > 1:
        result["status"] = "duplicate_record_id"
        result["errors"].append("Duplicate record_id matches were found in allowed canonical record directories.")
        result["warnings"].extend(_relative_path(resolved_root, path) for path, _payload in matches)
        return result

    source_path, _payload = matches[0]
    result["status"] = "found"
    result["found"] = True
    result["source_path"] = _relative_path(resolved_root, source_path)
    result["warnings"].append(
        "Local MVP lookup only; schema/hash validation, truth verification, QR authenticity, and signed payload verification are not performed."
    )
    return result
