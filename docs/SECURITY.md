# QR Security and Anti-Spoofing

## Purpose

QR codes are used as quick access references inside the HC-TRUST-LAYER protocol.

A QR code alone should not be treated as proof of authenticity.

## Verification Rules

Users should verify:

- repository source
- owner identity
- record ID
- SHA-256 hash consistency

## Official Source

Official records should point to the HC-TRUST-LAYER canonical repository:

github.com/yolculuk38-debug/HC-TRUST-LAYER

## Anti-Spoofing Logic

Fake QR codes may redirect users to modified or unofficial records.

HC-TRUST-LAYER verification depends on:

- trusted source
- traceable record structure
- public hash comparison
- transparent verification flow

## Future Security Layers

Potential future layers may include:

- signed verification
- optional 2FA protected actions
- public verification API
- cryptographic witness validation
