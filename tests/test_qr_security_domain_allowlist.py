import pytest

from qr_security import verify_qr_domain


def test_repository_backed_qr_domains_remain_allowed():
    assert verify_qr_domain("github.com") is True
    assert verify_qr_domain(" yolculuk38-debug.github.io ") is True


def test_legacy_humanitychain_domain_is_not_allowed():
    with pytest.raises(ValueError, match="untrusted qr verification domain"):
        verify_qr_domain("verify.humanitychain.org")
