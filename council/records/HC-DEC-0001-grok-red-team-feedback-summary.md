# HC-DEC-0001 — Grok Red-Team Feedback Summary

Status: advisory evidence only.

This record summarizes external Grok red-team, abuse-risk, and failure-mode feedback for HC-DEC-0001.

Main advisory points:

- The strongest product risk is perception creep: users may treat integrity signals as truth guarantees.
- Public verifier language must avoid absolute claims such as truth, authenticity, approval, or final verification.
- QR and record pages must clearly explain that hash match does not mean content truth.
- GitHub main@SHA remains a useful audit anchor, but sensitive paths still require protected review and regular audit.
- Witnesses should remain advisory and should not become automatic trust scores.
- AI-generated summaries must remain secondary to primary record evidence.
- Public demos should be clearly marked as advisory and non-production when applicable.
- HC Control Bot should remain read-only, low-noise, and advisory.

Recommended hardening order:

1. Put advisory-only disclaimers in README, verifier outputs, QR pages, examples, and demos.
2. Review all public wording to avoid overclaiming.
3. Keep protected paths and branch protection strict for trust-kernel files.
4. Require hash recomputation and mismatch warnings in verifiers.
5. Document QR and failure-mode demo scenarios clearly.
6. Require evidence bundles for witness or public record claims.
7. Publish responsible-use and reporting guidance.
8. Test the system internally with adversarial examples before wider public use.

Important visible warnings:

- HC-TRUST-LAYER provides cryptographic integrity and provenance signals only.
- It does not guarantee truth, authenticity, factual accuracy, or legal validity.
- Human judgment is required.
- Data Before Narrative.

Integrity boundary:

This document does not change runtime behavior, workflows, schemas, validators, bot permissions, final decision state, release status, or truth guarantees.
