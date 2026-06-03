# Security Policy

## Purpose

HC-TRUST-LAYER is the canonical repository for the HC:// verification infrastructure. This policy explains how to report public integrity concerns and private vulnerability concerns without expanding the risk of harm.

This repository remains an advisory, documentation-first protocol surface. Reports help maintain transparent provenance, audit trail continuity, and reviewable verification context, but they do not create production readiness, security certification, forensic certainty, or autonomous governance guarantees.

---

## Scope

This guidance applies to security, vulnerability, misuse, provenance, and integrity concerns related to HC-TRUST-LAYER repository materials, including public verification references, documentation, records references, validation guidance, and trust-kernel-adjacent review boundaries.

Use the safest reporting path when a concern could expose sensitive information, exploit details, private records, credentials, validator bypasses, policy-routing weaknesses, signing or trust-anchor concerns, supply-chain risk, or active abuse details.

---

## Public Integrity Reports

Public GitHub Issues may be used only for non-sensitive public integrity concerns that can be discussed without exposing private data, exploit steps, secrets, or active abuse details.

Appropriate public integrity reports may include:

- broken public verification links
- public documentation errors
- public record-reference inconsistencies
- public hash or QR reference concerns that do not expose private data or exploit steps
- misleading public attribution or provenance context

When opening a public integrity report, include only public, non-sensitive information needed for human review, such as the affected public file, link, record reference, or documentation section and a concise description of the concern.

---

## Private Vulnerability Reports

Sensitive vulnerability reports must not be posted publicly. Use GitHub private vulnerability reporting if it is available for this repository.

If GitHub private vulnerability reporting is unavailable, open a public GitHub Issue only to ask maintainers for a private security contact. Do not include exploit details, proof-of-concept material, private records, personal information, secrets, credentials, active abuse details, or other sensitive information in that public request.

Private vulnerability reports include concerns involving:

- exploit steps or proof-of-concept details
- private records or personal information
- secrets, tokens, keys, credentials
- validator bypass
- policy-routing weakness
- signing or trust-anchor concern
- GitHub Actions, dependency, package, or supply-chain vulnerability
- active abuse details that could increase harm if public
- uncertainty about whether disclosure is safe

Do not assume a security email address exists unless maintainers have approved and published one for this repository.

---

## What Not To Post Publicly

Do not post the following in public GitHub Issues, pull requests, discussions, comments, or other public channels:

- exploit steps or proof-of-concept details
- private records, personal information, or non-public provenance material
- secrets, tokens, keys, credentials, or authentication material
- validator bypass details
- policy-routing weakness details
- signing or trust-anchor weakness details
- GitHub Actions, dependency, package, or supply-chain exploit details
- active abuse details that could increase harm if public
- uncertain reports where public disclosure safety has not been established

When in doubt, ask maintainers for a private reporting path without sharing sensitive details.

---

## Human Oversight and Validation

Human-supervised validation remains required for sensitive archive, trust kernel, policy, signing, record-reference, and provenance decisions.

Agent-generated analysis may support triage and documentation review, but it is advisory unless validated through repository-defined checks and reviewer oversight. Maintainers may request additional evidence, reproduction context, or scoped remediation details through a private channel before deciding on changes.

---

## Experimental / Early-Stage Status

HC:// and HC-TRUST-LAYER remain experimental and early-stage. Security and integrity processes may evolve as repository-defined checks, reviewer practices, and protocol graph documentation mature.

This policy does not claim production readiness, security certification, forensic certainty, cryptographic guarantees, policy guarantees, or autonomous governance finality.
