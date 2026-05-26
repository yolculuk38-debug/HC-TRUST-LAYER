# Verified AI Validator and Automation Disclosure Model

This document defines how HC:// and HC-TRUST-LAYER distinguish verified AI-assisted analysis from fake or unverifiable AI claims.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.

## Purpose

Provide clear disclosure language and anti-spoof boundaries so operators and reviewers can evaluate whether AI-related analysis is traceable, reviewable, and safely interpreted.

## Core definitions

### verified AI validator

A **verified AI validator** is a documented AI-assisted analysis component whose identity and execution context are traceable through a validator trace.

Minimum characteristics:

- The validator identity is explicitly named and scoped.
- Execution context is linked to a reviewable validator trace.
- Model/provider/version are disclosed where possible.
- Output remains advisory and non-authoritative.

### unverified AI claim

An **unverified AI claim** is any statement implying AI validation without sufficient traceability evidence.

Examples:

- "AI checked" with no validator identity.
- Model claim with no provider/version context.
- Approval language with no validator trace.

### automated analysis

**Automated analysis** is machine-generated inspection output that supports review routing, continuity checks, or summarization.

Automated analysis in HC:// is support material, not a canonical truth verdict and not autonomous authority.

### AI-assisted review

**AI-assisted review** is a review flow where AI output helps human reviewers inspect provenance, continuity, and audit trail context.

AI-assisted review can improve speed and consistency, but does not remove review accountability.

### human-reviewed analysis

**Human-reviewed analysis** is analysis that includes explicit human-supervised validation before consequential interpretation or decision use.

Human-reviewed analysis remains required for consequential decisions in HC-TRUST-LAYER.

### validator trace

A **validator trace** is a reviewable evidence path for an AI-assisted validator run.

A validator trace should include, when available:

- validator identifier and run context
- timestamp and scope summary
- provider and model disclosure
- model version or release identifier (if available)
- artifact/reference pointer for audit trail continuity

## Disclosure and interpretation rules

### "AI checked" is not enough

"AI checked" alone is insufficient because it provides no auditable identity, no traceability, and no reviewer-verifiable execution context.

Use explicit state labeling and validator trace references instead of authority-like shorthand.

### AI validator identity must be traceable

AI validator statements must be tied to a specific validator identity and a validator trace pointer so reviewers can inspect provenance and audit trail continuity.

### Model/provider/version disclosure should be provided where possible

When the workflow can disclose model details safely, include provider, model name, and version/release metadata.

If any field is unavailable, mark it as unavailable instead of implying certainty.

### Output remains advisory

AI-assisted analysis output in HC:// remains advisory-only and cannot be treated as autonomous final authority.

### Human review remains required for consequential decisions

Consequential decisions require human-supervised validation, regardless of whether AI-assisted analysis is present.

## Fake-AI misuse risks

HC-TRUST-LAYER reviewers should treat the following as high-risk misuse patterns:

1. **fake AI approval badge**
   - Visual badge implies verified approval with no validator trace.
2. **fake validator name**
   - Claimed validator identity cannot be tied to repository-defined or reviewer-recognized evidence.
3. **unverifiable model claim**
   - Claimed model/provider/version cannot be substantiated through disclosed trace context.
4. **copied AI report**
   - Report text reused from unrelated context and presented as current analysis.
5. **manipulated analysis output**
   - AI output edited to change meaning without transparent disclosure or provenance continuity.

## Safe signal examples

Use these explicit signals in UI, reports, or review summaries:

- `AI-ASSISTED REVIEW`
- `VERIFIED AI VALIDATOR`
- `UNVERIFIED AI CLAIM`
- `HUMAN REVIEW REQUIRED`
- `VALIDATOR TRACE AVAILABLE`

Signal usage notes:

- Pair each signal with one sentence of meaning and one sentence of limitation.
- Never present signals as truth guarantees, autonomous authority, or forensic certainty.
- Keep advisory-only and human-supervised validation notices persistently visible.

## Implementation notes

- This model does not modify canonical records, schema contracts, validator logic, signing semantics, federation behavior, or policy evaluator behavior.
- This model standardizes disclosure language for review safety, anti-spoof posture, and audit trail clarity.

## Related documents


- `docs/accountability-defense-layer.md`
- `docs/verification-result-states.md`
- `docs/visual-verification-signals.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/public-verification-boundaries.md`
- `docs/authenticated-ai-validator-access.md`
- `docs/federated-oversight-model.md`
- `docs/public-verification-disputes.md`
