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
The static viewer implementation uses a simple timeline-style layout to group provenance events, validator reviews, replay indicators, dispute indicators, and audit snapshot context with plain-text section labels for mobile-readable interpretation.

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

Bundled demo permalink state is supported through URL hash values in `docs/verification-viewer.html`.
Recognized hashes (`verified-trace`, `partial-trace`, `replay-warning`, `disputed`, `unverified`) map to bundled demo packages so reviewers can share reproducible demo links.
Unknown hash values fail safely to a bundled fallback selection.

Local upload privacy boundary remains strict:

- uploaded local JSON content is not encoded in URL hash state
- uploaded local JSON content is not stored in browser local storage
- reset behavior returns to bundled demo state without exposing local uploaded data

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
Where validator review arrays are empty, the viewer shows an explicit empty-state message so missing review context is visible instead of implied.

## Replay Warning Visibility

MVP-1 replay visibility should include:

- replay warning indicator when repeated payload/hash reuse appears across conflicting provenance contexts
- clear caution language for suspicious reuse patterns
- unresolved-state marker requiring human-supervised validation
- advisory warning labels in the viewer when replay indicators are present

## Dispute Indicator Visibility

MVP-1 dispute visibility should include:

- disputed canonical record indicator
- dispute state summary label (open/resolved/unknown)
- pointer to dispute-related provenance and audit trail entries
- advisory warning labels when dispute indicators are present

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


## Package copy and download controls

The static viewer in `docs/verification-viewer.html` includes two local-only package actions:

- **Copy current package JSON** copies the currently displayed package JSON to the local clipboard.
- **Download current package JSON** downloads the currently displayed package JSON as a local `.json` file using a safe filename derived from `package_id`.

These controls work for both bundled example packages and locally uploaded JSON packages. They do not modify package content, do not upload data to any server, and require no backend services.

If no package is currently loaded, the viewer fails safely by showing a status message instead of attempting copy/download. Status messages are cleared automatically after action feedback to keep controls mobile-readable.

This behavior is demo-only and local-only, and does not alter HC:// trust-kernel behavior or canonical record semantics. Human-supervised validation remains required for consequential trust decisions.


## MVP-1 report output actions (static viewer)

The MVP-1 static viewer supports report output actions for bundled examples and local uploaded JSON:

- **Print report** for human-readable review and documentation sharing.
- **Export report summary (.txt)** for local text report capture.

Included report fields:

- package_id
- trust_result
- trust_confidence
- content_hash
- provenance summary
- replay indicators
- dispute indicators
- validator reviews
- audit snapshot
- human review required
- viewer warnings

Implementation boundaries:

- static HTML/JS only
- no backend
- no external dependencies
- local-only processing
- fail-safe behavior when no package is loaded

These actions do not change schema contracts, canonical record boundaries, trust-kernel behavior, or workflow policy. Human-supervised validation remains required.

## Raw structured field inspection (MVP-1)

MVP-1 includes a collapsible **Raw package fields** inspector in `docs/verification-viewer.html`.

Behavior coverage:

- works with bundled demo packages
- works with local uploaded JSON packages
- shows pretty-printed structured JSON
- includes a local **Copy raw JSON** control near the inspector
- preserves local-only behavior with no backend and no external dependencies
- preserves fail-safe no-package state messaging

Interpretation boundary:

- raw JSON is technical detail for transparent inspection only
- raw JSON display does not change schema contracts or canonical record boundaries
- raw JSON display does not modify package content, upload package content, or store local uploaded package content
- outputs remain advisory and require human-supervised validation
