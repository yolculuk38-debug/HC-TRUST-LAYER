# Release Evidence Reconciliation Decision Review

## Purpose

This report records the release evidence `related_records` reconciliation decision for `records/pending/HC-RELEASE-2026-0001.json` before v0.1.0. It determines whether the existing `related_records` paths should remain unchanged, whether archived-path references should be issued, or whether no `related_records` reconciliation is required before v0.1.0.

This is a REPORT ONLY governance decision review. It does not modify release evidence, records, hash files, QR artifacts, generated artifacts, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or canonical artifacts.

## Inspected Inputs

- `records/pending/HC-RELEASE-2026-0001.json`
- `docs/governance/post-migration-release-evidence-review.md`
- `docs/governance/v0.1.0-final-readiness-review.md`

## Current State

PR #610 moved historical HC:// records from `records/verified/` to `records/archived/` without modifying `records/pending/HC-RELEASE-2026-0001.json`. PR #613 reviewed post-migration release evidence `related_records` and found that the release evidence record still preserves three legacy `records/verified/` path bindings while the corresponding records now live under `records/archived/`.

Current `related_records` state:

| Related record ID | Legacy path in release evidence | Current repository location | Decision note |
| --- | --- | --- | --- |
| `HC-TEST-2026-0001` | `records/verified/HC-TEST-2026-0001.md` | `records/archived/HC-TEST-2026-0001.md` | Preserve as legacy pending-context evidence for v0.1.0. |
| `HC-CHATGPT-2026-0001` | `records/verified/HC-CHATGPT-2026-0001.md` | `records/archived/HC-CHATGPT-2026-0001.md` | Preserve as legacy pending-context evidence for v0.1.0. |
| `HC-CHATGPT-2026-0002` | `records/verified/HC-CHATGPT-2026-0002.md` | `records/archived/HC-CHATGPT-2026-0002.md` | Preserve as legacy pending-context evidence for v0.1.0. |

PR #617 decided to preserve legacy hash manifests for v0.1.0. PR #618 decided to preserve legacy QR artifacts for v0.1.0. Those decisions support a conservative release-stabilization pattern: preserve path-bound historical evidence, disclose the limitation, and defer current archived-path artifacts unless maintainers explicitly require a separate reviewed reconciliation PR.

## Decision Categories

### Preserve Legacy related_records

**Decision:** Recommended for v0.1.0.

The existing `related_records` entries should remain unchanged because they are pending release evidence context that records the path bindings present when `HC-RELEASE-2026-0001` was drafted. Editing the release evidence record before v0.1.0 would modify an evidence-bearing artifact and could blur the distinction between historical path bindings, current archived locations, and final release validation status.

Operational interpretation:

- Treat the existing `records/verified/` paths as legacy pending-context bindings.
- Treat the `records/archived/` files as the current repository locations for the same historical record IDs.
- Do not edit `records/pending/HC-RELEASE-2026-0001.json` before v0.1.0 only to normalize paths.
- Do not treat the unchanged `related_records` paths as proof that the legacy `records/verified/` files are current repository locations.
- Do not treat the referenced historical records as active v0.1.0 release evidence without a separate human-reviewed decision.

### Update related_records to Archived Paths

**Decision:** Defer until after v0.1.0 unless maintainers explicitly require a separate reviewed reconciliation PR before release.

Archived-path `related_records` could reduce contributor and tool confusion by pointing directly to current `records/archived/` locations. However, changing `HC-RELEASE-2026-0001` would alter release evidence, not merely documentation. That update should not be mixed into the v0.1.0 stabilization window unless maintainers decide that current archived-path release evidence references are required before release.

If maintainers choose this path later, the work should be a small, dedicated, human-reviewed PR that:

- records each old `records/verified/` path;
- records each new `records/archived/` path;
- identifies the reviewer or maintainer responsible for the decision;
- explains the rationale for changing path bindings;
- states whether the change affects the release evidence status or leaves `HC-RELEASE-2026-0001` pending;
- coordinates with legacy hash, QR, generated artifact, and documentation reference handling; and
- runs terminology, docs drift, canonical artifact, and any applicable record validation checks.

### No Action Required

**Decision:** Acceptable as the v0.1.0 release disposition when paired with explicit disclosure.

No `related_records` reconciliation is required before v0.1.0 if the release remains advisory, early-stage, and human-supervised, and if maintainers explicitly accept the legacy path-bound state as a known limitation. This does not mean reconciliation is complete. It means the issue is not a v0.1.0 release blocker because the current finding is path disposition, not a demonstrated content-integrity failure or release approval record.

## Recommendation

Adopt **Preserve Legacy related_records** for v0.1.0, with **No Action Required before v0.1.0** as the release disposition.

Do not edit `records/pending/HC-RELEASE-2026-0001.json` before release only to convert `related_records` paths from `records/verified/` to `records/archived/`. If archived-path `related_records` are needed, create a future small, human-reviewed PR that records old path, new path, reviewer, rationale, and release evidence status impact.

## Risks

- Reviewers or tools may attempt to resolve the legacy `records/verified/` paths and report missing files.
- Contributors may misinterpret legacy path bindings as current repository locations.
- Leaving the decision only in governance documentation may require extra reviewer attention during final release evidence review.
- Updating `related_records` without a dedicated review could imply release evidence validation or maintainer approval that has not been recorded.
- A path-only release evidence edit could diverge from legacy hash manifests, QR artifacts, generated artifact context, or archived record metadata.
- Deferring reconciliation indefinitely may keep downstream path-bound evidence issues open for future releases.

## v0.1.0 Impact

This decision should not block v0.1.0 if all of the following remain true:

1. v0.1.0 is presented as advisory, early-stage HC:// verification infrastructure, not production-ready infrastructure.
2. `records/pending/HC-RELEASE-2026-0001.json` remains unchanged unless maintainers explicitly approve a separate release evidence edit.
3. Release documentation acknowledges that legacy `related_records` paths remain as pending-context evidence.
4. The three referenced historical records remain historical context and are not promoted to active v0.1.0 release evidence without separate review.
5. Required terminology, docs drift, canonical artifact, and relevant validation checks pass or are explicitly dispositioned.
6. Human-supervised validation remains responsible for the final release decision.

This decision does not validate final release readiness by itself. It only resolves the `related_records` reconciliation strategy for the migrated historical records.

## Future Roadmap

After v0.1.0, maintainers should consider a dedicated release evidence reconciliation plan that:

1. Defines when release evidence should preserve historical path bindings versus current repository paths.
2. Establishes a review template for old path, new path, reviewer, rationale, and status impact.
3. Decides whether archived-path references belong directly in release evidence, a reconciliation index, or separate governance documentation.
4. Coordinates release evidence path policy with legacy hash manifest, QR artifact, generated artifact, and archived record metadata decisions.
5. Clarifies operator guidance for tools that encounter legacy `records/verified/` paths after archival.
6. Keeps any release evidence edit small, reversible, evidence-preserving, and human-reviewable.
7. Avoids retroactive production, forensic certainty, or autonomous governance claims.

## Final Decision

**Preserve Legacy related_records.**

No `related_records` reconciliation is required before v0.1.0 if release documentation records this disposition. Archived-path `related_records` may be useful later, but they should be introduced only through a separate reviewed reconciliation PR after the old path, new path, reviewer, rationale, and release evidence status impact are documented.
