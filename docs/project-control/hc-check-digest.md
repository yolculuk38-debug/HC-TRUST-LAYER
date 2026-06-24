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

PR review automation comments, P1/P2/P3 feedback, and review threads are included only as
external review signals. PR review automation is not an approval authority and does not replace
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
- REST review comments as non-blocking external review signals
- true review-thread metadata when resolved/outdated state is available
- workflow artifacts

The adapter follows GitHub pagination for list endpoints so later pages of
checks, reviews, review comments, workflow runs, and artifacts are included in
the local digest inputs. REST review comments are not treated as unresolved
threads because they do not carry reliable resolved-thread state. Only true
review-thread metadata with resolved/outdated state may create unresolved-thread
blocking signals.

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

## Refresh behavior

The v2 workflow refreshes on scoped pull request updates, PR review submissions
or edits, PR review comment changes, completed external check runs, and selected
completed GitHub Actions workflows, and commit status changes. This lets the
digest update after required checks complete or fail, after PR review automation P1/P2 feedback
appears, and after human review activity changes the PR health picture.

`workflow_run` refreshes are limited to named upstream check workflows and do
not include `HC Check Digest`. `check_run` refreshes also skip HC Check Digest
check names. For `status` events, the adapter resolves the related pull request
from the commit SHA using read-only API access before building local digest
inputs. These guards avoid a self-triggering digest loop.

Each refresh fetches live metadata at run time instead of relying only on the
event payload. The workflow intentionally does not use GitHub concurrency. Even
with `cancel-in-progress` disabled, GitHub may cancel older pending runs in the
same concurrency group, which can leave a cancelled HC Check Digest check on a
PR before the JSON output, Markdown output, job summary, and artifact are
published. Instead, each useful refresh is allowed to finish, while self-trigger
or no-op HC Check Digest events skip at the job guard before checkout or
metadata collection whenever possible. This avoids cancelled digest check noise
without adding write permissions or mutation.

Refreshes only rebuild the report, publish the job summary, and upload the
artifact. They do not comment, label, assign, approve, merge, enable auto-merge,
or otherwise mutate PR or repository state.

## v3 post-merge smoke snapshots

Post-merge smoke fixtures live in
`examples/hc-check-digest/post-merge-smoke/`. They provide deterministic local
inputs for a compact end-to-end digest shape that includes:

- passing required checks;
- one advisory warning;
- one failed required check;
- one open PR review automation `[P2]` review signal;
- one resolved review thread;
- one unresolved non-outdated review thread;
- available `hc-check-digest` artifact metadata.

The same directory stores expected snapshots for:

- `expected-hc-check-digest.json`
- `expected-hc-check-digest.md`
- `expected-job-summary.md`

Run the smoke locally with:

```bash
python scripts/hc_check_digest.py \
  --checks examples/hc-check-digest/post-merge-smoke/checks.json \
  --reviews examples/hc-check-digest/post-merge-smoke/reviews.json \
  --threads examples/hc-check-digest/post-merge-smoke/threads.json \
  --artifacts examples/hc-check-digest/post-merge-smoke/artifacts.json \
  --format json
```

Use `--format md` for the Markdown digest. To render the same advisory job
summary wrapper used by the workflow snapshot, run:

```bash
python scripts/hc_check_digest_render_summary.py \
  examples/hc-check-digest/post-merge-smoke/expected-hc-check-digest.json
```

The snapshots prove that the local JSON output, Markdown output, and job-summary
wrapper remain stable and human-readable for representative post-merge signals.
They also prove that advisory-only warnings remain non-blocking, resolved or
outdated review threads remain non-blocking, unresolved non-outdated review
threads block, failed required checks block, and open PR review automation P1/P2 feedback blocks.

This is snapshot and report coverage only. It adds no workflow permission
expansion, no PR comments, no labels, no assignments, no approvals, no merge or
auto-merge authority, no repository mutation, and no network access to the local
digest engine. Humans retain final authority.

## Merge guidance

Merge guidance is deterministic and advisory:

- `do_not_merge` when blocking items exist.
- `human_review_before_merge` when no blocking items exist but advisory items exist.
- `merge_allowed_after_human_review` when required checks pass and no advisory
  issues are present.

The final decision remains with human maintainers under repository governance.

## v4 repo-health signal pack

v4 adds a deterministic repo-health signal pack to the existing report-only
HC Check Digest output. The local engine can include a `repo_health_signals`
section grouped by:

- `changelog` for local GitHub Changelog or release-note signals;
- `dependabot` for local Dependabot update notes;
- `codeql` for local CodeQL baseline notes;
- `weekly_summary` for a recurring weekly repo health summary.

The local fixture inputs live in `examples/hc-check-digest/repo-health/`:

- `github-changelog-signals.json`
- `dependabot-update-notes.json`
- `codeql-baseline-notes.json`
- `weekly-repo-health-summary.json`

The repo-health pack distinguishes `blocker`, `advisory`,
`neutral/baseline`, and `informational` entries. GitHub Changelog and release
note signals are advisory unless a local fixture explicitly marks them blocking.
Dependabot update notes are advisory unless a local fixture explicitly marks a
security or blocking condition, including `security=true`, `security_blocking=true`,
or `security` / `blocking` values in `level`, `severity`, `category`, or `type`.
CodeQL baseline notes are neutral or advisory unless a local fixture explicitly
marks them blocking. The weekly repo health summary is report-only and remains
informational or advisory only.

Local usage:

```bash
python scripts/hc_check_digest.py \
  --repo-health examples/hc-check-digest/repo-health/github-changelog-signals.json \
  --repo-health examples/hc-check-digest/repo-health/dependabot-update-notes.json \
  --repo-health examples/hc-check-digest/repo-health/codeql-baseline-notes.json \
  --repo-health examples/hc-check-digest/repo-health/weekly-repo-health-summary.json \
  --format json
```

Expected JSON and Markdown snapshots are stored in the same repo-health fixture
directory. They prove the output shape remains stable for changelog,
Dependabot, CodeQL baseline, and weekly summary signals.

The v4 repo-health pack is local-file only. It does not call the network, does
not call the GitHub API, does not comment on PRs, does not add labels, does not
assign users, does not approve, does not merge, and does not enable auto-merge.
It only summarizes fixture data for human review.

This differs from Signal Watch. Signal Watch tracks external ecosystem signals
through its own local fixture-based signal support. HC Check Digest v4 consumes
local repo-health fixture summaries as part of the PR health digest shape. It
does not replace Signal Watch, does not fetch Signal Watch data, and does not
create independent authority from those signals.

Humans retain final authority. Repo-health signals are advisory report inputs;
they do not provide production readiness, legal truth, identity finality,
forensic certainty, certification authority, autonomous governance authority, or
guaranteed correctness.
