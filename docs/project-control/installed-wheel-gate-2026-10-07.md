# Installed wheel and tested-artifact handoff

Audit A5 has source-tree tests and schema-path unit checks, but no CI job that
installs a built wheel and executes outside the checkout. Editable installs can
hide missing modules/data and do not bind the tested code to a release artifact.

Build one wheel, install that exact wheel into a fresh Python 3.14 virtual
environment, and run an isolated smoke script from a temporary working
directory. Check the installed distribution's direct-URL archive hash against
the wheel, require imports and schema data to come from the environment, and
exercise the console command, SDK, canonical schema/hash checks, real package
bytes, tampering/missing-file rejection and CLI exit codes. Import the advisory
runtime app without starting a server.

Upload that same wheel plus a JSON result containing the source commit and
wheel SHA-256 only after the smoke gate passes. Do not rebuild after testing.
This is an inspectable artifact handoff, not a package registry publication,
signature, provenance attestation or claim of production readiness. Preserve
workflow permissions and the maintainer's final release decision.

## Local validation

Built the #1246 candidate source with CPython 3.14.7, installed the resulting
wheel into a fresh environment using pip, and ran the isolated smoke from
`/tmp`. All six reported check groups passed: installed archive hash binding,
runtime import, console help, installed schema/negative validation, real-file
package SDK/JSON/summary agreement, and tampered/missing-file failure exit codes.
A separately altered wheel was rejected before emitting a success report.
The final GitHub job must produce its own report on the current PR/main commit;
these local results do not substitute for that gate or release authorization.

The PR is based on the actual #1247 merge
`1a7bc1c9017333ce22ee6f01d077363d2f72d7a8`. The workflow runs on qualifying
PR and main changes with read-only repository permissions. The successful main
run's artifact is the handoff candidate for that exact source commit; a PR test
merge artifact is not evidence for a later main commit.

Codex P1 follow-up (4210630555): include `VERSION` and `CHANGELOG.md` in both
PR and main path filters. Otherwise the documented release-metadata-only commit
would have no exact-commit wheel evidence. The manual release sequence now
explicitly waits for that commit's installed-wheel gate before publication.
