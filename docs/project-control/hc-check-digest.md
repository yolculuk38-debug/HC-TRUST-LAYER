# HC Check Digest

HC Check Digest is a report-only PR health summary for HC-TRUST-LAYER review
signals. It groups check, review, thread, automation-helper, and artifact
metadata into a compact digest for human maintainers.

## Authority boundary

HC Check Digest is advisory-only:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- no approval authority
- no merge authority
- no repository mutation
- no label mutation
- no reviewer mutation
- no PR comments in v2

It does not approve, reject, label, assign, comment, or merge. Humans retain
final authority for review and merge decisions.

Codex review comments, P1/P2/P3 feedback, and review threads are included only as
external review signals. Codex is not an approval authority and does not replace
human-supervised validation.

## v1 local digest engine

`scripts/hc_check_digest.py` is the deterministic local engine. It reads local
JSON inputs and renders JSON or Markdown. The script remains network-free,
GitHub-API-free, and repository-mutation-free.

Local usage:

```bash
python scripts/hc_check_digest.py \
  --checks examples/hc-check-digest/checks-success-fixture.json \
  --reviews examples/hc-check-digest/reviews-codex-p2-fixture.json \
  --threads examples/hc-check-digest/threads-resolved-fixture.json \
  --artifacts examples/hc-check-digest/artifacts-fixture.json \
  --format json
```

Use `--format md` to render the same local signals as Markdown.

## v2 read-only PR workflow

`.github/workflows/hc-check-digest.yml` wraps the local engine for pull requests.
The workflow uses read-only GitHub API access only in
`scripts/hc_check_digest_github_adapter.py` to collect metadata for the PR head
SHA and PR review surface. The adapter converts that metadata into local JSON
inputs, then the existing local engine builds the digest.

The workflow may collect read-only metadata for:

- check runs and workflow runs for the PR head SHA
- PR reviews
- review comments or available review-thread style metadata
- workflow artifacts

The workflow writes:

- `hc-check-digest.json`
- `hc-check-digest.md`

It publishes the Markdown digest to `$GITHUB_STEP_SUMMARY` and uploads both
digest outputs as an artifact named `hc-check-digest`.

## v2 non-mutation boundary

The v2 workflow never mutates PR state. It does not:

- comment on PRs
- approve PRs
- request reviewers
- add labels
- assign users
- merge
- enable auto-merge
- change repository contents

The workflow permissions are read-only: `contents: read`, `actions: read`,
`checks: read`, and `pull-requests: read`.

## Merge guidance

Merge guidance is deterministic and advisory:

- `do_not_merge` when blocking items exist.
- `human_review_before_merge` when no blocking items exist but advisory items exist.
- `merge_allowed_after_human_review` when required checks pass and no advisory
  issues are present.

The final decision remains with human maintainers under repository governance.
