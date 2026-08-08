from pathlib import Path
from urllib.parse import parse_qs, urlparse

from hc_trust.qr_tools import (
    QR_CHECKSUM_PROFILE,
    generate_advisory_checksum,
    generate_qr,
)


def test_qr_link_uses_named_advisory_checksum_instead_of_signature(tmp_path):
    record_id = "HC-QR-2026-0001"
    content_hash = "a" * 64
    archive_ref = "records/verified/example.json"

    output_path, url = generate_qr(
        record_id,
        content_hash,
        archive_ref,
        output_dir=tmp_path,
    )

    query = parse_qs(urlparse(url).query)
    assert Path(output_path).is_file()
    assert query["checksum"] == [
        generate_advisory_checksum(record_id, content_hash, archive_ref)
    ]
    assert query["checksum_profile"] == [QR_CHECKSUM_PROFILE]
    assert "sig" not in query
