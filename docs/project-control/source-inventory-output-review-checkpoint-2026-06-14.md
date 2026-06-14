# Source Inventory Output Review Checkpoint — 2026-06-14

Status: advisory evidence checkpoint.

This checkpoint records the next safe source-inventory step after the current project-state handoff. It does not delete, move, archive, rewrite, or reclassify source files. It does not modify protected paths, runtime behavior, workflows, schemas, records, policies, generated artifacts, signing, federation, QR/hash evidence, or authority boundaries.

## Scope

The safe task is to review source inventory evidence before proposing cleanup or rewrite work.

Allowed output from this checkpoint:

- docs/project-control evidence notes;
- inventory review status;
- operator checklist updates;
- follow-up candidates that remain report-only until separately authorized.

Not allowed from this checkpoint:

- source deletion;
- source moves;
- test behavior rewrites;
- record normalization writes;
- protected-path edits;
- branch cleanup;
- authority-changing automation.

## Source inventory reporter boundary

The existing reporter is `scripts/hc_source_inventory.py`.

Current confirmed behavior from repository evidence:

- scans the default roots `src`, `scripts`, and `tests`;
- lists Python files and classifies them by path category;
- returns `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, `inventory_only=true`, and `modifies_repository=false`;
- avoids network calls, LLM calls, subprocess execution, repository writes, file deletion, file moves, workflow changes, GitHub Actions, secret reads, and authority-changing behavior.

Operator command:

```bash
python scripts/hc_source_inventory.py .
```

The output must be treated as evidence for review, not as permission to remove or move files.

## Review order

1. Confirm active implementation anchors first.
2. Confirm matching tests and documentation anchors.
3. Classify unsupported files as review-needed, not deletion candidates.
4. Mark experimental or archival classifications for manual review.
5. Keep protected-path-adjacent files out of cleanup until explicitly authorized.
6. Open a separate small PR only after a concrete evidence-backed change is identified.

## Confirmed active anchors to preserve

| Area | Current evidence | Review status |
| --- | --- | --- |
| Verification package core | `src/hc_trust/verification_package.py` plus verification-package tests | Active implementation |
| CLI entry point | `src/hc_trust/cli.py` exposing `hc-trust verify-package` | Active implementation |
| Runtime telemetry/response surface | `src/hc_runtime/**` plus runtime contract tests | Active / focused-review only |
| Record normalizer | `src/normalize_records.py` plus `tests/test_normalize_records.py` | Active utility with safety tests |
| Source inventory reporter | `scripts/hc_source_inventory.py` | Operator-support / inventory-only |
| Root integration script | `test_integration.py` | Existing root-level script; review before edits |

## normalize_records.py status

`normalize_records.py` is not an unresolved missing-file item. It currently exists at `src/normalize_records.py` and is covered by `tests/test_normalize_records.py`.

Current behavior:

- default mode does not write changes;
- `--dry-run` prints a diff preview;
- `--write` is required before writable records are updated;
- records under `archive`, `archived`, or `verified` path parts are protected from overwrite even when `--write` is used;
- tests cover protected archive, archived, verified, live-path, and write-enabled archived-record behavior.

Current decision:

- keep `src/normalize_records.py` as an active utility;
- do not move it, delete it, or rewrite its behavior from inventory evidence alone;
- any future relocation into a package namespace must be a separate explicit refactor with tests and human review.

## Remaining evidence items

Before cleanup or rewrite proposals, collect and review:

- full source inventory output;
- test inventory evidence;
- branch-count evidence from reliable branch listing or GitHub UI;
- import/reference anchors for review-needed source files;
- matching docs or quickstart anchors.

## Operating decision

No cleanup is authorized by this checkpoint. The next safe step is evidence review only.

Human final authority remains required for deletion, archival, protected-path work, branch cleanup, record writes, workflow changes, and authority-changing automation.
