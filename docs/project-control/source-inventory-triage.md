# Source Inventory Triage

Status: advisory inventory checkpoint.

This note starts the source-inventory pass requested after the external audit triage. It does not delete, archive, move, or reclassify implementation files. It records what is already confirmed and what still needs direct source review.

## Confirmed active implementation anchors

| Area | Paths | Status | Notes |
| --- | --- | --- | --- |
| Local verification package core | `src/hc_trust/verification_package.py` | Active implementation | Local manifest and SHA-256 package integrity core. |
| CLI entry point | `src/hc_trust/cli.py` | Active implementation | Exposes `hc-trust verify-package`. |
| Verification package tests | `tests/test_verification_package_hash_core.py`, `tests/test_verification_package_sample.py`, `tests/test_verification_package_witness_proof.py`, `tests/test_verification_package_timestamp_proof.py` | Active tests | Cover local package core, sample package, witness proof, timestamp proof, and fixture behavior. |
| Runtime telemetry surface | `src/hc_runtime/routes/health.py`, `tests/runtime/test_telemetry_payload_contract.py`, `tests/test_hc_runtime_app.py`, `tests/test_hc_runtime_response_contracts.py` | Active / needs focused review | Telemetry and runtime response contracts already have source and test anchors. |

## Not confirmed during this pass

| External finding | Current triage result | Next action |
| --- | --- | --- |
| `normalize_records.py` silently rewrites records. | Not found by root-path lookup or content search in this pass. | Search workflow references and archive-related docs before opening any fix PR. |
| Large number of stub or experimental source files. | Not classified yet. | Create a non-mutating source inventory table before moving or deleting anything. |
| Integration tests cover only narrow examples. | Not classified yet. | Inventory current tests before editing test behavior. |
| Shortened historical or genesis hashes. | Not classified yet. | Identify exact files and evidence source before editing historical records. |
| Excess branch count. | Not confirmed by current branch search tooling. | Verify in GitHub UI or reliable branch listing before cleanup. |

## Operating decision

Do not start by deleting, moving, or archiving source files. The safe sequence is:

1. Inventory source and test files.
2. Classify each item as active, test support, docs support, experimental, parked, or needs review.
3. Open separate small PRs only after the inventory identifies a concrete change.
4. Avoid protected paths unless explicitly authorized.

## Next safe action

Continue with a source inventory note or script that lists repository Python files and their rough category without changing implementation behavior.

Human final authority remains required for deletion, archival, or protected-path changes.
