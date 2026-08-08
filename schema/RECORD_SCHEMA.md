# HC:// Canonical Record Schema

## Executable source

The single executable JSON record contract is:

```text
schema/record-v1.schema.json
```

It uses JSON Schema Draft 2020-12 and the payload identifier
`schema_version=hc-record-v1`. The former conflicting
`schema/record-v1.json` contract has been retired.

## Required integrity profile

Every canonical JSON record declares:

```text
content_hash_profile=hc-content-sha256-v2
```

Text content is hashed as UTF-8 bytes. Structured JSON content is hashed with
the repository's versioned RFC 8785 JCS primitive. Schema conformance checks
shape and declared profile; digest verification separately checks whether the
declared digest matches the available content.

## Validation boundary

The shared validator:

- parses JSON without duplicate properties or non-finite numbers;
- validates with `Draft202012Validator`;
- applies a strict RFC 3339 `date-time` checker;
- returns deterministic, value-redacted rule failures;
- keeps requested-record binding separate from schema conformance.

Schema conformance does not prove content truth, author identity, witness
authority, signature validity, timestamp authority, or governance approval.
HC:// outputs remain advisory-only, public-safe, and subject to human review.
