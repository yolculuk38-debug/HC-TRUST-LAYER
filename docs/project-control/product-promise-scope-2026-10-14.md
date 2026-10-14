# Narrow product promise — report before implementation

## Finding

The independent audit's B1 item asks the public repository entry point to lead
with the strongest implemented, bounded use: local evidence-package integrity
checks, followed by the limits of those checks. Baseline is the #1252 main merge
`96d82ae26a7ad2a21dc285f017f810dd92aea875`.

README currently opens with broad trust-infrastructure positioning, then routes
first-time readers toward a demo before describing the local package command.
Later sections diagram integrity/provenance through a “trust result
classification” flow without distinguishing the implemented package hash core
from higher-level conceptual/research surfaces. The existing package quickstart
does explain integrity limits, but its expected output lists `VERIFIED` plus
issuer/timestamp fields, which can be mistaken for authenticated identity or
external time evidence when read without the later caveat.

Repository-confirmed scope: `src/hc_trust/verification_package.py` checks a
local manifest and listed package files, supports SHA-256 digests and path
containment, and reports declared issuer/timestamp/witness fixture presence
separately from identity, signature, witness-authority or external-time
verification. The existing sample CLI invocation returns `VERIFIED`,
`checks.manifest_files_checked=1`, `checks.issuer_identity_verified=false`,
`checks.external_timestamp_verified=false`, and `truth_guarantee=false`.

## Proposed bounded change

- Reshape only the README opening and verification-flow wording so a new user
  first sees the local manifest/file-integrity use case, a working command and
  its concrete result boundary.
- Clarify the package CLI quickstart output: `VERIFIED` is the verifier's local
  package-integrity status for the listed files and manifest in this run. It
  does not authenticate the manifest author, signer, witness, timestamp or
  package truth; “proof PRESENT/MATCH” labels describe included files and their
  hashes only.
- Keep the public static demo as a separate navigation surface. Do not remove
  its links, rename CLI commands, change status fields, or make a release or
  production claim.
- Validate every example against a real CLI run and run the documentation,
  terminology and canonical-artifact guards.

## Out of scope

No code, manifest/schema, stored evidence, signing, identity, timestamp, trust
policy, API, workflow, release, or authority changes. Those belong to B2/B3/C1-C4
and need their own reviewed scopes. This report makes no claim that the current
status contract is ideal; it records only what the implementation demonstrably
checks for this documentation slice.

## Acceptance

A first-time reader should be able to state what one command checks, see its
real success and failure meaning, and distinguish file-to-manifest integrity
from signer identity, authenticated time, witness authority and real-world
truth. Keep documentation precise to current code and existing tests.
