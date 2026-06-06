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
RESULT_FIELD_CONTRACT: tuple[str, ...] = (
    "record_id",
    "status",
    "found",
    "source_path",
    "advisory_only",
    "public_safe",
    "truth_guarantee",
    "human_review_required",
    "warnings",
    "errors",
    "checked_paths",
    "schema_validation",
    "hash_validation",
    "validation_summary",
)
ALLOWED_LOOKUP_STATUSES: frozenset[str] = frozenset(
    {"found", "not_found", "duplicate_record_id", "invalid_record_id", "lookup_error"}
)
ALLOWED_VALIDATION_STATUSES: frozenset[str] = frozenset({"pass", "fail", "not_checked"})
SAFETY_MARKERS: dict[str, bool] = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}
EXCLUDED_ARTIFACT_NAME_MARKERS: tuple[str, ...] = ("index", "manifest", "cache", "export")
_VALID_RECORD_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:_-]{0,199}$")


def _validation_result(status: str = "not_checked", errors: list[str] | None = None) -> dict[str, Any]:
    if status not in ALLOWED_VALIDATION_STATUSES:
        raise ValueError(f"Unsupported validation status: {status}")
    return {"status": status, "errors": list(errors or [])}


def _checked_paths() -> list[str]:
    return list(ALLOWED_RECORD_PATTERNS)


def _base_result(record_id: str, status: str, found: bool) -> dict[str, Any]:
    if status not in ALLOWED_LOOKUP_STATUSES:
        raise ValueError(f"Unsupported lookup status: {status}")
    result = {
        "record_id": record_id,
        "status": status,
        "found": found,
        "source_path": None,
        **SAFETY_MARKERS,
        "warnings": [],
        "errors": [],
        "checked_paths": _checked_paths(),
        "schema_validation": _validation_result(),
        "hash_validation": _validation_result(),
        "validation_summary": {
            "schema_passed": False,
            "hash_passed": False,
            "canonical_record_checked": False,
        },
    }
    if tuple(result) != RESULT_FIELD_CONTRACT:
        raise RuntimeError("Public Validator lookup result contract changed unexpectedly.")
    return result


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


def _check_schema_validation(record_path: Path, root: Path) -> dict[str, Any]:
    try:
        from hc_trust.verification import validate_record
    except ImportError as exc:
        return _validation_result("not_checked", [f"Existing schema validator is unavailable: {exc.__class__.__name__}."])

    schema_path = root / "schema" / "record-v1.schema.json"
    if not schema_path.is_file():
        return _validation_result("not_checked", ["Existing canonical record schema was not found at schema/record-v1.schema.json."])

    try:
        passed, message = validate_record(record_path, schema_path)
    except Exception as exc:  # pragma: no cover - defensive wrapper around existing helper
        return _validation_result("not_checked", [f"Existing schema validator could not be safely reused: {exc.__class__.__name__}."])

    if passed:
        return _validation_result("pass")
    return _validation_result("fail", [message])


def _check_hash_validation(record_path: Path) -> dict[str, Any]:
    try:
        from hc_trust.verification import verify_record_hash
    except ImportError as exc:
        try:
            from hc_trust.hashing import calculate_content_hash
        except ImportError:
            return _validation_result("not_checked", [f"Existing content hash verifier is unavailable: {exc.__class__.__name__}."])

        try:
            with record_path.open(encoding="utf-8") as handle:
                record = json.load(handle)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as read_exc:
            return _validation_result("not_checked", [f"Content hash input could not be loaded: {read_exc.__class__.__name__}."])
        if not isinstance(record, dict):
            return _validation_result("fail", ["Record JSON must be an object for content_hash validation."])
        if "content_hash" not in record:
            return _validation_result("fail", ["Missing 'content_hash' field for content_hash validation."])
        if "content" not in record:
            return _validation_result("fail", ["Missing 'content' field for content_hash validation."])
        calculated_hash = calculate_content_hash(record["content"])
        if str(record["content_hash"]) == calculated_hash:
            return _validation_result("pass")
        return _validation_result("fail", ["content_hash does not match canonical record content."])

    try:
        passed, message = verify_record_hash(record_path)
    except Exception as exc:  # pragma: no cover - defensive wrapper around existing helper
        return _validation_result("not_checked", [f"Existing content hash verifier could not be safely reused: {exc.__class__.__name__}."])

    if passed:
        return _validation_result("pass")
    return _validation_result("fail", [message])


def _apply_validation_signals(result: dict[str, Any], record_path: Path, root: Path) -> None:
    schema_validation = _check_schema_validation(record_path, root)
    hash_validation = _check_hash_validation(record_path)

    result["schema_validation"] = schema_validation
    result["hash_validation"] = hash_validation
    result["validation_summary"] = {
        "schema_passed": schema_validation["status"] == "pass",
        "hash_passed": hash_validation["status"] == "pass",
        "canonical_record_checked": True,
    }

    for label, validation in (("schema", schema_validation), ("hash", hash_validation)):
        if validation["status"] == "fail":
            result["warnings"].append(f"Advisory {label} validation failed; human review remains required.")
            result["errors"].extend(validation["errors"])
        elif validation["status"] == "not_checked":
            result["warnings"].append(f"Advisory {label} validation was not checked; human review remains required.")
            result["warnings"].extend(validation["errors"])


def lookup_public_validator_record(record_id: str, *, root: Path | str = ROOT) -> dict[str, Any]:
    """Resolve a record_id against allowed local canonical record directories only.

    The result is deterministic, public-safe, and advisory-only. It is not a
    production API response, truth verification, QR authenticity proof, or
    signed payload verification. Schema/hash validation signals are advisory
    and require human review.
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
    _apply_validation_signals(result, source_path, resolved_root)
    result["warnings"].append(
        "Local MVP lookup only; schema/hash validation signals are advisory and do not provide truth verification, QR authenticity, or signed payload verification."
    )
    return result
