# HC-DEC-0001 — External AI Council Feedback Synthesis

Status: advisory synthesis only.

This document summarizes the external AI Council evidence records collected for HC-DEC-0001.

## Source records

| Reviewer | Focus | Record |
|---|---|---|
| Claude | Governance, risk, authority boundaries | `council/records/HC-DEC-0001-claude-governance-summary.md` |
| Gemini | Research, standards, trust-root architecture | `council/records/HC-DEC-0001-gemini-research-standards-summary.md` |
| Meta | Product, UX, public verifier, contributor flow | `council/records/HC-DEC-0001-meta-product-feedback-summary.md` |
| Grok | Red-team, abuse risk, failure modes | `council/records/HC-DEC-0001-grok-red-team-feedback-summary.md` |
| Copilot | Implementation, testing, maintainability | `council/records/HC-DEC-0001-copilot-implementation-feedback-summary.md` |

## Common findings

The Council feedback converges on the same operating model:

- HC-TRUST-LAYER must remain advisory-only.
- Human maintainers retain final authority.
- The deterministic trust root must be stronger than any AI explanation.
- Repository state, especially `main@SHA`, is a key audit anchor.
- Hash, record structure, witness evidence, and public auditability come before AI-generated interpretation.
- Public language must avoid overclaiming truth, authenticity, approval, or legal validity.
- The bot should provide low-noise advisory reports, not decisions.

## Practical synthesis

The project should treat external AI feedback as design evidence, not runtime authority.

The correct path is:

1. Record external feedback as Council evidence.
2. Summarize shared conclusions in this synthesis record.
3. Convert stable conclusions into governance rules.
4. Implement deterministic scripts that read explicit repository configuration.
5. Emit advisory reports for human maintainer review.

## Bot design implication

HC Control Bot should not decide, approve, reject, close, or merge.

Its first reliable implementation target should be a deterministic changed-file scanner and structured advisory report artifact.

Recommended first implementation scope:

- read protected-path configuration from repository-controlled files,
- compare changed files against protected paths,
- emit structured JSON,
- flag trust-kernel touches,
- preserve advisory-only language,
- require human maintainer review for final action.

## Deferred work

The following should remain deferred until the deterministic core is stable:

- advanced AI interpretation,
- autonomous bot actions,
- external standards integrations,
- public hosted APIs,
- federation or multi-operator networks,
- automatic scoring or ranking.

## Final synthesis statement

HC-TRUST-LAYER should build trust from deterministic records, cryptographic integrity checks, repository auditability, and human authority. AI can explain, summarize, and warn, but it must not become the trust anchor.

## Integrity boundary

This document is not a final decision, release approval, production-readiness statement, or truth guarantee. It is an advisory synthesis record for human maintainer review.

This document does not change runtime behavior, workflows, schemas, validators, bot permissions, final decision state, or release status.
