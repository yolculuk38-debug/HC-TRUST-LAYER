"""Documentation contract tests for HC:// advisory rate-limit abuse controls."""

from __future__ import annotations

from pathlib import Path

SECURITY_NOTE = Path("docs/security/rate-limiting-abuse-control.md")
RUNTIME_CONTRACT = Path("docs/runtime/advisory-rate-limit-warning-contract.md")
PUBLIC_RESPONSE_CONTRACT = Path("docs/runtime/public-response-contract.md")
OPERATOR_ADVISORY = Path("docs/security/operator-abuse-protection-advisory.md")

REQUIRED_METADATA = (
    "advisory_only=true",
    "public_safe=true",
    "truth_guarantee=false",
)

FORBIDDEN_RUNTIME_DEPENDENCIES = (
    "no Redis implementation",
    "no database dependency",
    "no JWT implementation",
    "no Vault implementation",
)

PATTERN_TERMS = (
    "Repeated malformed validation inputs",
    "Brute-force style validation attempts",
    "Repeated QR spoof patterns",
    "Replay-risk markers",
)

PUBLIC_SAFE_BOUNDARY_TERMS = (
    "`warnings` as an always-present list",
    "request_denied=false",
    "human-supervised validation",
    "operator/infrastructure layer",
    "deterministic response keys",
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_rate_limiting_architecture_note_documents_advisory_boundaries() -> None:
    text = _read(SECURITY_NOTE)

    for metadata in REQUIRED_METADATA:
        assert metadata in text
    for dependency_boundary in FORBIDDEN_RUNTIME_DEPENDENCIES:
        assert dependency_boundary in text
    for pattern in PATTERN_TERMS:
        assert pattern in text

    assert "\"request_denied\": false" in text or "request_denied=false" in text
    assert "autonomous blocking" in text
    assert "operator/infrastructure enforcement layer" in text
    assert "Human final authority" in text


def test_advisory_rate_limit_warning_contract_preserves_public_safe_output_shape() -> None:
    text = _read(RUNTIME_CONTRACT)

    for metadata in REQUIRED_METADATA:
        assert metadata in text
    for boundary in PUBLIC_SAFE_BOUNDARY_TERMS:
        assert boundary in text

    assert "rate_limit_recommended" in text
    assert "repeated malformed validation attempts" in text
    assert "repeated QR spoof inputs" in text
    assert "replay-risk patterns" in text
    assert "Brute-force style probing" in text
    assert "no raw secrets, tokens, keys, credentials" in text
    assert "does not block a request" in text
    assert "does not block a request, deny a request, quarantine an input" in text


def test_public_response_contract_links_rate_limit_warning_without_enforcement() -> None:
    text = _read(PUBLIC_RESPONSE_CONTRACT)

    assert "## Rate-limit advisory warnings" in text
    assert "rate_limit_recommended" in text
    assert "warnings` always present as a list" in text
    assert "Enforcement belongs to the operator/infrastructure layer" in text
    assert "does not deny requests" in text
    assert "add Redis" in text
    assert "add database storage" in text
    assert "add JWT authentication" in text
    assert "add Vault secret access" in text


def test_operator_advisory_links_checklist_and_keeps_warning_advisory_only() -> None:
    text = _read(OPERATOR_ADVISORY)

    assert "docs/security/rate-limiting-abuse-control.md" in text
    assert "docs/runtime/advisory-rate-limit-warning-contract.md" in text
    assert "rate_limit_recommended" in text
    assert "not as a runtime block or denial" in text
    assert "Human final authority" in text
