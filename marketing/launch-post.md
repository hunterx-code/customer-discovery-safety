# Launch Post Draft

I built a small Codex skill for a specific failure mode: an agent helps with customer discovery, then weak notes quietly turn into unauthorized outreach or fake validation.

Customer Discovery Safety is meant to make that failure harder to miss.

It is for founders, PMs, and agent builders who use Codex to draft discovery plans, interview asks, or launch notes.

It helps the agent:

- separate real demand from weak signals;
- draft approval packets that show the exact target, sender, body, links, and stop conditions;
- avoid treating bounces, route pointers, and polite interest as proof;
- scan public files before private notes leak into a repo.

The core before/after:

Unsafe: "People want this. Send a buyer pitch and post in the community."

Safer: "Demand is not validated. Draft one no-send approval packet for a current-behavior interview, and block external action until the exact target, sender, body, attachments, and approval are shown."

It does not send anything. It does not make weak evidence stronger. It just makes the risky moments visible before anything leaves your machine.

Try it:

```bash
git clone https://github.com/hunterx-code/customer-discovery-safety.git
cd customer-discovery-safety
SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILLS_DIR"
cp -R customer-discovery-safety "$SKILLS_DIR/"
```

Then ask Codex:

```text
Use $customer-discovery-safety to review these discovery notes and prepare any needed approval packet.
```

Repo: https://github.com/hunterx-code/customer-discovery-safety
