"""Regression contracts for future HC-TRUST-LAYER namespace moves.

These tests intentionally lock current import, CLI, and package-discovery
behavior before any human-approved namespace/refactor PR moves source files.
Update them only when a reviewed refactor intentionally changes those
contracts while preserving HC:// advisory and human-review boundaries.
"""

from __future__ import annotations

import importlib
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

# Import paths below are existing package or module surfaces already exercised by
# tests, scripts, package metadata, or docs. They are not new public API claims.
IMPORT_CONTRACT_MODULES = (
    "hc_trust",
    "hc_trust.api_schema",
    "hc_trust.cli",
    "hc_trust.hashing",
    "hc_trust.result_formatter",
    "hc_trust.trust_engine",
    "hc_trust.verification",
    "hc_trust.verification_package",
    "hc_trust.verify_gateway",
    "hc_runtime",
    "hc_runtime.app",
    "hc_runtime.contracts",
    "hc_runtime.contracts.redaction",
    "hc_runtime.contracts.abuse_signals",
    "hc_runtime.contracts.decision_engine",
    "hc_runtime.redaction",
    "hc_runtime.abuse_signals",
    "hc_runtime.decision_engine",
    "hc_runtime.events",
    "hc_runtime.public_validator_lookup",
    "hc_runtime.qr_payload_parser",
    "hc_runtime.qr_record_bridge",
    "hc_runtime.runtime",
)

EXPECTED_DISCOVERED_PACKAGES = (
    "hc_trust",
    "hc_runtime",
    "hc_runtime.contracts",
    "hc_runtime.events",
)


def _project_metadata() -> dict:
    return tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))


def _resolve_dotted_target(target: str):
    module_name, separator, attribute_name = target.partition(":")
    assert separator, f"Entrypoint target must use module:attribute syntax: {target}"

    module = importlib.import_module(module_name)
    resolved = module
    for part in attribute_name.split("."):
        resolved = getattr(resolved, part)
    return module, resolved


def test_current_import_contract_modules_resolve() -> None:
    """Current package/module imports should fail clearly after unsafe moves."""

    for module_name in IMPORT_CONTRACT_MODULES:
        module = importlib.import_module(module_name)
        assert module.__name__ == module_name


def test_runtime_redaction_namespace_move_preserves_old_import_compatibility() -> None:
    """First low-risk runtime helper move keeps old and new import paths aligned."""

    old_module = importlib.import_module("hc_runtime.redaction")
    new_module = importlib.import_module("hc_runtime.contracts.redaction")

    assert old_module.redact_public_payload is new_module.redact_public_payload
    assert old_module.redact_secret_like_text is new_module.redact_secret_like_text
    assert new_module.redact_secret_like_text("api_key=example-secret") == "[REDACTED]"


def test_runtime_abuse_signals_namespace_move_preserves_old_import_compatibility() -> None:
    """Second low-risk runtime helper move keeps old and new import paths aligned."""

    old_module = importlib.import_module("hc_runtime.abuse_signals")
    new_module = importlib.import_module("hc_runtime.contracts.abuse_signals")

    assert old_module.AbuseSignalLevel is new_module.AbuseSignalLevel
    assert old_module.AbuseSignalResult is new_module.AbuseSignalResult
    assert old_module.AdvisoryAbuseSignalTracker is new_module.AdvisoryAbuseSignalTracker

    tracker = new_module.AdvisoryAbuseSignalTracker()
    result = tracker.inspect(
        record_id="namespace-helper-001",
        schema_valid=True,
        qr_risk_level=importlib.import_module("hc_runtime.qr_spoof_protection").QRRiskLevel.LOW,
        qr_risk_reasons=[],
        qr_risk_group_keys=[],
        replay_warning=False,
        degraded_mode=False,
    )

    assert result.summary()["advisory_only"] is True
    assert result.summary()["public_safe"] is True
    assert result.summary()["truth_guarantee"] is False
    assert result.summary()["human_final_authority"] is True


def test_runtime_decision_engine_namespace_move_preserves_old_import_compatibility() -> None:
    """Third low-risk runtime helper move keeps old and new import paths aligned."""

    old_module = importlib.import_module("hc_runtime.decision_engine")
    new_module = importlib.import_module("hc_runtime.contracts.decision_engine")

    assert old_module.TrustState is new_module.TrustState
    assert old_module.TrustStateDecisionEngine is new_module.TrustStateDecisionEngine

    engine = new_module.TrustStateDecisionEngine()
    trust_state, warnings = engine.classify(
        record_id="namespace-helper-002",
        qr_input="local advisory input",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=True,
        replay_warning=False,
    )

    assert trust_state is new_module.TrustState.ADVISORY
    assert warnings == []

    degraded_state, degraded_warnings = engine.classify(
        record_id="namespace-helper-degraded-002",
        qr_input="local advisory input",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=True,
        replay_warning=False,
    )

    assert degraded_state is old_module.TrustState.DEGRADED
    assert degraded_warnings == [
        "Runtime is operating in degraded advisory mode for this verification request.",
        "Human-supervised validation is required before trust interpretation.",
    ]


def test_runtime_event_store_public_import_contract_preserves_identity() -> None:
    """Event store public imports stay aligned before any namespace move."""

    public_module = importlib.import_module("hc_runtime.events")
    store_module = importlib.import_module("hc_runtime.events.store")
    from hc_runtime.events import RuntimeEventStore

    assert public_module.RuntimeEventStore is store_module.RuntimeEventStore
    assert public_module.RuntimeEventStore is RuntimeEventStore

    event_store = RuntimeEventStore()
    assert isinstance(event_store, RuntimeEventStore)


def test_configured_cli_entrypoint_target_resolves() -> None:
    metadata = _project_metadata()
    scripts = metadata["project"]["scripts"]

    assert scripts == {"hc-trust": "hc_trust.cli:main"}
    module, entrypoint = _resolve_dotted_target(scripts["hc-trust"])

    assert module.__name__ == "hc_trust.cli"
    assert callable(entrypoint)


def test_cli_help_contract_can_be_rendered_without_side_effects() -> None:
    cli = importlib.import_module("hc_trust.cli")

    parser = cli.build_parser()
    help_text = parser.format_help()

    assert "hc-trust" in help_text
    assert "verify-package" in help_text
    assert "local advisory evidence checks" in help_text
    assert "not trust authority" in help_text


def test_package_discovery_contract_matches_src_layout() -> None:
    metadata = _project_metadata()

    assert metadata["tool"]["setuptools"]["package-dir"] == {"": "src"}
    assert metadata["tool"]["setuptools"]["packages"]["find"]["where"] == ["src"]

    for package_name in EXPECTED_DISCOVERED_PACKAGES:
        package_path = SRC / Path(*package_name.split("."))
        assert package_path.is_dir()
        assert (package_path / "__init__.py").is_file()


def test_refactor_safety_marker_preserves_human_review_boundary() -> None:
    # Safety marker: these contracts guard future namespace/refactor moves and
    # should change only in a human-approved refactor PR that intentionally
    # updates import, CLI, or package-discovery behavior.
    assert "hc_trust.cli:main" == _project_metadata()["project"]["scripts"]["hc-trust"]
