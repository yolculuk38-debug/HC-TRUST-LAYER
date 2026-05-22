# HC:// Public Demo Dataset

## Purpose

This dataset provides portable examples for:
- verified records
- manipulated records
- revoked records
- recovered records
- federated verification

The goal is to support:
- public validator testing
- browser/mobile verifier demos
- explainability rendering
- trust badge rendering
- federation simulations

---

# Example Dataset Entries

## VERIFIED_RECORD
- verification: VERIFIED
- trust_score: 96
- provenance: CLEAN
- federation: CONSENSUS_REACHED
- risk: LOW

## MANIPULATED_RECORD
- verification: REVIEW_REQUIRED
- trust_score: 28
- provenance: REVIEW_REQUIRED
- manipulation: DETECTED
- risk: HIGH

## REVOKED_RECORD
- verification: REVOKED
- trust_score: 12
- provenance: INVALID
- federation: CONFLICT
- risk: CRITICAL

## RECOVERED_RECORD
- verification: VERIFIED
- recovery: RESTORED
- trust_score: 84
- provenance: CLEAN
- risk: LOW

## FEDERATED_RECORD
- verification: VERIFIED
- federation: CONSENSUS_REACHED
- witness_count: 5
- trust_score: 91
- risk: LOW

---

# Usage Areas

- public validator
- verification CLI
- browser verifier
- mobile verifier
- explainability renderer
- trust badge rendering
- federation simulation
- security gate testing
