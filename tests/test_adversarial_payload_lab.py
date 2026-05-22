from adversarial_payload_lab import inspect_payload



def test_clean_payload():
    result = inspect_payload(
        {
            "portable_package_version": "HC-PORTABLE-PACKAGE-V2",
            "record_id": "REC-1",
            "qr_url": "https://example.com/verify/REC-1",
        }
    )

    assert result["clean"] is True



def test_suspicious_payload():
    result = inspect_payload(
        {
            "portable_package_version": "UNKNOWN",
            "__debug": True,
            "qr_url": "http://unsafe.example",
            "provenance": "forged",
        }
    )

    assert result["clean"] is False
