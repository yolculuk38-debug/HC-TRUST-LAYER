# Public navigation audit archive/stub plan - 2026-06-24

## Purpose

This document records the proposed archive/stub plan for `docs/project-control/public-navigation-audit.md` after the final active-reference search found no active blockers.

The plan is advisory and evidence-preserving. It supports a later human-reviewed decision about conservative archive or stub handling without changing the original report in this PR.

## Scope

This PR is planning only. It does not perform archive, stub, move, rename, or delete.

No existing report, `README`, `START_HERE`, index, navigation file, workflow, runtime file, schema, validator, record, generated artifact, hash, QR material, signature, witness material, policy file, federation file, or governance file is changed by this plan.

## Source chain

This plan follows the prior report chain:

- `docs/project-control/report-lifecycle-index.md`
- `docs/project-control/archiveable-report-cleanup-plan-2026-06-23.md`
- `docs/project-control/archiveable-report-reference-check-2026-06-23.md`
- `docs/project-control/archiveable-report-reference-findings-2026-06-23.md`
- `docs/project-control/public-navigation-audit-final-reference-search-2026-06-24.md`

The chain moved from lifecycle classification to cleanup plan, then to reference check, reference findings, final reference search, and this archive/stub plan.

## Candidate

- `docs/project-control/public-navigation-audit.md`

## Current finding

- No active blocker was found in active navigation, public entrypoints, `README`, `START_HERE`, operator maps, active planning docs, governance/runtime dependency docs, or active user-facing docs.
- Informational lifecycle/cleanup/reference reports may mention the file, but those references do not block archive/stub by themselves.
- The report remains audit-significant and must not be deleted.

## Recommended handling

A later PR should use one of these conservative options.

### Option A - Stub in place

- Keep `docs/project-control/public-navigation-audit.md` as a short stub.
- Move historical detail to a clearly named archive/history location in a separate PR.
- The stub should explain the report was superseded by later report lifecycle/reference-search records.

### Option B - Keep in place but mark archived

- Keep the file where it is.
- Add a clear archived/superseded notice at the top in a later PR.
- Do not move the path.

### Option C - Archive copy only

- Copy or move only if a clear archive convention already exists or is created in a separate approved PR.
- Preserve a stub or pointer from the old path.

## Recommended default

Use Option B as the safest default unless maintainers explicitly prefer path movement: keep the file in place and mark it as archived/superseded in a later PR.

## Deletion boundary

Deletion is not recommended.

Deletion is not authorized by this plan.

Deletion would require a separate explicit human approval PR.

## Next PR proposal

Recommended next PR title:

`docs(project-control): mark public navigation audit archived`

That next PR may edit only:

`docs/project-control/public-navigation-audit.md`

This PR must not perform that edit.

advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false except this docs-only archive/stub plan
approval_authority=false
merge_authority=false
archive_authority=false
delete_authority=false
