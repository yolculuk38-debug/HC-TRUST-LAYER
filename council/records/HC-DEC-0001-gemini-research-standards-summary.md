# HC-DEC-0001 — Gemini Research and Standards Feedback Summary

Status: advisory evidence only.

This record summarizes external Gemini research and standards feedback for HC-DEC-0001.

Main advisory points:

- Position HC-TRUST-LAYER as an Advisory Consensus Broker.
- Keep the trust root lightweight, deterministic, local, and file-based.
- Treat C2PA, W3C Verifiable Credentials, and OpenTimestamps as complementary evidence standards.
- Preserve repository state, especially main@SHA, as a primary audit anchor.
- Keep AI advisory-only and preserve human maintainer final authority.
- Do not implement custom distributed consensus, production LLM workflows, or a standardized public witness API yet.

Future advisory suggestion:

- Consider a deterministic repository context manifest validator for .github/hc_context.json in a later PR.

Integrity boundary:

This document does not change runtime behavior, workflows, schemas, validators, bot permissions, final decision state, release status, or truth guarantees.
