# PR Repair Playbook (Terminology Guard)

This playbook helps repair pull requests when Terminology Guard fails on forbidden language.

## When to Use

Use this workflow when CI reports terminology violations (for example, `truth score`) and you need a safe local fix path.

## Commands

Run dry-run first (default):

```bash
python3 scripts/autofix_terminology.py
```

Apply safe replacement locally:

```bash
python3 scripts/autofix_terminology.py --write
```

Re-run Terminology Guard:

```bash
python3 scripts/check_terminology.py
```

## What the Autofix Does

- Scans repository text files.
- Replaces exact forbidden phrase `truth score` with `advisory trust summary`.
- Never edits binary files.
- Never edits `.git` content.
- Skips generated cache/artifact folders.
- Prints changed files.
- Prints remaining violations, if any.

## Mobile-First PR Repair Checklist

1. Pull latest branch state locally.
2. Run dry-run: `python3 scripts/autofix_terminology.py`.
3. Review listed violations and target files.
4. Run write mode: `python3 scripts/autofix_terminology.py --write`.
5. Review git diff for scoped terminology-only changes.
6. Run guard checks:
   - `python3 scripts/check_terminology.py`
   - `python3 scripts/check_docs_drift.py`
   - `python3 scripts/check_canonical_artifacts.py`
7. Commit with clear provenance and push.
8. Confirm CI passes before requesting human-supervised validation.

## Safety Warnings

- Do **not** weaken, bypass, or disable Terminology Guard.
- Do **not** replace advisory-only wording with truth guarantee language.
- Preserve HC:// and HC-TRUST-LAYER terminology.
