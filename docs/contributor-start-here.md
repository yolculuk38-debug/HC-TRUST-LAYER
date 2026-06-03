# Contributor Start Here

> **Documentation Status**
> - **status:** GUIDE
> - **scope:** Beginner contributor orientation for HC-TRUST-LAYER.
> - **canonical relevance:** Advisory onboarding surface; not a canonical record, schema, validator, policy, signing, federation, or runtime surface.
> - **runtime relevance:** None; this guide does not define runtime enforcement logic.

## 1. Purpose

This guide is the beginner-friendly entrypoint for first-time HC-TRUST-LAYER contributors.

Use it to understand what the repository is, which documents to read first, what work is safe to start with, which surfaces are protected, what checks to run, and when to stop for human review.

## 2. What HC-TRUST-LAYER Is

HC-TRUST-LAYER is early-stage HC:// verification infrastructure.

HC:// focuses on verification workflow transparency, provenance visibility, audit trail continuity, and human-supervised validation. The repository contains documentation, examples, scripts, records, and implementation surfaces that support a verification map and protocol graph for reviewable trust workflows.

Repository evidence is authoritative. Do not replace in-repository architecture notes, implementation status, validation outputs, or documented boundaries with external assumptions.

HC-TRUST-LAYER does not provide objective truth finality, forensic certainty, autonomous governance, or unsupported security guarantees.

## 3. First-Time Contributor Path

Start with a small, documentation-only change unless a maintainer has asked you to do something else.

Recommended path:

1. Read this guide from top to bottom.
2. Read the repository `README.md` for the current project overview.
3. Read `CONTRIBUTING.md` for contribution expectations and PR policy.
4. Pick a beginner-safe issue or a small documentation improvement.
5. Keep your branch focused on one topic.
6. Run the required checks before opening a PR.
7. Ask for review before changing sensitive surfaces.

## 4. Recommended Read Order

For a first pass, read in this order:

1. `README.md` — repository entrypoint and current orientation.
2. `CONTRIBUTING.md` — contribution workflow and review expectations.
3. `docs/limitations-and-risks.md` — current limitations and boundary language.
4. `docs/verification-map.md` — verification map orientation.
5. `docs/protocol-graph-index.md` — protocol graph navigation aid.
6. `docs/trust-kernel-index.md` — advisory trust kernel routing index.
7. `docs/pr-scope-boundaries.md` — PR scope and sensitive-surface guidance.
8. `SECURITY.md` — security and vulnerability reporting path.

You do not need to understand every document before making a typo fix or link repair. You do need to understand protected paths before changing anything that could affect HC:// behavior, records, policy, validation, signing, or governance controls.

## 5. Safe First Contributions

Beginner-safe work usually includes:

- typo fixes
- broken links
- documentation clarity
- navigation improvements
- small examples that do not change protocol behavior
- contributor guide improvements

Keep safe first contributions narrow. A good first PR should be easy to review, easy to revert, and clearly non-behavioral.

## 6. Work That Requires Review First

Stop and ask for review before working on changes involving:

- workflows
- runtime
- schemas
- validators
- records
- policy
- federation
- signing
- trust-kernel indexes
- governance-control changes

Human-supervised validation remains required for sensitive trust-kernel-impacting changes.

If you are unsure whether a change is trust-kernel-impacting, treat it as review-required.

## 7. Protected Paths and Sensitive Surfaces

Do not modify protected paths unless the task explicitly requests it and the expected review path is clear.

Protected or sensitive surfaces include:

- `.github/workflows/**`
- `schema/**`
- `validators/**`
- `records/**`
- `policy/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- trust-kernel indexes
- runtime verification behavior
- signing and trust anchor semantics
- validator logic
- policy evaluator behavior
- federation behavior
- governance-control changes

Canonical record boundaries are high-sensitivity surfaces. Changes that affect deterministic serialization, hash-linked artifacts, record identity, or provenance continuity require explicit reviewer attention.

## 8. Local Setup Quickstart

Basic setup:

```bash
git clone <repository-url>
cd HC-TRUST-LAYER
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you are only editing Markdown, you may not need every runtime dependency, but you should still run the documentation checks listed below when possible.

## 9. Checks to Run

For documentation-only contributions, run:

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
git diff --check
```

If your change touches code or executable behavior, run the relevant tests and validators for that area. Do not weaken guards, policy checks, or validation logic to make checks pass.

If a check cannot run in your environment, say so in the PR and do not imply success.

## 10. Issue Reporting Path

When reporting an issue:

1. Search existing issues or docs to avoid duplicates.
2. Describe the observed problem and where it appears.
3. Link to the affected file, section, command, or check output.
4. Explain whether the issue appears documentation-only or may affect protected surfaces.
5. Avoid claiming security impact unless the evidence supports it.

For sensitive security concerns, use the security reporting path instead of a public issue.

## 11. Pull Request Path

For a small PR:

1. Create a focused branch, such as `docs/contributor-start-here`.
2. Make one scoped change.
3. Confirm the diff does not include unrelated files.
4. Run the required checks.
5. Open a PR with a concise title and evidence-based summary.
6. List changed files, checks run, and any checks that could not run.
7. Request review when the change touches protected or ambiguous boundaries.

Keep PRs small enough to review and revert safely.

## 12. Security and Vulnerability Reporting

Use `SECURITY.md` for security and vulnerability reporting.

Do not disclose sensitive vulnerability details in a public issue if doing so could increase risk. Keep reports factual, scoped, and evidence-based. Do not claim security certification, forensic certainty, or guaranteed exploitability unless those claims are supported by repository evidence and reviewer validation.

## 13. AI-Assisted Contributions

AI-assisted contributions are allowed only if reviewed, scoped, and evidence-based.

If you use AI assistance:

- verify the output against repository evidence
- preserve HC:// and HC-TRUST-LAYER terminology
- keep the change small and auditable
- disclose AI assistance if the project workflow or reviewer asks for it
- do not let AI output override repository-defined boundaries
- do not introduce unsupported claims or behavior changes

Agent output is advisory until reviewed through repository-defined checks and human-supervised validation where required.

## 14. What Not To Claim

Do not claim:

- production readiness
- security certification
- forensic certainty
- truth finality
- autonomous governance
- complete dispute automation
- live federation guarantees
- cryptographic or policy guarantees not backed by tests and documentation

Use careful language such as "verification signal," "review boundary," "current repository evidence," and "requires human-supervised validation" when describing HC:// outcomes.

## 15. When To Stop and Ask

Stop and ask for review when:

- the change touches a protected path or sensitive surface
- the change may alter verification behavior
- the change may affect schemas, records, validators, policy, signing, federation, or governance controls
- you cannot determine whether a claim is supported by repository evidence
- a required check fails and the fix is not documentation-only
- you are tempted to broaden the PR beyond the original task
- the change could affect trust kernel boundaries or audit trail continuity

When in doubt, stop before editing and ask for maintainer guidance.

## 16. Related Documents

- `README.md`
- `CONTRIBUTING.md`
- `docs/community-governance.md`
- `SECURITY.md`
- `docs/limitations-and-risks.md`
- `docs/verification-map.md`
- `docs/verification-map-index.md`
- `docs/protocol-graph-index.md`
- `docs/trust-kernel-index.md`
- `docs/pr-scope-boundaries.md`
- `docs/trust-impact-analysis.md`
- `docs/trust-review-workflow.md`
- `docs/ai-assisted-review.md`
- `docs/ai-collaboration-workflow.md`
