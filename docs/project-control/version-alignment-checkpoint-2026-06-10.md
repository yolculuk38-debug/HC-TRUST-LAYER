# Version Alignment Checkpoint — 2026-06-10

> **Status:** Project-control checkpoint
>
> **Scope:** Dependency update wave, Python baseline migration, CI alignment, developer documentation, and governance follow-up
>
> **Mode:** Documentation only

> **Historical/report-only boundary:** This document is a historical/report-only checkpoint. It records Python, dependency, CI, test, or release observations from the review moment when it was written. It should not be read as the current Python support baseline, dependency baseline, workflow runtime baseline, or live CI/test evidence. Current package metadata must be confirmed from `pyproject.toml`. Current pinned install/test dependencies must be confirmed from `requirements.txt`. Current workflow runtime versions must be confirmed from `.github/workflows/**`. Current CI/test evidence must be confirmed from live GitHub Actions and current PR/release evidence.

## Purpose

This checkpoint records the version alignment governance work completed after the Python dependency update wave and Python 3.14 migration.

The purpose is to preserve the audit trail from dependency freshness warnings through coordinated package, CI, documentation, and governance alignment.

## Background

Dependabot surfaced Python dependency updates and Python version support warnings during the dependency monitoring wave.

The repository handled those changes through human-supervised review and small PRs instead of automatic merge.

The key lesson was:

```text
A runtime version change is not a single-file change.
```

Changing one version surface can require coordinated updates to package metadata, workflow runtime, dependencies, tests, developer documentation, and checkpoint records.

## Completed PR Chain

The following PR chain is now completed and should not return to TODO:

| PR | Purpose | Result |
| --- | --- | --- |
| #782 | `fastapi` dependency update | merged |
| #783 | `anyio` dependency update | merged |
| #784 | `pydantic` dependency update | merged |
| #785 | Python runtime dependency checkpoint | merged |
| #786 | Python baseline adjustment | merged |
| #787 | Python baseline checkpoint | merged |
| #788 | Python 3.14 CI and package migration | merged |
| #789 | Python 3.14 migration checkpoint | merged |
| #790 | Contributor and onboarding docs alignment | merged |
| #791 | Version alignment governance rule | merged |

## Current Baseline

The active Python baseline is:

```text
Python 3.14+
```

The coordinated baseline includes:

```text
pyproject.toml
.github/workflows/validate.yml
runtime/API tests
CONTRIBUTING.md
docs/developer-onboarding.md
version alignment governance rule
```

## Governance Rule Added

The repository now includes:

```text
docs/governance/version-alignment-review-rule.md
```

That rule records the required review order for future Python, Node, GitHub Actions, or dependency version changes:

```text
1. package metadata
2. workflow runtime
3. requirements / dependency declarations
4. test compatibility
5. developer documentation
6. checkpoint / audit record
7. CI status
8. human merge decision
```

## Preserved Boundaries

This checkpoint records that the completed chain preserved the following HC boundaries:

- AI advisory only;
- human final authority;
- no autonomous merge policy;
- no grouped security updates enabled;
- no schema changes in this checkpoint;
- no validator changes in this checkpoint;
- no record changes in this checkpoint;
- no truth guarantee introduced;
- `truth_guarantee = false` remains the project boundary.

## HC Control Bot Follow-Up

A future HC Control Bot / HC Trust Engineer update may add a deterministic version alignment signal.

That future signal should flag PRs that touch surfaces such as:

```text
pyproject.toml
requirements.txt
.github/workflows/**
CONTRIBUTING.md
docs/developer-onboarding.md
runtime/API dependency declarations
security or dependency checkpoint docs
```

The bot signal must remain advisory only.

It must not approve, reject, merge, close, certify, or override human review.

## Non-Goals

This checkpoint does not:

- change Python version again;
- change dependencies;
- modify workflows;
- modify runtime code;
- modify schemas;
- modify validators;
- modify records;
- enable auto-merge;
- enable grouped security updates;
- create a release claim;
- create a truth guarantee.

## Final Boundary

Version freshness is not the same as trust.

Version alignment is a review discipline, not a safety certificate.

Trust the record, not the narrative.

Historical Python, dependency, CI, and test evidence reports must be read in sequence with later migration checkpoints, dependency-wave checkpoints, current `pyproject.toml`, current `requirements.txt`, current workflow files, and live GitHub Actions evidence.
