# Standalone CLI record selection boundary

## Investigation and scope before implementation

Baseline: #1250 merge `dd27203180bf6c3ff95732e20efa3d0b4eb236f5`.
The standalone selector interprets the first absolute-path `records` component
as the canonical tree. A checkout under `records/cache/project` therefore hides
its own `records/pending` records. The hash command returns success when no
record is checked, and the legacy single-file validator reports an artifact skip.

Bound this A3 follow-up to the shared standalone selector, two CLI commands,
legacy validator, regression tests and operator documentation. Protected validator
paths must change because path context currently controls whether validation runs.
Do not change record/schema/hash data, public lookup semantics or workflow authority.

## Intended contract

- Accept an explicit repository root through `--repo-root` and Python keyword
  arguments. Relative input paths are relative to that root when it is supplied.
- Without an explicit root, infer only one plausible canonical `records` tree;
  refuse ambiguous nested trees rather than choosing a convenient inner anchor.
- Evaluate artifact rules relative to that root, including resolved targets.
  Canonical group directories must not be symlink aliases; files must resolve
  within the selected group. Existing exact artifact names/suffixes remain reserved.
- Both multi-record commands require at least one actual record check for exit 0.
- Preserve legacy explicit single-file validation outside a canonical tree, but
  do not interpret arbitrary ancestor directory names as evidence of an artifact.

## Required validation

Cover relocated checkouts, malformed records mixed with valid records, ambiguous
anchors and explicit-root recovery, nested generated trees, canonical-directory
and file symlink escapes, empty selections, legacy behavior and CLI invocation.
Run existing public/runtime selector regressions and the full suite. Require
current-head CI, installed-wheel gate and matching Codex review before merge.

## Local checkpoint

Implemented explicit-root context, unambiguous inference, lexical/resolved
containment, root-relative artifact classification, and nonzero empty hash checks.
Added 27 regressions covering relocation, mixed valid/invalid records, ambiguous
anchors, explicit-root recovery, generated nested trees, file/group symlinks,
empty/artifact-only sets, standalone legacy files and subprocess invocation.

On #1250 baseline with CPython 3.14.7 and FastAPI 0.142.2: 189 focused tests and
1415 full-suite tests passed (overlapping counts), one upstream TestClient warning.
Canonical, terminology, documentation and whitespace guards passed with the two
existing README wording warnings. The #1251 viewer patch is not in these counts.

## Continuation dependency

Preserve this local branch until the prioritized viewer PR #1251 is complete.
Rebase onto its actual merge, rerun relevant validation and open only one active
implementation PR. No CLI PR has been published at this checkpoint.

At the October 14 checkpoint the remote #1251 head is
`1b8d98a3b56e8530b0909c5261b5f6b2d6b98ee0`; Codex summary 6164451239 and clean
reaction 567082649 match that head. CodeQL reported test-helper comment
4268609031 / thread PRRT_kwDOSXQpRc6sO1O0. The case-insensitive extraction fix is
committed locally in the separate viewer worktree as `1047f44` but was not
published: GitHub create_tree failed automatic approval review because the
account usage limit prevented that review from running. Do not bypass this
control or merge the remote head with the failing CodeQL check. Publish the
saved follow-up when normal review is available, resolve its thread, obtain
fresh matching Codex review/CI, merge, then verify main scan results. Original
private alert #13/#14 closure has not been observed from this session.

## Rebase after viewer correction

The CLI checkpoint was rebased onto viewer merge
`033f9a5f8089700f2a923a36cec74345a159b44b` / tree
`5e9499cc906084933da545d09d71ba5a1eba6d3c`. The viewer follow-up changes no
record-selection paths. Re-run the complete suite on this combined tree before
publishing; the prior 1415 count was against the pre-viewer base.


## Combined validation after #1251

On rebased tree `5e9499cc906084933da545d09d71ba5a1eba6d3c`, CPython 3.14.7 /
FastAPI 0.142.2: 1423 full-suite tests passed, one upstream TestClient warning.
The CLI selector/public/runtime focused check had 189 passing tests before the
rebase; those sources were unchanged by #1251. Canonical, terminology, docs and
whitespace guards passed on the rebased tree with two existing README warnings.
The combined full-suite count includes both #1251's eight regressions and this
slice's 27 regressions; do not add focused counts to it.
