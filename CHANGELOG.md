# Changelog

## Unreleased

### Fixed

- Include SVG assets in the public-safety scan surface and CI validation.
- Fail empty scan surfaces instead of reporting a misleading clean scan.
- Delimit approval-packet body content with `BEGIN_BODY` / `END_BODY`.
- Return a clean CLI error when `--body-file` cannot be read.

## v0.1.0 - Ready To Tag After Push

Initial public release candidate for `customer-discovery-safety`.

### Added

- Codex skill workflow for approval-gated customer discovery.
- No-send approval packet template and helper script.
- Public-safety scanner for candidate public files.
- Synthetic examples for source notes, evidence readout, draft email, and approval packet.
- README positioning around approval-gated customer discovery for AI agents.
- Instruction-level limitation statement: this is not a sandbox, policy engine, compliance system, security control, or guaranteed prevention mechanism.
- Unit tests for approval-packet failure paths and scanner behavior.
- GitHub Actions CI for tests and normal public-safety scan.
- Demo transcript and visual demo card.
- Local marketing drafts for later review.

### Validation

- `python3 -B -m unittest discover -s tests`
- `python3 customer-discovery-safety/scripts/scan_public_safety.py README.md CHANGELOG.md assets docs examples marketing customer-discovery-safety tests .github`

### Not Included

- No automatic sending, posting, uploading, publishing, calling, or third-party system changes.
- No compliance guarantee or security enforcement.
- No broad launch campaign.
