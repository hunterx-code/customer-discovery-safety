# Feedback Playbook

Use this before broader marketing. It is a local review script, not an outreach campaign.

## Target Reviewers

Ask 3-5 people from these groups:

- technical founders using Codex or other coding agents;
- founding PMs doing customer discovery;
- agent workflow builders who care about external-action approval;
- startup operators who have seen weak discovery evidence turn into premature outreach.

Avoid positioning this for scaled outbound, AI SDR, CRM, deliverability, or sales automation buyers.

## Review Prompt

```text
I am testing a small public Codex skill repo.

Please look at the README for 2 minutes and answer:

1. What do you think this does?
2. Who is it for?
3. What problem phrase would you search for if you needed this?
4. Does it feel different from a generic "ask before sending" prompt?
5. What would make you trust it enough to try it?
6. What wording feels confusing, too strong, or not credible?

No need to be nice; I am checking whether the positioning is legible.
```

## Pass / Fail Criteria

Treat the README as working if at least 3 of 5 reviewers can say, without explanation:

- it is for AI-agent-assisted customer discovery;
- it blocks or gates external actions until exact human approval;
- it separates weak discovery signals from stronger demand evidence;
- it is not an outreach automation tool.

Treat it as not ready for broader marketing if reviewers:

- think it is an AI SDR or sales automation tool;
- think it technically guarantees safety;
- cannot explain how it differs from a generic prompt;
- do not understand what "customer-discovery safety" means;
- ask for a demo before they understand the README.

## Questions To Score

Score each 1-5.

| Question | Score | Notes |
| --- | ---: | --- |
| Clear target user |  |  |
| Clear pain |  |  |
| Clear difference from a generic prompt |  |  |
| Trustworthy safety wording |  |  |
| Install path understandable |  |  |
| Demo convincing |  |  |
| Would try or star |  |  |

## Decision Gate

Broader marketing is reasonable only if:

- average clarity score is at least 4;
- no more than 1 reviewer misclassifies it as outbound automation;
- at least 2 reviewers can suggest similar public language or search terms;
- there is no recurring concern that it overclaims enforcement.

If those conditions are not met, keep it as a quiet GitHub artifact and revise positioning before posting broadly.
