# HC Council Local Fixture Usage

## Purpose

This note explains how an operator can use the HC Council local command bridge without triggering production issue or pull request comment automation.

The current HC Council bridge is local-only and report-only. It is not wired to a live GitHub issue-comment listener.

## Safety warning

Do not test HC Council fixture commands by posting `/hc council ...` as a real GitHub issue or pull request comment.

The repository already has a generic HC Assistant Command Listener for real comments that begin with `/hc`. A production issue or pull request comment can therefore trigger that existing listener even though the HC Council bridge is not wired into it.

Use a local JSON fixture instead.

## Safe local flow

1. Prepare a local event fixture JSON file.
2. Put the intended command in `comment.body`.
3. Set `event_name` to `issue_comment`.
4. Set `comment.author_association` to an allowed value such as `OWNER`, `MEMBER`, or `COLLABORATOR`.
5. Run the local bridge module from the repository root.
6. Review the emitted public-safe report-only JSON.
7. Use the result as advisory evidence only.

Example command from the repository root:

```bash
python -m scripts.hc_council_issue_command_bridge examples/hc_council_issue_command.example.json --pretty
```

Do not use direct script execution for this example. The module form keeps the repository root on Python's import path and matches the bridge import layout.

## Example fixture shape

```json
{
  "event_name": "issue_comment",
  "repository": {
    "full_name": "yolculuk38-debug/HC-TRUST-LAYER"
  },
  "issue": {
    "number": 1201,
    "pull_request": {
      "url": "https://api.github.com/repos/yolculuk38-debug/HC-TRUST-LAYER/pulls/1201"
    }
  },
  "comment": {
    "body": "/hc council review pr 1201",
    "author_association": "OWNER"
  },
  "evidence_refs": [
    "scripts/hc_council_issue_command_bridge.py",
    "scripts/hc_council_command.py"
  ]
}
```

## Expected output boundary

The output must remain:

- report-only
- advisory-only
- public-safe
- truth-guarantee false
- local fixture based

The bridge must not perform:

- network calls
- provider API calls
- repository writes
- workflow changes
- schema changes
- credential access
- approval, merge, close, label, assignment, or reviewer authority

## Fail-closed behavior

The bridge rejects unsupported or unsafe inputs. Examples include:

- unsupported event type
- empty comment body
- non-`/hc council` command text
- ambiguous multiline comments
- unauthorized comment author association
- invalid command syntax inherited from the command parser

Rejected inputs must return a public-safe stop response, not an action request.

## Mobile operator guidance

For mobile-only operation, do not paste experimental `/hc council ...` commands into live PR comments.

Instead:

1. Open the repository files for reference.
2. Copy the example fixture content into a controlled local or Codex task context.
3. Modify the PR number and evidence refs there.
4. Ask the local runner or Codex task to execute the module command against the fixture.
5. Bring the emitted JSON back into the PR discussion only as an advisory report after human review.

## Future automation gate

A later PR may connect HC Council commands to a report-only workflow, but that must remain separate from this local fixture usage note.

Before any live automation is introduced, the change must pass the normal gate:

1. single-open-PR discipline
2. explicit protected-path review if workflows are touched
3. checks green before merge
4. comments and review threads resolved
5. scope and duplicate-risk review
6. human-authorized merge

No future automation may add approve, reject, close, merge, label, assignment, or reviewer authority unless explicitly approved in a separate governance change.
