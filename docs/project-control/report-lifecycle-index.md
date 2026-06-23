# Report lifecycle index

## Purpose

This index prevents blind deletion of HC-TRUST-LAYER audit, review, readiness, and report documents. It gives each report a lifecycle state so reviewers can preserve evidence, understand review boundaries, and decide whether future cleanup should retain, archive, supersede, or separately evaluate a document.

The index is advisory. It does not delete, move, rename, or replace any report, and it does not create governance authority or approval authority.

## Report lifecycle states

- **active**: Currently used for project-control, review, readiness, source evaluation, or operator decision support.
- **reference**: Preserved as audit, release, signoff, governance, security, or historical review evidence.
- **superseded**: Replaced by a newer report or decision record, while retained for evidence continuity unless a separate human-approved cleanup PR states otherwise.
- **archiveable**: Candidate for archive/stub treatment because it is duplicate, noisy, or no longer part of an active navigation surface; archival requires a separate scoped PR.
- **obsolete**: No longer reflects current repository state and should not guide decisions without a newer source, but may still be kept as historical evidence.
- **delete-candidate**: Candidate for deletion only after explicit separate human approval in a dedicated PR. This state is not approval to delete.

## Decision rules

- Audit evidence is not deleted by default.
- Release, signoff, security, and governance reports are kept unless explicitly superseded.
- External-source reports must keep source and evidence gap notes so reviewers can distinguish repository evidence from outside-source claims.
- Duplicate or noise reports may become archiveable after review.
- Delete-candidate status requires a separate human approval PR before removal.
- Generated artifacts are not canonical reports unless explicitly marked as canonical report evidence.
- No report is deleted from this PR.

## Initial report groups

This initial index is non-exhaustive and conservative. It is intended to make future cleanup safer, not to finalize report disposition.

### External / source-derived reports

- `docs/project-control/source-roadmap-evaluation-2026-06-23.md`
- `docs/project-control/external-audit-triage.md`
- `docs/project-control/external-audit-followup-status.md`

### Navigation / cleanup / repository organization reports

- `docs/project-control/public-navigation-audit.md`
- `docs/project-control/repository-cleanup-audit-2026-06-15.md`
- `docs/project-control/workflow-run-noise-audit-2026-06-16.md`
- `docs/project-control/public-explorer-planning-gap-review.md`

### Release / readiness / migration reviews

- `docs/governance/v0.1.0-tag-readiness-review.md`
- `docs/governance/v0.1.0-final-readiness-review.md`
- `docs/governance/v0.1.0-release-signoff-review.md`
- `docs/governance/archive-migration-readiness-review.md`
- `docs/project-control/public-validator-mvp-readiness-review.md`

### Runtime / telemetry / workflow security reviews

- `docs/runtime/runtime-stabilization-review.md`
- `docs/runtime/telemetry-contract-coverage-review.md`
- `docs/workflow-security-review.md`
- `docs/runtime/production-readiness-checklist.md`

### Operating layer / governance evidence reviews

- `docs/project-control/hc-operating-layer-review.md`
- `docs/project-control/generated-governance-evidence-artifacts-review.md`
- `docs/project-control/governance-evidence-review-checklist.md`
- `docs/project-control/shift-change-checklist.md`

## Initial lifecycle table

| Report | Type | Current lifecycle state | Evidence / source pointer | Decision impact | Next action |
| --- | --- | --- | --- | --- | --- |
| `docs/project-control/source-roadmap-evaluation-2026-06-23.md` | External / source-derived | active | Current source-roadmap evaluation and gap notes | Supports source-roadmap follow-up without treating external material as repository truth | Keep active; update only through separate scoped review |
| `docs/project-control/external-audit-triage.md` | External / source-derived | reference | External audit triage notes | Preserves external-source review context and evidence gaps | Keep as reference unless explicitly superseded |
| `docs/project-control/external-audit-followup-status.md` | External / source-derived | reference | External audit follow-up status | Preserves follow-up state and unresolved-source boundaries | Keep as reference; classify superseded only with newer follow-up |
| `docs/project-control/public-navigation-audit.md` | Navigation / cleanup | archiveable | Navigation audit report | May inform future navigation cleanup without requiring deletion | Review for archive/stub PR if no active navigation surface depends on it |
| `docs/project-control/repository-cleanup-audit-2026-06-15.md` | Navigation / cleanup | archiveable | Repository cleanup audit report | May identify duplicate or historical cleanup findings | Review for archive/stub PR; do not delete in this PR |
| `docs/project-control/workflow-run-noise-audit-2026-06-16.md` | Navigation / cleanup | archiveable | Workflow run noise audit report | May inform workflow-noise cleanup history | Review for archive/stub PR; keep evidence trail |
| `docs/project-control/public-explorer-planning-gap-review.md` | Navigation / cleanup | archiveable | Public Explorer planning gap review | May support planning history and gap tracking | Review before archiving; keep if still cited by active planning |
| `docs/governance/v0.1.0-tag-readiness-review.md` | Release / readiness | reference | v0.1.0 tag readiness evidence | Preserves release-readiness review context | Keep unless explicitly superseded by release governance review |
| `docs/governance/v0.1.0-final-readiness-review.md` | Release / readiness | reference | v0.1.0 final readiness evidence | Preserves release-readiness decision support | Keep as release evidence |
| `docs/governance/v0.1.0-release-signoff-review.md` | Release / signoff | reference | v0.1.0 signoff review evidence | Preserves signoff boundary and human-review context | Keep as signoff reference |
| `docs/governance/archive-migration-readiness-review.md` | Migration / readiness | reference | Archive migration readiness review | Preserves migration readiness context | Keep unless newer migration review explicitly supersedes it |
| `docs/project-control/public-validator-mvp-readiness-review.md` | Readiness / MVP | active/reference | Public validator MVP readiness review | Supports current readiness and future MVP review boundaries | Keep active/reference; update only through scoped readiness review |
| `docs/runtime/runtime-stabilization-review.md` | Runtime review | reference | Runtime stabilization review | Preserves runtime stabilization evidence and limits | Keep as reference |
| `docs/runtime/telemetry-contract-coverage-review.md` | Telemetry review | reference | Telemetry contract coverage review | Preserves telemetry coverage review context | Keep as reference |
| `docs/workflow-security-review.md` | Workflow security review | reference | Workflow security review | Preserves security review evidence and boundaries | Keep as security reference |
| `docs/runtime/production-readiness-checklist.md` | Runtime readiness checklist | reference | Runtime checklist and readiness notes | Preserves readiness checklist without implying production guarantee | Keep as reference; avoid overstating capability |
| `docs/project-control/hc-operating-layer-review.md` | Operating layer review | reference | HC Operating Layer review | Preserves operating-layer review context | Keep as reference |
| `docs/project-control/generated-governance-evidence-artifacts-review.md` | Governance evidence review | reference | Generated governance evidence artifact review | Preserves evidence-artifact review boundaries | Keep as reference; generated artifacts are not canonical unless marked |
| `docs/project-control/governance-evidence-review-checklist.md` | Governance evidence checklist | reference | Governance evidence checklist | Supports human-supervised governance evidence review | Keep as reference |
| `docs/project-control/shift-change-checklist.md` | Operating layer checklist | reference | Shift-change checklist | Supports handoff continuity and operator review | Keep as reference |

## Cleanup process

1. Index reports.
2. Classify lifecycle state.
3. Open a separate archive/stub PR for archiveable reports.
4. Never delete audit-significant reports without explicit human approval.
5. Keep a redirect or stub when removing an active navigation surface.

advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false except this docs-only index
approval_authority=false
merge_authority=false
