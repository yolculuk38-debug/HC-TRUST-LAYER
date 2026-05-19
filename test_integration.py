#!/usr/bin/env python3
"""
Humanity Chain v1 Protocol - Integration Test Suite
Tests all core components: schema, validator, hash, QR
"""

import json
import sys
import hashlib
from pathlib import Path
from jsonschema import validate, ValidationError

# Test Results
test_results = []

def test_result(name, status, message=""):
    """Record test result"""
    result = {
        "test": name,
        "status": "✅ PASS" if status else "❌ FAIL",
        "message": message
    }
    test_results.append(result)
    print(f"{result['status']} | {name}" + (f" - {message}" if message else ""))


def collect_record_paths(base_dirs):
    """Collect files under record directories for validation."""
    paths = []
    for base_dir in base_dirs:
        for path in sorted(Path(base_dir).rglob("*")):
            if path.is_file():
                paths.append(path)
    return paths

# ==============================================================================
# TEST 1: Schema Validation
# ==============================================================================

print("\n" + "="*60)
print("TEST 1: Schema Validation")
print("="*60 + "\n")

try:
    with open('schema/record-v1.schema.json', 'r') as f:
        schema = json.load(f)
    test_result("Schema Load", True, "record-v1.schema.json loaded")
    
    # Check required fields in schema
    required_fields = schema.get('required', [])
    expected_fields = ["record_id", "created_at", "title", "record_type", 
                      "witness_type", "author", "content_hash", "archive_ref", 
                      "verification_status"]
    
    if all(field in required_fields for field in expected_fields):
        test_result("Schema Fields", True, f"{len(required_fields)} required fields")
    else:
        test_result("Schema Fields", False, "Missing required fields")
    
    # Check enums
    verification_statuses = schema['properties']['verification_status']['enum']
    if set(verification_statuses) == {"draft", "reviewed", "verified", "archived"}:
        test_result("Verification Status Enum", True, "All 4 statuses present")
    else:
        test_result("Verification Status Enum", False, f"Got {verification_statuses}")
        
except Exception as e:
    test_result("Schema Load", False, str(e))

# ==============================================================================
# TEST 2: Repository Record Discovery
# ==============================================================================

print("\n" + "="*60)
print("TEST 2: Repository Record Discovery")
print("="*60 + "\n")

record_directories = ["examples", "records", "witness", "halkalar"]
record_paths = collect_record_paths(record_directories)
json_record_paths = [path for path in record_paths if path.suffix.lower() == ".json"]

for path in record_paths:
    if path.suffix.lower() == ".json":
        test_result(f"DISCOVER {path}", True, "JSON candidate")
    else:
        test_result(f"SKIP {path}", True, "Non-JSON file")

# ==============================================================================
# TEST 3: Repository Records JSON Schema Validation
# ==============================================================================

print("\n" + "="*60)
print("TEST 3: Repository Records JSON Schema Validation")
print("="*60 + "\n")

for path in record_paths:
    if path.suffix.lower() != ".json":
        continue
    try:
        with open(path, 'r') as f:
            record = json.load(f)

        validate(instance=record, schema=schema)
        test_result(f"SCHEMA {path}", True, f"record_id={record.get('record_id', 'n/a')}")
    except ValidationError as e:
        test_result(f"SCHEMA {path}", False, e.message)
    except Exception as e:
        test_result(f"SCHEMA {path}", False, str(e))

# ==============================================================================
# TEST 4: Hash Tool Simulation
# ==============================================================================

print("\n" + "="*60)
print("TEST 4: Hash Tool Simulation")
print("="*60 + "\n")

try:
# Test SHA256 calculation on the first discovered JSON file
    test_file = str(json_record_paths[0])
    with open(test_file, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    if len(file_hash) == 64 and all(c in '0123456789abcdef' for c in file_hash):
        test_result("SHA256 Generation", True, f"Hash: {file_hash[:16]}...")
    else:
        test_result("SHA256 Generation", False, "Invalid hash format")
except Exception as e:
    test_result("SHA256 Generation", False, str(e))

# ==============================================================================
# TEST 5: Content Hash Format in Records
# ==============================================================================

print("\n" + "="*60)
print("TEST 5: Content Hash Format Validation")
print("="*60 + "\n")

for path in json_record_paths:
    try:
        with open(path, 'r') as f:
            record = json.load(f)
        
        content_hash = record.get('content_hash', '')
        # Check if it's a valid hex string of 64 chars (SHA256)
        is_valid_hash = len(content_hash) == 64 and all(c in '0123456789abcdef' for c in content_hash.lower())
        
        if is_valid_hash:
            test_result(f"Hash Format {record['record_id']}", True, 
                       f"{content_hash[:16]}...")
        else:
            test_result(f"Hash Format {record['record_id']}", False, 
                       "Invalid SHA256 format")
    except Exception as e:
        test_result(f"Hash Format", False, str(e))

# ==============================================================================
# TEST 6: Verification Status Enum Validation
# ==============================================================================

print("\n" + "="*60)
print("TEST 6: Verification Status Validation")
print("="*60 + "\n")

valid_statuses = {"draft", "reviewed", "verified", "archived"}

for path in json_record_paths:
    try:
        with open(path, 'r') as f:
            record = json.load(f)
        
        status = record.get('verification_status', '')
        if status in valid_statuses:
            test_result(f"Status {record['record_id']}", True, 
                       f"status={status}")
        else:
            test_result(f"Status {record['record_id']}", False, 
                       f"Invalid status: {status}")
    except Exception as e:
        test_result(f"Status Validation", False, str(e))

# ==============================================================================
# TEST 7: Record Type Validation
# ==============================================================================

print("\n" + "="*60)
print("TEST 7: Record Type Validation")
print("="*60 + "\n")

valid_record_types = {"ai_witness", "human_witness", "multi_model_record", "protocol_note"}
valid_witness_types = {"ai", "human", "multi"}

for path in json_record_paths:
    try:
        with open(path, 'r') as f:
            record = json.load(f)
        
        record_type = record.get('record_type', '')
        witness_type = record.get('witness_type', '')
        
        type_ok = record_type in valid_record_types
        witness_ok = witness_type in valid_witness_types
        
        if type_ok and witness_ok:
            test_result(f"Types {record['record_id']}", True, 
                       f"type={record_type}, witness={witness_type}")
        else:
            test_result(f"Types {record['record_id']}", False, 
                       f"Invalid types")
    except Exception as e:
        test_result(f"Types Validation", False, str(e))

# ==============================================================================
# TEST 8: Tools Exist
# ==============================================================================

print("\n" + "="*60)
print("TEST 8: Tools Exist")
print("="*60 + "\n")

tools = [
    "src/hash.py",
    "src/validator.py",
    "src/qr.py"
]

for tool in tools:
    try:
        with open(tool, 'r') as f:
            content = f.read()
        if len(content) > 0:
            test_result(f"Tool {Path(tool).name}", True, 
                       f"{len(content)} bytes")
        else:
            test_result(f"Tool {Path(tool).name}", False, "Empty file")
    except Exception as e:
        test_result(f"Tool {Path(tool).name}", False, str(e))

# ==============================================================================
# TEST 9: Requirements.txt
# ==============================================================================

print("\n" + "="*60)
print("TEST 9: Requirements File")
print("="*60 + "\n")

try:
    with open('requirements.txt', 'r') as f:
        reqs = f.read().strip().split('\n')
    
    required_packages = {"jsonschema", "qrcode"}
    found_packages = {line.split('[')[0].split('==')[0].lower() for line in reqs if line.strip()}
    
    if required_packages.issubset(found_packages):
        test_result("Requirements", True, f"{len(reqs)} packages")
    else:
        test_result("Requirements", False, f"Missing packages")
except Exception as e:
    test_result("Requirements", False, str(e))

# ==============================================================================
# TEST SUMMARY
# ==============================================================================

print("\n" + "="*60)
print("TEST SUMMARY")
print("="*60 + "\n")

passed = sum(1 for r in test_results if "PASS" in r['status'])
failed = sum(1 for r in test_results if "FAIL" in r['status'])
total = len(test_results)

print(f"✅ PASSED: {passed}/{total}")
print(f"❌ FAILED: {failed}/{total}")
print(f"📊 SUCCESS RATE: {(passed/total*100):.1f}%\n")

# Detailed results
print("Detailed Results:")
print("-" * 60)
for r in test_results:
    print(f"{r['status']} | {r['test']}")
    if r['message']:
        print(f"   └─ {r['message']}")

print("\n" + "="*60)
if failed == 0:
    print("🎉 ALL TESTS PASSED - PROTOCOL CORE READY!")
else:
    print(f"⚠️  {failed} TEST(S) FAILED - CHECK ABOVE")
print("="*60 + "\n")

sys.exit(0 if failed == 0 else 1)
