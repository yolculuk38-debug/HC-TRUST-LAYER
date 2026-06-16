# Repository Cleanup Phase 1 Checkpoint — 2026-06-16

Status: advisory checkpoint.

This document records the completion of the first repository cleanup mapping phase.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This checkpoint is documentation only.
- This checkpoint does not change runtime behavior, workflows, tests, schemas, records, QR data, hash data, generated artifacts, policy, federation, signatures, or repository settings.
- This checkpoint does not approve moving, renaming, deleting, archiving, or consolidating files.

## Completed phase 1 mapping chain

Phase 1 produced purpose indexes for the main repository surfaces:

1. [`root-file-purpose-index-2026-06-16.md`](root-file-purpose-index-2026-06-16.md)
2. [`docs-directory-purpose-index-2026-06-16.md`](docs-directory-purpose-index-2026-06-16.md)
3. [`src-module-purpose-index-2026-06-16.md`](src-module-purpose-index-2026-06-16.md)
4. [`scripts-tool-purpose-index-2026-06-16.md`](scripts-tool-purpose-index-2026-06-16.md)
5. [`generated-reference-artifact-index-2026-06-16.md`](generated-reference-artifact-index-2026-06-16.md)
6. [`historical-evidence-index-2026-06-16.md`](historical-evidence-index-2026-06-16.md)
7. [`public-demo-docs-index-2026-06-16.md`](public-demo-docs-index-2026-06-16.md)
8. [`repository-index-chain-2026-06-16.md`](repository-index-chain-2026-06-16.md)

Phase 1 also produced path-level verified anchor passes:

1. [`generated-artifact-inventory-pass-2026-06-16.md`](generated-artifact-inventory-pass-2026-06-16.md)
2. [`historical-path-inventory-pass-2026-06-16.md`](historical-path-inventory-pass-2026-06-16.md)
3. [`public-demo-inventory-pass-2026-06-16.md`](public-demo-inventory-pass-2026-06-16.md)

## Current conclusion

The repository now has a safer map for cleanup discussions.

The map is sufficient for:

- locating root, docs, source, scripts, generated/reference, historical/evidence, and public/demo surfaces;
- separating protected, evidence-bearing, demo, generated, and tooling surfaces;
- preventing cleanup from being driven by visual clutter alone;
- preparing a future small proposal if evidence supports it.

The map is not sufficient for:

- automatic deletion;
- moving protected areas;
- renaming evidence paths;
- changing workflow permissions;
- changing runtime or validator behavior;
- weakening public/demo safety language;
- treating generated artifacts as canonical records.

## Protected or parked surfaces

The following remain parked unless explicitly scoped, reviewed, and validated in a separate PR:

- `.github/workflows/**`
- `schema/**`
- `validators/**`
- `records/**`
- `hash/**`
- `qr/**`
- `policy/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- runtime behavior under `src/**`
- executable regression evidence under `tests/**`

## Safe phase 2 candidates

Phase 2 should start with one small, reversible, documentation-only or navigation-only PR.

Recommended candidates:

1. update `next-actions.md` to point at this checkpoint;
2. update `operator-entry-map.md` to point at the repository index chain and checkpoint;
3. prepare a single future move proposal only if a path is non-protected, non-evidence-bearing, not required by tooling/CI, and has a better documented target;
4. produce a deterministic complete tree inventory if exact file-level coverage is needed.

## Not approved by this checkpoint

This checkpoint does not approve:

- moving files;
- deleting files;
- closing issues;
- deleting branches;
- disabling workflows;
- changing authority boundaries;
- changing validator, QR, hash, record, schema, policy, federation, signature, or canonical behavior.

## Final rule

Phase 1 makes the repository easier to inspect. Phase 2 must stay small, reversible, and evidence-backed.

```text
map completed
inventory anchors linked
no structure change yet
small reversible PRs only
human review remains required
```
