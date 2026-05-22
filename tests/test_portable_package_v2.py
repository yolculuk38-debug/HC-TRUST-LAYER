from portable_package_v2 import (
    build_portable_package_v2,
    validate_portable_package_v2,
)



def test_valid_portable_package_v2():
    package = build_portable_package_v2(
        record_id="REC-1",
        exported_proof={"proof": True},
        certificate={"verified": True},
        risk_summary={"risk_level": "LOW"},
        policy_state={"decision": "ALLOW"},
        audit_snapshot={"snapshot": True},
        timeline={"events": []},
    )

    result = validate_portable_package_v2(package)

    assert result["valid"] is True



def test_invalid_portable_package_v2():
    result = validate_portable_package_v2(
        {
            "record_id": "REC-2",
        }
    )

    assert result["valid"] is False
