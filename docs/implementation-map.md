# HC-TRUST-LAYER Implementation Map

## Purpose

This map connects the six master architecture layers to concrete repository artifacts and current maturity status for HC-TRUST-LAYER verification infrastructure.

Status scale:
- implemented
- partial
- planned
- research

## Layer-to-Implementation Map

## 1) Record Integrity Layer

**Status:** implemented

**Primary files and docs**
- `schema/record-v1.schema.json`
- `src/hc_trust/verification.py`
- `src/hc_trust/hashing.py`
- `src/hc_trust/tamper_detection.py`
- `src/hc_trust/deterministic_export.py`
- `tests/test_schema_hardening.py`
- `tests/test_deterministic_export.py`
- `docs/record-format.md`

**Coverage notes**
- Canonical schema, deterministic hash generation, and verification checks are present and tested.
- Deterministic export and tamper detection logic indicate stable baseline behavior.

## 2) Witness & Signature Layer

**Status:** partial

**Primary files and docs**
- `src/signed_witness.py`
- `src/witness_signature.py`
- `src/hc_trust/signed_payload.py`
- `src/hc_trust/witness_integrity.py`
- `src/revocation.py`
- `tests/test_signed_witness.py`
- `tests/test_signed_payload.py`
- `docs/witness-layer.md`
- `docs/signed-witness-model.md`

**Coverage notes**
- Signature and witness primitives exist with tests.
- Revocation and witness integrity paths are present but still evolving and not fully standardized end-to-end.

## 3) Public Verification Layer

**Status:** implemented

**Primary files and docs**
- `src/hc_trust/cli.py`
- `src/verification_cli.py`
- `src/public_validator.py`
- `src/public_validator_api.py`
- `src/public_verification_response.py`
- `src/hc_trust/verifier_api.py`
- `tests/test_verification_cli.py`
- `tests/test_public_validator.py`
- `tests/test_public_validator_api.py`
- `docs/verify.md`
- `docs/VERIFICATION_FLOW.md`
- `docs/api/verification-api-v1.md`

**Coverage notes**
- Public CLI/API routes and machine-readable output are implemented.
- Verification summaries and status models are documented and test-backed.

## 4) Federation & Sync Layer

**Status:** planned

**Primary files and docs**
- `src/federation_sync.py`
- `src/federation_consensus.py`
- `src/federation_registry.py`
- `src/federation_discovery.py`
- `src/federation_exchange.py`
- `src/signed_federation_exchange.py`
- `tests/test_federation_sync.py`
- `tests/test_federation_consensus.py`
- `tests/test_signed_federation_exchange.py`
- `docs/federation-architecture.md`
- `docs/federation-sync.md`

**Coverage notes**
- Building blocks and tests exist for sync and consensus behavior.
- Production convergence semantics, rollout policy, and operational hardening remain incomplete.

## 5) External Integration Layer

**Status:** research

**Primary files and docs**
- `src/external_verification_package.py`
- `src/export_package.py`
- `src/portable_package_v2.py`
- `src/browser_validator.py`
- `src/social_media_bridge.py`
- `src/public_explorer_api.py`
- `tests/test_export_import.py`
- `tests/test_portable_package_v2.py`
- `tests/test_browser_validator.py`
- `tests/test_social_media_bridge.py`
- `docs/external-verification-packages.md`
- `docs/export-import-verification.md`
- `docs/verification-package-spec.md`
- `docs/verification-package-format.md`
- `docs/verification-package-validation.md`
- `docs/verification-package-generation.md`

**Coverage notes**
- Multiple integration surfaces are prototyped.
- Interface stability, version guarantees, and partner-facing compatibility contracts are not finalized.

## 6) Governance & Dispute Layer

**Status:** planned

**Primary files and docs**
- `src/governance_layer.py`
- `src/governance_policy.py`
- `src/governance_vote.py`
- `src/community_governance.py`
- `src/reviewer_policy.py`
- `src/review_queue.py`
- `src/revocation_registry.py`
- `tests/test_registry_revocation_integration.py`
- `docs/GOVERNANCE.md`
- `docs/reviewer-registry.md`
- `docs/reviewer-selection.md`
- `docs/limitations-and-risks.md`

**Coverage notes**
- Governance and reviewer-policy components are present.
- Dispute lifecycle automation, decision logging standards, and appeal workflows are not yet complete.

## Gap Summary (No Hype)

1. **Layer maturity is uneven.** Integrity and public verification are stronger than federation, governance, and integrations.
2. **Several modules are naming-level complete but process-level incomplete.** Some files exist without a fully defined operational policy around them.
3. **Cross-layer contracts are not uniformly versioned.** Interface stability and compatibility guarantees are incomplete for external consumption.
4. **Dispute workflow completeness is limited.** Governance docs exist, but deterministic execution paths for appeals/supersession are still partial.
5. **Federation production readiness is unclear.** Local test coverage exists, but distributed failure and convergence guarantees are still developing.

## Next-Step Priority Table

| Priority | Area | Why now | Concrete next step | Target status shift |
|---|---|---|---|---|
| P0 | Federation & Sync | Needed for multi-node consistency and audit continuity. | Define and document convergence + conflict-resolution invariants; add scenario tests for partition/rejoin behavior. | planned → partial |
| P0 | Governance & Dispute | Required for contested-record handling and policy transparency. | Implement a minimal dispute lifecycle spec (intake, adjudication, supersession, revocation linkage) with deterministic state transitions. | planned → partial |
| P1 | Witness & Signature | Core attribution exists but needs stricter interoperability. | Freeze witness/signature envelope fields and publish compatibility matrix + migration notes. | partial → implemented (baseline) |
| P1 | External Integration | Integrations exist but contracts are still fluid. | Version external package/API contracts and publish compatibility policy (supported/unsupported fields). | research → planned |
| P2 | Cross-layer observability | Needed to evaluate trust-layer behavior over time. | Add architecture-level metrics map tying verification outcomes to layer-level signals and failures. | planned internal hardening |

## References

- Master architecture baseline: `docs/master-architecture.md`
- Capability status matrix: `docs/capability-status.md`
- Public verification API architecture draft: `docs/public-verification-api.md`
- Protocol and verification docs: `docs/PROTOCOL.md`, `docs/verify.md`, `docs/VERIFICATION.md`
- AI collaboration workflow: `docs/ai-collaboration-workflow.md`

## Related Governance Reference

- Trusted auto-merge governance model: `docs/trusted-auto-merge.md`

