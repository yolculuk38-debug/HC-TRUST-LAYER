# HC:// Trust Scoring

> Status: **Planned / Experimental**
>
> Trust scoring in HC:// TRUST LAYER is experimental, non-authoritative, and must not be treated as a final truth signal.

## Definition

A trust score is a derived, advisory indicator that summarizes verification-related signals for a record.

It is intended to help prioritization and review workflows, not to replace independent validation or human judgment.

## Non-Authoritative Policy

- Trust score outputs are **informational only**.
- A high score is not proof of authenticity.
- A low score is not automatic proof of manipulation.
- Final decisions require full verification context (hash, provenance, witness, and archive data).

## Planned Scoring Factors

The following factors are planned inputs to future scoring models:

1. **Hash Validity**
   - Whether record content matches the expected hash material.
2. **Witness Count**
   - Number of witness entries attached to a record.
3. **Witness Diversity**
   - Diversity across witness classes (human, AI, system, commit/timestamp).
4. **Provenance Depth**
   - Strength and depth of source lineage and traceable references.
5. **Validation Status**
   - Current technical verification state (pass/fail/pending).
6. **Archive Integrity**
   - Consistency and integrity of archived verification artifacts over time.

## Implementation Note

This document describes a forward-looking concept only. It does not modify runtime validation logic or repository workflows.
