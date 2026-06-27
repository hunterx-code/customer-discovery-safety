#!/usr/bin/env python3
"""Build a body-visible approval packet for one external action."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "action",
    "channel",
    "identity",
    "target",
    "body",
    "purpose",
    "approval_phrase",
]


def read_body(args: argparse.Namespace) -> str:
    if args.body and args.body_file:
        raise ValueError("Use either --body or --body-file, not both.")
    if args.body_file:
        path = Path(args.body_file).expanduser()
        try:
            return path.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise ValueError(f"Could not read body file {path}: {exc.strerror}") from exc
        except UnicodeDecodeError as exc:
            raise ValueError(f"Could not read body file {path}: {exc}") from exc
    return (args.body or "").strip()


def missing_fields(values: dict[str, str]) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not values.get(field, "").strip()]


def format_packet(values: dict[str, str]) -> str:
    subject = values.get("subject") or "n/a"
    attachments = values.get("attachments_or_links") or "none"
    not_authorized = values.get("not_authorized") or "any adjacent external action not listed here"
    prechecks = values.get("prechecks") or (
        "source verified; duplicate checked; account/identity checked; "
        "body reviewed; attachment/link state checked; stop words checked"
    )
    stop_conditions = values.get("stop_conditions") or (
        "stop if the user hesitates, changes the target/body/account, or asks to wait"
    )

    return f"""ACTION: {values["action"]}
CHANNEL: {values["channel"]}
ACCOUNT_OR_IDENTITY: {values["identity"]}
TARGET: {values["target"]}
SUBJECT: {subject}
BODY:
BEGIN_BODY
{values["body"]}
END_BODY

ATTACHMENTS_OR_LINKS: {attachments}
PURPOSE: {values["purpose"]}
NOT_AUTHORIZED: {not_authorized}
PRECHECKS: {prechecks}
STOP_CONDITIONS: {stop_conditions}
APPROVAL_PHRASE: {values["approval_phrase"]}
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a complete no-send approval packet for one external action."
    )
    parser.add_argument("--action", required=True)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--identity", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--subject", default="")
    parser.add_argument("--body", default="")
    parser.add_argument("--body-file", default="")
    parser.add_argument("--attachments-or-links", default="")
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--not-authorized", default="")
    parser.add_argument("--prechecks", default="")
    parser.add_argument("--stop-conditions", default="")
    parser.add_argument("--approval-phrase", required=True)
    args = parser.parse_args()

    try:
        body = read_body(args)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    values = {
        "action": args.action,
        "channel": args.channel,
        "identity": args.identity,
        "target": args.target,
        "subject": args.subject,
        "body": body,
        "attachments_or_links": args.attachments_or_links,
        "purpose": args.purpose,
        "not_authorized": args.not_authorized,
        "prechecks": args.prechecks,
        "stop_conditions": args.stop_conditions,
        "approval_phrase": args.approval_phrase,
    }
    missing = missing_fields(values)
    if missing:
        print("Missing required field(s): " + ", ".join(missing), file=sys.stderr)
        return 2

    print(format_packet(values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
