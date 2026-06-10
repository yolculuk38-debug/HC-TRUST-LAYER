# Python 3.14 Migration Checkpoint — 2026-06-10

Status: checkpoint record.

This document records the Python 3.14 migration sequence for HC-TRUST-LAYER.

## Purpose

The purpose of this checkpoint is to preserve the audit trail for the Python baseline and validation runtime migration.

This is a governance and operational record. It is not a runtime trust guarantee.

## Background

Dependabot surfaced warnings around the older Python 3.9 support baseline.

The project first moved from:

```text
requires-python = ">=3.9"
```

to:

```text
requires-python = ">=3.11"
```

That intermediate step dropped Python 3.9 while preserving compatibility with the active CI runtime at the time.

## Final migration

The active package baseline and validation CI runtime were then moved to Python 3.14.

The final intended state is:

```text
requires-python = ">=3.14"
```

and the active validation workflow uses:

```text
python-version: '3.14'
```

for both:

- canonical validation job;
- runtime/API test job.

## Pull request sequence

| PR | Purpose | Outcome |
| --- | --- | --- |
| #786 | Raised Python baseline from 3.9 and corrected review-time incompatibility | merged with final `>=3.11` baseline |
| #787 | Recorded the Python support baseline decision and rejected `>=3.14`-without-CI alignment path | merged as checkpoint |
| #788 | Raised package baseline and active validation workflow runtime to Python 3.14 | merged |

## Why CI alignment was required

A package metadata-only move to Python 3.14 was not sufficient.

When `requires-python` was set to `>=3.14` while CI still used Python 3.11, package installation failed before runtime/API tests could execute.

Therefore, the final Python 3.14 move required aligning both:

- `pyproject.toml` package metadata;
- `.github/workflows/validate.yml` validation runtime.

## Scope of the migration

This migration intentionally changed:

- declared Python package support baseline;
- validation workflow Python runtime;
- runtime/API test workflow Python runtime inside the validation workflow.

This migration did not intentionally change:

- dependency versions;
- runtime verification logic;
- schema files;
- validator logic;
- record contents;
- signing behavior;
- federation behavior;
- QR semantics;
- generated artifact semantics;
- advisory-only semantics;
- `truth_guarantee = false` semantics.

## Review boundary

Python baseline migrations are workflow-adjacent and runtime-adjacent.

They must remain manual-review changes because they can affect:

- dependency installation behavior;
- package metadata compatibility;
- pytest behavior;
- FastAPI/runtime behavior;
- Pydantic validation behavior;
- CI reproducibility;
- future contributor environment expectations.

## Operational rule

Future Python version changes must update package metadata and CI runtime together unless the PR is explicitly marked report-only.

Recommended rule:

```text
Do not raise requires-python beyond the active CI Python runtime.
```

## Final boundary

Python 3.14 support improves maintenance hygiene.

Python 3.14 support is not a claim that records are true.

Trust the record, not the narrative.
