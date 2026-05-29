"""Documentation guard tests for the advisory HC:// runtime hardening gap report."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SECURITY_REPORT = REPO_ROOT / "docs/security/runtime-hardening-gap-report.md"
RUNTIME_NOTES = REPO_ROOT / "docs/runtime/runtime-contract-risk-notes.md"

PROTECTED_PREFIXES = (
    "schema/",
    "validators/",
    "federation/",
    "signatures/",
    "canonical/",
    "policy/",
    ".github/workflows/",
    "records/",
)

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_runtime_hardening_docs_exist() -> None:
    assert SECURITY_REPORT.exists()
    assert RUNTIME_NOTES.exists()


def test_gap_report_contains_required_checklist_sections() -> None:
    text = _read(SECURITY_REPORT)

    required_sections = [
        "## Verified repo findings",
        "## Advisory-only risk checklist",
        "## Secret handling review checklist",
        "## Rate-limit and abuse-protection recommendations",
        "## Future options, not current implementation",
        "## Human authority and review boundary",
    ]
    for section in required_sections:
        assert section in text


def test_advisory_public_safe_contract_language_is_present() -> None:
    combined = _read(SECURITY_REPORT) + "\n" + _read(RUNTIME_NOTES)

    assert "advisory_only=true" in combined
    assert "public_safe=true" in combined
    assert "truth_guarantee=false" in combined
    assert "Runtime behavior change: public-safe redaction of secret-like runtime output only." in combined
    assert "Schema mutation: none." in combined
    assert "telemetry-like payloads" in combined
    assert "<redacted-token>" in combined
    assert "Workflow mutation: none." in combined
    assert "Human final authority" in combined
    assert "human-supervised validation" in combined


def test_future_security_options_are_not_described_as_implemented() -> None:
    text = _read(SECURITY_REPORT)

    for option in ["Redis", "Vault", "JWT", "ECC", "RSA"]:
        assert option in text
    assert text.count("Future option only.") >= 5
    assert "It does not implement Redis, JWT, Vault, ECC, RSA" in text


def test_runtime_contract_risk_notes_are_present() -> None:
    text = _read(RUNTIME_NOTES)

    required_phrases = [
        "## Contract risks to keep visible",
        "## Runtime contract review checklist",
        "New routes could accidentally omit",
        "No runtime behavior change is introduced by documentation-only PRs.",
    ]
    for phrase in required_phrases:
        assert phrase in text


def test_no_protected_governance_paths_changed_in_worktree() -> None:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=REPO_ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    changed_paths = [line[3:].strip() for line in result.stdout.splitlines() if line.strip()]

    protected_changes = [
        path
        for path in changed_paths
        if path.startswith(PROTECTED_PREFIXES)
    ]
    assert protected_changes == []


def test_no_secret_token_or_key_material_added_to_gap_docs() -> None:
    combined = _read(SECURITY_REPORT) + "\n" + _read(RUNTIME_NOTES)

    for pattern in SECRET_PATTERNS:
        assert pattern.search(combined) is None
