# Public Validator MVP Implementation Plan

> **Mode:** DOCUMENTATION ONLY  
> **Scope:** Public Validator MVP implementation plan for presenting HC:// verification results to public users while preserving advisory-only trust semantics.  
> **Boundary:** This plan does not modify runtime, schema, validators, workflows, records, signing, federation, policy, or GitHub Actions. It does not add production claims or autonomous decision making.

## Executive Summary

The Public Validator MVP should provide a small, mobile-readable path for public users to inspect HC:// record verification signals. The MVP presents available evidence, warnings, provenance, source chain, responsibility chain, and QR integrity signals without converting those signals into final truth, legal certification, safety certification, or autonomous governance outcomes.

Every result must preserve the required public posture:

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

The first implementation should remain local-first and documentation-led where possible. A backend, persistent account system, live federation dependency, or autonomous enforcement surface should remain out of scope unless explicitly approved in a later PR.

## Goals

- Define a clear Public Validator MVP user flow for HC:// records and verification packages.
- Make missing evidence, conflicting evidence, warnings, and human review status visible in every result.
- Preserve advisory-only semantics for all public-facing result language.
- Support public-safe display of `chain_of_custody`, `batch_id`, `lot_id`, and `sample_id` when present.
- Identify future API integration points without requiring backend implementation in the MVP.

## Non-Goals

The Public Validator MVP must not:

- modify runtime, schema, validators, workflows, records, signing, federation, policy, or GitHub Actions;
- create production-readiness, legal, safety, forensic certainty, ministry approval, or enforcement claims;
- decide whether a record is objectively true;
- approve, reject, archive, sign, federate, or mutate HC:// records;
- hide missing evidence or conflicting evidence;
- replace human-supervised validation;
- add autonomous decision making.

## Required Result Semantics

Every public result must carry these visible fields or labels:

| Field | Required MVP value | Display requirement |
| --- | --- | --- |
| `advisory_only` | `true` | Show that the output is advisory and supports reviewer judgment. |
| `public_safe` | `true` | Show that the result excludes non-public or restricted details. |
| `truth_guarantee` | `false` | Show that the result is not a final truth claim. |
| `human_review_required` | `true` | Show a visible human-review reminder in the result header and detail view. |

The result must also expose these state containers, even when empty:

- `warnings`
- `missing_evidence`
- `conflicting_evidence`
- `provenance`
- `source_chain`
- `responsibility_chain`
- `evidence`
- `chain_of_custody`
- `batch_id`
- `lot_id`
- `sample_id`

## Validator User Flow

1. User opens the Public Validator MVP surface from a public link, local demo, or future HC:// Control Panel entry point.
2. User selects one input path:
   - paste an HC:// record identifier;
   - paste a public-safe canonical URL;
   - scan or paste a QR payload;
   - load a local verification package;
   - use a bundled public-safe example.
3. MVP explains that the input is untrusted until checked.
4. MVP runs only approved public-safe checks available in the local environment or explicitly approved integration.
5. MVP returns a compact result summary with advisory-only posture flags.
6. User expands detail sections for provenance, source chain, responsibility chain, evidence, and warnings.
7. User escalates any consequential, incomplete, disputed, conflicting, or ambiguous result to human review.

## Record Lookup Flow

The lookup flow should identify the candidate record boundary without mutating repository state.

1. Normalize input into one of these lookup keys:
   - `record_id`
   - `canonical_url`
   - `qr_payload`
   - `verification_package_id`
   - local package path or uploaded package object
2. Validate input shape and reject malformed payloads with a visible warning.
3. Resolve a candidate public-safe record or verification package reference.
4. Display lookup confidence separately from verification status.
5. If no record is found, return `MISSING` or `UNKNOWN` with `human_review_required=true`.
6. If multiple candidate records are found, return `NEEDS_REVIEW` and list the ambiguity without choosing an autonomous winner.

Recommended lookup states:

| State | Meaning |
| --- | --- |
| `FOUND` | One candidate public-safe record or package boundary was found. |
| `NOT_FOUND` | No matching public-safe record or package boundary was found. |
| `AMBIGUOUS` | More than one candidate boundary may match. |
| `MALFORMED_INPUT` | Input cannot be parsed safely. |
| `UNSUPPORTED_INPUT` | Input type is outside the MVP scope. |

## Verification Result Flow

The MVP should separate check execution from public interpretation.

```text
input
→ lookup state
→ available public-safe checks
→ evidence and warning aggregation
→ advisory result summary
→ human-review checkpoint
```

Recommended top-level statuses:

| Status | Public meaning |
| --- | --- |
| `PASS` | Available MVP checks passed within their limited scope only. |
| `WARNING` | One or more warnings require attention. |
| `FAIL` | A supplied value conflicts with an implemented check. |
| `PARTIAL` | Some evidence exists, but expected evidence is incomplete. |
| `MISSING` | Required or expected public-safe evidence is absent. |
| `NEEDS_REVIEW` | Human review is required before relying on the result. |
| `UNKNOWN` | The MVP cannot determine a public-safe result. |

The summary card should show:

- overall status;
- `advisory_only=true`;
- `public_safe=true`;
- `truth_guarantee=false`;
- `human_review_required=true`;
- lookup state;
- evidence count;
- warning count;
- missing evidence count;
- conflicting evidence count.

## Warnings Model

Warnings must be visible, user-readable, and structured enough for later API reuse.

Recommended warning fields:

```yaml
warnings:
  - code: string
    severity: INFO | WARNING | REVIEW_REQUIRED | BLOCKED
    message: string
    affected_section: lookup | schema | hash | provenance | source_chain | responsibility_chain | evidence | qr | custody | api
    human_review_required: true
```

Required warning categories:

- missing evidence;
- conflicting evidence;
- malformed input;
- ambiguous lookup;
- unsupported input;
- hash mismatch or unavailable hash;
- provenance gap;
- source chain gap;
- responsibility chain gap;
- chain-of-custody gap;
- QR payload mismatch;
- non-public or redacted evidence reference;
- stale or incomplete verification package.

Warning language should explain what was observed and what remains unresolved. It must not present advisory signals as final truth.

## Provenance Display Model

The provenance section should answer: where did this record or package come from, and what public-safe references support that path?

Display fields:

| Field | Purpose |
| --- | --- |
| `record_id` | HC:// record identifier or public-safe record reference. |
| `record_type` | Declared record or package type when available. |
| `created_at` | Declared creation timestamp when public-safe. |
| `updated_at` | Declared update timestamp when public-safe. |
| `provenance_status` | Public-safe provenance check state. |
| `provenance_links` | Public-safe upstream or related references. |
| `missing_evidence` | Explicit list of expected but absent provenance support. |
| `conflicting_evidence` | Explicit list of conflicting provenance claims or values. |

If provenance cannot be checked, the MVP should state that the provenance signal is unavailable and keep `human_review_required=true` visible.

## Source Chain Display

The source chain display should show public-safe upstream evidence in order from source to presented result.

Recommended display order:

1. originating source or declared issuer;
2. source document, record, sample, or package reference;
3. intermediate derived artifact or verification package reference;
4. validator input boundary;
5. public advisory result.

Each source-chain item should include:

- label;
- public-safe identifier;
- relationship to the next item;
- hash or integrity status when available;
- evidence status;
- warning count;
- human-review note when incomplete.

Generated, derived, or exported artifacts must be labeled as derived and must not be elevated above canonical HC:// record boundaries.

## Responsibility Chain Display

The responsibility chain should show who is declared to have created, submitted, reviewed, approved, witnessed, or accepted responsibility for the record or package when those fields are public-safe.

Recommended fields:

| Field | Meaning |
| --- | --- |
| `role` | Creator, submitter, reviewer, approver, witness, custodian, operator, or other declared role. |
| `entity` | Public-safe person, organization, system, or role label. |
| `declared_at` | Timestamp or period when available. |
| `responsibility_scope` | What the entity is responsible for within the record boundary. |
| `evidence_ref` | Public-safe evidence reference supporting the responsibility claim. |
| `status` | `PRESENT`, `MISSING`, `CONFLICTING`, `REDACTED`, or `UNKNOWN`. |

The MVP must not infer authority beyond declared evidence. Missing reviewer, approver, witness, or custodian information should remain visible.

## Evidence Display

The evidence panel should be simple enough for mobile use while preserving auditability.

Required evidence grouping:

- **Presented evidence:** public-safe evidence available to inspect.
- **Missing evidence:** expected evidence that is absent or not publicly available.
- **Conflicting evidence:** public-safe values or references that disagree.
- **Redacted or restricted evidence:** evidence known to exist but not displayable publicly, if such a signal is available.
- **Not checked:** checks outside the MVP scope.

Recommended evidence item fields:

```yaml
evidence:
  - evidence_id: string | null
    evidence_type: string
    public_safe: true
    reference: string | null
    hash_status: PASS | WARNING | FAIL | PARTIAL | MISSING | UNKNOWN
    provenance_status: PASS | WARNING | FAIL | PARTIAL | MISSING | UNKNOWN
    display_status: PRESENT | MISSING | CONFLICTING | REDACTED | NOT_CHECKED | UNKNOWN
    human_review_required: true
```

The display should avoid long technical blocks by default. A details expansion may show raw public-safe fields, hashes, or package metadata.

## Chain-of-Custody Support

The MVP should reserve a dedicated `chain_of_custody` section for custody events when the record or package provides them.

Recommended event fields:

| Field | Purpose |
| --- | --- |
| `custody_event_id` | Public-safe event identifier when available. |
| `actor` | Declared custodian, reviewer, system, or role. |
| `action` | Declared custody action. |
| `occurred_at` | Declared event time when public-safe. |
| `from` | Prior custodian or boundary when available. |
| `to` | Next custodian or boundary when available. |
| `evidence_ref` | Public-safe support for the custody event. |
| `status` | `PRESENT`, `MISSING`, `CONFLICTING`, `PARTIAL`, or `UNKNOWN`. |

Custody gaps should create visible warnings and should not be auto-resolved.

## Batch, Lot, and Sample Support

When available, the MVP should display these identifiers in a compact traceability block:

```yaml
traceability:
  batch_id: string | null
  lot_id: string | null
  sample_id: string | null
```

Display rules:

- Show `batch_id`, `lot_id`, and `sample_id` exactly as public-safe record data provides them.
- Do not invent or normalize identifiers into new authority claims.
- If an identifier is expected but missing, add a missing-evidence warning.
- If identifiers conflict across evidence, add a conflicting-evidence warning.
- Keep traceability separate from final result status so users do not mistake identifier presence for proof of truth.

## QR Verification Flow

The QR flow should prioritize user safety and clear escalation.

1. User scans or pastes a QR payload.
2. MVP decodes the payload locally when possible.
3. MVP identifies whether the QR payload contains a supported HC:// record reference, canonical URL, package reference, or unsupported payload.
4. MVP compares the decoded payload against the resolved record or package boundary when available.
5. MVP shows `qr_integrity` separately from overall status.
6. MVP warns on unsupported, malformed, ambiguous, mismatched, replay-like, or generic marketing links.
7. MVP keeps `human_review_required=true` visible for every QR result.

Recommended QR states:

| State | Meaning |
| --- | --- |
| `PASS` | QR payload matches the implemented public-safe check scope. |
| `WARNING` | QR payload has a concern but may still contain useful information. |
| `FAIL` | QR payload conflicts with the resolved record or package boundary. |
| `PARTIAL` | QR payload is readable but lacks expected verification fields. |
| `MISSING` | QR evidence expected by the record is absent. |
| `NOT_PROVIDED` | No QR payload was submitted. |
| `UNKNOWN` | QR state cannot be determined safely. |

QR status must not be presented as a standalone truth result.

## Future API Integration Points

The MVP should reserve integration seams without requiring a backend in the first implementation.

Potential future endpoints or adapters:

| Integration point | Purpose | MVP stance |
| --- | --- | --- |
| `GET /public-validator/records/{record_id}` | Resolve a public-safe record summary. | Future adapter only. |
| `POST /public-validator/verify` | Submit a public-safe record, package, URL, or QR payload for advisory verification. | Future adapter only. |
| `GET /public-validator/packages/{package_id}` | Resolve a public-safe verification package summary. | Future adapter only. |
| `POST /public-validator/qr` | Decode and inspect a QR payload. | Future adapter only; local decode preferred first. |
| `GET /public-validator/evidence/{evidence_id}` | Fetch public-safe evidence metadata. | Future adapter only; must preserve evidence boundaries. |
| `GET /public-validator/chain-of-custody/{record_id}` | Fetch public-safe custody event summaries. | Future adapter only. |

Future API responses should reuse the same required posture fields and containers:

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
warnings: []
missing_evidence: []
conflicting_evidence: []
source_chain: []
responsibility_chain: []
evidence: []
chain_of_custody: []
batch_id: null
lot_id: null
sample_id: null
```

Any future API work should be reviewed separately for privacy, rate limiting, public-safe redaction, audit logging, replay handling, and abuse-risk warnings.

## Implementation Phases

### Phase 1: Documentation-led MVP

- Publish this implementation plan.
- Reuse the existing Public Validator MVP specification and readiness review as planning inputs.
- Select demo-safe examples for future UI or local helper work.
- Keep all changes outside runtime, schema, validators, workflows, records, signing, federation, and policy.

### Phase 2: Local UI or CLI Adapter

- Build a local-only input-to-result path using existing approved helpers.
- Display required posture fields and warning containers.
- Prefer mobile-readable cards and expandable details.
- Avoid backend dependency unless separately approved.

### Phase 3: Public-Safe API Adapter

- Add API integration only through a separate scoped PR.
- Preserve the same result contract and warnings model.
- Add explicit privacy, redaction, replay, and rate-limit review before public deployment.

## Review and Validation Checklist

Before implementation PRs proceed, reviewers should confirm:

- `advisory_only=true` is visible in every result.
- `public_safe=true` is visible in every result.
- `truth_guarantee=false` is visible in every result.
- `human_review_required=true` is visible in every result.
- Missing evidence is visible.
- Conflicting evidence is visible.
- `chain_of_custody` is supported as a visible section.
- `batch_id`, `lot_id`, and `sample_id` are supported as visible traceability fields.
- QR status is separate from overall status.
- Source chain and responsibility chain are visible and do not create authority beyond evidence.
- No runtime, schema, validator, workflow, record, signing, federation, or policy path is modified by this planning PR.
- No production, final truth, forensic certainty, autonomous governance, or enforcement claim is introduced.

## Open Questions for Later PRs

- Which bundled example should become the first public-safe demo input?
- Should the first local MVP be a static page, CLI command, or HC:// Control Panel panel?
- Which existing helper should own response shaping if code is later added?
- What public-safe redaction rules are required before any API adapter is exposed?
- What replay, rate-limit, and abuse-warning language should appear in public UI copy?

## PR #639 Scope Statement

PR #639 is limited to adding this documentation-only implementation plan. It intentionally does not change runtime behavior, canonical records, schemas, validators, workflows, signing logic, federation logic, security workflows, policy files, or GitHub Actions.
