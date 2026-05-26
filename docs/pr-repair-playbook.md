# PR Repair Playbook (Terminology Guard)

This playbook helps repair pull requests when Terminology Guard fails on forbidden language.

## When to Use

Use this workflow when CI reports terminology violations (for example, `truth score`) and you need a safe local fix path.

For broader failed-check triage (terminology, docs drift, canonical artifact, CodeQL/security, and auto-merge-only outcomes), see `docs/failed-check-diagnosis.md`.

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

## Merge-Blocking Conversation and Auto-Merge Notes

After terminology repair and passing checks:

1. Confirm required checks passed on the latest SHA.
2. Confirm unresolved review conversations are resolved appropriately.
3. If Safe Auto Merge shows cancelled due to duplicate/concurrency behavior, use manual **Merge pull request** only when PR is mergeable and review threads are clear.

Do not treat a cancelled duplicate auto-merge run as proof of branch failure when required checks are successful.

Do not merge when unresolved review conversations remain.

For mobile-first merge flow details, use `docs/mobile-pr-merge-guide.md`.
