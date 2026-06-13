# Signature and Witness Verification Proposal

Status: proposal only

This document defines the next safe planning layer for HC-TRUST-LAYER after the completed local verification package hash core and HC Engineer planning helpers. It is documentation-only and does not implement signing, witness authority, federation, QR binding, runtime behavior, or production verification.

## Purpose

Signature and witness verification is the next trust-layer planning step because the local package integrity path can already answer a narrow question:

```text
Does this local package contain the expected files, and do their SHA-256 digests match the manifest evidence?
```

The next planning question is narrower than legal truth or identity finality:

```text
What local evidence could later show that a package, record, or hash was signed or witnessed, and what boundaries must prevent that evidence from becoming an unsupported truth claim?
```

This proposal keeps that question in the planning lane before implementation.

## Existing completed foundation

Repository evidence already records these local, advisory foundations:

- local verification package hash core;
- local CLI entry point for verification packages;
- sample package quickstart;
- HC Trust Engineer report generator;
- HC Engineer task planner;
- task planner hardening for skipped checks and scanner-marked human-review paths;
- task planner operator quickstart.

These layers support small, local, deterministic evidence handling. They do not create truth finality, production readiness, or external authority.

## Relationship to the existing witness-proof proposal

`docs/project-control/witness-proof-next-layer-proposal.md` already defines a witness-proof planning direction for local manifest evidence, subject binding, and witness proof states.

This document does not replace that proposal. It adds a broader verification planning boundary for both signature evidence and witness evidence under `docs/verification/`, so later implementation work can be split into smaller, separately reviewed slices.

## Advisory boundaries

All future work under this line must preserve:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human final authority required
```

A signature or witness record may strengthen provenance evidence, but it must not be presented as proof of legal truth, identity truth, forensic certainty, production readiness, or institutional authority unless a later, explicit, human-reviewed layer supports that limited claim.

## Out of scope

This proposal does not authorize or implement:

- production signing;
- witness authority;
- federation;
- QR or canonical-domain binding;
- C2PA ingestion;
- OpenTimestamps verification;
- W3C Verifiable Credential issuance or verification;
- legal truth;
- identity finality;
- forensic certainty;
- external network calls;
- LLM calls;
- repository write behavior;
- label, assignment, reviewer-request, close, approve, reject, merge, or auto-merge automation;
- workflow, schema, validator, record, policy, signing, federation, QR, generated-artifact, or runtime changes.

## Proposed phased path

### 1. Documentation-only threat and boundary proposal

Define the minimum threat model, expected misuse cases, and output language before implementation. This PR is that planning step.

Required result:

- clear scope;
- clear non-goals;
- clear advisory wording;
- clear relationship to existing witness-proof planning;
- no runtime or protected-path changes.

### 2. Local fixture format proposal

Define public-safe local fixture examples for signature and witness evidence without parsing or trusting them yet.

A later fixture proposal may include fields such as:

```json
{
  "subject_sha256": "...",
  "evidence_type": "signature-or-witness",
  "statement": "local sample attestation",
  "issuer_or_witness_hint": "sample-local-identifier"
}
```

The fixture format must require explicit subject binding before any later helper can report evidence as present for a package or record.

### 3. Deterministic test-only parser

Add a small test-only parser for public-safe local fixtures. It should validate shape and subject binding rules without treating any evidence as authoritative.

The parser should not:

- verify cryptographic signatures;
- validate W3C VCs;
- ingest C2PA assertions;
- verify OpenTimestamps attestations;
- call networks;
- mutate the repository;
- change public validator output contracts.

### 4. Local-only verification helper

Only after the parser is reviewed, add a local-only helper that can report limited states such as:

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`
- `SUBJECT_MISMATCH`
- `UNVERIFIED_SIGNATURE`
- `UNVERIFIED_WITNESS`

The helper must keep `truth_guarantee=false` and must escalate uncertain or authority-like claims to human review.

### 5. Later integration review

Integration with QR binding, canonical-domain binding, C2PA, OpenTimestamps, W3C VC, federation, or public validator UX must happen only after a separate human-reviewed design and risk review.

## Real-world example

A journalist, institution, AI system, or maintainer may publish a local verification package containing a claim, source file, manifest, and later a signature or witness evidence file.

HC-TRUST-LAYER should not say the claim is true. It should only report whether the local evidence is present, digest-valid, subject-bound to the expected hash or package, and still within advisory boundaries. If the evidence points to another hash, the result must show a mismatch rather than treating the signature or witness as valid for the current package.

## Safe next action

The next safe action after this proposal is not production implementation. It is a small docs-only fixture format proposal or a test-only parser proposal that preserves local-only, deterministic, public-safe, advisory behavior.
