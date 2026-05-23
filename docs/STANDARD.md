# HC Standard

## Purpose

HC Standard defines the minimum structure required for a HC-TRUST-LAYER record to be considered verifiable, traceable, and archive-compatible.

---

# HC Standard Record Structure

## Identity Layer

- Record ID
- Protocol Version
- Record Status
- Record Type

---

## Source Layer

- Author
- Timestamp
- Origin
- Witness Type

---

## Verification Layer

- SHA-256 Hash
- Hash Reference
- QR Reference
- Git Commit Reference

---

## Witness Layer

Supported witness types:

- human-witness
- ai-witness
- multi-ai-witness
- system-witness
- commit-witness

---

## Archive Layer

Records must remain:

- Publicly traceable
- Hash verifiable
- QR accessible
- Commit linked
- Historically auditable

---

## Integrity Rule

If the content changes:

- Hash must change
- QR reference must update
- Verification status must be re-evaluated
- Git history must preserve previous states

---

## HC Verification Principles

HC-TRUST-LAYER verification is based on:

1. Public archive history
2. Hash integrity
3. QR-linked verification
4. Witness transparency
5. Multi-layer provenance
6. Open verification workflows

---

Status: Experimental  
Protocol: HC://  
Version: HC-STD-1.0
