# Federation Readiness Model

This document defines federation-readiness boundaries for HC-TRUST-LAYER and HC:// without introducing distributed authority, autonomous trust claims, or canonical-record changes.

## Scope and posture

- This model is documentation-only and advisory.
- Canonical records remain authoritative.
- External verification remains advisory-only.
- Human-supervised validation remains required for consequential decisions.

## Boundary terms

### local verifier

A **local verifier** is a verifier process operated within the local HC:// review environment. It evaluates canonical records and related references using repository-defined checks.

### external verifier

An **external verifier** is a verifier process outside the local HC-TRUST-LAYER operating boundary. External outputs can provide interoperability signals but do not override canonical records.

### federation participant

A **federation participant** is a party that exchanges verification package references for interoperability testing and review continuity. Participation does not imply automatic trust or delegated authority.

### verification package boundary

A **verification package boundary** is the boundary around transportable verification references exchanged between local and external verifiers. Verification packages are review inputs and interoperability aids.

### canonical artifact boundary

A **canonical artifact boundary** is the strict boundary for canonical record surfaces, including canonical records and their schema-constrained validation pathways. Canonical boundaries remain authoritative for HC:// verification conclusions.

### generated artifact boundary

A **generated artifact boundary** is the boundary for derived artifacts such as indexes, snapshots, and example exchange packages under `generated/**`. Generated artifacts are non-canonical and must not be treated as canonical records.

## Federation principles for future interoperability

1. **Federation is interoperability, not automatic trust.** Federation exchanges provide cross-environment compatibility signals and review context, not autonomous authority.
2. **External verification remains advisory.** External verifier outcomes are evidence inputs that require local interpretation and reviewer oversight.
3. **Human review remains required.** Human-supervised validation is required before material trust-kernel conclusions or consequential actions.
4. **Provenance continuity must remain auditable.** Reference chains between record identity, hash continuity, and audit trail artifacts must stay inspectable.
5. **Canonical records remain authoritative.** Canonical record surfaces remain the source of truth for verification decisions in HC-TRUST-LAYER.

## Lightweight federation verification package model

A lightweight federation package can contain reference pointers for interoperability review:

- record reference
- hash reference
- audit reference
- explorer reference
- advisory metadata
- generated artifact warning

The package is non-canonical and does not enter canonical record validation workflows.

## Validation and guard expectations

- Do not modify canonical schema as part of federation-readiness packaging.
- Do not weaken validators or guard workflows.
- Keep federation package artifacts under generated, non-canonical paths.
- Exclude generated federation package examples from strict canonical validation surfaces.

## References

- `docs/public-verification-boundaries.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/verification-signal-model.md`
- `docs/implementation-map.md`
