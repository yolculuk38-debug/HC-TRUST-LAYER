# HC-TRUST-LAYER HC:// MVP-1 Verification Package Viewer Specification

## Status

- static frontend implementation available in `docs/verification-viewer.html`
- local JSON package parsing implemented in-browser for demo interpretation
- no backend workflow changes
- no schema or validator logic changes
- no production readiness claim
- no automatic trust decisions

## MVP-1 Overview

MVP-1 defines the first small working HC:// verification experience for viewing and understanding verification packages.

The MVP-1 surface is focused on transparent evidence reading, provenance continuity awareness, replay warning visibility, validator review visibility, and audit trail-linked trust snapshot interpretation.

MVP-1 is an interpretive view layer and does not alter trust kernel behavior.

## Minimal Verification Experience

MVP-1 should provide a minimal, public-readable package inspection flow:

1. open a verification package
2. inspect package identity and canonical record linkage
3. review hash verification visibility
4. review provenance continuity visibility
5. review validator review status visibility
6. inspect replay/dispute indicators
7. inspect trust snapshot context
8. inspect audit trail references
9. escalate uncertain outcomes to human-supervised validation

## Upload/Open Verification Package Flow

MVP-1 package access concepts:

- open package by file upload or package reference
- show package identifier and package version metadata
- show canonical record linkage fields used for package context
- show package scope boundaries (included evidence vs missing evidence)
- show non-parsed fallback state when package content cannot be interpreted in this phase

In MVP-1, local package parsing is available in a static HTML/JS viewer and remains advisory.
This behavior should not imply runtime trust-kernel guarantees.

## Hash Verification Visibility

MVP-1 hash visibility should include:

- presented hash values in package metadata
- hash-to-canonical-record linkage status labels
- explicit mismatch/unknown states
- timestamp context for the last visible hash verification event

Hash visibility is a verification signal, not an automatic truth guarantee.

## Provenance Visibility

MVP-1 provenance visibility should include:

- provenance event summary for package-covered records
- continuity markers between origin/revision/supersession references
- unknown-gap indicators when provenance chain continuity is incomplete
- links to provenance and canonical record references

## Validator Visibility

MVP-1 validator visibility should include:

- validator identity references
- validator review timestamps
- outcome category labels (`PASS`, `WARNING`, `FAIL`, `UNKNOWN`)
- validator evidence or rationale pointers when available

Validator visibility is advisory context and does not replace human-supervised validation.

## Replay Warning Visibility

MVP-1 replay visibility should include:

- replay warning indicator when repeated payload/hash reuse appears across conflicting provenance contexts
- clear caution language for suspicious reuse patterns
- unresolved-state marker requiring human-supervised validation

## Dispute Indicator Visibility

MVP-1 dispute visibility should include:

- disputed canonical record indicator
- dispute state summary label (open/resolved/unknown)
- pointer to dispute-related provenance and audit trail entries

## Trust Snapshot Visibility

MVP-1 trust snapshot visibility should include:

- snapshot timestamp
- snapshot scope summary
- package-to-snapshot linkage state
- drift note when newer provenance or audit trail entries exist beyond the snapshot

## Audit Trail Visibility

MVP-1 audit trail visibility should include:

- append-oriented event list reference
- verification/provenance/review event category labels
- actor and validator linkage hints
- continuity note for missing or delayed audit entries

## Simplicity-First UX Goals

MVP-1 UX goals:

- keep verification concepts visible without requiring deep protocol expertise
- preserve HC-TRUST-LAYER and HC:// canonical terminology
- use short plain-language labels before advanced details
- separate verification evidence from interpretation hints
- emphasize escalation to human-supervised validation for uncertain/high-impact outcomes

## Boundaries

- no automatic truth guarantee
- no forensic certainty claims
- no legal certification claims
- no political authority claims
- provenance and verification focus only
- local processing only (no server upload path in static viewer)
- fail safely on invalid JSON package content

## Related Foundations
- `docs/mvp-1-viewer-implementation-plan.md`

- `docs/mvp-1-user-flow.md`
- `docs/mvp-1-ui-principles.md`
- `docs/mvp-1-boundaries.md`
- `docs/verification-explorer-architecture.md`
- `docs/provenance-viewer.md`
- `docs/public-verification-flow.md`

- `docs/core-stabilization-plan.md`
- `docs/mvp-priority-roadmap.md`
- `docs/trust-ux-principles.md`
- `docs/architecture-consolidation.md`

## Related References

- `docs/trust-result-standard.md`
- `docs/verification-status-ux.md`
- `docs/provenance-timeline-format.md`
- `docs/replay-warning-standard.md`
- `docs/demo-index.md`
- `docs/mvp-1-cli-viewer.md`
- `docs/static-viewer.md`
- `docs/verification-viewer.html`
