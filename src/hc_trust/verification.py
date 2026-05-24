import json
from pathlib import Path
from jsonschema import validate, ValidationError

from .hashing import calculate_content_hash

CANONICAL_RECORD_DIRS = {
    Path("records") / "pending",
    Path("records") / "verified",
    Path("records") / "archived",
}

SKIP_NAME_MARKERS = (
    "index",
    "manifest",
    "cache",
    "export",
)

SKIP_PATH_MARKERS = (
    "generated",
    "cache",
    "exports",
    "export",
    "manifests",
)


def load_schema(schema_path="schema/record-v1.schema.json"):
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_record(record_path, schema_path="schema/record-v1.schema.json"):
    schema = load_schema(schema_path)
    try:
        with open(record_path, "r", encoding="utf-8") as f:
            record = json.load(f)
    except FileNotFoundError:
        return False, f"Hata: Dosya bulunamadı: {record_path}"
    except json.JSONDecodeError:
        return False, f"Hata: Geçersiz JSON: {record_path}"

    try:
        validate(instance=record, schema=schema)
        return True, f"✅ VALID RECORD: {record_path}"
    except ValidationError as e:
        return False, f"❌ VALIDATION ERROR: {e.message}"


def verify_record_hash(record_path):
    try:
        with open(record_path, "r", encoding="utf-8") as f:
            record = json.load(f)
    except FileNotFoundError:
        return False, f"File not found: {record_path}"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {record_path} -> {e}"

    if "content_hash" not in record:
        return False, f"Missing 'content_hash' field in {record_path}"
    if "content" not in record:
        return False, f"Missing 'content' field in {record_path}"

    content_hash_declared = record["content_hash"]
    content_hash_actual = calculate_content_hash(record["content"])

    if content_hash_declared == content_hash_actual:
        return True, f"PASS: {record_path} (hash: {content_hash_actual[:16]}...)"
    return False, (
        f"FAIL: {record_path}\n"
        f"  Expected: {content_hash_declared}\n"
        f"  Got:      {content_hash_actual}"
    )


def _normalized_relative_path(file_path):
    path = Path(file_path)
    try:
        return path.resolve().relative_to(Path.cwd().resolve())
    except ValueError:
        return path


def _is_canonical_record_file(file_path):
    relative_path = _normalized_relative_path(file_path)
    return (
        relative_path.suffix == ".json"
        and relative_path.parent in CANONICAL_RECORD_DIRS
    )


def _skip_reason(file_path):
    relative_path = _normalized_relative_path(file_path)
    lower_name = relative_path.name.lower()
    lower_parts = {part.lower() for part in relative_path.parts}

    if _is_canonical_record_file(file_path):
        return None
    if any(marker in lower_name for marker in SKIP_NAME_MARKERS):
        return "generated/index/manifest/cache/export artifact"
    if any(marker in lower_parts for marker in SKIP_PATH_MARKERS):
        return "generated/cache/export artifact path"
    return "non-canonical record path"


def find_record_files(search_path="records"):
    search_path = Path(search_path)

    if search_path.is_file() and search_path.suffix == ".json":
        reason = _skip_reason(search_path)
        if reason is None:
            return [search_path]
        print(f"SKIP: {search_path} ({reason})")
        return []

    if search_path.is_dir():
        record_files = []
        for file_path in sorted(search_path.rglob("*.json")):
            reason = _skip_reason(file_path)
            if reason is None:
                record_files.append(file_path)
            else:
                print(f"SKIP: {file_path} ({reason})")
        return record_files

    return []
