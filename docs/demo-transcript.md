# Demo Transcript

This transcript shows the failure mode the skill is designed to catch.

## Input Notes

```text
Three operators mentioned the dashboard takes "too long" at month-end.
One buyer asked whether the tool has SOC 2, but did not describe current pain.
A community comment said "I would try this."
One partner directory suggested a procurement inbox.
No budget owner, weekly workflow, or approved message is confirmed.
```

## Unsafe Agent Interpretation

```text
People want this. Send the buyer a pitch, post in the community, and start a pilot thread.
```

## Safer Skill-Guided Output

```text
DECISION: do not launch outreach yet.

DEMAND EVIDENCE:
- Possible monthly workflow pain.
- Not validated as weekly, urgent, budget-owned, or pilot-ready.

ROUTE EVIDENCE:
- Procurement inbox may be a route.
- Route evidence is not buyer proof.

WEAK SIGNAL:
- Community interest and compliance questions.

NEXT SAFE WORK:
- Draft one no-send approval packet for a current-behavior interview.

EXTERNAL ACTION:
- Blocked until exact target, sender identity, channel, body, attachments,
  purpose, stop conditions, and approval phrase are shown.
```

## Approval Packet Command

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

## Approval Packet Output

```text
ACTION: send one email
CHANNEL: email
ACCOUNT_OR_IDENTITY: founder@example.com
TARGET: ops-lead@example.com
SUBJECT: Customer-discovery question
BODY:
Hi,

I am doing early customer-discovery work on a workflow tool and trying to understand how teams currently review external data before analysis.

Would you be open to a 10-minute conversation about who usually owns that readiness check? I am not selling anything and I am not asking for private customer data.

If you are not the right person, a pointer to the right role or public resource is completely fine.

ATTACHMENTS_OR_LINKS: none
PURPOSE: Test whether this route can produce one current-behavior interview
NOT_AUTHORIZED: follow-ups, calls, attachments, links, public posts
PRECHECKS: source verified; duplicate checked; account/identity checked; body reviewed; attachment/link state checked; stop words checked
STOP_CONDITIONS: stop if the user hesitates, changes the target/body/account, or asks to wait
APPROVAL_PHRASE: Send this exact email with no attachments
```

No message is sent by this command. It only prints the review surface.
