# Public Validator Local Demo Adapter Plan

> **Status:** planning document
> **Scope:** documentation-only local demo adapter plan
> **Authority:** advisory-only; human review remains final
> **Production readiness:** not claimed

## Executive Summary

This plan defines a small local demo adapter that can later connect the existing HC:// Public Validator MVP specification and public validator result examples to a normalized public-safe result shape.

The adapter is intentionally limited. It would read an example record, normalize visible fields into a public validator result, preserve warnings and evidence gaps, surface source and responsibility chains, and require human review. It would not change runtime code, schemas, validators, workflows, governance rules, canonical records, hashes, QR artifacts, signing, federation, or policy.

## Purpose

The purpose of the local demo adapter is to make the Public Validator MVP easier to demonstrate without expanding trust-kernel behavior.

The adapter plan should help a future implementation:

- show a simple local-only record-to-result flow;
- preserve HC:// and HC-TRUST-LAYER review boundaries;
- keep result output advisory, public-safe, and human-supervised;
- expose missing, warning, and conflicting evidence signals clearly;
- avoid backend, remote-fetch, schema, validator, record, QR, signing, federation, policy, or workflow changes by default.

## Non-Goals

The local demo adapter must not:

- decide truth;
- certify food safety;
- certify building safety;
- certify news truth;
- provide legal authority;
- act autonomously;
- bypass human review;
- fetch untrusted remote data by default;
- modify canonical records;
- write or rewrite hashes;
- generate signatures;
- alter QR artifacts;
- change schemas, validators, workflows, governance rules, signing, federation, policy, records, runtime, code, or tests.

## Existing Inputs

The local demo adapter should be designed around existing documentation inputs only:

- the HC:// Public Validator Core specification;
- the Public Validator MVP implementation plan from the prior PR;
- public validator result examples for food provenance, building material provenance, news source provenance, and QR / non-canonical link warnings;
- local demo records or fixtures that may be proposed in a later PR.

These inputs are explanatory. They are not canonical records, signed payloads, generated artifacts, certification outputs, or proof that any real-world claim is true.

## Proposed Local Demo Flow

The future local demo adapter should follow this bounded flow:

```text
example record
→ local adapter
→ normalized public validator result
→ warnings / missing_evidence / conflicting_evidence
→ source_chain / responsibility_chain
→ chain_of_custody where applicable
→ human_review_required
```

The flow should remain local-only unless a later reviewed PR explicitly introduces a different mode. Any remote or network behavior should be disabled by default and treated as out of scope for the first adapter implementation.

## Example Record Input

A future fixture may use a small public-safe demo record shape like this:

```yaml
record_id: HC-DEMO-PV-LOCAL-0001
record_type: public_validator_local_demo
scenario: food_provenance_demo
input_scope: explanatory_fixture_only
public_safe: true
canonical_record: false
signed_payload: false
generated_artifact: false
source_chain:
  - Demo supplier packing note
  - Demo inspection summary
responsibility_chain:
  - Demo supplier
  - Demo importer
  - Human reviewer
missing_evidence:
  - Destination intake photo evidence
conflicting_evidence: []
warnings:
  - Advisory fixture only; not a certification output.
```

The input should be fictional, public-safe, and clearly labeled as a demo fixture. It should not reuse or modify canonical repository records.

## Adapter Responsibilities

A future local demo adapter should be responsible only for local normalization and presentation of demo input fields.

Allowed responsibilities:

- read a local example record or fixture;
- confirm required demo fields are present where possible;
- copy or normalize `warnings`, `missing_evidence`, and `conflicting_evidence` into list fields;
- copy or normalize `source_chain` and `responsibility_chain` into list fields;
- include `chain_of_custody` when the demo input provides custody steps;
- add safe default warnings when demo evidence is absent, partial, ambiguous, or conflicting;
- emit a public-safe result with the required output posture;
- keep all output advisory and human-review-required.

The adapter should not interpret real-world truth, certify outcomes, or make consequential decisions.

## Output Contract

A future adapter result should preserve this minimum output contract:

```yaml
record_id: HC-DEMO-PV-LOCAL-0001
result_label: NEEDS_HUMAN_REVIEW
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
warnings: []
missing_evidence: []
conflicting_evidence: []
source_chain: []
responsibility_chain: []
chain_of_custody: []
```

Required output posture:

- `advisory_only: true`
- `public_safe: true`
- `truth_guarantee: false`
- `human_review_required: true`
- `warnings` must exist as a list;
- `missing_evidence` must exist as a list;
- `conflicting_evidence` must exist as a list;
- `source_chain` must exist as a list;
- `responsibility_chain` must exist as a list.

`chain_of_custody` should exist when applicable. If the selected scenario does not include custody material, the adapter may emit an empty list or a warning that custody evidence was not provided, depending on the future fixture design.

## Warning / Missing Evidence Handling

The adapter should preserve warnings and evidence gaps instead of hiding them.

Expected handling:

- if `warnings` is missing, emit a warning that no warning list was supplied by the fixture;
- if `missing_evidence` is missing, emit an empty list and add a warning that missing-evidence input was absent;
- if `conflicting_evidence` is missing, emit an empty list and add a warning that conflict input was absent;
- if evidence is partial, ambiguous, redacted, placeholder-only, or demo-only, keep that limitation visible;
- if any high-impact scenario is present, keep `human_review_required: true`.

Warnings must be public-safe and must not imply fraud, liability, forensic certainty, safety certification, regulatory approval, or objective truth.

## Chain-of-Custody Handling

For scenarios involving physical goods, samples, lab material, QR labels, or transfer events, a future adapter may surface `chain_of_custody` as a list of local demo custody steps.

Each custody step should remain explanatory and may include:

- `step`;
- `custodian`;
- `timestamp` when available;
- `evidence_status`;
- `notes` for public-safe limitations.

The adapter must not invent custody events. If custody input is absent, incomplete, or placeholder-only, the result should preserve that gap through `missing_evidence` or `warnings`.

## QR / Link Handling

For QR or link scenarios, the adapter may compare local fixture fields such as `scanned_url` and `canonical_url` only when both are present in the demo input.

Allowed local handling:

- show whether the scanned URL differs from the expected HC:// reference in the fixture;
- emit a public-safe non-canonical link warning;
- preserve `truth_guarantee: false` and `human_review_required: true`;
- avoid claims of spoofing, fraud, legal liability, malicious intent, or forensic certainty.

The adapter must not fetch remote URLs by default, follow redirects by default, rewrite QR artifacts, create QR codes, or validate signatures unless a later scoped PR explicitly implements those behaviors with review.

## Human Review Boundary

The local demo adapter output is advisory only. It supports human reviewers by organizing visible demo signals, but it does not replace reviewer judgment.

Human review remains required for:

- real-world reliance decisions;
- evidence sufficiency decisions;
- disputed or conflicting evidence;
- food, building, news, legal, safety, regulatory, or other high-impact contexts;
- escalation, correction, rejection, approval, or additional investigation.

The result must always include `human_review_required: true`.

## Deferred Components

The following components are deferred and should not be included in the first local demo adapter PR:

- runtime integration;
- schema changes;
- validator changes;
- workflow changes;
- governance rule changes;
- canonical record changes;
- hash generation or rewriting;
- QR artifact generation or rewriting;
- generated artifact updates;
- signing or signature verification changes;
- federation behavior;
- policy evaluation changes;
- backend service behavior;
- remote data fetching by default;
- production UI claims;
- autonomous decision behavior.

## Security Boundaries

The adapter should be designed as a local, read-only demonstration layer.

Security boundaries:

- no canonical record mutation;
- no protected path mutation;
- no automatic remote fetches;
- no signature fabrication;
- no hash fabrication;
- no QR artifact rewriting;
- no bypass of human review;
- no production, legal, safety, truth, or forensic-certainty claims;
- no weakening of existing repository checks, validators, policies, or workflows.

Any future implementation should be small enough to inspect and revert safely.

## Implementation Checklist

A future implementation PR should verify that it:

- adds only local demo adapter files and demo fixtures approved for that PR;
- keeps processing local-only by default;
- reads demo input without modifying canonical records;
- emits `advisory_only: true`;
- emits `public_safe: true`;
- emits `truth_guarantee: false`;
- emits `human_review_required: true`;
- always emits `warnings` as a list;
- always emits `missing_evidence` as a list;
- always emits `conflicting_evidence` as a list;
- always emits `source_chain` as a list;
- always emits `responsibility_chain` as a list;
- emits `chain_of_custody` where applicable;
- documents that the adapter does not decide truth, certify safety, certify news truth, provide legal authority, or act autonomously;
- runs terminology, docs drift, canonical artifact, whitespace, and status checks where available.

## Recommended Next PR

Recommended next PR: **#642 Public Validator demo fixture records**.

The next PR should add small public-safe demo fixture records for local adapter development without modifying canonical records, schemas, validators, workflows, signing, federation, policy, hashes, QR artifacts, generated artifacts, runtime code, or protected governance paths.
