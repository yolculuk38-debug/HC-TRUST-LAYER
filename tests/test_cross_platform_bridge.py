from cross_platform_bridge import (
    PlatformSource,
    normalize_platform_payload,
)



def test_valid_platform_payload():
    result = normalize_platform_payload(
        {
            "record_id": "REC-1",
            "content_hash": "abc123",
        },
        platform=PlatformSource.API,
    )

    assert result["valid"] is True



def test_invalid_platform_payload():
    result = normalize_platform_payload(
        {
            "metadata": {},
        },
        platform=PlatformSource.WEB,
    )

    assert result["valid"] is False
