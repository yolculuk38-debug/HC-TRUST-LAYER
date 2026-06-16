# Test Coverage Map — 2026-06-16

Status: advisory test navigation map.

This document explains why the `tests/` directory appears crowded from the GitHub mobile file browser and how to read the test suite without treating overlapping names as deletion targets.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This map does not delete, move, rename, consolidate, skip, or weaken tests.
- No runtime, source, schema, validator, record, QR, hash, policy, federation, signing, workflow, generated artifact, canonical, or trust-kernel behavior is changed by this document.

## Why tests do not look ordered in GitHub

GitHub shows files alphabetically inside `tests/`. Alphabetical order is not the same as HC:// engineering order.

The test suite grew feature-by-feature and PR-by-PR. That means related tests can appear as separate files because they protect different boundaries, such as:

- module-level behavior,
- integration behavior,
- API/CLI behavior,
- public-safe response shape,
- regression edge cases,
- governance/security boundary language,
- historical behavior that must not silently change.

So files with similar names are not automatically duplicates. They may protect different parts of the trust layer.

## High-level test groups

### 1. Runtime and response-contract tests

Purpose: protect the HC:// advisory runtime response shape and runtime-state behavior.

Examples:

- `tests/test_hc_runtime_app.py`
- `tests/test_hc_runtime_pipeline.py`
- `tests/test_hc_runtime_response_contracts.py`
- `tests/runtime/test_telemetry_payload_contract.py`
- `tests/runtime/test_replay_continuity_edge_cases.py`
- `tests/runtime/test_degraded_recovery_edge_cases.py`

Protected behavior:

- stable response keys,
- advisory-only status,
- public-safe output,
- `truth_guarantee=false`,
- telemetry visibility,
- replay and continuity warnings,
- degraded runtime recovery behavior,
- append-only event history.

### 2. Verification package tests

Purpose: protect local verification package behavior, hash core, witness proof, timestamp proof, CLI output, sample fixture behavior, and summary output.

Examples:

- `tests/test_verification_package_hash_core.py`
- `tests/test_verification_package_sample.py`
- `tests/test_verification_package_cli.py`
- `tests/test_verification_package_cli_summary_present.py`
- `tests/test_verification_package_cli_summary_timestamp.py`
- `tests/test_verification_package_timestamp_proof.py`
- `tests/test_verification_package_witness_proof.py`

Why separate:

- hash correctness, CLI behavior, timestamp proof, witness proof, and output summary are different contract surfaces.
- These should not be merged unless an assertion-level comparison proves no unique coverage is lost.

### 3. QR safety and QR-public-validator tests

Purpose: protect QR boundary behavior, domain/path allowlists, payload parsing, local record bridging, public validator QR scenarios, and no-network behavior.

Examples:

- `tests/test_qr_guard.py`
- `tests/test_qr_hardening.py`
- `tests/test_qr_orchestrator_integration.py`
- `tests/test_qr_passport_integration.py`
- `tests/test_qr_payload_parser.py`
- `tests/test_qr_public_validator.py`
- `tests/test_qr_record_bridge.py`
- `tests/test_qr_security_domain_allowlist.py`
- `tests/runtime/test_qr_spoof_protection.py`

Why separate:

- parser, hardening, guard, bridge, validator, orchestrator, allowlist, and spoof-protection tests protect different security-adjacent layers.
- Similar QR terms do not mean duplicate coverage.
- QR tests should remain high-review before any consolidation.

### 4. Public validator, public explorer, and public verification tests

Purpose: protect public-facing demo, lookup, API, static viewer, explorer, and public response behavior.

Examples:

- `tests/test_public_validator.py`
- `tests/test_public_validator_api.py`
- `tests/test_public_validator_demo_runner.py`
- `tests/test_public_validator_lookup.py`
- `tests/test_public_validator_static_viewer_smoke.py`
- `tests/test_public_verification_explorer_mvp.py`
- `tests/test_public_verification_explorer_smoke.py`
- `tests/test_public_verification_response.py`

Why separate:

- proof validation, local lookup, demo runner, static viewer, explorer rendering, API response, and response formatter behavior are related but not identical.
- This area is user-facing, so deletion risk is high.

### 5. HC assistant, HC Control Bot, HC Trust Engineer, and handoff tests

Purpose: protect deterministic assistant commands, report-only bot behavior, handoff packages, source inventory, repo inventory, and release-audit helpers.

Examples:

- `tests/test_hc_assistant_command.py`
- `tests/test_hc_bot_status.py`
- `tests/test_hc_control_bot.py`
- `tests/test_hc_engineer_task_plan.py`
- `tests/test_hc_release_audit.py`
- `tests/test_hc_repo_inventory.py`
- `tests/test_hc_source_inventory.py`
- `tests/test_hc_task_handoff.py`
- `tests/test_hc_task_handoff_example.py`
- `tests/test_hc_task_handoff_issue.py`
- `tests/test_hc_trust_engineer_report.py`

Why separate:

- command parsing, changed-file risk scanning, status reporting, task packaging, inventory, and release audit protect different operating-layer boundaries.
- These tests guard against accidental authority expansion.

### 6. Governance, policy, security, and ruleset tests

Purpose: protect policy decisions, governance preflight, security gate behavior, supply-chain risk, ruleset readiness, audit, and evidence review behavior.

Examples:

- `tests/test_pr_governance_preflight.py`
- `tests/test_ruleset_readiness.py`
- `tests/test_security_gate_layer.py`
- `tests/test_supply_chain_risk.py`
- `tests/test_policy_engine.py`
- `tests/test_policy_response_integration.py`
- `tests/test_ai_automation_audit.py`
- `tests/test_evidence_review.py`

Why separate:

- these files protect governance, security, and audit behavior.
- they should not be consolidated casually because they can encode different trust-boundary assumptions.

### 7. Trust graph, trust score, registry, revocation, and risk tests

Purpose: protect trust graph behavior, score normalization, registry, revocation, status, risk flags, risk summary, and recovery behavior.

Examples:

- `tests/test_trust_graph.py`
- `tests/test_trust_engine.py`
- `tests/test_trust_score.py`
- `tests/test_trust_score_engine.py`
- `tests/test_score_normalizer.py`
- `tests/test_trust_registry.py`
- `tests/test_revocation.py`
- `tests/test_registry_revocation_integration.py`
- `tests/test_risk_flags.py`
- `tests/test_risk_summary.py`
- `tests/test_trust_recovery.py`

Why separate:

- graph, scoring, registry, revocation, and risk are different conceptual layers.
- some overlap may exist, but this is not enough to delete tests.

### 8. Federation, signing, certificate, witness, and consensus tests

Purpose: protect trust-kernel-adjacent behavior for federation, signatures, witness records, certificates, and consensus simulation.

Examples:

- `tests/test_federation_consensus.py`
- `tests/test_federation_simulation.py`
- `tests/test_federation_sync.py`
- `tests/test_federation_trust.py`
- `tests/test_signed_federation_exchange.py`
- `tests/test_signed_payload.py`
- `tests/test_signed_witness.py`
- `tests/test_certificate_chain.py`
- `tests/test_certificate_verifier.py`
- `tests/test_consensus_engine.py`
- `tests/test_consensus_rules.py`
- `tests/test_witness_consensus_integration.py`
- `tests/test_witness_standard.py`
- `tests/test_witness_summary.py`

Why separate:

- this is high-risk, trust-kernel-adjacent coverage.
- do not consolidate or delete without a separate protected-domain review.

### 9. Media, manipulation, social, provenance, and evidence tests

Purpose: protect media provenance, manipulation detection, social/media bridge behavior, evidence engines, and provenance scanning.

Examples:

- `tests/test_media_provenance.py`
- `tests/test_media_evidence_integration.py`
- `tests/test_manipulation_detection.py`
- `tests/test_manipulation_detection_additional.py`
- `tests/test_manipulation_engine.py`
- `tests/test_social_media_bridge.py`
- `tests/test_evidence_engine.py`
- `tests/test_evidence_trust_graph_integration.py`
- `tests/test_evidence_weight.py`
- `tests/test_provenance_integrity_scanner.py`

Why separate:

- some files may be future consolidation candidates, especially manipulation detection variants.
- however, additional files may preserve unique edge cases, so no deletion is supported from naming alone.

### 10. Import/export, package, bridge, and offline verifier tests

Purpose: protect export/import formats, portable packages, offline verification, bridges, and deterministic exports.

Examples:

- `tests/test_export_import.py`
- `tests/test_exported_proof.py`
- `tests/test_deterministic_export.py`
- `tests/test_portable_package_v2.py`
- `tests/test_cross_platform_bridge.py`
- `tests/test_offline_verifier.py`
- `tests/test_verifier_entry.py`
- `tests/test_verify_gateway.py`
- `tests/test_verify_payload.py`

Why separate:

- import/export and offline verification are separate external-facing boundaries.
- deterministic export tests can overlap with package tests but protect different artifacts.

## Known overlap areas

Existing report-only duplicate review identified possible overlap in these groups:

- manipulation detection tests,
- QR-related tests,
- public validator / public verification tests,
- assistant / control bot tests,
- protected-domain federation/signing/policy tests.

Current rule:

- overlap is not deletion evidence;
- similar names are not duplicate proof;
- no test should be deleted or consolidated without assertion-level comparison and successful targeted CI;
- high-risk or trust-kernel-adjacent tests require explicit human review.

## Safer future cleanup sequence

1. Keep all tests active.
2. Add navigation maps first.
3. For a suspected duplicate group, compare imports, fixtures, assertions, and protected behavior.
4. Run targeted tests.
5. Open a report-only PR first.
6. Only then consider consolidation in a separate human-reviewed implementation PR.

## Immediate recommendation

Do not reorder or move test files yet. Use this map as the first reading layer. A later PR may add subfolder-level test grouping, but only after maintainers agree on import stability and CI impact.
