---
name: customer-discovery-safety
description: Customer-discovery safety circuit breaker for Codex. Use when reviewing discovery notes, classifying weak vs strong market evidence, preparing no-send outreach/email/DM/form/public-post drafts, enforcing exact approval before external actions, or scrubbing private project history from public docs.
---

# Customer Discovery Safety

Use this skill to keep customer discovery useful while reducing the chance that local planning drifts into unauthorized outreach, overclaimed evidence, or publishable material that leaks private project details.

## What This Skill Produces

Use it to produce one of four concrete outputs:

- **Decision readout**: whether to continue, pause, stop, pivot, or gather stronger evidence.
- **No-send approval packet**: a complete, body-visible approval card for one external action.
- **Evidence readout**: a conservative classification of facts, assumptions, weak signals, demand evidence, route evidence, and blockers.
- **Public-readiness review**: a release gate for packages, docs, posts, or skill artifacts that may contain private operational details.

## Core Rule

Treat every external action as gated until the user approves the exact action.

External actions include sending emails or messages, submitting forms, posting publicly, replying publicly, booking, buying, cancelling, uploading, deploying, publishing, calling, or changing a live third-party system. Read-only checks and local drafting are allowed when needed.

Before any external action, show the exact target, account or identity, channel, full body or payload, attachments or links, and the exact action that will occur. Wait for a clear confirmation such as `send`, `submit`, `confirm`, `发`, `提交`, or `确认`. Stop immediately on hesitation such as `wait`, `not yet`, `stop`, `等一下`, `先别`, `不要`, or `停`.

This is an instruction-level workflow, not a sandbox, policy engine, compliance system, security control, or guaranteed prevention mechanism. It helps surface gates clearly inside the agent workflow; it does not technically enforce them outside that workflow.

## Workflow

1. Read the local source of truth first.
   - Prefer `AGENTS.md`, `HANDOFF.md`, `PROGRESS.md`, or the repo README before older chat memory.
   - Check current git status before edits.
   - If the project has live channels, distinguish local docs from live state.

2. Restate the job in operational terms.
   - Identify whether the user wants research, local drafting, evidence review, public-release preparation, or a real external action.
   - Separate facts, assumptions, unknowns, and risks.
   - Do not infer permission for a new send/post/form from a previous approved action.

3. Classify evidence conservatively.
   - Stronger evidence: current pain described before seeing the concept, repeated weekly use, willingness to pay, pilot intent, concrete referral, budget ownership, or a clear disqualifying objection.
   - Weaker evidence: "cool idea" reactions, generic category size, competitor existence, silence, auto-replies, bounces, public comments with no intent, or route pointers.
   - Treat delivery failures as channel evidence, not buyer rejection.
   - Treat "not a fit" as route refusal unless it clearly addresses the target buyer and problem.

4. Build no-send assets first.
   - Draft locally.
   - Keep one route or approval card per action.
   - Prefer direct interviews and current-behavior questions before showing a concept.
   - Include stop conditions so the agent knows when not to push.

5. Publish only generalized material.
   - Remove personal names, personal email addresses, email-provider message IDs, chat IDs, social handles, phone numbers, private URLs, local file paths, live outreach history, and project-specific recipients.
   - Replace specifics with roles, segments, examples, or placeholders.
   - Remove visible AI/tool/provenance wording unless it is required by the publication context.
   - Do not publish drafts that imply a real message, form, post, or campaign is already approved.

6. End with the next concrete gate.
   - If local work is enough, name the next local artifact.
   - If an external action is needed, provide the approval packet and stop.
   - If evidence is too weak, say what stronger evidence would change the decision.

## Approval Packet Template

Use this shape before any external action:

```markdown
ACTION: send one email / submit one form / publish one post / reply once
CHANNEL: email / contact form / public forum / DM / call
ACCOUNT_OR_IDENTITY: exact sender account, profile, or public identity
TARGET: exact recipient, URL, group, or thread
SUBJECT: exact subject, if any
BODY:
BEGIN_BODY
full final body
END_BODY
ATTACHMENTS_OR_LINKS: none, or exact files/links
PURPOSE: what uncertainty this tests
NOT_AUTHORIZED: list adjacent actions that are not included
PRECHECKS: source, duplicate, timing, account, attachment/link, stop-word checks
STOP_CONDITIONS: when to abandon or ask again
APPROVAL_PHRASE: the exact phrase the user can reply with
```

Do not shorten the approval surface when sender identity, recipient, body, attachment state, or public/private channel matters.

For deterministic scaffolding, run:

```bash
python3 scripts/build_approval_packet.py \
  --action "send one email" \
  --channel "email" \
  --identity "founder@example.com" \
  --target "operator@example.com" \
  --subject "Customer-discovery question" \
  --body-file draft.txt \
  --purpose "Test whether this route can produce a current-behavior interview" \
  --not-authorized "follow-up, attachments, calls, public posts" \
  --approval-phrase "Send this exact email with no attachments"
```

## Evidence Readout Template

Use this shape when deciding whether discovery is working:

```markdown
WHAT WE KNOW:
- Observed facts only.

WHAT WE DO NOT KNOW:
- Missing evidence and unresolved assumptions.

EVIDENCE CLASSIFICATION:
- Demand evidence:
- Route/routing evidence:
- Channel failure:
- Refusal/non-fit:
- Weak signal:

DECISION:
- Continue / pause / stop / pivot.

NEXT SAFE WORK:
- Local-only work:
- External action requiring exact approval:
```

## Stop / Pivot Rules

Recommend stopping or pausing when:

- The project creates stress or pressure out of proportion to the evidence.
- Current conversations do not reveal concrete pain before the concept is shown.
- Signals are mostly silence, auto-replies, bounces, route pointers, or polite "interesting" reactions.
- The next step would be broad outreach, posting, or building before sharper evidence exists.
- A user explicitly says the project should stop or feels like it has no market.

Recommend continuing only when the next step tests a specific uncertainty and can be done locally or with exact approval.

## Public-Readiness Gate

Before calling a customer-discovery artifact or skill publish-ready:

1. Confirm it is an actual publishable artifact, not only source notes.
2. Confirm source-specific details have been generalized or removed.
3. Confirm external-action instructions preserve exact approval gates.
4. Confirm examples are synthetic or safely anonymized.
5. Confirm no live route, identity, or body is framed as already approved.
6. Run the bundled scan on candidate public files:

```bash
python3 scripts/scan_public_safety.py <file-or-directory> [...]
```

The scan is a helper, not a substitute for review. Treat any finding as something to inspect before publication.

## "Make It Public" Gate

Do not treat "make it public" as approval to publish. First identify:

- Target platform or repository.
- Account or organization.
- Exact files or payload.
- License, if any.
- Public description and README text.
- Whether public release reveals a live workflow, identity, or previous private work.

Then show an approval packet for the publish/upload action and wait for exact confirmation.

## Output Standards

- For simple questions, answer directly.
- For discovery strategy, lead with the decision and the evidence.
- For outreach work, produce no-send drafts or approval packets unless the user has already approved the exact external action.
- For stopped projects, make the stopped state obvious at the top of the maintained handoff.
- For public skill/package work, keep only reusable procedure; do not include private project history.
