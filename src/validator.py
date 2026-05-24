#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from jsonschema import validate, ValidationError

def load_schema(schema_path="schema/record-v1.schema.json"):
    """Schema dosyasını yükle"""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

SKIP_HINTS = ("index", "manifest", "cache", "export", "generated")


def validate_record(record_path):
    """Record dosyasını doğrula"""
    schema = load_schema()
    
    file_name = Path(record_path).name.lower()
    if any(hint in file_name for hint in SKIP_HINTS):
        print(f"⏭️ SKIPPED ARTIFACT: {record_path}")
        return True

    try:
        with open(record_path, 'r', encoding='utf-8') as f:
            record = json.load(f)
    except FileNotFoundError:
        print(f"Hata: Dosya bulunamadı: {record_path}")
        return False
    except json.JSONDecodeError:
        print(f"Hata: Geçersiz JSON: {record_path}")
        return False
    
    try:
        validate(instance=record, schema=schema)
        print(f"✅ VALID RECORD: {record_path}")
        return True
    except ValidationError as e:
        print(f"❌ VALIDATION ERROR: {e.message}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python src/validator.py <record.json>")
        sys.exit(1)
    
    record_path = sys.argv[1]
    success = validate_record(record_path)
    sys.exit(0 if success else 1)
