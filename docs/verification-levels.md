# HC-TRUST-LAYER Verification Levels

## Purpose

This document defines conceptual verification levels for HC-TRUST-LAYER verification infrastructure.

It standardizes escalation language from minimal checks to high-confidence states while preserving human-supervised validation as a core role.

This is a documentation-only framework:
- no production-ready claim
- no decentralization claim
- no blockchain claim
- no cryptographic implementation in this document

## Level Model

### 1) UNVERIFIED

**Requirements**
- record exists but has not completed verification checks.

**Limitations**
- no integrity assurance
- no provenance confidence
- no trust graph contribution beyond placeholder status

**Escalation path**
- move to HASH_VERIFIED by completing canonical hash checks.

### 2) HASH_VERIFIED

**Requirements**
- canonical payload hash matches expected canonical record reference.

**Limitations**
- proves integrity consistency only within checked context
- no signature-backed witness or validator attestation required yet

**Escalation path**
- move to SIGNED when at least one valid signature envelope is verified.

### 3) SIGNED

**Requirements**
- at least one valid signature linked to canonical record and provenance context
- signature source identified as witness or validator.

**Limitations**
- single-signer risk remains
- trust score remains sensitive to signer quality and revocation status

**Escalation path**
- move to MULTI_WITNESS when independent witness diversity criteria are met.

### 4) MULTI_WITNESS

**Requirements**
- multiple valid witness signatures with independent origin context
- witness set includes traceable provenance references
- policy may require AI witness plus human witness composition.

**Limitations**
- validator-level adjudication may still be pending
- witness collusion risk must still be evaluated

**Escalation path**
- move to FEDERATED when cross-node verification infrastructure confirms artifacts.

### 5) FEDERATED

**Requirements**
- verification artifacts successfully validated across federated nodes
- canonical record linkage remains consistent across federation topology
- validator evidence includes federation context.

**Limitations**
- federation consistency does not automatically equal objective truth
- trust anchor quality still determines confidence boundaries

**Escalation path**
- move to ARCHIVED when durable audit trail and archival package criteria are met.

### 6) ARCHIVED

**Requirements**
- verification result and related provenance/audit trail artifacts preserved in archival form
- replay lineage references captured for future re-verification
- revocation/supersession linkage retained.

**Limitations**
- archived status is historical durability, not permanent certainty
- future evidence can still trigger reclassification

**Escalation path**
- move to HIGH_TRUST only when policy-level confidence conditions are satisfied.

### 7) HIGH_TRUST

**Requirements**
- criteria from prior levels satisfied
- strong witness and validator diversity with no unresolved high-risk contradictions
- policy-driven human-supervised validation completed for high-impact use cases
- current revocation and replay checks are clear at review time.

**Limitations**
- still bounded by available evidence and policy scope
- does not represent objective truth certainty or irreversible finality

**Escalation path**
- maintain through periodic re-verification and audit trail updates.

## Human-Supervised Validation Role

Human-supervised validation is a cross-level control, not a single level.

Roles:
- review ambiguous provenance conflicts
- adjudicate disputes involving witness or validator inconsistency
- approve high-impact escalations to HIGH_TRUST where policy requires
- trigger downgrade or quarantine when new risk evidence appears

## Cross-Level Notes

- Verification levels express confidence in integrity/provenance handling under HC-TRUST-LAYER rules.
- Levels support trust graph interpretation and verification infrastructure interoperability.
- Levels should map to explicit audit trail events for transparency.
- Levels are policy-governed and can change over time with new provenance evidence.

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
