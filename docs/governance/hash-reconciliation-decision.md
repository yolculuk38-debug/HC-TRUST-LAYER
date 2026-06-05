# Hash Reconciliation Decision Review

## Purpose

This report records the hash reconciliation decision for legacy HC:// hash manifests before v0.1.0. It determines whether legacy hash manifests should remain unchanged, whether archived-path manifests should be issued, or whether no reconciliation is required before v0.1.0.

This is a REPORT ONLY governance decision review. It does not modify hash files, records, schemas, validators, signing logic, federation logic, security workflows, policy files, GitHub Actions, release evidence, generated artifacts, or canonical artifacts.

## Inspected Inputs

- `hash/`
- `docs/governance/post-migration-hash-review.md`
- `docs/governance/v0.1.0-final-readiness-review.md`

## Current State

The legacy hash manifests for the three migrated historical records remain bound to their former `records/verified/` paths:

| Manifest | Legacy path recorded in manifest | Current record location | Digest status |
| --- | --- | --- | --- |
| `hash/HC-TEST-2026-0001.sha256` | `records/verified/HC-TEST-2026-0001.md` | `records/archived/HC-TEST-2026-0001.md` | Archived content digest matches the legacy manifest digest. |
| `hash/HC-CHATGPT-2026-0001.sha256` | `records/verified/HC-CHATGPT-2026-0001.md` | `records/archived/HC-CHATGPT-2026-0001.md` | Archived content digest matches the legacy manifest digest. |
| `hash/HC-CHATGPT-2026-0002.sha256` | `records/verified/HC-CHATGPT-2026-0002.md` | `records/archived/HC-CHATGPT-2026-0002.md` | Archived content digest matches the legacy manifest digest. |

The post-migration review identifies this as a path reconciliation issue rather than a content-integrity failure. Standard `sha256sum -c` checks against these legacy manifests fail because the referenced `records/verified/` files are no longer present, even though recalculating SHA-256 over the archived files produces the same digest values.

The final readiness review treats legacy `related_records` path disposition as an open release decision and recommends deciding whether legacy path references are acceptable as pending historical context for v0.1.0 or require separate reconciliation before release.

## Decision Categories

### Preserve Legacy Hashes

**Decision:** Recommended for v0.1.0.

The existing manifests should remain unchanged because they are historical, path-bound evidence for the original record locations. Editing these files would blur the distinction between the original hash evidence and any post-migration evidence. Preservation keeps the review boundary narrow and avoids rewriting historical artifacts.

Operational interpretation:

- Treat current `hash/*.sha256` files for the migrated records as legacy path-bound manifests.
- Do not edit the legacy manifests before v0.1.0.
- Document that `sha256sum -c` against those manifests will fail by current path lookup unless a reviewer restores or maps the historical paths for verification.
- Use direct archived-file digest recalculation when reviewing content continuity, while preserving the legacy path context.

### Issue Archived-Path Hashes

**Decision:** Defer until after v0.1.0 unless maintainers explicitly require a separate reviewed reconciliation PR before release.

Archived-path manifests could reduce operator confusion by providing current-path verification files. However, issuing them before v0.1.0 would create new evidence artifacts and would require clear naming, provenance notes, review expectations, and validation guidance. Without that policy, new archived-path manifests may be mistaken for replacements for legacy manifests or for broader release approval evidence.

If maintainers choose this path later, the work should be a small, dedicated, human-reviewed PR that:

- leaves legacy manifests unchanged;
- creates clearly labeled archived-path manifests or a separate reconciliation index;
- records the command used to calculate each digest;
- explains that the new artifacts are post-migration path evidence, not replacements for historical manifests;
- updates operator guidance for how to verify both legacy path-bound evidence and current archived-path evidence.

### No Action Required

**Decision:** Acceptable only as a v0.1.0 release disposition when paired with explicit disclosure.

No hash-file action is required before v0.1.0 if the release remains advisory, early-stage, and human-supervised, and if the release evidence or release notes disclose the legacy path-bound status. This does not mean the issue is absent. It means the issue is not a release blocker because current evidence indicates content digest continuity for the migrated archived records and the remaining gap is path reconciliation.

## Recommendation

Adopt **Preserve Legacy Hashes** for v0.1.0, with **No Action Required before v0.1.0** as the release disposition.

Do not issue archived-path hash manifests before v0.1.0 unless maintainers explicitly decide that current-path `sha256sum -c` verification must be available for the release candidate. If that decision is made, issue archived-path manifests in a separate scoped PR with review notes and without modifying the legacy manifests.

## Risks

- Reviewers or tools may treat path-bound legacy manifests as current-path manifests and report verification failures.
- Contributors may misinterpret the mismatch as a content-integrity failure rather than a migration path issue.
- Issuing archived-path manifests without clear labeling may blur historical evidence and post-migration evidence.
- Leaving the issue only in governance documentation may require extra reviewer attention during release evidence review.
- Future generated artifacts, QR references, or release evidence may continue to point at legacy paths unless handled through a broader reconciliation plan.

## v0.1.0 Impact

This decision should not block v0.1.0 if all of the following remain true:

1. v0.1.0 is presented as advisory, early-stage HC:// verification infrastructure, not production-ready infrastructure.
2. Legacy hash manifests remain unchanged and are described as historical path-bound evidence.
3. Release evidence records the path reconciliation disposition.
4. Required terminology, docs drift, canonical artifact, and relevant validation checks pass or are explicitly dispositioned.
5. Human-supervised validation remains responsible for the final release decision.

This decision does not validate release readiness by itself. It only resolves the hash reconciliation strategy for the migrated historical records.

## Future Roadmap

After v0.1.0, maintainers should consider a dedicated reconciliation plan that:

1. Defines naming and placement rules for any archived-path hash manifests.
2. Decides whether archived-path manifests should be standalone files, a reconciliation index, or generated release evidence.
3. Documents verification commands for legacy path-bound evidence and current archived-path evidence.
4. Reviews QR artifacts, generated indexes, and release evidence for legacy path references.
5. Adds operator-facing guidance for interpreting path-bound hash failures without implying content failure.
6. Preserves historical manifests as evidence and avoids replacing them with post-migration artifacts.
7. Keeps any automation bounded, explainable, reversible, and human-reviewable.

## Final Decision

**Preserve Legacy Hashes.**

No hash-file reconciliation is required before v0.1.0 if the release documentation records this disposition. Archived-path manifests may be useful later, but they should be introduced only through a separate reviewed reconciliation PR after their status and verification semantics are documented.
