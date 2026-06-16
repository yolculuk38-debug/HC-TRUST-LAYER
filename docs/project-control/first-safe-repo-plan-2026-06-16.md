# First Safe Repo Plan — 2026-06-16

Status: advisory proposal.

This document records the first safe repository-structure proposal after the completed purpose-index chain.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This proposal is documentation only.
- This proposal does not change runtime behavior, workflows, tests, schemas, records, QR data, hash data, generated artifacts, policy, federation, signatures, or repository settings.

## Source evidence

Use these indexes before any future structure change:

1. [`repository-index-chain-2026-06-16.md`](repository-index-chain-2026-06-16.md)
2. [`root-file-purpose-index-2026-06-16.md`](root-file-purpose-index-2026-06-16.md)
3. [`docs-directory-purpose-index-2026-06-16.md`](docs-directory-purpose-index-2026-06-16.md)
4. [`src-module-purpose-index-2026-06-16.md`](src-module-purpose-index-2026-06-16.md)
5. [`scripts-tool-purpose-index-2026-06-16.md`](scripts-tool-purpose-index-2026-06-16.md)
6. [`generated-reference-artifact-index-2026-06-16.md`](generated-reference-artifact-index-2026-06-16.md)
7. [`historical-evidence-index-2026-06-16.md`](historical-evidence-index-2026-06-16.md)
8. [`public-demo-docs-index-2026-06-16.md`](public-demo-docs-index-2026-06-16.md)

## Current conclusion

The first structure-changing PR should not touch protected or evidence-bearing surfaces.

Protected or high-risk surfaces remain out of scope:

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
- `src/**`
- `tests/**`

## First candidate work

The first practical follow-up should be a navigation-only refresh, not a file move.

Recommended next PR:

```text
Add links from project-control navigation docs to the completed index chain.
```

Why:

- it improves discoverability;
- it does not disturb evidence paths;
- it does not change runtime behavior;
- it does not touch workflows;
- it keeps the cleanup path reviewable.

## Later candidates

Only after the navigation refresh, consider one small proposal at a time:

| Candidate | Type | Gate |
|---|---|---|
| Complete generated artifact inventory | report-only | Must identify source, generator, and consumer. |
| Complete historical path inventory | report-only | Must preserve origin and evidence status. |
| Complete public/demo inventory | report-only | Must preserve local/demo limits. |
| Public docs link refresh | navigation-only | Must keep public-safe language. |

## Not approved by this proposal

This proposal does not approve:

- moving files;
- renaming paths;
- changing workflow permissions;
- changing validation behavior;
- changing public demo behavior;
- changing canonical or evidence records;
- merging multiple unrelated cleanup scopes.

## Final rule

First make the map easy to follow. Then make one small change at a time.

```text
index chain first
navigation refresh second
structure changes later
small PRs only
human review remains required
```
