# HC-TRUST-LAYER Capability Status Matrix

## Purpose

This document tracks current capability status for HC-TRUST-LAYER using repository evidence.

HC-TRUST-LAYER currently has a trust kernel and verification/provenance foundations.
External ecosystem integrations are planned, not currently implemented.

Verification results in this repository indicate integrity and provenance status under defined rules; they do not prove objective truth.

Capability interpretation is aligned with human-supervised validation and public verification boundaries.

## Status matrix

| Capability | Current status | Repo evidence | Layer | Notes |
|---|---|---|---|---|
| SHA256 record verification | Implemented | `src/hc_trust/hashing.py`, `src/hc_trust/verification.py`, `tests/test_schema_hardening.py` | Record Integrity | Deterministic hash + verification pipeline exists. |
| canonical record boundary | Implemented | `schema/record-v1.schema.json`, `docs/record-format.md`, `src/hc_trust/deterministic_export.py` | Record Integrity | Canonical schema and deterministic export boundaries are defined. |
| immutable audit trail | Partial | `src/hc_trust/witness_integrity.py`, `src/revocation_registry.py`, `docs/witness-layer.md` | Witness & Signature | Audit signals exist, but full immutable multi-system trail guarantees are incomplete. |
| provenance tracking | Implemented | `docs/verify.md`, `src/public_verification_response.py`, `src/hc_trust/verification.py` | Public Verification | Provenance is part of verification outputs and docs. |
| QR verification | Implemented | `src/qr.py`, `tests/test_qr_hardening.py`, `docs/demo-flow.md` | Public Verification | QR generation and demo verification flow are present. |
| explorer/index generation | Partial | `src/public_explorer_api.py`, `docs/drafts/architecture-roadmap.md` | External Integration | Early explorer API surface exists; index ecosystem is not complete. |
| public verification | Implemented | `src/hc_trust/cli.py`, `src/public_validator.py`, `docs/verify.md` | Public Verification | Public CLI/validator verification pathways are available. |
| federation | Planned | `docs/federation-architecture.md`, `docs/federation-sync.md`, `src/federation_sync.py` | Federation & Sync | Design and module foundations exist; production integration is pending. |
| multi-witness validation | Partial | `src/signed_witness.py`, `src/witness_signature.py`, `tests/test_signed_witness.py` | Witness & Signature | Witness/signature building blocks exist; broader witness policy remains incomplete. |
| AI-assisted witness | Partial | `docs/ai-assisted-review.md`, `examples/ai_witness_example.json` | Witness & Signature | AI-assisted witness workflow is documented as guided support, not autonomous authority. |
| trust scoring | Partial | `docs/trust-scoring.md`, `docs/trust-score.md`, `docs/trust-engine-v1.md` | Governance & Dispute | Scoring model foundations exist and are marked experimental/draft. |
| SSL-like trust model | Planned | `docs/master-architecture.md`, `docs/drafts/architecture-roadmap.md` | External Integration | Trust-comparison framing exists at roadmap level, not as implemented protocol parity. |
| banking/security message verification | Research | `docs/drafts/architecture-roadmap.md` | External Integration | Directional idea only; no dedicated implementation path finalized. |
| Gmail / Message Trust Layer | Research | `docs/drafts/architecture-roadmap.md` | External Integration | Listed as future ecosystem path; no production module exists. |
| video/media verification | Planned | `src/external_verification_package.py`, `docs/verification-package-spec.md` | External Integration | Packaging foundations can support media workflows; end-to-end productization is pending. |
| archive verification | Partial | `docs/master-architecture.md`, `docs/implementation-map.md` | Federation & Sync | Archival resilience strategy exists; automated archive verification is incomplete. |
| social media integration | Research | `src/social_media_bridge.py`, `tests/test_social_media_bridge.py` | External Integration | Prototype bridge exists; partner-grade integration contracts are not finalized. |
| government/institution integration | Research | `docs/master-architecture.md`, `docs/drafts/architecture-roadmap.md` | External Integration | Declared as future adapter direction only. |
| C2PA compatibility | Not implemented | `docs/drafts/architecture-roadmap.md` | External Integration | No explicit C2PA implementation exists in current repository. |
| Ed25519 signing | Partial | `src/witness_signature.py`, `src/signed_witness.py`, `tests/test_signed_witness.py` | Witness & Signature | Signature support exists; compatibility and rollout guarantees are incomplete. |
| browser extension | Research | `src/browser_validator.py`, `tests/test_browser_validator.py` | External Integration | Browser validation prototype exists; extension distribution model is not implemented. |
| public API | Implemented | `src/public_validator_api.py`, `src/hc_trust/verifier_api.py`, `docs/api/verification-api-v1.md` | Public Verification | API verification interfaces are available. |
| live trust graph | Not implemented | `docs/trust-scoring.md`, `docs/drafts/architecture-roadmap.md` | Governance & Dispute | No live graph subsystem is currently implemented. |

## Interpretation notes

- This matrix is a repository-status snapshot, not a product promise.
- "Implemented" means directly supported by current code/docs/tests in this repository.
- "Partial" means foundational components exist but complete operational coverage is not finished.
- "Planned" and "Research" indicate roadmap direction rather than currently deployed capability.

## Documentation Terminology Guard

- Automated terminology check: `.github/workflows/terminology.yml`
- Local checker: `scripts/check_terminology.py`
- Docs drift workflow: `.github/workflows/docs-drift.yml`
- Docs drift checker: `scripts/check_docs_drift.py`
- Scope: `README.md`, `docs/**/*.md`, `.github/**/*.md`
- Canonical artifact boundary workflow: `.github/workflows/canonical-artifacts.yml`
- Canonical artifact boundary checker: `scripts/check_canonical_artifacts.py`
- Verification package format draft: `docs/verification-package-format.md`
- Verification package validation semantics: `docs/verification-package-validation.md`
- Verification package generation architecture: `docs/verification-package-generation.md`
- Public verification API architecture draft: `docs/public-verification-api.md`
- Trust kernel stabilization checkpoint (PR #300): `docs/trust-kernel-checkpoint-300.md`
- Agent governance foundation: `docs/agent-governance.md`
- Execution audit trail foundation: `docs/execution-audit-trail.md`
- Approval checkpoints baseline: `docs/approval-checkpoints.md`
- Trust graph foundation (documentation baseline): `docs/trust-graph.md`
- Trust decay and risk history foundation (documentation baseline): `docs/trust-decay-risk-history.md`
- Message/content provenance foundation (documentation baseline): `docs/message-content-provenance.md`
- Signing architecture foundation (documentation baseline): `docs/signing-architecture.md`
- Dispute resolution and challenge architecture foundation (documentation baseline): `docs/dispute-challenge-architecture.md`
- Verification levels model (documentation baseline): `docs/verification-levels.md`

## Related Governance Reference

- Trusted auto-merge governance model: `docs/trusted-auto-merge.md`
- Policy engine architecture: `docs/policy-engine-architecture.md`
- Repository security audit checklist: `docs/repo-security-audit.md`

- Validator identity architecture foundation: `docs/validator-identity-architecture.md`
- Replay and duplicate detection foundation: `docs/replay-duplicate-detection.md`
- Verification package v2 architecture foundation: `docs/verification-package-v2.md`
- Privacy and redaction model foundation: `docs/privacy-redaction-model.md`
- C2PA bridge considerations foundation: `docs/c2pa-bridge-considerations.md`

- Institutional governance foundation: `docs/institutional-governance.md`
- Evidence retention lifecycle foundation: `docs/evidence-retention-lifecycle.md`
- Trust query routing foundation: `docs/trust-query-routing.md`
- Sustainability model foundation: `docs/sustainability-model.md`
- Long-term archival integrity foundation: `docs/long-term-archival-integrity.md`
- Trust graph data model foundation: `docs/trust-graph-data-model.md`
- Validator capability model foundation: `docs/validator-capability-model.md`
- Evidence continuity foundation: `docs/evidence-continuity.md`
- Verification routing model foundation: `docs/verification-routing-model.md`
