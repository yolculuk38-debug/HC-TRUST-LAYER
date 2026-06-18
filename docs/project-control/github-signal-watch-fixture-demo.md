# HC Signal Watch GitHub Changelog Fixture Demo

> Status: local fixture demo
> Scope: end-to-end saved-fixture report generation
> Authority: advisory only
> Network access: not required
> Repository mutation: not required

## Purpose

This demo shows a maintainer how to run the HC Signal Watch GitHub Changelog fixture flow from a saved RSS fixture to local JSON and Markdown reports.

The flow is local fixture-only and report-only. It reads the saved fixture in `examples/hc-signal-watch/github-changelog-rss-fixture.xml`, writes outputs to a temporary directory, and does not fetch live GitHub Changelog data or mutate repository state.

## Safety markers

Expected boundaries for this demo:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
network_access=false
repository_mutation=false
issue_comment_automation=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

These markers mean the output is advisory evidence for human-supervised review. The demo does not create issues or comments, change labels or reviewers, approve pull requests, merge pull requests, or claim truth, correctness, production readiness, legal authority, identity finality, forensic certainty, or autonomous governance authority.

## Full local fixture flow

Run from the repository root.

### 1. Create a temporary output directory

```bash
SIGNAL_WATCH_TMP="$(mktemp -d)"
printf 'HC Signal Watch fixture output: %s\n' "$SIGNAL_WATCH_TMP"
```

The directory is outside tracked repository paths unless your local `TMPDIR` points inside the repository.

### 2. Normalize the saved GitHub Changelog RSS fixture

```bash
python scripts/hc_signal_watch_rss_ingest.py \
  examples/hc-signal-watch/github-changelog-rss-fixture.xml \
  > "$SIGNAL_WATCH_TMP/github-changelog-signals.json"
```

This step reads only the saved XML fixture and writes normalized advisory Signal Watch JSON. It does not perform live RSS fetching or network calls.

Optional local inspection:

```bash
python -m json.tool "$SIGNAL_WATCH_TMP/github-changelog-signals.json" \
  > "$SIGNAL_WATCH_TMP/github-changelog-signals.pretty.json"
```

### 3. Generate a JSON Signal Watch report

```bash
python scripts/hc_signal_watch_report.py \
  --changelog-signals "$SIGNAL_WATCH_TMP/github-changelog-signals.json" \
  --format json \
  > "$SIGNAL_WATCH_TMP/hc-signal-watch-report.json"
```

### 4. Generate a Markdown Signal Watch report

```bash
python scripts/hc_signal_watch_report.py \
  --changelog-signals "$SIGNAL_WATCH_TMP/github-changelog-signals.json" \
  --format md \
  > "$SIGNAL_WATCH_TMP/hc-signal-watch-report.md"
```

### 5. Review the local outputs

```bash
printf 'Generated files:\n'
printf '  %s\n' \
  "$SIGNAL_WATCH_TMP/github-changelog-signals.json" \
  "$SIGNAL_WATCH_TMP/hc-signal-watch-report.json" \
  "$SIGNAL_WATCH_TMP/hc-signal-watch-report.md"
```

Optional preview:

```bash
sed -n '1,120p' "$SIGNAL_WATCH_TMP/hc-signal-watch-report.md"
```

## Cleanup

Remove the temporary output directory when it is no longer needed:

```bash
rm -rf "$SIGNAL_WATCH_TMP"
```

Only remove the temporary directory you created for this demo. Do not remove repository fixtures, records, schemas, validators, signing material, federation material, workflows, generated artifacts, or canonical records.

## Non-goals

This fixture demo does not add or authorize:

- live RSS fetching;
- network calls;
- repository mutation;
- issue or comment creation;
- label or reviewer mutation;
- approval automation;
- merge automation;
- workflow changes;
- runtime API changes;
- validator changes;
- schema changes;
- canonical record changes;
- signing changes;
- federation changes;
- generated artifact updates.

Human review remains required before any follow-up repository action.
