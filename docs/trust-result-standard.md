# HC-TRUST-LAYER HC:// Trust Result Standard (MVP-1)

## Purpose

This document defines a documentation-only, human-readable trust result format for HC-TRUST-LAYER and HC:// MVP-1 verification surfaces.

The standard is designed to help non-technical readers interpret verification outcomes quickly without requiring deep protocol graph, provenance, validator, or replay-analysis expertise.

## Scope and Boundaries

- documentation standard only
- no runtime implementation in this phase
- no automatic truth determination
- no forensic certainty claims
- no production-readiness claim
- all outcomes remain advisory and require human-supervised validation for high-impact decisions

## Trust Result Overview

A trust result is a concise outcome label paired with plain-language explanation.

Each trust result should communicate:

- what signals were visible
- what uncertainty remains
- what human-supervised validation is recommended

## Human-Readable Verification Goals

The trust result format should optimize for:

- fast interpretation in seconds
- plain-language readability
- explicit uncertainty boundaries
- consistent status semantics across views
- audit trail-aware interpretation

## Simplicity-First Communication

Primary trust result presentation should prioritize a short summary before technical depth.

Recommended summary pattern:

1. result class label
2. one-sentence meaning
3. one-sentence caution or uncertainty note
4. human-supervised review guidance

For MVP-1 viewer readability, include explicit status labels where applicable:

- Verified trace
- Partial trace
- Replay warning
- Disputed
- Unverified
- Human review required

## Mobile-First Readability

Trust result content should remain readable on small screens:

- short headings
- compact bullet blocks
- no dense paragraph walls
- progressive disclosure for deep evidence details
- brief explanation blocks for meaning, review needs, assumption boundaries, and demo-only limitations

## Trust-Oriented UX Principles

Trust result messaging should preserve HC:// boundary semantics:

- show evidence-linked signals, not certainty inflation
- communicate limitations directly
- preserve provenance and audit trail context
- route ambiguity to human-supervised validation

## Result Classes

### VERIFIED TRACE

**Meaning**

Verification signals within displayed scope are materially consistent with available provenance continuity and validator context.

**Typical causes**

- continuity signals present across expected artifact relationships
- validator outcomes align with displayed scope
- no material replay warning in visible scope

**Recommended user interpretation**

Treat as a positive trust signal for the displayed scope only.

**Limitations**

Does not prove complete truth certainty, complete ecosystem coverage, or future-state validity.

**Human-supervised review guidance**

Use normal reviewer confirmation for consequential decisions and confirm scope boundaries before relying on the result.

### PARTIAL TRACE

**Meaning**

Some verification signals are present, but continuity or supporting context is incomplete.

**Typical causes**

- incomplete provenance linkage
- missing validator rationale in visible scope
- partial snapshot chronology visibility

**Recommended user interpretation**

Treat as incomplete verification coverage requiring cautious interpretation.

**Limitations**

Does not support strong confidence claims for missing segments of the canonical record context.

**Human-supervised review guidance**

Request expanded evidence review and confirm whether missing continuity affects the decision boundary.

### LOW CONFIDENCE

**Meaning**

Verification evidence is present but weak, sparse, or materially ambiguous.

**Typical causes**

- conflicting low-strength indicators
- sparse provenance evidence
- outdated or limited validator coverage

**Recommended user interpretation**

Treat as uncertainty-first; do not over-interpret as pass/fail certainty.

**Limitations**

Cannot support high-assurance interpretation without additional evidence and reviewer analysis.

**Human-supervised review guidance**

Escalate for deeper human-supervised validation and request additional provenance or validator inputs.

### REPLAY WARNING

**Meaning**

Potential replay-related risk signal indicates suspicious reuse, duplication, or context mismatch patterns.

**Typical causes**

- duplicate propagation patterns
- mismatched metadata across linked artifacts
- suspicious timing or continuity anomalies

**Recommended user interpretation**

Treat as a caution state requiring direct reviewer attention before trust decisions.

**Limitations**

Replay warning indicates risk, not definitive proof of malicious behavior.

**Human-supervised review guidance**

Escalate for targeted replay analysis and document reviewer conclusions in the audit trail.

### DISPUTED

**Meaning**

Verification context includes an active dispute signal affecting trust interpretation.

**Typical causes**

- conflicting reviewer claims
- unresolved policy interpretation disagreements
- contested provenance continuity assertions

**Recommended user interpretation**

Treat as unresolved trust state pending dispute workflow outcomes.

**Limitations**

Does not imply automatic invalidity or automatic acceptance while dispute remains unresolved.

**Human-supervised review guidance**

Route through documented dispute review workflows with explicit reviewer accountability.

### UNVERIFIED

**Meaning**

Insufficient verification evidence is available in displayed scope to support a stronger trust result.

**Typical causes**

- missing required verification inputs
- unavailable provenance chain details
- absent validator review context

**Recommended user interpretation**

Treat as no meaningful trust conclusion yet.

**Limitations**

Should not be reframed as either positive or negative certainty.

**Human-supervised review guidance**

Gather missing evidence, then re-run human-supervised validation using documented workflows.

## Related References
- `docs/mvp-1-viewer-implementation-plan.md`

- `docs/verification-status-ux.md`
- `docs/provenance-timeline-format.md`
- `docs/replay-warning-standard.md`
- `docs/trust-ux-principles.md`
- `docs/verification-map.md`
