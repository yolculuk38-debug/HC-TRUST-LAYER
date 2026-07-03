# QR Verification Layer

This directory contains QR-related references for HC:// archive records.

## Purpose

The QR layer is designed to provide simple public access to archive records, verification pages, and hash references.

A QR code may link to:

- a public record page
- a verified archive entry
- a hash reference
- a timeline entry
- a public verification path

## QR Principle

QR codes should not contain private or secret information.

They should only point to official public HC:// archive links.

## Recommended Format

Each QR reference may include:

- Record ID
- Target URL
- Related hash reference
- Archive status
- Date created

## Demo Policy (Text-Only)

When demonstrating QR generation in this repository:

- Document command examples in Markdown.
- Show expected output paths as text.
- Do **not** commit generated binary QR images (`.png`, `.jpg`, etc.).

Example (documentation-only):

```bash
python src/qr.py HC-CHATGPT-2026-0001 --output qr/HC-CHATGPT-2026-0001-demo.png
```

Expected output path (example only):

`qr/HC-CHATGPT-2026-0001-demo.png`


## HC-TEST-2026-0001 QR Path Reconciliation

`qr/HC-TEST-2026-0001.txt` is a post-migration QR/path reconciliation artifact and reviewable access aid for `HC-TEST-2026-0001`.

It is not production QR evidence and is not replacement historical QR evidence. Existing binary QR evidence, including `qr/qr-code.jpg`, is preserved and not overwritten by this text-only reconciliation.

Reconciliation note:

- Old target: `records/verified/HC-TEST-2026-0001.md`
- Archived record path: `records/archived/HC-TEST-2026-0001.md`
- Reviewable access aid URL: `https://github.com/yolculuk38-debug/HC-TRUST-LAYER/blob/main/records/archived/HC-TEST-2026-0001.md`
- Reason: post-migration QR/path reconciliation

The old verified-path target is legacy/stale and should not be presented as active QR evidence.

## Security Notice

Users should verify that QR links point to the official HC:// archive location or approved GitHub Pages/GitHub repository address.

QR codes are access tools, not proof of truth.

Verification still depends on public records, hash references, revision history, and human review.
