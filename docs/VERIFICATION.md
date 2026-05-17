# Humanity Chain — Verification Standard

## Purpose

This document defines the basic verification standard for the Humanity Chain protocol.

The goal is to describe how HC:// records are created, stored, and verified.

---

## Core Verification Flow

The basic HC:// verification flow is:

1. Content is submitted.
2. A SHA-256 hash is generated.
3. A timestamp is attached.
4. A HC record ID is created.
5. Verification metadata is stored.
6. Optional QR reference is generated.
7. The record becomes traceable.

---

## Content Fingerprint

Each content item may receive a digital fingerprint.

The fingerprint may include:

- Content hash
- Timestamp
- Record ID
- Source reference
- Verification status
- Optional QR reference
- Optional witness reference

---

## SHA-256 Hash

SHA-256 is used to create a unique integrity fingerprint.

If the content changes, the hash changes.

This helps detect whether a file, message, image, video, audio, or document has been altered after registration.

---

## HC Record ID Format

A basic record ID may follow this format:

```text
HC-YYYY-NNNN
