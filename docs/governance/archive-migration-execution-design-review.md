# Archive Migration Execution Design Review

## Executive Summary

This report reviews the final execution design for a future historical archive migration from `records/verified/` to `records/archived/` after the PR #607 **Conditionally Ready** decision and the PR #608 implementation checklist.

This is a report-only design review. It does not move records, modify records, modify hashes, modify QR artifacts, modify generated artifacts, modify release evidence, modify schemas, modify validators, modify workflows, or modify runtime behavior.

Decision: **Go for opening the next actual migration PR, with constraints**.

The next PR may proceed to implement the historical archive migration if it remains limited to the exact scope below, preserves record contents, uses `records/archived/` as the target path, and applies the documented evidence-handling decisions through human-supervised review. This decision is not approval to merge an actual migration PR without validation output, reviewer confirmation, and explicit handling of path-sensitive artifacts.

## Reviewed Inputs

Design inputs reviewed for this decision:

- `docs/governance/archive-migration-readiness-review.md`
- `docs/governance/archive-migration-implementation-plan.md`
- `docs/governance/archive-target-path-decision.md`
- `docs/governance/historical-record-hash-handling-plan.md`
- `docs/governance/historical-record-qr-handling-plan.md`
- `docs/governance/release-evidence-related-records-handling-plan.md`
- `docs/governance/generated-artifact-handling-plan.md`

Repository artifacts inspected for path-sensitive impact:

- `records/verified/HC-TEST-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0002.md`
- `hash/`
- `qr/`
- `generated/audit_snapshot.json`
- `records/pending/HC-RELEASE-2026-0001.json`

## Exact Future Migration Scope

The future migration PR should only relocate the three reviewed historical HC:// records from `records/verified/` to `records/archived/`.

No additional records, examples, release evidence records, hash files, QR files, generated files, schemas, validators, workflows, runtime files, signing files, federation files, policy files, or trust-kernel materials are in the approved movement scope.

The future migration must preserve record content unless maintainers explicitly approve a separate content-update decision. If record-internal path references are proposed for update, they should be reviewed as documentation/content changes, not treated as automatic consequences of the file move.

## Files That Would Move in the Future Migration

The only files approved for movement in the future migration design are:

| Current path | Future path |
| --- | --- |
| `records/verified/HC-TEST-2026-0001.md` | `records/archived/HC-TEST-2026-0001.md` |
| `records/verified/HC-CHATGPT-2026-0001.md` | `records/archived/HC-CHATGPT-2026-0001.md` |
| `records/verified/HC-CHATGPT-2026-0002.md` | `records/archived/HC-CHATGPT-2026-0002.md` |

The future PR should create `records/archived/` only if it does not already exist and only as needed to hold the scoped moved records.

## Files That Must Remain Unchanged Unless Explicitly Approved

The following files and directories must remain unchanged in the future migration PR unless maintainers explicitly approve a path-sensitive evidence update in that same PR:

- `hash/HC-TEST-2026-0001.sha256`
- `hash/HC-CHATGPT-2026-0001.sha256`
- `hash/HC-CHATGPT-2026-0002.sha256`
- all other files under `hash/`
- `qr/HC-CHATGPT-2026-0001.txt`
- `qr/qr-code.jpg`
- `qr/README.md`
- all other files under `qr/`
- `generated/audit_snapshot.json`
- `records/pending/HC-RELEASE-2026-0001.json`
- schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, and canonical or trust-kernel materials

If any of these artifacts are updated later, the future PR must explain the old path, new path, rationale, command or manual review method, reviewer expectation, and validation result. No hash, QR, release evidence, generated artifact, signature, approval, timestamp, or validation result may be fabricated.

## Hash Handling Decision Recommendation

Recommendation: **preserve digest integrity and update path-bound hash manifests only if explicitly approved in the migration PR**.

The inspected hash manifests bind SHA-256 digests to `records/verified/` paths for all three scoped records. Moving the records without updating manifests would preserve legacy evidence but leave path references pointing to the former location. Updating manifests after the move may be appropriate, but it must be treated as a reviewed path-binding update rather than a new content claim.

If maintainers approve hash manifest updates in the actual migration PR, the PR should:

1. move the scoped records first without content edits;
2. recompute or verify SHA-256 digests from the moved files using repository-approved commands;
3. update only the path portion if the digest is unchanged;
4. document any digest change as a blocker unless an explicit content edit was separately approved;
5. include command output or a concise validation summary; and
6. preserve the old-to-new path mapping in the PR description or governance notes.

If maintainers do not approve hash updates in the actual migration PR, the PR should leave `hash/` unchanged and document that hash manifests remain legacy path-bound evidence pending a later reviewed update.

## QR Handling Decision Recommendation

Recommendation: **do not regenerate, replace, or edit QR artifacts unless explicitly approved; document stale or missing QR path references as known migration follow-up items**.

The inspected QR materials are incomplete for the scoped records. `qr/HC-CHATGPT-2026-0001.txt` points to a `records/verified/` GitHub path, while no corresponding QR text artifact was found for every scoped record in `qr/`. Existing binary QR material should not be modified in the migration PR unless maintainers approve a separate QR regeneration or deprecation decision.

If QR handling is approved in the actual migration PR, the PR should prefer text-based, reviewable QR target updates or explicit deprecation notes. It should not fabricate QR evidence for missing records. Any generated QR artifact must identify the generator command, target URL, reviewer rationale, and validation result.

## Release Evidence Handling Decision Recommendation

Recommendation: **leave `records/pending/HC-RELEASE-2026-0001.json` unchanged during the actual migration unless maintainers explicitly approve release evidence path updates**.

The pending release evidence record currently lists the three scoped records under `related_records` with `records/verified/` paths. Because the record remains pending and path-sensitive, silently changing `related_records` during file movement could alter release evidence context without a documented reviewer decision.

If maintainers approve release evidence updates in the actual migration PR, the PR should document each old path, each new path, the release evidence status impact, the reviewer rationale, and whether `HC-RELEASE-2026-0001` remains `pending`, becomes `reviewed`, or becomes `verified`. Without that explicit approval, the release evidence record should remain unchanged and the migration PR should document the retained legacy paths as pending-context bindings.

## Generated Artifact Regeneration Recommendation

Recommendation: **regenerate generated artifacts only after approved record movement and approved path-sensitive updates are complete, and only through repository tooling**.

`generated/audit_snapshot.json` currently reflects pre-migration source state and includes `records/verified/` and `records/archived/` source directories. It must not be hand edited.

If maintainers approve regeneration in the actual migration PR, the PR should run the repository-approved generator, record the exact command, review the generated diff manually, and include validation results. If regeneration is not approved, the file should remain unchanged and the PR should document generated artifact drift as an expected follow-up item.

## Documentation Update Recommendation

Recommendation: **update documentation references only by intent, not by blanket replacement**.

Future documentation updates should distinguish between:

- current-state references that must change after the migration;
- historical references that should remain unchanged;
- target-path guidance that already points to `records/archived/`;
- compatibility references for `records/archive/`; and
- examples that should change only if they are intended to describe post-migration state.

The actual migration PR may include minimal governance documentation updates needed to explain the migration result, but it should not perform broad documentation cleanup unless that cleanup is explicitly scoped and reviewable.

## Validation Checklist

The actual migration PR should run and record at least these checks:

- [ ] `python scripts/check_terminology.py`
- [ ] `python scripts/check_docs_drift.py`
- [ ] `python scripts/check_canonical_artifacts.py`
- [ ] `python scripts/check_pr_scope.py`
- [ ] hash verification for each moved record, if hash manifests are updated or reviewed
- [ ] QR target review, if QR artifacts are updated, deprecated, or intentionally retained as legacy references
- [ ] generated artifact command and manual diff review, if generated artifacts are regenerated
- [ ] release evidence review, if `records/pending/HC-RELEASE-2026-0001.json` is updated
- [ ] manual confirmation that only the three scoped records moved
- [ ] manual confirmation that no schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or unrelated records changed

Validation failures must be treated as blockers unless maintainers explicitly document why a failure is an accepted limitation for the migration PR.

## Rollback Checklist

If the actual migration PR fails validation or review, rollback should remain limited and reversible:

- [ ] move `records/archived/HC-TEST-2026-0001.md` back to `records/verified/HC-TEST-2026-0001.md`;
- [ ] move `records/archived/HC-CHATGPT-2026-0001.md` back to `records/verified/HC-CHATGPT-2026-0001.md`;
- [ ] move `records/archived/HC-CHATGPT-2026-0002.md` back to `records/verified/HC-CHATGPT-2026-0002.md`;
- [ ] revert any approved hash, QR, release evidence, generated artifact, or documentation changes made in the migration PR;
- [ ] remove `records/archived/` only if it was created by the migration PR and is empty after rollback;
- [ ] re-run the same validation commands used by the migration PR;
- [ ] document the failed decision point and remaining blocker before attempting a new migration PR.

Rollback must not delete legacy evidence, fabricate replacement evidence, weaken guards, or normalize evidence paths without review.

## Go / No-Go Decision for Actual Migration PR

Decision: **Go for a future actual migration PR, conditional on strict scope and validation**.

The implementation design from PR #608 is sufficiently constrained for the next PR to perform the actual archive migration. More planning is not required before opening that PR, provided the PR:

- moves only the three scoped records from `records/verified/` to `records/archived/`;
- preserves record content unless a separate explicit content-update approval is recorded;
- treats hash, QR, release evidence, generated artifact, and documentation changes as separately reviewable path-sensitive decisions;
- does not modify schemas, validators, workflows, runtime, signing logic, federation logic, policy files, or unrelated records;
- runs the validation checklist and reports results; and
- records human-supervised review before merge.

No-Go conditions for the actual migration PR include any unresolved scope expansion, unapproved evidence edits, generated artifact hand editing, fabricated validation or approval claims, failed required checks without documented maintainer acceptance, or any change that weakens HC:// and HC-TRUST-LAYER governance controls.
