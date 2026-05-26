# Failed Check Diagnosis Guide (HC:// Mobile PR Operations)

This guide provides a short, repeatable flow to diagnose failed pull request checks from a mobile-first workflow in HC-TRUST-LAYER.

Use this guide to identify failure type, take the first correct action, and avoid wasting time on stale or irrelevant failures.

## Quick Diagnosis Flow

1. Open the failed check in GitHub and read the exact job name.
2. Classify it into one of the buckets below:
   - terminology
   - docs drift
   - canonical artifact
   - CodeQL/security
   - auto-merge only
3. Take the first action listed for that bucket before rerun.
4. Rerun only when rerun is likely to produce new signal.
5. If there is no content change to address root cause, avoid rerun loops.

## Failure Types, Meaning, and First Action

### 1) Terminology failure

**How to identify**
- Check name includes Terminology Guard, or logs reference `scripts/check_terminology.py`.

**What it means**
- Content uses prohibited or non-canonical terms that conflict with HC:// and HC-TRUST-LAYER terminology baselines.

**First action**
- Fix wording in changed files to align with canonical terminology.
- Re-run local terminology guard after edits.

**When rerun is useful**
- After terminology content has been corrected and pushed.

**When rerun is useless without code/content change**
- If the same wording remains in branch content.

### 2) Docs drift failure

**How to identify**
- Check name includes docs drift, or logs reference `scripts/check_docs_drift.py`.

**What it means**
- Documentation index, linkage, or expected docs consistency is out of sync with changed content.

**First action**
- Update affected docs references/indexes required by repository docs drift expectations.
- Re-run docs drift guard locally.

**When rerun is useful**
- After docs synchronization changes are committed and pushed.

**When rerun is useless without code/content change**
- If drift source remains unresolved in the same commit set.

### 3) Canonical artifact failure

**How to identify**
- Check name includes canonical artifact, or logs reference `scripts/check_canonical_artifacts.py`.

**What it means**
- Repository-defined canonical artifact continuity checks detected mismatch or missing update.

**First action**
- Inspect changed files and restore canonical artifact consistency according to repository rules.
- If uncertain about boundary impact, escalate for human-supervised validation before additional edits.

**When rerun is useful**
- After canonical artifact consistency is restored with a new commit.

**When rerun is useless without code/content change**
- If artifact mismatch still exists in the same branch state.

### 4) CodeQL/security failure

**How to identify**
- Check name references CodeQL, security scan, or vulnerability/policy scan output.

**What it means**
- Security analysis found an issue, or security workflow execution failed and needs inspection.

**First action**
- Read exact finding and location.
- For docs-only PRs, verify whether failure is from code scanning outside changed scope versus a transient workflow issue.
- If a real finding is in scope, fix content/code root cause first.

**When rerun is useful**
- After root-cause fix is pushed.
- When logs indicate transient infrastructure failure (for example, timeout or runner interruption).

**When rerun is useless without code/content change**
- If actionable security finding remains unaddressed.

### 5) Auto-merge only failure

**How to identify**
- Failure appears in trusted auto-merge or merge queue automation rather than content guard checks.

**What it means**
- Merge automation conditions were not met; content may still be valid.

**First action**
- Confirm whether PR is already merged or superseded.
- Confirm required guard checks (terminology, docs drift, canonical artifact) status independently.

**When rerun is useful**
- When automation state changed (for example, required review/check state is now satisfied).

**When rerun is useless without code/content change**
- If automation prerequisites are still unmet and no state has changed.

## Avoiding Stale/Cached Failure Confusion

Use this pattern to avoid wasting time on old workflow results:

1. Confirm latest commit SHA on the PR.
2. Ensure failed check you are viewing ran on that same SHA.
3. Ignore older failed runs tied to earlier SHAs once a newer valid run exists.
4. After pushing fixes, inspect only the newest run per workflow.
5. If rerunning, rerun the failed job on the latest SHA, not an outdated run page.

## Mobile-First Checklist

- [ ] Verify latest PR commit SHA before reading failures.
- [ ] Open failed job log and classify failure bucket.
- [ ] Apply first corrective action for that bucket.
- [ ] Run local guards where applicable:
  - `python3 scripts/check_terminology.py`
  - `python3 scripts/check_docs_drift.py`
  - `python3 scripts/check_canonical_artifacts.py`
- [ ] Push content fix before triggering rerun.
- [ ] Rerun only when branch content or workflow state changed.
- [ ] Re-check status on latest SHA only.
- [ ] Request human-supervised validation after checks pass.

## Warnings

- Never weaken policy or guard scripts just to pass a PR.
- Fix content first, rerun second.
- Auto-merge failures may be harmless if the PR is already merged.

## Cancelled Safe Auto Merge Interpretation

Cancelled Safe Auto Merge jobs are not always code/content failures.

Use this interpretation order:

1. Check required checks on the latest PR commit SHA.
2. Check whether the cancelled run is an older duplicate/concurrency-cancelled run.
3. Check unresolved review conversations before merge action.

Operational rule: successful required checks on the latest SHA carry more decision weight than a cancelled duplicate auto-merge job.

If required checks are green, unresolved conversations are resolved, and PR is mergeable, manual **Merge pull request** is an acceptable fallback.

If unresolved conversations remain, do not merge even if checks are green.
