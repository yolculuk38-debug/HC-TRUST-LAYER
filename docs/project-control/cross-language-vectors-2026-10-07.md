# Cross-language canonicalization vectors

Audit A2 already has a shared Python RFC 8785 implementation and negative input
tests, but no independently executed ECMAScript byte/digest fixtures. Add a
versioned fixture with explicit expected canonical UTF-8 bytes and SHA-256.
Cover number spelling, UTF-16 key order, numeric-looking keys, nested objects,
array order, escapes, Turkish text, emoji and unnormalized Unicode.

Python must parse through the production strict JSON boundary and compare the
real canonicalizer against the fixture. A separate test-only ECMAScript module
serializes the checked-in valid fixtures using native number/string encoding
and sorted key emission; Web Crypto computes SHA-256. It is browser-compatible
test code, not a new public parser or proof verifier. In particular JSON.parse
does not detect duplicate keys, so production strict-parser rejection remains
covered by Python negative tests and must not be inferred from the JS harness.

The expected strings are specified independently of the Python implementation;
the numeric/ordering cases follow [RFC 8785 sections 3.2.2–3.2.4](https://www.rfc-editor.org/rfc/rfc8785.html#section-3.2.2).
CI executes both languages with the same fixture and fails on byte/hash drift.
No runtime profile, existing record digest, schema, signing or trust authority
changes. CI permissions remain unchanged.

## Validation

14 explicit canonical byte/SHA-256 vectors passed through production Python
and independently through ECMAScript/Web Crypto (Node v24.19.0). The Python
vector and strict-input suite passed 42 tests. The full suite passed 1340 tests
on CPython 3.14.7, with one upstream TestClient deprecation warning. Canonical,
terminology, docs and whitespace guards passed with two existing README warnings.
The patch is based on actual #1246 merge
`9e2f1b1cfeee7504640f38f2f9972951f748476a`; both language checks passed again
after that rebase. Matching current-head CI/review remains required.
