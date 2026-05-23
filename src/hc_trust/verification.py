import json
from pathlib import Path
from jsonschema import validate, ValidationError

from .hashing import calculate_content_hash

ALLOWED_RECORD_DIRS = ("pending", "verified", "archived")
SKIP_HINTS = (
    "index",
    "manifest",
    "cache",
    "export",
    "generated",
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
