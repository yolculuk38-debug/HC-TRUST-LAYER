# Archiveable report reference check - 2026-06-23

## Purpose

This document records a reference check before any archive, stub, or delete action for reports currently listed as archiveable cleanup candidates.

The purpose is to preserve review boundaries and prevent premature cleanup of reports that may still be referenced by active documentation, operator entrypoints, lifecycle indexes, or planning material.

## Method

The check should look for references from active documentation and project-control entrypoints, including but not limited to:

- `README.md`
- `docs/START_HERE.md`
- `docs/project-control/operator-entry-map.md`
- `docs/project-control/report-lifecycle-index.md`
- `docs/project-control/archiveable-report-cleanup-plan-2026-06-23.md`
- `docs/project-control/**`
- `docs/governance/**`
- `docs/runtime/**`

The check should preserve HC:// and HC-TRUST-LAYER terminology, avoid changing source reports, and treat audit-significant rationale as evidence-preserving material unless a later human-reviewed PR records a narrower disposition.

## Reference table

| Candidate report | Expected reference check scope | Current lifecycle state | Reference result | Risk if archived too early | Recommended next action |
| --- | --- | --- | --- | --- | --- |
| `docs/project-control/public-navigation-audit.md` | Active navigation, `README.md`, `docs/START_HERE.md`, operator maps, lifecycle indexes, project-control reports, governance docs, and runtime docs | Archiveable cleanup candidate | Reference-check required; do not archive until active navigation references are confirmed absent | May remove active navigation context or obscure prior public-entrypoint rationale | Complete reference check only; keep active until navigation references are confirmed absent |
| `docs/project-control/repository-cleanup-audit-2026-06-15.md` | Cleanup plans, lifecycle indexes, operator maps, project-control reports, governance docs, runtime docs, and repository maintenance references | Archiveable cleanup candidate | Reference-check required; do not archive until cleanup rationale is confirmed superseded | May obscure cleanup rationale, prior scope decisions, or audit context used by later project-control work | Complete reference check only; do not archive until cleanup rationale is confirmed superseded |
| `docs/project-control/workflow-run-noise-audit-2026-06-16.md` | Workflow-noise plans, CI review docs, lifecycle indexes, project-control reports, governance docs, runtime docs, and operator guidance | Archiveable cleanup candidate | Reference-check required; do not archive until workflow-noise decisions are confirmed superseded | May hide workflow-noise decision context or make later CI-noise review less auditable | Complete reference check only; do not archive until workflow-noise decisions are confirmed superseded |
| `docs/project-control/public-explorer-planning-gap-review.md` | Public Explorer planning, project-control reports, lifecycle indexes, governance docs, runtime docs, operator maps, and future planning references | Archiveable cleanup candidate | Reference-check required; likely keep active/reference until Public Explorer planning is superseded | May remove planning-gap context before Public Explorer planning has been superseded | Keep active/reference unless a later review confirms Public Explorer planning has been superseded |

## Decision rule

- Inventory, checklist, cleanup-plan, lifecycle-index, and reference-check mentions are informational references only; they are not blockers by themselves.
- If a candidate is mentioned only by lifecycle inventory, cleanup plan, or reference-check documents, that mention alone does not block archive/stub consideration.
- If a candidate is referenced by active navigation, `README`, `START_HERE`, operator maps, active planning docs, governance/runtime dependency docs, or public entrypoints, do not archive it yet.
- If a candidate is unreferenced by active blockers but contains audit-significant rationale, prefer archive/stub instead of deletion.
- Deletion remains prohibited without a separate explicit human approval PR.

## Output classification

This PR produces a reference-check plan/report only. It does not determine final disposition and does not authorize cleanup.

advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false except this docs-only reference-check report
approval_authority=false
merge_authority=false
