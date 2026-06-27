# Customer Discovery Safety

[![CI](https://github.com/hunterx-code/customer-discovery-safety/actions/workflows/ci.yml/badge.svg)](https://github.com/hunterx-code/customer-discovery-safety/actions/workflows/ci.yml)

Approval-gated customer discovery for AI agents.

This Codex skill is for the moment when an agent is helping with customer discovery and things can get sloppy: a draft starts looking sendable, a weak reply starts looking like validation, or private notes start drifting into public docs.

It keeps the work useful while making the agent pause before weak evidence turns into outreach, publishing, or fake validation.

## Who It Is For

Use this if you ask coding agents to help with:

- customer-discovery planning;
- outreach drafts, interview asks, contact-form drafts, or public-post drafts;
- evidence synthesis from interviews, replies, bounces, comments, or silence;
- publishing sanitized examples, docs, or launch notes from private project history.

The useful niche is not "AI writes better outreach." It is the opposite: the skill makes the agent slow down when the next step could contact a real person, overclaim weak evidence, or leak private source material.

## Why It Exists

Customer discovery work has a failure mode: local notes become real outreach too easily, and weak signals start looking like market proof.

Agents can draft fast, but that speed creates risk:

- weak signals get treated as market validation;
- bounces and auto-replies get misread as buyer evidence;
- old approvals get reused for new sends;
- private notes get copied into public artifacts;
- "can you post this?" turns into a live external action before the user has reviewed the exact target and body.

This skill makes those moments explicit before anything leaves your machine.

## What You Get

- A reusable `SKILL.md` workflow for Codex.
- A deterministic approval-packet helper for no-send external-action review.
- A public-safety scanner for candidate README, examples, posts, and docs.
- Synthetic examples that show how to classify weak discovery evidence.
- Local launch copy drafts that are safe to review before posting anywhere.

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

## When It Should Trigger

Good fit:

- "Review these customer-discovery notes and tell me whether this is real demand."
- "Draft an interview ask, but do not send anything."
- "Prepare an approval packet for one exact email/form/post."
- "Check this public README or launch post for private project leakage."
- "Should we continue, pause, pivot, or stop this idea based on the evidence?"

Bad fit:

- fully autonomous sales sequencing;
- scraping or enriching leads at scale;
- improving deliverability or conversion rates;
- legal compliance review;
- making weak evidence look stronger.

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
- It is not a sandbox, policy engine, compliance system, security control, or guaranteed prevention mechanism.

This is an instruction-level workflow for Codex. It helps the agent present external-action gates clearly, but it does not technically enforce those gates outside the agent workflow.

## Install

Clone this repo:

```bash
git clone https://github.com/hunterx-code/customer-discovery-safety.git
cd customer-discovery-safety
```

Install with Codex's `$skill-installer` from this GitHub repo when available:

```text
Use $skill-installer to install hunterx-code/customer-discovery-safety path customer-discovery-safety.
```

Or copy the skill folder directly into your Codex skills directory. The Codex skill installer installs into `$CODEX_HOME/skills/<skill-name>`, defaulting to `$HOME/.codex/skills/<skill-name>` when `CODEX_HOME` is unset.

```bash
SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILLS_DIR"
cp -R customer-discovery-safety "$SKILLS_DIR/"
```

Then invoke it in Codex:

```text
Use $customer-discovery-safety to review this customer-discovery plan and prepare any needed approval packet.
```

## Verify The Package

Run these checks after cloning:

```bash
python3 -B -m unittest discover -s tests
python3 customer-discovery-safety/scripts/scan_public_safety.py README.md examples marketing customer-discovery-safety
```

Expected normal scan result:

```text
No public-safety scan findings.
```

The stricter scan intentionally flags external-action words for manual review:

```bash
python3 customer-discovery-safety/scripts/scan_public_safety.py --include-action-words README.md examples marketing customer-discovery-safety
```

That mode can exit `1` when it finds terms like `send`, `post`, or `publish`. For this package, those hits are expected because the skill teaches external-action boundaries; inspect them before release rather than treating the exit code as an automatic failure.

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
python3 customer-discovery-safety/scripts/scan_public_safety.py README.md examples marketing customer-discovery-safety
```

Use a stricter scan that also flags generic action words:

```bash
python3 customer-discovery-safety/scripts/scan_public_safety.py --include-action-words README.md examples marketing customer-discovery-safety
```

This stricter mode may exit `1` for expected action-language hits. Inspect each hit manually before release.

## Example Output

See:

- [examples/synthetic-source-notes.md](examples/synthetic-source-notes.md)
- [examples/safe-evidence-readout.md](examples/safe-evidence-readout.md)
- [examples/safe-approval-packet.md](examples/safe-approval-packet.md)

## Publishing Boundary

Publishing this repository, posting about it, or submitting it anywhere is itself an external action. The skill's rule still applies: show the exact target, account, body, files, and payload first, then wait for explicit confirmation.

## GitHub Readiness

This repository is intended to stand alone as the public artifact. Private customer-discovery notes, live outreach history, local handoffs, message IDs, account names, and project-specific recipients should stay out of this repo.

Before pushing a change or cutting a GitHub Release:

- run the normal public-safety scan;
- inspect the stricter action-word scan manually;
- confirm examples are synthetic;
- confirm no public file implies a real external action is already approved;
- confirm the README still explains the specific customer-discovery failure mode, not only generic approval gates.

## License

MIT
