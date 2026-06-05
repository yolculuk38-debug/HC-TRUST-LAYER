# Mini Public Validator Demo Guide

> **Status:** demo / explanatory guide  
> **Scope:** documentation-only public verification walkthrough  
> **Authority:** advisory-only; human review remains final  
> **Production readiness:** not claimed

This guide shows one small, visible HC:// verification flow for new visitors who want to understand what HC-TRUST-LAYER can currently explain without reading the full governance or runtime documentation first.

The demo is intentionally narrow. It describes how a public-safe validator result can present record-shape, hash/provenance, and review-boundary signals without claiming production readiness, objective truth verification, forensic certainty, autonomous finality, or governance approval.

## Quick Flow

```text
HC record
→ validation
→ hash/provenance checks where applicable
→ advisory result
→ human review reminder
```

## What a Visitor Should Understand

A visitor should be able to see that HC-TRUST-LAYER can organize an HC record review into visible steps:

1. **HC record** — the item under review has an identifier and expected record context.
2. **Validation** — available checks inspect whether the record appears to match an expected shape or schema boundary.
3. **Hash/provenance checks where applicable** — when hash or provenance material exists, checks may compare or surface those signals; when not available, the result stays `UNKNOWN` or `NOT_RUN`.
4. **Advisory result** — the output summarizes visible verification signals for review.
5. **Human review reminder** — a human reviewer remains responsible for final interpretation, escalation, and any real-world decision.

## Example Demo Input

Use a small demo record identity rather than a canonical repository record:

```yaml
record_id: HC-DEMO-2026-0001
record_type: public_validator_demo
purpose: explanatory_flow_only
```

This example is not a signed record, not a canonical record, and not a generated artifact. It exists only to explain the result shape.

## Example Result Shape

```yaml
record_id: HC-DEMO-2026-0001
schema: PASS / UNKNOWN / NOT_RUN
hash: PASS / UNKNOWN / NOT_RUN
status: VERIFIED / NEEDS_REVIEW / DEMO_ONLY
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
warnings: []
```

### Field Notes

- `record_id` identifies the demo review target.
- `schema` shows whether a schema or record-shape check passed, was unknown, or was not run.
- `hash` shows whether hash/provenance checks passed, were unknown, or were not run.
- `status` summarizes the demo output as a review signal, not a final authority.
- `advisory_only: true` preserves AI-assisted and tool-assisted output as advisory.
- `public_safe: true` means the example is suitable for public explanation and does not expose private evidence.
- `truth_guarantee: false` means the result does not prove objective truth.
- `human_review_required: true` preserves human final authority.
- `warnings` lists visible cautions when the demo detects missing, partial, or ambiguous signals.

## Demo Interpretation Rules

- `VERIFIED` means the visible checks in the demo scope are consistent enough to show a positive advisory signal.
- `NEEDS_REVIEW` means a human reviewer should inspect missing, partial, ambiguous, disputed, or high-impact context before relying on the result.
- `DEMO_ONLY` means the example exists for explanation and should not be treated as a live validation result.
- `UNKNOWN` means the demo does not have enough information to make that check meaningful.
- `NOT_RUN` means that check was not executed in the demo flow.

## What This Demo Does

- Shows a simple HC:// record-to-result explanation.
- Demonstrates public-safe status language with `public_safe: true`.
- Preserves `truth_guarantee: false` as an explicit boundary.
- Keeps AI, automation, and validator output advisory-only.
- Reminds visitors that human review remains required.

## What This Demo Does Not Claim

- No production readiness.
- No objective-truth finality.
- No forensic certainty.
- No autonomous governance finality.
- No signature, federation, policy, schema, validator, workflow, hash, QR, record, or generated-artifact change.
- No claim that a passing technical check proves the real-world truth of a record's contents.

## Human Review Reminder

HC-TRUST-LAYER helps expose integrity and provenance signals for review. It does not replace reviewer judgment.

A human reviewer must decide whether the record context, evidence quality, provenance continuity, and any warnings are sufficient for the intended use. High-impact, disputed, incomplete, or ambiguous results should be escalated through the appropriate governance and review process.

## Related Reading

Start with these existing repository references when moving beyond the mini demo:

- [Repository README](../../README.md)
- [Start Here](../START_HERE.md)
- [Runtime documentation](../runtime/)
- [Project control documentation](../project-control/)
- [Governance documentation](../governance/)

