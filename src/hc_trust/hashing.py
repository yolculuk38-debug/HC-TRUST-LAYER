import hashlib

from .canonicalization import CanonicalizationError, canonicalize_json

DIGEST_ALGORITHM = "sha-256"
HC_CONTENT_HASH_PROFILE = "hc-content-sha256-v2"
# This identifier names the algorithm-absent text compatibility path. P0-2 does
# not accept it as an explicit record field value; schema transition is P0-3.
LEGACY_TEXT_HASH_PROFILE = "hc-content-raw-utf8-sha256-v1"
HC_QR_PAYLOAD_HASH_PROFILE = "hc-qr-payload-jcs-sha256-v1"
CONTENT_HASH_PROFILE_FIELD = "content_hash_profile"
_CONTENT_HASH_PROFILE_ABSENT = object()


class ContentHashError(ValueError):
    """Public-safe failure raised when an HC digest cannot be computed."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def calculate_content_hash(
    content,
    content_hash_profile=_CONTENT_HASH_PROFILE_ABSENT,
):
    """Return an HC content digest or fail closed on an ambiguous profile."""

    if content_hash_profile is _CONTENT_HASH_PROFILE_ABSENT:
        if type(content) is not str:
            raise ContentHashError("legacy_structured_content_algorithm_ambiguous")
        try:
            content_bytes = content.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise ContentHashError("content_encoding_failed") from exc
    elif type(content_hash_profile) is str and content_hash_profile == HC_CONTENT_HASH_PROFILE:
        if type(content) is str:
            try:
                content_bytes = content.encode("utf-8")
            except UnicodeEncodeError as exc:
                raise ContentHashError("content_encoding_failed") from exc
        else:
            try:
                content_bytes = canonicalize_json(content)
            except CanonicalizationError as exc:
                raise ContentHashError("content_canonicalization_failed") from exc
    else:
        raise ContentHashError("unknown_content_hash_profile")
    return hashlib.sha256(content_bytes).hexdigest()


def calculate_qr_payload_hash(payload):
    """Return the hc-qr-payload-jcs-sha256-v1 digest without mutating input."""

    if type(payload) is not dict:
        raise ContentHashError("qr_payload_object_required")
    payload_without_hash = dict(payload)
    payload_without_hash.pop("payload_hash", None)
    try:
        canonical_bytes = canonicalize_json(payload_without_hash)
    except CanonicalizationError as exc:
        raise ContentHashError("qr_payload_canonicalization_failed") from exc
    return hashlib.sha256(canonical_bytes).hexdigest()


__all__ = [
    "CONTENT_HASH_PROFILE_FIELD",
    "DIGEST_ALGORITHM",
    "HC_CONTENT_HASH_PROFILE",
    "HC_QR_PAYLOAD_HASH_PROFILE",
    "LEGACY_TEXT_HASH_PROFILE",
    "ContentHashError",
    "calculate_content_hash",
    "calculate_qr_payload_hash",
    "calculate_sha256",
]
