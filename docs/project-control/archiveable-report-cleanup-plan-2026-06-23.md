# Archiveable report cleanup plan - 2026-06-23

## Purpose

This document defines a scoped cleanup plan for reports currently marked `archiveable` in `docs/project-control/report-lifecycle-index.md`.

`archiveable` does not mean disposable. It means a report may be a candidate for archive, stub, or reference treatment after a separate reference check and human-supervised review. Audit evidence, planning context, and review history should be preserved unless a later scoped PR records explicit approval for a narrower disposition.

## Candidate reports

| Report | Current cleanup review | Proposed disposition |
| --- | --- | --- |
| `docs/project-control/public-navigation-audit.md` | Candidate archiveable report | archive-or-reference review |
| `docs/project-control/repository-cleanup-audit-2026-06-15.md` | Candidate archiveable report | archive-or-reference review |
| `docs/project-control/workflow-run-noise-audit-2026-06-16.md` | Candidate archiveable report | archive-or-reference review |
| `docs/project-control/public-explorer-planning-gap-review.md` | Candidate archiveable report | keep-or-archive review |

## Boundary of this PR

This PR does not delete, move, rename, archive, or stub any report. It adds only this docs-only cleanup planning document so future report lifecycle work can remain small, reviewable, and evidence-preserving.

## Next PR sequence

1. Reference check only.
2. Archive/stub only for unreferenced reports.
3. Deletion only with explicit human approval.

advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false except this docs-only plan
approval_authority=false
merge_authority=false
