# Source Advisory Placement Index

Status: advisory project-control index
Scope: documentation only
Issue: #1113
Authority: non-canonical, non-binding

This index records where source-advisory material should be placed before any
implementation, record, validator, signing, federation, schema, policy, or
canonical artifact change is proposed.

It preserves HC:// and HC-TRUST-LAYER terminology while keeping source-advisory
work public-safe, reviewable, and human-supervised.

## Boundary markers

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false
approval_authority=false
merge_authority=false
```

Source-advisory notes do not create legal truth, identity finality, forensic
certainty, certification authority, production readiness, autonomous governance
authority, or guaranteed correctness.

## Placement rules

| Source-advisory material | Preferred placement | Purpose | Do not place in |
| --- | --- | --- | --- |
| Maintainer-provided external summaries, screenshots, prompt notes, or uploaded-source summaries | `docs/project-control/` | Record an advisory project-control reference with clear evidence gaps and boundaries. | `records/`, `schema/`, `policy/`, `validators/`, `federation/`, `signatures/`, `canonical/`, `.github/workflows/` |
| Follow-up inventory findings that do not change runtime behavior | `docs/project-control/` | Preserve review status, affected paths, uncertainty, and recommended validation. | Protected paths or generated artifacts |
| Draft designs requiring later review | `docs/drafts/` or `docs/project-control/` | Separate proposals from active implementation and canonical records. | Runtime code, records, schemas, validators, signing, federation, or policy paths |
| Future-facing concepts that are not approved implementation work | `docs/future/` | Park long-term ideas without implying roadmap commitment. | Active protocol, runtime, or governance-control paths |
| Governance interpretation notes | `docs/governance/` only when governance scope is explicit | Explain review expectations without granting bot or agent authority. | Policy files or workflow enforcement paths unless explicitly requested |

## Required source-advisory fields

Each new source-advisory note should include:

- status and scope;
- issue or source pointer when available;
- authority boundary;
- evidence status and known gaps;
- affected paths, if any;
- what the note does not change;
- recommended next safe action;
- the boundary markers from this index.

## Review sequence

1. Inspect existing docs to avoid duplicate scope.
2. Place advisory material in the smallest suitable docs path.
3. Keep the note non-canonical unless a separate human-reviewed decision says otherwise.
4. Do not modify protected paths from source-advisory material alone.
5. Run docs validation before review.

## Protected-path reminder

Source-advisory placement must not modify or create authority over these paths
unless a later task explicitly requests it and the change receives the required
human-supervised review:

- `schema/**`
- `validators/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- `policy/**`
- `.github/workflows/**`
- `records/**`

## Related project-control references

- `docs/project-control/source-inventory-triage.md`
- `docs/project-control/source-inventory-review-checklist.md`
- `docs/project-control/source-roadmap-evaluation-2026-06-23.md`

## Next safe action

Use this index when converting future source-advisory material into small,
docs-only, reviewable PRs. Human final authority remains required before any
advisory note becomes implementation, governance control, canonical record, or
trust-kernel change.
