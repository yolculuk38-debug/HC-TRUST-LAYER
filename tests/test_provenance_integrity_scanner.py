from provenance_integrity_scanner import (
    ProvenanceRisk,
    scan_provenance_integrity,
)



def test_clean_provenance():
    result = scan_provenance_integrity(
        {
            "orphan_revision": False,
            "broken_lineage": False,
            "forged_reference": False,
            "tamper_anomaly": False,
        }
    )

    assert result["decision"] == ProvenanceRisk.CLEAN



def test_invalid_provenance():
    result = scan_provenance_integrity(
        {
            "orphan_revision": True,
            "broken_lineage": True,
            "forged_reference": True,
            "tamper_anomaly": True,
        }
    )

    assert result["decision"] == ProvenanceRisk.INVALID
