# Test Taxonomy Review

## 1. Purpose

This document is an advisory, documentation-only review of the observed HC-TRUST-LAYER test taxonomy and coverage boundaries.

It supports backlog item 4-2, “test taxonomy / coverage boundary review.” It maps observed tests to the trust surfaces they appear to protect so maintainers can discuss coverage boundaries after the core package boundary review in `docs/project-control/core-package-boundary-review.md`.

This review does not add tests, modify tests, modify code, modify schemas, modify validators, modify records, modify generated or canonical artifacts, modify workflows, change package metadata, change CI behavior, add dependencies, add enforcement, or add approval, merge, comment, label, reviewer-request, or autonomous governance authority.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true`.
- Tests are evidence, not trust authority.
- Passing tests do not establish legal truth, identity finality, forensic certainty, certification, production readiness, guaranteed correctness, or autonomous governance authority.
- The human maintainer remains the final authority.

HC-TRUST-LAYER tests, checks, documents, records, examples, validators, scripts, workflows, generated artifacts, and local tools must be treated as review evidence only until human maintainers validate the boundary and decide the outcome.

## 3. Review method

This review inspected the existing repository and classified tests by observed role. It used visible test file paths, test names, imported modules where visible, and apparent purpose. It does not assert hidden maintainer intent and does not claim full semantic coverage.

The review inspected:

- test file paths;
- test names or apparent purpose;
- protected surface covered;
- whether the test appears deterministic;
- whether the test appears unit, integration, docs, governance, fixture, schema, validator, or runtime oriented;
- whether it protects a trust-critical boundary;
- whether it appears to use network, external services, time-sensitive behavior, randomness, generated artifacts, or fixtures;
- relationship to `docs/project-control/core-package-boundary-review.md`.

Categories not observed are marked as `not observed`. Where path names or test names suggest coverage but the authority boundary is unclear, the row uses `needs maintainer confirmation`.

## 4. Test taxonomy table

| Test path | Observed role | Protected surface | Test type | Trust sensitivity | Determinism expectation | Coverage boundary | Notes |
|---|---|---|---|---|---|---|---|
| `tests/test_schema_hardening.py` | Schema hardening package checks. | Schema/contracts. | schema/validator | critical | deterministic | Direct schema-shaped validation examples. | Needs maintainer confirmation that this is sufficient for schema boundary changes. |
| `tests/test_api_schema.py` | API response shape checks. | Public response contracts. | schema/runtime | high | deterministic | API payload contract boundary. | Protects response shape, not legal truth or production readiness. |
| `tests/runtime/test_canonical_schema_hash_bridge.py` | Canonical record, schema, and hash bridge behavior. | Schema/contracts, records/evidence, generated/canonical-adjacent artifacts. | runtime/schema/fixture | critical | deterministic | Boundary between local records, schema advisory validation, and content hashes. | Appears trust-critical and related to the core package boundary review. |
| `tests/runtime/test_canonical_record_loader.py` | Canonical record loading and malformed/cache handling. | Records/evidence and generated/canonical-adjacent artifacts. | runtime/fixture | critical | deterministic | Approved-directory and content-hash boundary. | Uses local fixtures or temporary records; no live authority implied. |
| `tests/test_public_validator_lookup.py` | Public validator lookup for records, schema, hash, duplicate IDs, and demo fixture separation. | Validators, records/evidence, demos. | validator/runtime/fixture | critical | deterministic | Record lookup boundary and demo-vs-record separation. | Strong boundary coverage signal, still advisory only. |
| `tests/test_public_validator.py`, `tests/test_public_validator_api.py`, `tests/test_qr_public_validator.py` | Public validation, API requests, QR-to-record validation, missing provenance, conflicts, and no-network behavior. | Validators, records/evidence, QR evidence. | validator/integration | critical | deterministic; no live network expected where named | Public validation boundary. | Tests negative paths but do not create final trust authority. |
| `tests/test_verify_payload.py`, `tests/test_verify_gateway.py`, `tests/test_verifier_entry.py`, `tests/test_verification_api.py`, `tests/test_verification_status_engine.py`, `tests/test_verification_orchestrator.py` | Verification payload, gateway, entrypoint, status, API, and orchestration checks. | Validators and runtime verification surfaces. | unit/integration/runtime | critical | deterministic | Core runtime verification behavior. | Directly maps to `src/` core-package boundary. |
| `tests/test_hc_runtime_pipeline.py`, `tests/test_hc_runtime_response_contracts.py`, `tests/test_hc_runtime_app.py`, `tests/runtime/test_public_response_contract.py` | Runtime pipeline and public response contract checks. | Runtime and public-safe output boundaries. | runtime/contract | critical | deterministic | Runtime response shape and validator semantics. | Maintainer confirmation needed for complete runtime coverage. |
| `tests/runtime/test_degraded_recovery_edge_cases.py`, `tests/runtime/test_replay_continuity_edge_cases.py`, `tests/runtime/test_secret_redaction_runtime_outputs.py`, `tests/runtime/test_telemetry_payload_contract.py`, `tests/runtime/test_telemetry_payload_safety_contract.py`, `tests/runtime/test_abuse_advisory_signals.py` | Runtime degraded-state, replay continuity, telemetry, redaction, and abuse advisory checks. | Runtime safety, public-safe telemetry, advisory-only behavior. | runtime/negative-path | critical | deterministic | Runtime hardening and safety boundaries. | Important trust-critical runtime tests; not a substitute for human review. |
| `tests/test_verification_package_hash_core.py`, `tests/test_verification_package_cli.py`, `tests/test_verification_package_cli_summary_present.py`, `tests/test_verification_package_cli_summary_timestamp.py`, `tests/test_verification_package_sample.py`, `tests/test_verification_package_timestamp_proof.py`, `tests/test_verification_package_witness_proof.py` | Verification package, manifest, issuer proof, witness proof, timestamp proof, CLI summaries, and tampering checks. | Records/evidence, generated package artifacts, CLI. | integration/fixture/CLI | critical | deterministic | Verification package evidence boundary. | Appears to use local fixtures and negative paths; no live external authority implied. |
| `tests/test_deterministic_export.py`, `tests/test_export_import.py`, `tests/test_exported_proof.py`, `tests/test_portable_package_v2.py` | Export/import, portable package, proof, digest, and deterministic export checks. | Generated/canonical-adjacent artifacts and package evidence. | generated-artifact/integration | high | deterministic | Reproducibility and tamper-detection boundary. | Generated/canonical ownership still needs maintainer confirmation. |
| `tests/test_revision_chain.py`, `tests/test_revision_status_integration.py`, `tests/test_audit_trail.py`, `tests/test_audit_snapshot.py`, `tests/test_audit_snapshots_v2.py`, `tests/test_hc_release_audit.py` | Revision chains, audit trails, snapshots, and release audit reports. | Records/evidence and audit continuity. | unit/integration/report-only | critical | deterministic | Evidence continuity and audit-report boundary. | Tests evidence behavior, not forensic certainty. |
| `tests/test_evidence_engine.py`, `tests/test_evidence_review.py`, `tests/test_evidence_weight.py`, `tests/test_evidence_trust_graph_integration.py`, `tests/test_media_evidence_integration.py`, `tests/test_media_provenance.py`, `tests/test_social_media_bridge.py` | Evidence bundles, media/social references, weighting, provenance, and trust-graph integration. | Records/evidence and external-reference evidence. | unit/integration | high | deterministic | Evidence handling boundary. | External services are not observed from names; maintainers should confirm fixture-only behavior. |
| `tests/test_qr_guard.py`, `tests/test_qr_hardening.py`, `tests/test_qr_payload_parser.py`, `tests/test_qr_record_bridge.py`, `tests/test_qr_orchestrator_integration.py`, `tests/test_qr_security_domain_allowlist.py`, `tests/test_qr_passport_integration.py`, `tests/runtime/test_qr_spoof_protection.py` | QR payload parsing, domain allowlist, record bridge, spoofing, passport, and orchestrator checks. | QR/hash/signature-adjacent evidence. | validator/integration/negative-path | critical | deterministic; no live network expected where named | QR evidence boundary. | Useful negative-path signal; signing claims still need explicit signing-path review. |
| `tests/test_signed_payload.py`, `tests/test_signed_witness.py`, `tests/test_signed_federation_exchange.py`, `tests/test_certificate_chain.py`, `tests/test_certificate_verifier.py`, `tests/test_verification_certificate.py`, `tests/test_witness_standard.py`, `tests/test_witness_summary.py`, `tests/test_witness_consensus_integration.py` | Signed payloads, witnesses, certificate-like chains, federation exchange signatures, and witness summaries. | Signing/signature material and witness evidence. | unit/integration/negative-path | critical | deterministic | Signature and witness boundary. | Observed tests do not imply production signing readiness or certification authority. |
| `tests/test_federation_sync.py`, `tests/test_federation_trust.py`, `tests/test_federation_consensus.py`, `tests/test_federation_simulation.py`, `tests/test_public_explorer_api.py`, `tests/test_node_registry.py`, `tests/test_registry_revocation_integration.py` | Federation packets, node registry, revocation, simulation, consensus, and explorer federation summary. | Federation/external trust interfaces. | unit/integration/simulation | high | deterministic; default CI should avoid live network | Federation boundary. | Live federation guarantees are not established; maintainers should confirm external calls are mocked or fixture-based. |
| `tests/test_consensus_engine.py`, `tests/test_consensus_rules.py`, `tests/test_consensus_status_integration.py`, `tests/test_trust_graph.py`, `tests/test_explainable_trust_graph.py`, `tests/test_trust_graph_passport_integration.py` | Consensus, graph, explainability, and passport integration. | Runtime trust surfaces and evidence aggregation. | unit/integration | high | deterministic | Aggregation and interpretation boundary. | Does not establish final truth or identity finality. |
| `tests/test_policy_engine.py`, `tests/test_policy_response_integration.py`, `tests/test_evaluate_policy.py`, `tests/test_security_gate_layer.py`, `tests/test_zero_trust_gateway.py`, `tests/test_revocation.py` | Policy, gateway, security gate, revocation, and response integration. | Policy/governance-adjacent runtime boundaries. | unit/integration | high | deterministic | Policy interpretation boundary. | Policy paths themselves remain protected and were not modified. |
| `tests/test_pr_governance_preflight.py`, `tests/test_hc_control_bot.py`, `tests/test_hc_check_digest.py`, `tests/test_hc_check_digest_github_adapter.py`, `tests/test_hc_check_digest_workflow.py`, `tests/test_hc_control_bot_report_workflow.py`, `tests/test_hc_review_window_marker_workflow.py`, `tests/test_ruleset_readiness.py`, `tests/test_check_github_actions_versions.py` | Governance preflight, digest, workflow/readiness, control-bot, marker, and action-version checks. | Workflow/governance boundaries. | governance/report-only/workflow-static | high | deterministic; no mutation expected | Governance automation and workflow evidence boundary. | Tests should not be treated as approval, merge, label, comment, or reviewer-request authority. |
| `tests/project_control/test_hc_trust_engineer_local_emitter.py`, `tests/project_control/test_hc_trust_engineer_output_contract.py`, `tests/test_hc_trust_engineer_report.py`, `tests/test_hc_engineer_task_plan.py`, `tests/test_hc_task_claim.py`, `tests/test_hc_task_handoff.py`, `tests/test_hc_task_handoff_issue.py`, `tests/test_hc_task_handoff_example.py` | Project-control emitters, task planning, claim, handoff, and report contracts. | Workflow/governance and project-control boundaries. | governance/report-only/fixture | high | deterministic | Human-supervised operating-layer boundary. | Supports advisory-only operating flow; no autonomous governance finality. |
| `tests/test_hc_signal_watch_rss_ingest.py`, `tests/test_hc_signal_watch_live_rss_fetch.py`, `tests/test_hc_signal_watch_report.py`, `tests/test_hc_signal_watch_suggest.py`, `tests/test_hc_signal_watch_console_comment.py` | Signal-watch RSS ingest, live-fetch failure handling, reporting, suggestions, and console comment payloads. | External signal/report-only scanner boundaries. | report-only/scanner/governance | high | deterministic; live network should be avoided in default CI | External-source scanner boundary. | Names include live RSS fetch, but tests appear to emphasize safe failure and manual/read-only behavior; maintainer confirmation needed. |
| `tests/test_hc_repo_inventory.py`, `tests/test_hc_source_inventory.py`, `tests/test_hc_workflow_taxonomy_drift_report.py`, `tests/test_hc_stale_baseline_report.py`, `tests/test_ai_automation_audit.py`, `tests/test_normalize_records.py`, `tests/test_normalize_records_safety.py` | Repository inventory, workflow taxonomy drift, stale baseline, AI automation audit, and record normalization safety. | Report-only scanners, records/evidence, governance. | report-only/governance/fixture | high | deterministic | Scanner and protected-record mutation boundary. | These tests are important for proving advisory-only or dry-run behavior. |
| `tests/runtime/test_runtime_hardening_gap_report.py`, `tests/runtime/test_secret_boundary_architecture_docs.py`, `tests/runtime/test_rate_limiting_abuse_control_docs.py`, `tests/runtime/test_persistence_roundtrip_audit.py` | Runtime hardening, secret boundary, rate-limiting, and persistence limitation documentation checks. | Docs/terminology/governance rules and runtime safety docs. | docs/governance | medium | deterministic | Documentation boundary for runtime safety claims. | Docs checks do not validate runtime enforcement. |
| `tests/test_public_validator_demo_runner.py`, `tests/test_public_validator_static_viewer_contract.py`, `tests/test_public_validator_static_viewer_smoke.py`, `tests/test_public_verification_explorer_mvp.py`, `tests/test_public_verification_explorer_smoke.py`, `tests/test_browser_validator.py`, `tests/test_mobile_verification_flow.py` | Demo runner, static viewer, explorer, browser, and mobile-facing checks. | CLI/demo/local tools and public views. | demo/integration/docs-adjacent | medium | deterministic | Public demo and viewer boundary. | Demos and public views must not imply trust guarantees. |
| `tests/test_verification_cli.py`, `tests/test_offline_verifier.py`, `tests/test_sdk_response.py`, `tests/test_result_formatter.py`, `tests/test_public_verification_response.py`, `tests/test_verification_output_summary.py`, `tests/test_browser_validator.py`, `tests/test_mobile_verification_flow.py` | CLI, offline verifier, SDK, formatter, public response, browser, and mobile response checks. | CLI/demo/local tools and runtime outputs. | unit/CLI/runtime | medium | deterministic | Local-tool output boundary. | CLI and SDK outputs remain advisory evidence unless separately reviewed. |
| `tests/test_trust_engine.py`, `tests/test_trust_score.py`, `tests/test_trust_score_engine.py`, `tests/test_score_normalizer.py`, `tests/test_risk_flags.py`, `tests/test_risk_summary.py`, `tests/test_adaptive_risk_engine.py`, `tests/test_manipulation_engine.py`, `tests/test_manipulation_detection.py`, `tests/test_manipulation_detection_additional.py`, `tests/test_adversarial_payload_lab.py`, `tests/test_supply_chain_risk.py`, `tests/test_temporal_trust_decay.py`, `tests/test_trust_badge.py`, `tests/test_trust_passport.py`, `tests/test_trust_orchestrator.py`, `tests/test_trust_registry.py`, `tests/test_trust_recovery.py`, `tests/test_status_passport_integration.py`, `tests/test_cross_platform_bridge.py`, `tests/test_protocol_self_integrity.py` | Trust scoring, risk, manipulation, supply-chain, trust passport, recovery, registry, and integrity checks. | Runtime interpretation and advisory trust surfaces. | unit/integration | high | deterministic | Advisory scoring and integrity boundary. | These tests should not be read as final trust, risk, or identity authority. |
| `tests/fixtures/**` | Fixture samples for project-control and other tests. | Fixture/example material. | fixture/example | low to medium | deterministic | Local fixture input boundary. | Fixtures are not canonical records unless separately promoted. |
| `test_integration.py` | Legacy integration import-safety entrypoint. | Runtime import surface. | integration | low | deterministic | Import compatibility boundary. | Narrow smoke coverage only. |
| `validators/**` tests | not observed. | Validators. | not observed | needs maintainer confirmation | not observed | Top-level validator path boundary. | No top-level `validators/` directory was observed in the core package boundary review. |
| `canonical/**` tests | not observed as a top-level path-specific suite. | Canonical artifacts. | not observed | needs maintainer confirmation | not observed | Canonical top-level artifact boundary. | Canonical-adjacent checks are observed through runtime and package tests. |
| `signing/**` tests | not observed as a top-level path-specific suite. | Signing implementation path. | not observed | needs maintainer confirmation | not observed | Top-level signing path boundary. | Signature-related tests exist, but no top-level `signing/` path was observed in the core package boundary review. |

## 5. Coverage boundary findings

Trust-critical areas that appear covered include runtime verification surfaces under `src/`, public validator lookup, QR payload and record bridging, verification packages, audit trails, revision chains, signatures or witness material, policy response behavior, and governance/report-only automation.

Areas that appear partially covered include schema/contracts, generated/canonical-adjacent artifacts, federation/external trust interfaces, signing/signature material, and workflow/governance checks. Tests exist for related behavior, but the repository still needs maintainer confirmation before treating the coverage as complete for protected-path changes.

Areas needing maintainer confirmation include the absence of a top-level `validators/` path, the absence of a top-level `canonical/` path, the absence of a top-level `signing/` path, the ownership boundary between generated artifacts and local fixtures, and whether all federation or external-interface tests avoid live network dependency in default CI.

Docs-only or governance-only areas appear covered by static documentation and report-only scanner checks, including runtime hardening docs, secret boundary docs, rate-limiting docs, project-control emitters, task planning, task handoff, check digest, workflow taxonomy drift, and control-bot reporting.

Docs/governance checks should not be the only protection for runtime validators, schema contracts, generated/canonical artifacts, signing/signature behavior, federation behavior, or protected records. Documentation can describe boundaries, but executable validation should protect trust-critical behavior before future enforcement or production-facing claims are considered.

Generated/canonical artifacts appear to have boundary tests through deterministic export, verification package hash checks, portable package checks, canonical record loading, and canonical schema/hash bridge tests. A dedicated ownership and reproducibility review is still needed before generated/canonical coverage is considered complete.

Validators and schemas appear to have direct or adjacent tests through schema hardening, API schema, public validator lookup, public validator, verification payload, verification gateway, and runtime pipeline tests. Because no top-level `validators/` directory was observed in the core package boundary review, maintainer confirmation is needed for the intended validator boundary.

Workflow/governance checks appear to have local tests and static workflow evidence checks. Those tests provide evidence about report-only behavior, read-only behavior, and advisory boundaries, but Actions evidence and local tests do not grant approval, merge, comment, label, reviewer-request, or autonomous governance authority.

## 6. Recommended HC testing rules

- Trust-critical validators must be deterministic and test-covered.
- Schema/contract changes need direct validation tests.
- Generated/canonical artifacts should have reproducibility or boundary checks.
- Signing/signature paths need explicit negative tests before production use is claimed.
- Federation/external trust interfaces should avoid live network dependency in default CI.
- Docs/governance checks should not be treated as runtime validation.
- Demos/examples should not imply trust guarantees.
- Report-only scanners should have tests proving advisory-only behavior.
- Any future enforcement promotion requires separate tests and human review.

## 7. Ideal vs current practical state

### Ideal

- Clear test taxonomy.
- Unit, integration, governance, schema, validator, and generated-artifact tests separated.
- Trust-kernel tests mapped to core boundaries.
- Deterministic default CI.
- Fixtures separated from canonical/generated artifacts.
- Negative tests for spoofing, missing evidence, conflicting evidence, and invalid signatures.

### Current practical next step

- Document observed test coverage first.
- Do not add or rewrite tests in this PR.
- Propose small follow-up PRs for missing coverage.

## 8. Real-world analogy

SSL/TLS systems test certificate parsing, chain validation, key handling, revocation logic, and UI warnings separately.

Banks and e-devlet-style systems test transaction records, audit logs, operator actions, and public views separately.

HC-TRUST-LAYER should similarly separate tests for validators, evidence records, generated artifacts, governance, and demos so maintainers can see which checks protect trust-critical behavior and which checks only support advisory documentation or local examples.

## 9. Follow-up items

- 4-2b optional: add missing validator/schema boundary tests in a separate PR.
- 4-2c optional: add generated/canonical artifact reproducibility tests in a separate PR.
- 4-2d optional: add spoofing/negative-path tests for QR/hash/signature evidence if not already covered.
- 4-3: public API / CLI boundary review.
- 4-4: generated/canonical artifact ownership review.
- 4-5: demo/example boundary review.

These follow-ups should remain small, scoped, evidence-preserving, and human-reviewed. They should not modify protected paths unless explicitly authorized, and they should not add approval, merge, comment, label, reviewer-request, close, or autonomous governance authority.
