# QR Verification Security Model

This document defines a permission-aware HC:// QR verification entry model for HC-TRUST-LAYER.

QR verification remains advisory-only and requires human-supervised validation.

## Scope

- Documentation-only guidance for QR verification entry behavior.
- No canonical schema changes.
- No validator, guard, signing, federation, or policy weakening.
- No private data storage in QR payloads.

## Design principles

1. **Minimal verification parameters only**
   - QR payloads should carry only non-secret parameters needed to open a verification entry page.
   - Typical parameters are bounded identifiers such as `record` and optional `hash` comparison input.

2. **No private secrets in QR**
   - QR content must not include API keys, credentials, private tokens, personal secrets, or hidden trust anchors.
   - QR payloads are treated as public and copyable by default.

3. **QR opens verification entry, not automatic trust**
   - Scanning a QR code routes the user to a verification page.
   - A scan event does not grant trust, authority, or truth status.

4. **Required visible verification context**
   - The verification page must clearly show:
     - record ID
     - hash status (match/mismatch/missing)
     - canonical source link
     - advisory verification boundary language

5. **Explicit spoofing-risk awareness**
   - QR-based entry introduces redirection and impersonation risk.
   - Users and reviewers must evaluate domain, route, and canonical link continuity before relying on results.

## Permission-aware verification flow

1. User scans HC:// QR code.
2. User is routed to a verification entry page (for example `docs/verify.html`).
3. Page displays input and expected continuity details (record ID, full hash state, canonical source link).
4. User confirms official domain and route.
5. User reviews advisory-only result state.
6. User escalates consequential use to human-supervised validation.

This flow is designed to keep QR interaction low-friction while preserving trust-kernel boundaries and audit trail clarity.

## QR threat model

### 1) Malicious QR redirect

Risk: A QR points to an attacker-controlled domain that mimics HC:// verification UX.

Mitigation: Require explicit official domain and page check before accepting any verification output.

### 2) Copied QR

Risk: A legitimate-looking copied QR is reused out of context.

Mitigation: Verify record ID visibility, canonical source linkage, and advisory boundary text on the official HC-TRUST-LAYER verification page.

### 3) Stale QR

Risk: An old QR references outdated continuity context.

Mitigation: Re-check canonical source link and current repository continuity artifacts before consequential decisions.

### 4) Mismatched hash

Risk: QR-provided hash differs from canonical record hash.

Mitigation: Treat mismatch as a continuity warning and require human-supervised validation before any consequential interpretation.

### 5) Fake verification page

Risk: A spoofed page fabricates “verified” status without canonical continuity checks.

Mitigation: Confirm official domain/page route and compare against repository-linked canonical source and advisory boundary wording.

## Safe QR operating rules

- Check official HC:// domain and verification page route before trusting page output.
- Ensure record ID is visible and reviewable.
- Display and compare full hash; short hash may be shown only as a secondary convenience view.
- Keep canonical source link visible for manual continuity inspection.
- Preserve advisory-only trust boundary and human-supervised validation requirements.

## Trust boundary statement

In HC-TRUST-LAYER, QR verification is an entry point into continuity diagnostics.

A hash match confirms integrity alignment for referenced bytes under this workflow. It does not prove objective truth, intent, or autonomous authority.
