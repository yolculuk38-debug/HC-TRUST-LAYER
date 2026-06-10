# Python Support Baseline Checkpoint — 2026-06-10

Status: checkpoint record.

This document records the Python support baseline change that followed Dependabot warnings about Python 3.9 support.

## Purpose

The goal of this checkpoint is to preserve the audit trail for the Python support baseline decision and the correction made during review.

## Background

Dependabot surfaced warnings about future support expectations around Python 3.9.

The repository previously declared:

```text
requires-python = ">=3.9"
```

## Reviewed outcome

The support baseline was raised to:

```text
requires-python = ">=3.11"
```

This drops the old Python 3.9 baseline while remaining compatible with the current CI runtime observed during review.

## Rejected outcome

A stricter baseline was briefly proposed during review:

```text
requires-python = ">=3.14"
```

That stricter baseline was rejected because the active CI runtime used Python 3.11 and package installation failed with the stricter requirement.

The final merged change is therefore `>=3.11`, not `>=3.14`.

## Scope

This checkpoint records a package metadata support-policy change only.

The change did not intentionally modify:

- dependency versions;
- workflow logic;
- runtime code;
- schema files;
- validator logic;
- record contents;
- signing behavior;
- federation behavior;
- generated artifacts;
- QR semantics.

## Operational rule

Future Python baseline changes must be reviewed against:

- the active CI Python version;
- dependency support expectations;
- runtime/API test compatibility;
- package installation behavior;
- advisory-only runtime boundaries.

## Final boundary

A newer Python baseline can improve support hygiene.

A newer Python baseline is not a trust guarantee.

Trust the record, not the narrative.
