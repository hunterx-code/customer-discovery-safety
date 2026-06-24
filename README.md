# Customer Discovery Safety

Stop agents from turning weak customer-discovery notes into unauthorized outreach or fake validation.

This Codex skill is for the moment when an agent is helping with customer discovery and things can get sloppy: a draft starts looking sendable, a weak reply starts looking like validation, or private notes start drifting into public docs.

It keeps the work useful while making the agent stop at the risky parts.

## Why It Exists

Customer discovery work has a failure mode: local notes become real outreach too easily, and weak signals start looking like market proof.

Agents can draft fast, but that speed creates risk:

- weak signals get treated as market validation;
- bounces and auto-replies get misread as buyer evidence;
- old approvals get reused for new sends;
- private notes get copied into public artifacts;
- "can you post this?" turns into a live external action before the user has reviewed the exact target and body.

This skill makes those moments explicit before anything leaves your machine.

## Demo

Messy notes:

```text
Three operators mentioned the dashboard takes "too long" at month-end.
One buyer asked whether the tool has SOC 2, but did not describe current pain.
A community comment said "I would try this."
One partner directory suggested a procurement inbox.
No budget owner, weekly workflow, or approved message is confirmed.
```

Unsafe interpretation:

```text
People want this. Send the buyer a pitch, post in the community, and start a pilot thread.
```

Safe output:

```text
DECISION: do not launch outreach yet.
DEMAND EVIDENCE: possible monthly workflow pain, not validated as weekly or urgent.
ROUTE EVIDENCE: procurement inbox may be a route, not buyer proof.
WEAK SIGNAL: community interest and compliance questions.
NEXT SAFE WORK: draft one no-send approval packet for a current-behavior interview.
EXTERNAL ACTION: blocked until exact target, sender identity, body, attachments, and approval are shown.
```

## Why Not Just A Prompt?

Generic human-in-the-loop prompts usually say "ask before sending." This skill is narrower: it is a customer-discovery circuit breaker. It makes the agent separate real demand from weak signals, write no-send approval packets, call out stop/pivot conditions, and check public files before they leak private history.

## What It Does

- Produces body-visible no-send approval packets.
- Separates demand evidence from route evidence, silence, bounces, and weak reactions.
- Requires agents to surface exact approval before sends, forms, posts, replies, calls, uploads, or publishing.
- Scans candidate public files for emails, phone numbers, long IDs, local paths, social handles, and optional external-action wording.
- Keeps public packages generalized instead of leaking private project history.

## What It Does Not Do

- It does not send outreach.
- It does not publish or upload anything.
- It does not make weak evidence stronger.
- It does not replace manual review.

## Install

Copy the skill folder into your Codex skills directory:

```bash
SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILLS_DIR"
cp -R customer-discovery-safety "$SKILLS_DIR/"
```

Then invoke it in Codex:

```text
Use $customer-discovery-safety to review this customer-discovery plan and prepare any needed approval packet.
```

## Quick Start

Generate an approval packet from a draft:

```bash
python3 customer-discovery-safety/scripts/build_approval_packet.py \
  --action "send one email" \
  --channel "email" \
  --identity "founder@example.com" \
  --target "ops-lead@example.com" \
  --subject "Customer-discovery question" \
  --body-file examples/synthetic-draft-email.txt \
  --purpose "Test whether this route can produce one current-behavior interview" \
  --not-authorized "follow-ups, calls, attachments, links, public posts" \
  --approval-phrase "Send this exact email with no attachments"
```

Scan public-facing files before release:

```bash
python3 customer-discovery-safety/scripts/scan_public_safety.py README.md examples marketing
```

Use a stricter scan that also flags generic action words:

```bash
python3 customer-discovery-safety/scripts/scan_public_safety.py --include-action-words README.md examples marketing
```

This stricter mode may exit `1` for expected action-language hits. Inspect each hit manually before release.

## Example Output

See:

- [examples/synthetic-source-notes.md](examples/synthetic-source-notes.md)
- [examples/safe-evidence-readout.md](examples/safe-evidence-readout.md)
- [examples/safe-approval-packet.md](examples/safe-approval-packet.md)

## Publishing Boundary

Publishing this repository, posting about it, or submitting it anywhere is itself an external action. The skill's rule still applies: show the exact target, account, body, files, and payload first, then wait for explicit confirmation.

## License

MIT
