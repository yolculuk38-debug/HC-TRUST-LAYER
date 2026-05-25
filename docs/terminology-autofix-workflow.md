# Terminology Autofix Suggest Workflow (Advisory)

HC-TRUST-LAYER includes an advisory-only GitHub Actions workflow at `.github/workflows/terminology-autofix-suggest.yml` to assist documentation PR review when Terminology Guard fails on known forbidden phrases.

## Purpose

When `scripts/check_terminology.py` fails on a pull request, the workflow runs `python3 scripts/autofix_terminology.py` in dry-run mode and publishes a report artifact (`terminology-autofix-report.txt`) for reviewer use.

The report includes:

- detected forbidden phrases
- suggested replacements
- affected files
- remaining unresolved phrases

## Why Autofix Is Bounded

This workflow is intentionally bounded to preserve trust-kernel safety and review integrity:

- It does **not** run with `--write`, so it does not modify repository files.
- It does **not** commit, push, auto-merge, or bypass review.
- It does **not** change policy rules, validator behavior, or terminology guard enforcement.

## Why Policy Guards Must Remain Strict

Terminology Guard remains the canonical enforcement control for forbidden language. The advisory workflow is a repair aid only and cannot weaken, suppress, or replace guard outcomes. Guard failures still require corrective changes in the PR before merge.

## Why Human Review Still Exists

Human-supervised validation remains required because phrase-level replacement suggestions can require context-sensitive interpretation. Reviewers confirm language intent, provenance continuity, and protocol boundary correctness before accepting edits.

## Safe vs Unsafe Automation Boundaries

### Safe automation in this workflow

- Detecting known forbidden phrases via existing guard logic.
- Producing non-destructive replacement suggestions.
- Publishing advisory artifacts for reviewer triage.

### Unsafe automation excluded by design

- Direct file mutation in CI.
- Automatic commits or branch rewrites.
- Automatic merges based on suggestion output.
- Any change to trust-kernel, policy evaluator, validator, signing, or federation semantics.
