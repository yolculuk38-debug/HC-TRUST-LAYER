# Version Alignment Review Rule

> **Status:** Governance review rule
>
> **Scope:** Runtime, package, dependency, CI, and developer documentation version changes
>
> **Mode:** Documentation only

## Purpose

HC-TRUST-LAYER treats version changes as coordinated maintenance work when they can affect runtime behavior, CI execution, dependency resolution, contributor setup, or public verification safety.

A version bump must not be reviewed as a single-file change when package metadata, CI runtime, dependency declarations, tests, developer documentation, or checkpoints also need to move together.

This rule exists to prevent version drift between declared support, actual validation runtime, and contributor instructions.

## Core Rule

Version alignment changes must be reviewed as a coordinated set.

If a version baseline changes in one place, maintainers must check related surfaces before merge.

This applies especially to:

- Python runtime baselines;
- Node or JavaScript toolchain baselines if introduced;
- GitHub Actions runtime versions;
- Python package dependency versions;
- package metadata;
- test environment assumptions;
- contributor and developer onboarding instructions;
- checkpoint or audit documentation.

## Required Review Order

For every Python, Node, GitHub Actions, or dependency version change, reviewers must check:

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

A PR does not satisfy this rule only because one file was updated.

The reviewer must consider whether the version change creates required companion updates.

## Python Baseline Alignment

When `pyproject.toml` changes `requires-python`, CI must be reviewed for compatibility.

Example risk:

```text
pyproject.toml: requires-python = ">=3.14"
.github/workflows/validate.yml: python-version: "3.11"
```

This creates a version alignment failure because package metadata requires Python 3.14 while CI still runs under Python 3.11.

Expected handling:

```text
requires-python >= X
+
CI python-version compatible with X
+
dependency and test compatibility reviewed
+
developer docs updated
+
checkpoint recorded
+
CI green
+
human merge
```

## Dependency Alignment

Dependency updates may affect runtime, validation, QR generation, schema behavior, public verifier behavior, or test assumptions.

Reviewers must classify dependency updates by affected area.

| Area | Example surface | Review concern |
| --- | --- | --- |
| Runtime/API | `fastapi`, `anyio`, `pydantic` | response behavior, async behavior, contract drift |
| Schema/validation | `jsonschema` | schema validation behavior |
| QR/provenance | `qrcode[pil]` | QR generation or demo output changes |
| GitHub Actions | `actions/*` | workflow execution and artifact behavior |

A dependency update improves freshness.

A dependency update does not prove safety.

## Workflow Alignment

Changes under `.github/workflows/**` are workflow-adjacent and must be reviewed carefully.

Workflow version updates must preserve HC review boundaries:

- automation remains advisory or validation-only;
- human review remains required;
- validation checks must not be weakened;
- workflow changes must be documented when they are required by package metadata.

## Documentation Alignment

When supported runtime versions change, contributor-facing documentation must be reviewed.

Common documentation surfaces include:

- `CONTRIBUTING.md`;
- `docs/developer-onboarding.md`;
- setup or quickstart documents;
- runtime runbooks;
- security or dependency update checkpoints.

Documentation must not claim support for a runtime version that package metadata or CI no longer supports.

## Checkpoint Requirement

Baseline migrations should leave a checkpoint or audit note.

A checkpoint should record:

- what version changed;
- why it changed;
- which related surfaces were reviewed;
- which safety boundaries were preserved;
- whether the change was dependency-only, workflow-adjacent, runtime-adjacent, or documentation-only;
- that the change does not create a truth guarantee.

## HC Control Bot Signal

HC Control Bot / HC Trust Engineer may flag a version alignment risk when changed files include one or more of:

```text
pyproject.toml
requirements.txt
.github/workflows/**
CONTRIBUTING.md
docs/developer-onboarding.md
runtime/API dependency declarations
security or dependency checkpoint docs
```

A bot warning must remain advisory only.

The bot must not approve, reject, merge, close, or certify the PR.

Human maintainers retain final authority.

## Protected Review Boundaries

This rule does not authorize automatic merge.

This rule does not authorize grouped security updates.

This rule does not authorize weakening CI.

This rule does not authorize changing Python, Node, GitHub Actions, dependency, schema, validator, runtime, or record behavior without human review.

## Preserved HC Semantics

Version alignment review must preserve:

- AI advisory only;
- human final authority;
- public-safe output expectations;
- no autonomous merge;
- no production-readiness implication;
- no objective-truth guarantee;
- `truth_guarantee = false`.

## Final Boundary

Version freshness is not the same as trust.

A repository can be up to date and still unsafe.

A version change is complete only when the related metadata, CI runtime, dependencies, tests, documentation, checkpoint, CI result, and human review are aligned.

Trust the record, not the narrative.
