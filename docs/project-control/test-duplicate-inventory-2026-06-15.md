# Test Duplicate Inventory - 2026-06-15

advisory_only=true  
public_safe=true  
truth_guarantee=false

## 1. Executive summary

This is a report-only test inventory for possible duplicate, overlapping, stale, or consolidation-candidate tests in the HC-TRUST-LAYER repository cleanup sequence.

No tests are deleted or modified. No runtime, source, workflow, generated artifact, schema, validator, record, policy, federation, signature, canonical, or other protected trust-kernel files are changed. This report only adds documentation under `docs/project-control/`.

All findings are advisory only. CI and repository checks are evidence for reviewers, not trust authority. Generated artifacts, if reviewed in future work, remain advisory evidence and are not canonical records. Human final authority remains required before any future test cleanup, consolidation, deletion, or scope change.

## 2. Test inventory method

The inventory inspected tests by:

- file name;
- imported modules;
- referenced modules and command-line entry points where visible from imports;
- test function names;
- apparent purpose inferred from test names and surrounding module names.

Findings are classified as advisory only. This report does not claim a duplicate unless evidence is clear from file names, imports, and apparent assertions. Where coverage uniqueness is uncertain, the report uses candidate language and recommends human review instead of deletion.

This inventory did not perform a full assertion-by-assertion equivalence proof. That means no test deletion is recommended here.

## 3. Candidate groups

### A. Manipulation detection tests

Files inspected:

- `tests/test_manipulation_detection.py`
- `tests/test_manipulation_detection_additional.py`
- `tests/test_manipulation_engine.py`

Tested behavior or module if identifiable:

- `tests/test_manipulation_detection.py` imports `manipulation_detection` and `trust_graph`; it appears to test low-risk graph behavior, mirror-cluster behavior, synchronized timing detection, and invalid graph handling.
- `tests/test_manipulation_detection_additional.py` imports `detect_coordinated_manipulation` from `manipulation_detection` and `trust_graph`; it appears to add repost-cluster and self-reference loop coverage.
- `tests/test_manipulation_engine.py` imports `manipulation_engine`; it appears to test lower and critical manipulation risk outcomes at an engine-level boundary.

Overlap risk: Medium. The first two files both exercise `manipulation_detection` with graph-shaped inputs, so there may be consolidation opportunities if assertion coverage and edge cases overlap. `tests/test_manipulation_engine.py` appears adjacent but likely covers a different engine-level surface.

Deletion risk: Medium to high. The additional tests may preserve unique edge cases for repost clusters and self-reference loops. Engine-level tests may protect a separate interface even if risk concepts overlap.

Recommendation: CONSOLIDATE_CANDIDATE for `tests/test_manipulation_detection.py` and `tests/test_manipulation_detection_additional.py`; KEEP_ACTIVE and NEEDS_HUMAN_REVIEW for `tests/test_manipulation_engine.py` unless a future assertion-level comparison proves equivalent coverage.

### B. QR-related tests

Files inspected:

- `tests/test_qr_guard.py`
- `tests/test_qr_hardening.py`
- `tests/test_qr_orchestrator_integration.py`
- `tests/test_qr_payload_parser.py`
- `tests/test_qr_public_validator.py`
- `tests/test_qr_record_bridge.py`
- `tests/test_qr_security_domain_allowlist.py`

Tested behavior or module if identifiable:

- `tests/test_qr_guard.py` imports `qr_guard`; it appears to test trusted HC:// and repository-backed payloads plus rejection of a legacy public verifier payload.
- `tests/test_qr_hardening.py` imports `qr_hardening`; it appears to test signed, unsigned, tampered, unsafe URL, missing-field, JSON-string, and allowed-domain behavior.
- `tests/test_qr_orchestrator_integration.py` imports `qr_orchestrator_integration` and `qr_hardening`; it appears to test QR verification behavior when connected to orchestration logic.
- `tests/test_qr_payload_parser.py` imports `hc_runtime.qr_payload_parser`; it appears to test payload contract shape, status values, safety markers, hash checks, CLI JSON behavior, fixture shape, and no-network behavior.
- `tests/test_qr_public_validator.py` imports `hc_runtime.qr_public_validator`; it appears to test combined QR payload and local-record validation behavior, duplicate record handling, no-network behavior, and boundary language.
- `tests/test_qr_record_bridge.py` imports `hc_runtime.qr_record_bridge`; it appears to test QR payload to local record bridge behavior, content-hash match and mismatch cases, duplicate records, CLI output, determinism, no-network behavior, and boundary language.
- `tests/test_qr_security_domain_allowlist.py` imports `qr_security`; it appears to test repository-backed domain allowlist behavior and legacy-domain rejection.

Overlap risk: Medium. Several files cover QR safety, URL/domain behavior, hash behavior, local-record behavior, CLI output, and advisory boundary language. The overlap appears architectural rather than clearly duplicate: parser, hardening, guard, bridge, validator, orchestrator, and domain allowlist surfaces each appear to protect different boundaries.

Deletion risk: High. QR behavior is security-adjacent and public-facing. Deleting tests without a full assertion and fixture comparison could reduce regression protection for no-network behavior, public-safe output, domain allowlists, or advisory boundary wording.

Recommendation: KEEP_ACTIVE and NEEDS_HUMAN_REVIEW for all listed QR tests. A QR test map documentation PR may be useful before any consolidation investigation. Do not delete or consolidate from this report alone.

### C. Public validator / public verification tests

Files inspected:

- `tests/test_public_validator.py`
- `tests/test_public_validator_api.py`
- `tests/test_public_validator_demo_runner.py`
- `tests/test_public_validator_lookup.py`
- `tests/test_public_validator_static_viewer_smoke.py`
- `tests/test_public_verification_explorer_mvp.py`
- `tests/test_public_verification_explorer_smoke.py`
- `tests/test_public_verification_response.py`

Tested behavior or module if identifiable:

- `tests/test_public_validator.py` imports `public_validator`; it appears to test proof validation cases including valid proof, invalid hash, broken revision chain, missing witness signature, and conflicting witnesses.
- `tests/test_public_validator_api.py` imports `public_validator_api`; it appears to test API request and response behavior.
- `tests/test_public_validator_demo_runner.py` appears to run public validator demo scenarios and compare deterministic JSON fixture output.
- `tests/test_public_validator_lookup.py` imports `hc_runtime.public_validator_lookup`; it appears to test local lookup, schema and hash validation fields, malformed records, unknown and invalid record IDs, duplicate record IDs, ignored generated or demo paths, deterministic CLI output, and golden fixture contracts.
- `tests/test_public_validator_static_viewer_smoke.py` appears to test static viewer entry points, supported fixture IDs, and unsupported record ID behavior.
- `tests/test_public_verification_explorer_mvp.py` imports `public_verification_explorer`; it appears to test search by record ID, hash, legacy content-hash alias, status, source path, no-results behavior, and human-readable rendering.
- `tests/test_public_verification_explorer_smoke.py` appears to test public verification explorer advisory boundaries, filter options, status badge logic, non-canonical generated indexes, detail sections, and zero-witness rendering.
- `tests/test_public_verification_response.py` imports `public_verification_response`; it appears to test verified, review-required, and invalid public response construction.

Overlap risk: Medium. Several tests include public-safe output, deterministic JSON, local lookup, and public verification display behavior. However, the imported modules and apparent boundaries differ across proof validation, API, demo runner, lookup, static viewer, explorer, and response construction.

Deletion risk: High. Public validator and public verification tests help preserve user-facing advisory boundaries and should not be reduced without a full behavior map and targeted runs.

Recommendation: KEEP_ACTIVE and NEEDS_HUMAN_REVIEW for the group. A public validator test map documentation PR may help identify future consolidation candidates. No immediate deletion is supported.

### D. Assistant / control bot tests

Files inspected:

- `tests/test_hc_assistant_command.py`
- `tests/test_hc_control_bot.py`
- `tests/test_hc_bot_status.py`

Tested behavior or module if identifiable:

- `tests/test_hc_assistant_command.py` imports `scripts.hc_assistant_command`; it appears to test help, empty command behavior, static advisory status, next guidance, and evidence checklist output.
- `tests/test_hc_control_bot.py` imports `scripts.hc_control_bot`; it appears to test changed-path scanning for non-protected docs, governance paths, workflow paths, and runtime paths.
- `tests/test_hc_bot_status.py` imports `scripts.hc_bot_status`; it appears to test report-only and public-safe status output, network and write boundaries, active and parked component separation, authority-safe next steps, and CLI machine-readable output.

Overlap risk: Low to medium. These files all involve assistant or control-bot surfaces and advisory boundaries, but they appear to test separate command, path-scope, and status-report modules.

Deletion risk: Medium. These tests protect authority boundaries and report-only behavior. Removing one could weaken regression coverage for human-supervised governance language or scope handling.

Recommendation: KEEP_ACTIVE and NEEDS_HUMAN_REVIEW. No consolidation should proceed without assertion-level comparison and confirmation that authority-boundary coverage remains intact.

### E. Protected-domain tests

Files inspected:

- `tests/test_federation_consensus.py`
- `tests/test_federation_simulation.py`
- `tests/test_federation_sync.py`
- `tests/test_federation_trust.py`
- `tests/test_signed_federation_exchange.py`
- `tests/test_signed_payload.py`
- `tests/test_signed_witness.py`
- `tests/test_policy_engine.py`

Tested behavior or module if identifiable:

- Federation tests import federation-related modules and appear to cover consensus, simulation, packet validation, protocol safety, trusted and suspended federation behavior, and signed federation exchange cases.
- Signed tests import signing-related modules and appear to cover deterministic canonical payloads, signature verification, tamper rejection, replay or expiration behavior, witness signatures, invalid signature versions, and missing signatures.
- `tests/test_policy_engine.py` imports `policy_engine`; it appears to test allow, review-required, and denied decisions.

Overlap risk: Not evaluated for consolidation in this report. These tests touch federation, signing, and policy behavior, which are protected or trust-kernel-adjacent domains.

Deletion risk: Very high. Any deletion, weakening, or consolidation could reduce regression protection for governance, security, provenance, signing, federation, or policy behavior.

Recommendation: DO_NOT_TOUCH_PROTECTED. KEEP_ACTIVE unless a separate human-reviewed protected-domain process explicitly authorizes a deeper investigation. This report does not recommend consolidation or deletion for these tests.

## 4. Safe next steps

Safe next steps are limited to report-only or human-reviewed follow-up:

- prepare an assertion-level manipulation test consolidation investigation without editing or deleting tests;
- prepare a QR test map documentation PR that documents module boundaries, fixture use, no-network expectations, and public-safe output contracts;
- prepare a public validator test map documentation PR that documents proof, lookup, API, static viewer, explorer, and response boundaries.

No test deletion should be recommended unless future evidence proves all of the following:

- the same assertions are covered elsewhere;
- the same module behavior is covered elsewhere;
- no unique edge cases are lost;
- CI remains green after targeted runs;
- a human reviewer approves the cleanup.

## 5. Stop conditions

Stop any cleanup or consolidation proposal if:

- a test touches protected domains;
- coverage uniqueness is unclear;
- deleting a test could reduce regression protection;
- a test is linked to governance, security, provenance, signing, federation, or policy behavior;
- imports or assertions were not fully compared.

These stop conditions preserve HC:// and HC-TRUST-LAYER review boundaries. They also preserve the project boundary that `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and human final authority remains required.

## 6. Suggested future PRs

The following future PRs may be considered only if reviewers agree that the supporting evidence is useful:

- one PR for a manipulation test consolidation investigation;
- one PR for QR test map documentation;
- one PR for public validator test map documentation.

Do not propose immediate deletion from this inventory. Future generated reports are advisory evidence only and not canonical records. CI and checks remain evidence for human review, not trust authority.
