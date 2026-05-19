# HC:// TRUST LAYER — Limitations and Risks

> Status: **Current limitations documentation**
>
> This document explains what HC:// TRUST LAYER can and cannot guarantee today.

HC:// TRUST LAYER is designed to make integrity and provenance checks auditable.
It is **not** a truth engine.

## What the Protocol Verifies

HC:// TRUST LAYER can verify whether:

- a record matches an expected structure,
- a hash matches the submitted content under defined normalization rules,
- provenance metadata is present and consistent with the recorded format,
- verification steps can be reproduced by another reviewer.

These checks support integrity and traceability.
They do not determine whether every claim inside the content is factually correct.

## Trust vs Integrity

**Integrity** answers: *"Was this content changed after it was recorded?"*

**Trust** answers: *"Should I believe this claim is true and reliable?"*

HC:// TRUST LAYER primarily addresses integrity and provenance.
A valid hash proves byte-level consistency with a referenced artifact, but it does **not** prove objective truth.

## Threat Model Basics

The current model assumes adversaries may attempt to:

- submit manipulated or low-quality evidence,
- copy and replay previously valid-looking artifacts in misleading contexts,
- spoof presentation channels such as QR-linked verification paths,
- misrepresent AI involvement, model identity, or witness quality.

The system is built to make technical verification easier, not to eliminate social engineering, misinformation, or governance failures.

## Known Risks

- **Fake submissions:** validly formatted records may still describe false or misleading events.
- **Replay attempts:** previously captured identifiers or payloads may be reused out of context.
- **QR spoofing:** users may be directed to lookalike pages or altered destinations.
- **Misleading AI attribution:** content can be incorrectly labeled as AI-verified, AI-generated, or human-reviewed.
- **Centralized infrastructure dependency:** availability and operational trust can degrade if key hosting or distribution services fail.

## AI Content Limitations

AI-generated or AI-assisted content can pass integrity checks while still containing hallucinations, factual errors, bias, or fabricated citations.

A successful technical validation should be treated as **one signal**, not final proof of correctness.
Independent review, source checking, and context evaluation remain necessary.

## Witness System Clarification

Witness-related mechanisms are currently experimental.
Witness presence should not be interpreted as automatic endorsement, consensus, or legal-grade attestation.

Witness metadata can improve traceability, but witness quality, independence, and incentives still require further governance design.

## Future Mitigations

Planned mitigations include:

- **Dispute/revocation flow:** formal processes to challenge or invalidate problematic records.
- **Witness weighting:** calibrated weighting based on reliability history and role separation.
- **Nonce/replay protection:** stronger anti-replay semantics for submissions and verification artifacts.
- **Stronger canonicalization:** tighter normalization rules to reduce ambiguity across toolchains.

These are roadmap items, not guarantees of current behavior.

## Practical Interpretation

Use HC:// TRUST LAYER as a verification and provenance layer.
Do not use it as a standalone oracle of factual truth.

Where decisions are high-impact, combine protocol checks with human review, independent evidence, and domain-specific validation.
