# HC-DEC-0001 — Meta Product Feedback Summary

Status: advisory evidence only.

This record summarizes external Meta product and UX feedback for HC-DEC-0001.

Main advisory points:

- Start with one simple verification flow.
- Keep the MVP read-only, no-login, and easy to run from web and CLI.
- Use GitHub Pages and repository files as the first public demo surface.
- Keep GitHub main@SHA visible as the audit anchor.
- Show users verification status, hash match, witness presence, source link, trust root, timestamp, and advisory disclaimer.
- Keep merge authority, witness policy, record changes, governance edits, and incident handling maintainer-only.
- HC Control Bot should be low-noise: one helpful comment on important files, silent on routine documentation changes.
- Contributor onboarding should focus on one successful verification in under ten minutes.
- Postpone advanced integrations, hosted APIs, federation, and AI memory until the deterministic core is stable.

Recommended implementation order:

1. Lock the deterministic record schema and SHA-256 hash behavior.
2. Provide one example record and one local verification command.
3. Add a minimal public verifier using GitHub Pages.
4. Keep HC Control Bot advisory-only and focused on trust-kernel file changes.
5. Add public limitations and risk language before expanding integrations.
6. Treat C2PA, W3C Verifiable Credentials, OpenTimestamps, mirrors, and hosted APIs as later optional evidence layers.

Integrity boundary:

This document does not change runtime behavior, workflows, schemas, validators, bot permissions, final decision state, release status, or truth guarantees.
