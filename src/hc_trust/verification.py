import re
import sysconfig
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError

from .canonicalization import CanonicalizationError, canonicalize_json, strict_json_load
from .hashing import (
    CONTENT_HASH_PROFILE_FIELD,
    HC_CONTENT_HASH_PROFILE,
    ContentHashError,
    calculate_content_hash,
)

ALLOWED_RECORD_DIRS = ("pending", "verified", "archived")
RECORD_SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"
RECORD_SCHEMA_ID = (
    "https://raw.githubusercontent.com/yolculuk38-debug/HC-TRUST-LAYER/"
    "main/schema/record-v1.schema.json"
)
RECORD_SCHEMA_VERSION = "hc-record-v1"
_SOURCE_RECORD_SCHEMA_PATH = Path(__file__).resolve().parents[2] / "schema" / "record-v1.schema.json"
_INSTALLED_RECORD_SCHEMA_PATH = (
    Path(sysconfig.get_path("data"))
    / "share"
    / "hc-trust-layer"
    / "schema"
    / "record-v1.schema.json"
)
DEFAULT_RECORD_SCHEMA_PATH = (
    _SOURCE_RECORD_SCHEMA_PATH
    if _SOURCE_RECORD_SCHEMA_PATH.is_file()
    else _INSTALLED_RECORD_SCHEMA_PATH
)
RECORD_FORMAT_CHECKER = FormatChecker()
_RFC3339_DATETIME = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]+)?(?:Z|[+-][0-9]{2}:[0-9]{2})$"
)
SKIP_HINTS = (
    "index",
    "manifest",
    "cache",
    "export",
    "generated",
)


@RECORD_FORMAT_CHECKER.checks("date-time", raises=ValueError)
def _is_rfc3339_datetime(value: object) -> bool:
    """Validate the strict RFC 3339 profile used by canonical HC:// records."""

    if not isinstance(value, str) or _RFC3339_DATETIME.fullmatch(value) is None:
        return False
    normalized = f"{value[:-1]}+00:00" if value.endswith("Z") else value
    datetime.fromisoformat(normalized)
    return True


class RecordSchemaError(ValueError):
    """Fail-closed error raised when the canonical record schema is unusable."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


def load_schema(schema_path: str | Path = DEFAULT_RECORD_SCHEMA_PATH) -> dict[str, Any]:
    try:
        with Path(schema_path).open("r", encoding="utf-8") as handle:
            schema = strict_json_load(handle)
    except FileNotFoundError as exc:
        raise RecordSchemaError("record_schema_missing") from exc
    except (OSError, UnicodeDecodeError, CanonicalizationError) as exc:
        raise RecordSchemaError("record_schema_unreadable") from exc

    if not isinstance(schema, dict):
        raise RecordSchemaError("record_schema_object_required")
    if schema.get("$schema") != RECORD_SCHEMA_DIALECT:
        raise RecordSchemaError("record_schema_dialect_mismatch")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RecordSchemaError("record_schema_invalid") from exc

    if schema.get("$id") != RECORD_SCHEMA_ID:
        raise RecordSchemaError("record_schema_id_mismatch")
    properties = schema.get("properties")
    if not isinstance(properties, dict):  # pragma: no cover - check_schema guard
        raise RecordSchemaError("record_schema_invalid")
    schema_version = properties.get("schema_version")
    if not isinstance(schema_version, dict) or schema_version.get("const") != RECORD_SCHEMA_VERSION:
        raise RecordSchemaError("record_schema_version_mismatch")
    hash_profile = properties.get(CONTENT_HASH_PROFILE_FIELD)
    if not isinstance(hash_profile, dict) or hash_profile.get("const") != HC_CONTENT_HASH_PROFILE:
        raise RecordSchemaError("record_schema_hash_profile_mismatch")
    return schema


def _validation_path(error: ValidationError) -> str:
    path = "$"
    for segment in error.absolute_path:
        if isinstance(segment, int):
            path += f"[{segment}]"
        else:
            path += f".{segment}"
    return path


def _validation_error_message(error: ValidationError) -> str:
    path = _validation_path(error)
    rule = str(error.validator or "schema")
    if rule == "required" and isinstance(error.instance, dict):
        expected = set(error.validator_value) if isinstance(error.validator_value, list) else set()
        missing = sorted(expected - set(error.instance))
        if missing:
            return f"{path}: required constraint failed ({', '.join(missing)})"
    return f"{path}: {rule} constraint failed"


def validate_record_payload(
    record: object,
    schema_path: str | Path = DEFAULT_RECORD_SCHEMA_PATH,
) -> tuple[bool, list[str]]:
    """Validate one parsed record against the shared Draft 2020-12 contract."""

    if not isinstance(record, dict):
        return False, ["$: type constraint failed"]
    try:
        canonicalize_json(record)
    except CanonicalizationError as exc:
        return False, [f"$: strict_json constraint failed ({exc.reason})"]
    try:
        schema = load_schema(schema_path)
    except RecordSchemaError as exc:
        return False, [f"$: schema unavailable ({exc.reason})"]

    validator = Draft202012Validator(schema, format_checker=RECORD_FORMAT_CHECKER)
    errors = sorted(
        validator.iter_errors(record),
        key=lambda error: (
            tuple(str(segment) for segment in error.absolute_path),
            str(error.validator),
        ),
    )
    messages = list(dict.fromkeys(_validation_error_message(error) for error in errors))
    return not messages, messages


def validate_record(
    record_path: str | Path,
    schema_path: str | Path = DEFAULT_RECORD_SCHEMA_PATH,
) -> tuple[bool, str]:
    try:
        with Path(record_path).open("r", encoding="utf-8") as handle:
            record = strict_json_load(handle)
    except FileNotFoundError:
        return False, f"Record file not found: {record_path}"
    except OSError:
        return False, f"Record file could not be read: {record_path}"
    except (CanonicalizationError, UnicodeDecodeError):
        return False, f"Invalid record JSON: {record_path}"

    passed, errors = validate_record_payload(record, schema_path)
    if passed:
        return True, f"VALID RECORD: {record_path}"
    return False, f"SCHEMA VALIDATION FAILED: {'; '.join(errors)}"


def verify_record_hash(record_path):
    try:
        with open(record_path, "r", encoding="utf-8") as f:
            record = strict_json_load(f)
    except FileNotFoundError:
        return False, f"File not found: {record_path}"
    except (CanonicalizationError, UnicodeDecodeError) as exc:
        reason = exc.reason if isinstance(exc, CanonicalizationError) else "invalid_unicode"
        return False, f"Invalid JSON: {record_path} -> {reason}"

    if not isinstance(record, dict):
        return False, f"Record JSON must be an object: {record_path}"

    if "content_hash" not in record:
        return False, f"Missing 'content_hash' field in {record_path}"
    if "content" not in record:
        return False, f"Missing 'content' field in {record_path}"

    content_hash_declared = record["content_hash"]
    try:
        if CONTENT_HASH_PROFILE_FIELD in record:
            content_hash_actual = calculate_content_hash(
                record["content"], record[CONTENT_HASH_PROFILE_FIELD]
            )
        else:
            content_hash_actual = calculate_content_hash(record["content"])
    except ContentHashError as exc:
        return False, f"Content hash verification could not be performed: {exc.reason}."

    if content_hash_declared == content_hash_actual:
        return True, f"PASS: {record_path} (hash: {content_hash_actual[:16]}...)"
    return False, (
        f"FAIL: {record_path}\n"
        f"  Expected: {content_hash_declared}\n"
        f"  Got:      {content_hash_actual}"
    )


def find_record_files(search_path="records"):
    search_path = Path(search_path)
    if search_path.is_file() and search_path.suffix == ".json":
        files = [search_path]
    elif search_path.is_dir():
        files = sorted(search_path.rglob("*.json"))
    else:
        return [], []

    selected = []
    skipped = []
    for file_path in files:
        if should_validate_record_file(file_path):
            selected.append(file_path)
        else:
            skipped.append(file_path)
    return selected, skipped


def should_validate_record_file(file_path):
    file_path = Path(file_path)
    parts = file_path.parts

    if "records" not in parts:
        return False
    records_idx = parts.index("records")
    if len(parts) <= records_idx + 2:
        return False

    record_group = parts[records_idx + 1]
    if record_group not in ALLOWED_RECORD_DIRS:
        return False

    filename = file_path.name.lower()
    if filename == "explorer_index.json":
        return False
    if any(hint in filename for hint in SKIP_HINTS):
        return False
    return True
