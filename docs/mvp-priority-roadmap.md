# HC-TRUST-LAYER HC:// MVP Priority Roadmap

## Purpose

This roadmap defines MVP interaction-layer priorities for HC-TRUST-LAYER and HC:// with a simplicity-first, mobile-first, documentation-only scope.

## Priority Order

### 1) Verification package viewer

- **Purpose:** Provide first-line visibility into package identity, canonical record linkage, provenance, audit trail references, and verification context.
- **Minimum usable scope:** Open a package reference, show key metadata, show visible outcome states, and surface escalation guidance for uncertain outcomes.
- **Mobile-first considerations:** Single-column summary, collapsible details, clear status chips, and low-scroll critical evidence panel.
- **Simplicity goals:** Present core trust signals first and defer advanced detail unless requested.

### 2) Provenance timeline

- **Purpose:** Help users understand provenance continuity and change history in chronological form.
- **Minimum usable scope:** Show ordered provenance events, revision/supersession markers, and visible continuity-gap warnings.
- **Mobile-first considerations:** Vertical timeline cards, compact timestamps, and one-tap event expansion.
- **Simplicity goals:** Emphasize sequence and continuity before deep metadata.

### 3) Replay warning visibility

- **Purpose:** Make suspicious payload/hash reuse signals explicit for safer interpretation.
- **Minimum usable scope:** Show warning indicator, short explanation, and unresolved-state escalation guidance.
- **Mobile-first considerations:** Persistent warning banner and concise context drawer.
- **Simplicity goals:** Use direct caution language and avoid overloaded threat terminology.

### 4) Validator visibility

- **Purpose:** Expose validator review context without implying absolute authority.
- **Minimum usable scope:** Show validator identity reference, timestamp, outcome category, and rationale pointer when available.
- **Mobile-first considerations:** Compact validator cards with expandable rationale blocks.
- **Simplicity goals:** Keep `PASS`/`WARNING`/`FAIL`/`UNKNOWN` labels readable and standardized.

### 5) Trust result card

- **Purpose:** Provide a concise trust interpretation snapshot tied to visible evidence.
- **Minimum usable scope:** Show outcome summary, confidence framing language, evidence links, and escalation reminder.
- **Mobile-first considerations:** Sticky top summary card with quick jump to evidence sections.
- **Simplicity goals:** Avoid score over-complexity and prioritize plain-language interpretation.

### 6) QR verification flow

- **Purpose:** Support quick entry into verification context through HC:// QR payloads.
- **Minimum usable scope:** Accept QR input, resolve record context, and route to verification package and provenance summary.
- **Mobile-first considerations:** Camera-first flow, fallback text input, and immediate parsing feedback.
- **Simplicity goals:** Reduce steps between scan and core verification evidence.

### 7) Verification explorer

- **Purpose:** Offer navigable exploration across canonical record, package, provenance, and audit trail surfaces.
- **Minimum usable scope:** Search by record identifier/hash/package reference and open linked evidence views.
- **Mobile-first considerations:** Progressive disclosure navigation and lightweight search results.
- **Simplicity goals:** Keep exploration deterministic and evidence-linked rather than feature-dense.

### 8) Trust graph viewer

- **Purpose:** Visualize trust-relevant relationships as a later MVP extension after core comprehension tools stabilize.
- **Minimum usable scope:** Render basic nodes/edges for provenance and validator relationships with clear legend and boundary notes.
- **Mobile-first considerations:** Simplified graph mode, focus-node view, and non-graph fallback list.
- **Simplicity goals:** Use graph visuals only when they improve comprehension over linear views.

## Implementation Discipline

This roadmap is documentation guidance only and preserves existing trust-kernel boundaries:

- no runtime behavior changes
- no schema changes
- no validator changes
- no workflow/policy gate changes

## Related References

- `docs/core-stabilization-plan.md`
- `docs/trust-ux-principles.md`
- `docs/mvp-1-verification-package-viewer.md`
- `docs/verification-explorer-architecture.md`
