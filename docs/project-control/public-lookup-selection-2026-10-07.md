# Public lookup selection alignment

## Scope and evidence

Audit A3 remains open after #1243/#1244: the local Public Validator uses flat
globs and substring artifact exclusions, while the shared CLI/runtime selects
nested canonical records and the documented legacy archive. A duplicate in a
nested directory or `records/archive/` can therefore escape public lookup.
An ordinary record ID containing INDEX/EXPORT can disappear from that path.

Reuse the shared directory list and artifact predicate, recurse inside each
approved canonical directory, and constrain resolved paths to that directory
and the repository root. Check both lexical and resolved artifact paths.
Keep duplicate results fail-closed with schema/hash checks not performed.
The selector constants/predicate move unchanged into the dependency-light
`hc_trust.record_selection` module and remain re-exported by `verification`.
This preserves the public lookup's not-checked response when the optional local
schema helper dependency is unavailable, rather than failing at module import.

The QR bridge imports the lookup patterns and currently derives directory names
from them. Update its source guard with the recursive lookup contract so normal
and nested lookups continue working without widening source paths. Preserve
the local-only, advisory boundary and existing canonical hash requirement.

Update checked-path fixtures and active lookup/QR documentation deliberately;
historical project-control snapshots remain historical. Add lookup and QR
regressions for nested/legacy duplicates, precise artifact exclusions, symlink
escape/aliases and normal IDs containing artifact words. Run the related suites,
full suite, repository guards and current-head CI/review. The existing CI test
job will include the public lookup/QR suites. No schema, evidence, network,
signing, identity, workflow permission or production-authority changes.

## Validation

Based on actual #1245 merge `fe105a00cb62c62ef94b8ce0653cd3be2c69bdfd`.
On CPython 3.14.7, 140 focused lookup/QR/shared-selector/runtime-loader tests and
1314 full-suite tests passed. One upstream Starlette TestClient deprecation
warning remains. Canonical, terminology and documentation guards passed with
the same two existing README warnings. The shared selector extraction preserves
all existing artifact names/suffixes; no canonical evidence was rewritten.
Current-head GitHub checks and Codex review remain the merge gate.

Codex review of `1f1a3f596a6f` identified an absolute-path predicate issue:
a checkout below an ancestor such as `records/cache/project` could exclude all
public records. Both artifact checks now receive paths relative to the lookup
root, while resolved-path containment remains enforced. Public lookup and QR
regressions cover relocated roots and still-excluded generated records.
The runtime loader had the same absolute-path call, so apply the same root-relative
predicate correction and regress it there as well. This preserves runtime/public
selection parity without changing the shared filename rules or loader locking.

After the review fix, 147 focused and 1321 full-suite tests passed on CPython
3.14.7 with the same upstream TestClient warning. The standalone CLI selectors
still accept caller-supplied paths without an explicit repository-root argument;
their relocated absolute-path behavior is separate follow-up scope, not evidence
that every record-selection entry point is now fully identical.
