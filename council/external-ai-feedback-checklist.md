# External AI Feedback Checklist

Use this checklist when collecting manual advisory feedback for HC Multi-AI Council records.

This process is manual.

It does not authorize automation.

## Before asking external AI systems

- [ ] Confirm the Council decision record exists.
- [ ] Confirm the decision question is clear.
- [ ] Confirm the current repository state is not guessed.
- [ ] Use `council/external-ai-review-prompts.md` as the source prompt packet.
- [ ] Keep all AI output advisory-only.
- [ ] Do not ask any AI system to approve, merge, release, label, or modify repository files.

## Required response shape

Each response should include:

- [ ] Role perspective
- [ ] Main recommendation
- [ ] Risks
- [ ] Missing safeguards
- [ ] Next small PR suggestion
- [ ] What should not be automated yet
- [ ] One-sentence final advice

## Source capture

For each response, record:

- [ ] AI system name
- [ ] role used
- [ ] date collected
- [ ] prompt version or source file
- [ ] summary of answer
- [ ] important disagreement or warning
- [ ] whether the response changed the final recommendation

## Safety review

Before copying any response into a Council record, check:

- [ ] Does the response claim final authority?
- [ ] Does the response suggest live automation too early?
- [ ] Does the response imply truth guarantee?
- [ ] Does the response bypass human review?
- [ ] Does the response ask for repository credentials, secrets, or private data?
- [ ] Does the response rely on unsupported claims?

If yes, summarize the useful part and mark the unsafe part as rejected.

## Updating Council records

When updating a Council record:

- [ ] Keep the original final decision human-authored.
- [ ] Separate summary from direct AI recommendation.
- [ ] Record unresolved disagreements.
- [ ] Record missing evidence.
- [ ] Preserve advisory-only language.
- [ ] Keep `Human final authority: true`.
- [ ] Keep `Truth guarantee: false` unless a separate approved protocol changes this.

## Minimum acceptance condition

External AI feedback is ready to summarize when:

- [ ] at least one governance/risk perspective is collected
- [ ] at least one implementation perspective is collected
- [ ] at least one red-team or abuse-risk perspective is collected
- [ ] conflicts are listed
- [ ] final decision remains pending until maintainer review

## Final boundary

AI feedback may inform a decision record.

AI feedback must not become the decision itself.
