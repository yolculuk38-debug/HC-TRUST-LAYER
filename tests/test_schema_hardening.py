from schema_hardening import validate_hardened_package



def test_valid_hardened_package():
    result = validate_hardened_package(
        {
            "portable_package_version": "HC-PORTABLE-PACKAGE-V2",
            "record_id": "REC-1",
            "exported_proof": {},
            "certificate": {},
            "risk_summary": {},
            "policy_state": {},
            "audit_snapshot": {},
            "timeline": {},
        }
    )

    assert result["valid"] is True



def test_invalid_hardened_package():
    result = validate_hardened_package(
        {
            "portable_package_version": "UNKNOWN",
            "record_id": 123,
            "__tampered": True,
        }
    )

    assert result["valid"] is False
