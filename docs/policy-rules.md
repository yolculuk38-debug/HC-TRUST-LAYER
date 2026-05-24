# HC-TRUST-LAYER Policy Rules (v1)

## Purpose

This document defines the first machine-readable **policy rules** baseline for HC-TRUST-LAYER governance and merge evaluation.

The policy rules are represented in `policy/hc-policy-v1.yml` and are designed to support consistent, auditable policy evaluation for merge risk and trust kernel protection while preserving **human-supervised validation**.

The policy rules use repository path risk classification, terminology constraints, and explicit human review triggers so future policy enforcement can evaluate changes consistently against canonical record and workflow boundaries.

## Policy File

- File: `policy/hc-policy-v1.yml`
- Policy version: `1.0`
- Current role: advisory baseline for future policy enforcement integration

## Risk Levels

The policy rules define four merge risk levels:

- `low`
- `medium`
- `high`
- `blocked`

These risk levels are used to classify changed paths and route merge outcomes for HC-TRUST-LAYER governance.

## Path-Based Rules

### Low risk

- `README.md`
- `docs/**/*.md`
- `examples/**/*.json`

### Medium risk

- `.github/workflows/**/*.yml`
- `scripts/check_*.py`
- `scripts/export_verification_package.py`
- `schema/verification-package-v1.schema.json`

### High risk

- `schema/record-v1.schema.json`
- `src/verify_hashes.py`
- `records/pending/**/*.json`
- `records/verified/**/*.json`
- `records/archived/**/*.json`

### Blocked unless explicitly reviewed

- `generated/**`
- `exports/cache/**`
- `docs/generated/**`
- `records/**/cache/**`
- `records/**/generated/**`
- `records/**/*_index.json`
- `records/**/explorer_index.json`

This classification keeps policy enforcement aligned with merge risk boundaries and protects trust-sensitive areas such as canonical record and trust kernel surfaces.

## Forbidden Terminology Policy

The policy rules include blocked terminology entries (see `policy/hc-policy-v1.yml`) to prevent authority inflation and truth-guarantee language.

This supports HC:// governance language discipline and avoids claims that conflict with human-supervised validation.

## Required Human Review Triggers

The policy rules require explicit human review for:

- canonical record schema changes
- validator behavior changes
- signing/key management changes
- federation semantics
- trust scoring semantics
- branch protection/workflow permission changes
- security policy changes

These categories represent trust-sensitive governance areas where human adjudication remains mandatory.

## Merge Policy Outcomes

The policy rules define these outcomes:

- `auto_merge_allowed`
- `conditional_merge`
- `human_review_required`
- `blocked`

## Baseline Requirements for `auto_merge_allowed`

Auto-merge is allowed only when all baseline requirements pass:

- all checks pass
- terminology guard passes
- docs drift guard passes
- canonical artifact guard passes
- no unresolved review threads
- no high-risk paths touched

## Non-Goals

This PR does **not**:

- implement a runtime policy engine
- modify validators
- modify schemas
- change branch protection settings
- claim production-ready enforcement

## Advisory Status

These policy rules are currently **advisory** until runtime policy enforcement is implemented.

The immediate goal is to establish stable machine-readable governance inputs now, so future enforcement can evaluate HC-TRUST-LAYER changes consistently and transparently.
