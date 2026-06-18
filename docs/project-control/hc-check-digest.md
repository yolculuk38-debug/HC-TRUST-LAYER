# HC Check Digest v1

HC Check Digest v1 is a deterministic, repo-local summary for PR health signals.
It reads local JSON inputs and renders a human-readable digest in JSON or Markdown.

Checks, reviews, threads, and artifact records are raw signals. The digest groups
those signals so a maintainer can quickly see what appears blocking, advisory,
automation-helper related, external-review related, or artifact related.

## Authority boundary

HC Check Digest is advisory-only:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `network_access=false`
- `repository_mutation=false`
- `approval_authority=false`
- `merge_authority=false`

It does not approve, reject, label, assign, comment, or merge. It does not call
the GitHub API, fetch from the network, or mutate the repository. Humans retain
final authority for review and merge decisions.

Codex review comments, P1/P2/P3 feedback, and review threads are included only as
external review signals. Codex is not an approval authority and does not replace
human-supervised validation.

## Local usage

```bash
python scripts/hc_check_digest.py \
  --checks examples/hc-check-digest/checks-success-fixture.json \
  --reviews examples/hc-check-digest/reviews-codex-p2-fixture.json \
  --threads examples/hc-check-digest/threads-resolved-fixture.json \
  --artifacts examples/hc-check-digest/artifacts-fixture.json \
  --format json
```

Use `--format md` to render the same local signals as Markdown.

## Merge guidance

Merge guidance is deterministic and advisory:

- `do_not_merge` when blocking items exist.
- `human_review_before_merge` when no blocking items exist but advisory items exist.
- `merge_allowed_after_human_review` when required checks pass and no advisory
  issues are present.

The final decision remains with human maintainers under repository governance.
