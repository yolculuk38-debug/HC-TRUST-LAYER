# HC-TRUST-LAYER Signing Architecture Foundation

## Purpose

This document defines a foundational signing architecture for HC-TRUST-LAYER verification infrastructure.

It describes signature concepts, witness/validator signature roles, trust anchors, and verification lifecycle behavior.

This document is architectural guidance only:
- no production-ready claim
- no blockchain claim
- no decentralization claim
- no cryptographic implementation included

## Signing Overview

Signing in HC-TRUST-LAYER is used to bind verification artifacts to identifiable actors and canonical record context.

Core objectives:
- integrity of signed claims
- attribution of witness and validator actions
- replay-aware verification lifecycle behavior
- auditable linkage to provenance and audit trail records

## Detached Signatures

Detached signatures are preferred for flexibility and transport safety.

Concept:
- canonical payload remains independent
- signature object references payload hash and metadata
- verification infrastructure can validate signatures without mutating original records

## Canonical Payload Signing

Canonical payload signing requires stable serialization boundaries.

Concepts:
- signature input must be deterministic
- signing context should include canonical record identifier
- payload hash should be explicitly referenced in signature metadata
- provenance linkage should be included in signed envelope context

## Ed25519 Future Integration

Ed25519 is a planned signing profile direction for HC-TRUST-LAYER.

Scope notes:
- algorithm profile is future integration guidance
- compatibility and migration policy remain to be finalized
- current repository status should continue to mark signing maturity as partial where applicable

## Witness Signatures

Witness signatures represent attestation actions.

Concepts:
- witness signs attestation payload bound to canonical record and provenance scope
- witness type (AI or human) must be represented in signed metadata
- witness signatures may be single or part of multi-witness sets
- human-supervised validation policies may require human witness signatures for specific escalation outcomes

## Validator Signatures

Validator signatures represent verification outcome statements.

Concepts:
- validator signs result package including status and evidence references
- validator signatures should include timestamp and policy/version context
- validators must not sign unverifiable payload transformations outside canonical boundaries

## Multi-Signature Concepts

Multi-signature support is conceptual and policy-driven.

Patterns:
- threshold style: minimum number of witness/validator signatures
- role-mix style: required combination of witness classes (for example AI + human)
- staged signatures: witness first, validator second, archive attestation third

Multi-signature policy should be explicit per verification level and risk class.

## Trust Anchor Concepts

Trust anchors are root references used to evaluate signer legitimacy.

Concepts:
- known validator identities and key fingerprints
- known witness registries where applicable
- federation trust anchor exchange for cross-node verification
- anchor update and revocation audit trail requirements

## Signature Verification Lifecycle

A conceptual lifecycle for verification infrastructure:
1. ingest signature envelope
2. validate canonical payload linkage
3. verify signature against expected key material
4. check timestamp and replay constraints
5. check revocation/rotation status
6. attach decision to audit trail and trust graph

## Key Rotation Concepts

Key rotation supports long-term signing hygiene.

Concepts:
- pre-announced rotation windows where possible
- overlap periods with old/new key acceptance rules
- rotation events logged in audit trail
- verifier behavior for historical vs active keys

## Revocation Concepts

Revocation handles compromised or retired signers/keys.

Concepts:
- revocation registry or equivalent signed status feed
- explicit reason categories (compromise, retirement, policy violation)
- historical record preservation with current status overlays
- revocation checks integrated into verification lifecycle

## Replay Protection Concepts

Replay protection prevents old signed artifacts from being reused misleadingly.

Concepts:
- nonce or unique envelope identifiers
- bounded validity windows where policy requires
- signature context binding to canonical record + provenance scope
- duplicate-detection linkage in audit trail

## Security Considerations

### Stolen Key Scenarios

Risk:
- attacker signs seemingly valid witness or validator artifacts.

Mitigation direction:
- rapid revocation propagation
- anomaly monitoring on signer behavior
- high-risk fallback to human-supervised validation

### Fake Witness Risks

Risk:
- fabricated witness identities introduce misleading attestations.

Mitigation direction:
- identity verification controls for witness registries
- trust anchor checks for witness key material
- lower default trust weighting for unknown witness profiles

### Compromised Validator Risks

Risk:
- a trusted validator emits incorrect or malicious signed outcomes.

Mitigation direction:
- cross-validator comparison in federated verification
- validator behavior analytics and quarantine flags
- emergency validator suspension with audit trail traceability

### Timestamp Manipulation

Risk:
- forged or shifted timestamps alter interpretation of provenance order.

Mitigation direction:
- signed timestamp context plus independent receipt logs
- tolerance windows with explicit policy
- contradiction detection across federation nodes

### Forged Provenance Chains

Risk:
- attacker constructs synthetic provenance references around authentic signatures.

Mitigation direction:
- strict canonical record linkage validation
- parent-child provenance consistency checks
- federated replay lineage comparison
- mandatory human-supervised validation for high-impact conflicts

## Terminology Alignment

This document aligns with HC:// architecture terminology and explicitly uses:
- HC-TRUST-LAYER
- provenance
- trust graph
- verification infrastructure
- audit trail
- witness
- validator
- canonical record
- human-supervised validation
