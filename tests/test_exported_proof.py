from exported_proof import build_exported_proof


def test_exported_proof_build():
    proof = build_exported_proof(
        record_id="HC-EXPORT-1",
        content_hash="abc123",
        verification_level="LEVEL_3_MULTI_WITNESS_VERIFIED",
        trust_passport={"status": "VERIFIED"},
        witnesses=[{"witness_signature": "sig1"}],
    )

    assert proof["proof_version"] == "HC-EXPORTED-PROOF-V1"
    assert proof["record_id"] == "HC-EXPORT-1"
    assert proof["verification_level"] is None
    assert proof["source_claims"]["verification_level"] == "LEVEL_3_MULTI_WITNESS_VERIFIED"
    assert proof["source_claims"]["trust_passport"] == {"status": "VERIFIED"}
    assert proof["trust_passport"] == {}
    assert proof["content_hash_valid"] is None
    assert proof["content_hash_checked"] is False
    assert proof["verified"] is False
    assert proof["signature_verified"] is False
    assert proof["source_claims_verified"] is False
    assert proof["public_safe"] is False
