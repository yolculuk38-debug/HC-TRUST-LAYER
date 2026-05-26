# Authenticated AI Validator Access Model

This document defines authenticated access boundaries for AI-assisted validators in HC:// and HC-TRUST-LAYER so only registered and authorized AI systems can submit traceable advisory analysis.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No repository-stored secrets.

## Purpose

Provide a secure, traceable authentication model for AI validator access that reduces spoofing and replay risk while preserving review accountability, provenance continuity, and audit trail integrity.

## Core definitions

### registered AI validator

A **registered AI validator** is an AI-assisted validator identity enrolled through repository-defined governance and reviewer-recognized registration procedures.

A registered AI validator must have:

- a unique validator identifier
- declared ownership or accountable operator context
- approved access scope for advisory analysis
- auditable registration metadata outside secret material

### validator identity

**Validator identity** is the stable, reviewable identity surface used to associate analysis runs with a specific registered AI validator.

Validator identity should include:

- validator identifier
- issuer or trust domain identifier
- declared advisory-only role
- trace reference linkage for audit continuity

### signed access token

A **signed access token** is a time-bound, integrity-protected access credential used to authorize a registered AI validator for a specific advisory analysis session.

Requirements:

- cryptographic signature verification by the receiving system
- explicit expiration timestamp
- scope restriction to advisory analysis actions
- token identifier for trace and revocation workflows

### API key boundary

The **API key boundary** is the control boundary that separates secret bearer credentials from repository artifacts.

Rules:

- API keys or private secrets must never be committed to HC-TRUST-LAYER.
- Secrets must be managed in secure runtime or operator-controlled secret stores.
- Repository content may document boundary expectations, but must not contain live credentials.

### timestamp

A **timestamp** is a recorded time value associated with token issuance, challenge verification, and analysis submission events.

Timestamp requirements:

- consistent format for machine review
- explicit timezone context (for example UTC)
- retention in validator trace metadata for audit trail continuity

### nonce and replay protection

A **nonce** is a single-use cryptographic challenge value used to prevent replay of prior authentication exchanges.

Replay protection requirements:

- nonce must be unique per challenge
- nonce must have short validity window
- nonce reuse must be rejected and logged

### audit trace

An **audit trace** is the reviewable provenance path connecting access authentication events to advisory analysis output.

Minimum audit trace elements:

- validator identity
- token identifier (non-secret reference)
- timestamp sequence
- nonce/challenge verification status
- analysis artifact reference
- human review state

### human-supervised review requirement

The **human-supervised review requirement** means authenticated AI output remains non-final and advisory until appropriate human validation steps are completed for consequential interpretation.

Authenticated access does not grant autonomous authority.

## Authentication flow

1. **AI requests analysis access**
   - The AI validator requests advisory analysis access using its registered validator identity.
2. **System verifies validator identity**
   - The system confirms the identity is registered, allowed, and in-scope for advisory analysis.
3. **System checks signed token and challenge**
   - The system validates token signature, expiration, scope, and nonce-based challenge response.
4. **System records timestamp and validator trace**
   - The system records authentication event timestamps and validator trace linkage for provenance continuity.
5. **AI submits advisory analysis**
   - The authenticated AI validator submits analysis within authorized advisory scope.
6. **Result remains non-final until human review where required**
   - Output is marked advisory-only and cannot be treated as final authority absent required human-supervised validation.

## Misuse protections

### fake AI validator prevention

- Reject access when validator identity is not registered or cannot be mapped to trusted registration evidence.
- Require explicit validator identity trace in all AI-assisted submissions.

### copied token prevention

- Use short-lived signed access tokens with scope limits.
- Bind token usage to validator identity and challenge context.
- Reject tokens used outside their declared scope or validity window.

### replay attack prevention

- Require nonce-based challenge/response per session.
- Reject reused nonce values.
- Log replay rejection events into audit trace.

### fake approval badge prevention

- Do not render approval-like badges from unauthenticated or untraceable AI claims.
- Display verification state labels tied to validator trace evidence only.

### unverifiable AI claim warning

- Mark claims without validator identity and trace evidence as `UNVERIFIED AI CLAIM`.
- Present clear warning language that unverifiable claims are not trusted validation outputs.

## Safe signal states

Use these states in operator and public-facing advisory contexts where applicable:

- `AUTHENTICATED AI VALIDATOR`
- `UNVERIFIED AI CLAIM`
- `TOKEN EXPIRED`
- `VALIDATOR TRACE AVAILABLE`
- `HUMAN REVIEW REQUIRED`

Signal usage guidance:

- Pair each state with concise meaning and limitation text.
- Keep advisory-only and human-supervised validation notices visible.
- Do not imply certainty, autonomous authority, or production guarantees.

## Implementation notes

- This model does not modify canonical schema, validators, guards, signing logic, federation logic, policy files, or canonical records.
- This model is a documentation baseline for authenticated AI validator access controls and traceability expectations.
- Secret material remains outside repository boundaries.

## Related documents


- `docs/accountability-defense-layer.md`
- `docs/verified-ai-validator-model.md`
- `docs/verification-result-states.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/public-verification-boundaries.md`
