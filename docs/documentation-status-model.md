# HC-TRUST-LAYER Documentation Status Model

> **Documentation Status**
> - **status:** IMPLEMENTED
> - **scope:** Standard documentation classification model for HC:// repository-facing status visibility.
> - **canonical relevance:** Advisory policy for documentation classification; does not alter canonical schema or record identity rules.
> - **runtime relevance:** High for contributor alignment; no direct runtime behavior effect.

## Purpose

This model standardizes how HC-TRUST-LAYER documentation communicates implementation maturity.

It is designed to reduce ambiguity between:
- current runtime logic,
- partial/experimental foundations,
- planned architecture,
- and research-only concepts.

All classification remains advisory and must preserve human-supervised validation.

## Standard Status Labels

Use only these labels in repository-facing documentation headers and status sections:

- **IMPLEMENTED**
- **PARTIAL**
- **PLANNED**
- **RESEARCH**
- **ARCHIVED**

## Status Meanings

### IMPLEMENTED
Use when repository evidence shows active behavior already supported by code paths, docs, and relevant checks/tests.

### PARTIAL
Use when foundational components exist, but end-to-end behavior, operational hardening, or coverage is incomplete.

### PLANNED
Use when architecture direction is intentionally defined but not yet fully implemented as stable runtime capability.

### RESEARCH
Use when the topic is exploratory, conceptual, or prototyped without a finalized implementation contract.

### ARCHIVED
Use when the document is retained for historical provenance/audit trail continuity and is not active guidance for current implementation.

## Contributor Classification Rules

When classifying a document:

1. Identify whether the doc primarily describes runtime behavior, design intent, or historical context.
2. Validate status against repository evidence (code, checks, tests, and canonical references).
3. Prefer conservative classification when uncertain (for example, PARTIAL instead of IMPLEMENTED).
4. Do not claim production readiness, objective truth guarantees, or autonomous governance finality.
5. Preserve advisory-only verification language and human-supervised validation boundaries.

## Header Block Standard

Major documentation files should include a compact status header near the top:

- **status**
- **scope**
- **canonical relevance**
- **runtime relevance**

Recommended format:

```md
> **Documentation Status**
> - **status:** PARTIAL
> - **scope:** <short scope statement>
> - **canonical relevance:** <how this doc relates to canonical boundaries>
> - **runtime relevance:** <how this doc relates to runtime logic>
```

## Runtime Logic vs Conceptual Architecture

### Runtime logic
Runtime logic refers to executable behavior and enforced validation surfaces such as validators, trust-kernel pathways, and canonical boundary checks.

### Conceptual architecture
Conceptual architecture refers to target-state design, roadmap layers, or research direction that may guide future implementation but does not itself enforce runtime behavior.

A document may describe both. In such cases:
- classify based on the strongest currently evidenced state,
- explicitly distinguish implemented behavior from planned/research components,
- and preserve audit trail continuity in wording.
