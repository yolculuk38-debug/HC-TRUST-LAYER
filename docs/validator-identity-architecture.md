# HC-TRUST-LAYER Validator Identity Architecture

## Purpose

This document defines validator identity foundations for HC-TRUST-LAYER and HC:// verification infrastructure.

It is architecture guidance only and does not claim production interoperability, cryptographic guarantees, or automatic authenticity determination.

## Validator Identity Overview

Validator identity is the policy and metadata layer that explains who issued a verification outcome, under which declared role, and with which trust constraints.

In HC-TRUST-LAYER, validator identity supports provenance visibility, audit trail continuity, and human-supervised validation.

## `validator_id` Concepts

A `validator_id` is a stable identifier for a validator entity within a trust graph context.

Conceptual requirements:
- globally unique within a federation scope
- bound to canonical record verification events, not to content truth claims
- version-aware so lifecycle and key changes can be audited
- portable across verification package exchanges where policy allows

## Validator Classes

Example validator classes for architecture planning:
- public validator
- institutional validator
- domain-specialized validator (for example forensic or media workflow)
- archival validator
- federation relay validator

Class labels are descriptive capability hints and do not imply autonomous authority.

## Federation Roles

Validator identity may include federation role declarations such as:
- origin validator
- corroboration validator
- mirror validator
- dispute-review validator

Role declarations should be explicit in verification infrastructure outputs so downstream consumers can interpret provenance and trust graph edges correctly.

## Signing Authority Concepts

Validator identity should distinguish legal or organizational identity from signing authority.

Concepts:
- signer key material represents technical signing authority
- policy metadata represents organizational approval scope
- delegated signing authority should be time-bounded and auditable
- signing scope should be constrained to canonical record verification boundaries

## Trust Anchors

Validator identity evaluation requires trust anchors.

Concepts:
- anchor registries for known validator profiles
- key fingerprint references for validator signing material
- federation anchor exchange with versioned update history
- anchor supersession/revocation notices recorded in an audit trail

## Validator Capability Declaration

Each validator identity should publish capability declarations, such as:
- supported verification package versions
- supported signature envelopes
- replay detection support level
- evidence source handling limits
- offline verification compatibility claims

Capability declarations should be machine-readable where possible and human-readable in policy references.

## Validator Revocation State

Validator identity should include revocation state visibility.

Concepts:
- active
- suspended
- revoked
- retired
- unknown

Revocation status should be represented as a canonical record-linked signal with timestamps and reason classes.

## Validator Lifecycle Concepts

A validator lifecycle can include:
1. registration
2. activation
3. capability publication
4. rotation (keys/policies)
5. suspension or constrained mode
6. revocation or retirement
7. archival trace preservation

Lifecycle transitions should preserve provenance continuity and audit trail traceability.

## Validator Trust Risks

Key validator identity risks include:
- impersonation of legitimate validators
- stale trust anchors after key rotation
- forged or replayed validator outputs
- over-trust in a single validator class
- role confusion between witness and validator authorities

Mitigation direction should remain human-supervised and policy-driven.

## Terminology Alignment

This architecture note explicitly aligns with:
- HC-TRUST-LAYER
- HC://
- provenance
- verification infrastructure
- validator identity
- trust graph
- audit trail
- canonical record
- human-supervised validation

## Related Protocol Graph Integrity and Anti-Spoofing References

- `docs/protocol-graph-integrity.md`
- `docs/anti-spoofing-foundations.md`
- `docs/trusted-relationship-model.md`
