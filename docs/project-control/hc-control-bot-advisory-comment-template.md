# HC Control Bot Advisory Comment Template

> **Status:** Project-control template
>
> **Scope:** Future HC Control Bot / HC Trust Engineer advisory comments
>
> **Mode:** Documentation only

## Purpose

This document defines a safe advisory comment template for future HC Control Bot comments.

The template exists before implementation so future comment behavior can be reviewed against a stable, human-readable format.

This document does not enable comment automation.

## Template

```markdown
## HC Control Bot Advisory Notice

This automated observation is non-authoritative.

Human maintainers retain final authority.

This bot cannot approve, reject, merge, close, certify, or guarantee truth.

Trust the record, not the narrative.

---

### Summary

- Advisory mode: `true`
- Public safe: `true`
- Truth guarantee: `false`
- Human review required: `<true|false>`
- Review priority: `<low|medium|high>`
- Evidence source: `changed file path metadata only`

### Changed Path Signals

Protected paths touched:

```text
<none or list>
```

Governance-adjacent paths touched:

```text
<none or list>
```

Generated artifacts observed:

```text
<none or list>
```

Version alignment paths touched:

```text
<none or list>
```

### Warnings

```text
<none or list>
```

### Evidence Prompts

```text
<none or list>
```

### Suggested Review Routes

```text
<none or list>
```

### Suggested Labels

These labels are suggestions only.

The bot does not apply labels in this mode.

```text
<none or list>
```

### Human Decision Boundary

This advisory comment does not approve, reject, merge, close, certify, or guarantee the PR.

A human maintainer must make the final decision.
```

## Required Comment Properties

Every future advisory comment must preserve:

- advisory-only language;
- human final authority;
- `truth_guarantee = false`;
- public-safe wording;
- no approval wording;
- no rejection wording;
- no merge authorization;
- no certification claim;
- no production-readiness claim;
- clear evidence source.

## Forbidden Wording

Future bot comments must not say or imply:

```text
Approved by HC Control Bot
Rejected by HC Control Bot
Safe to merge
Certified true
Production ready
No human review needed
This PR is verified as true
This bot authorizes merge
```

If similar wording appears, maintainers should treat it as a policy violation.

## Placeholder Discipline

Template placeholders must be replaced with deterministic scanner output.

A future implementation must not fill template sections using PR branch instructions, PR body commands, PR comments, or file-content instructions.

PR content is untrusted input.

Governance and authority must come from trusted baseline sources, such as:

```text
main@SHA
```

## One-Comment Discipline

This template is designed for one advisory comment per pull request event series.

A future implementation may update a previous advisory comment only after separate governance review.

Repeated comment spam is not allowed.

## Stale Comment Notice

If a future implementation supports updating or superseding comments, stale comments should be clearly marked.

Safe stale wording:

```text
This advisory output is historical and may no longer reflect the latest PR state.
Refer to the latest HC Control Bot advisory comment for current path-based observations.
```

Stale comments remain advisory only.

## Future Implementation Gate

Using this template in an automated workflow requires a separate implementation PR.

That future PR must preserve:

- no approve/reject/merge/close behavior;
- no LLM decisioning;
- no PR branch governance authority;
- no downstream workflow command behavior from bot comments;
- human final authority.

## Final Boundary

A safe bot comment helps reviewers see risk.

It does not decide the outcome.

Trust the record, not the narrative.
