"""Documentation contract tests for HC:// secret boundary architecture."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SECRET_ARCHITECTURE = REPO_ROOT / "docs/security/secret-boundary-architecture.md"
CONFIG_CHECKLIST = REPO_ROOT / "docs/runtime/configuration-boundary-checklist.md"
PUBLIC_RESPONSE_CONTRACT = REPO_ROOT / "docs/runtime/public-response-contract.md"
RUNTIME_RISK_NOTES = REPO_ROOT / "docs/runtime/runtime-contract-risk-notes.md"
SECURITY_GAP_REPORT = REPO_ROOT / "docs/security/runtime-hardening-gap-report.md"

REQUIRED_METADATA = (
    "advisory_only=true",
    "public_safe=true",
    "truth_guarantee=false",
)

FORBIDDEN_IMPLEMENTATION_BOUNDARIES = (
    "no Vault implementation",
    "no Redis implementation",
    "no JWT implementation",
    "no secret storage implementation",
    "Runtime behavior change: none.",
    "Schema mutation: none.",
    "Workflow mutation: none.",
)

REQUIRED_CLASSIFICATIONS = (
    "Public verification data",
    "Runtime configuration data",
    "Signing material",
    "Operational secrets",
    "Operator incident notes",
)

REQUIRED_TRUST_ZONES = (
    "Public verification zone",
    "Runtime configuration zone",
    "Signing custody zone",
    "Operational secret zone",
    "Human review zone",
)

PUBLIC_SAFE_PLACEHOLDERS = (
    "<redacted-token>",
    "<redacted-private-key>",
    "<operator-config-name>",
    "<public-record-id>",
)

DETERMINISTIC_REFERENCES = (
    "docs/security/secret-boundary-architecture.md",
    "docs/runtime/configuration-boundary-checklist.md",
    "docs/runtime/public-response-contract.md",
    "docs/runtime/runtime-contract-risk-notes.md",
    "docs/security/runtime-hardening-gap-report.md",
    "docs/security/persistence-risk-checklist.md",
    "docs/security/rate-limiting-abuse-control.md",
    "docs/signing-architecture.md",
)

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/=-]{16,}"),
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_secret_boundary_documents_required_metadata_and_non_goals() -> None:
    text = _read(SECRET_ARCHITECTURE)

    for metadata in REQUIRED_METADATA:
        assert metadata in text
    for boundary in FORBIDDEN_IMPLEMENTATION_BOUNDARIES:
        assert boundary in text

    assert "documentation only" in text
    assert "does not implement secret managers" in text
    assert "does not change signing logic" in text or "Signing mutation: none." in text


def test_secret_boundary_classifies_public_private_and_signing_data() -> None:
    text = _read(SECRET_ARCHITECTURE)

    for classification in REQUIRED_CLASSIFICATIONS:
        assert classification in text
    for trust_zone in REQUIRED_TRUST_ZONES:
        assert trust_zone in text

    assert "public verification data" in text
    assert "runtime configuration" in text
    assert "Signing material is not public verification data" in text
    assert "operational secrets" in text
    assert "secret exposure risks" in text.lower()
    assert "operator responsibilities" in text.lower()
    assert "environment separation guidance" in text.lower()


def test_configuration_checklist_contains_public_safe_examples_and_operator_steps() -> None:
    text = _read(CONFIG_CHECKLIST)

    for metadata in REQUIRED_METADATA:
        assert metadata in text
    for placeholder in PUBLIC_SAFE_PLACEHOLDERS:
        assert placeholder in text
    for boundary in FORBIDDEN_IMPLEMENTATION_BOUNDARIES:
        assert boundary in text

    assert '"advisory_only": true' in text
    assert '"public_safe": true' in text
    assert '"truth_guarantee": false' in text
    assert "does not define a new runtime response schema" in text
    assert "Operator configuration checklist" in text
    assert "No secret leakage examples" in text


def test_secret_boundary_docs_do_not_contain_secret_like_examples() -> None:
    combined = _read(SECRET_ARCHITECTURE) + "\n" + _read(CONFIG_CHECKLIST)

    for pattern in SECRET_PATTERNS:
        assert pattern.search(combined) is None
    assert ".env files" in combined
    assert "Do not add `.env` files" in combined or "`.env` files" in combined


def test_deterministic_documentation_references_are_present_and_existing() -> None:
    combined = _read(SECRET_ARCHITECTURE) + "\n" + _read(CONFIG_CHECKLIST)

    for reference in DETERMINISTIC_REFERENCES:
        assert reference in combined
        assert (REPO_ROOT / reference).exists()

    assert PUBLIC_RESPONSE_CONTRACT.exists()
    assert RUNTIME_RISK_NOTES.exists()
    assert SECURITY_GAP_REPORT.exists()
