import json
from pathlib import Path
from jsonschema import validate, ValidationError

from .hashing import calculate_content_hash


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
        return [search_path]
    if search_path.is_dir():
        return sorted(search_path.rglob("*.json"))
    return []
