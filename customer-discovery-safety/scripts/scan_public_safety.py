#!/usr/bin/env python3
"""Scan candidate public files for customer-discovery safety risks."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {
    ".md",
    ".mdx",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".csv",
    ".tsv",
    ".py",
    ".js",
    ".ts",
}

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
SAFE_EXAMPLE_DOMAINS = {"example.com", "example.org", "example.net"}

BASE_PATTERNS = [
    ("email_address", EMAIL_RE),
    ("phone_number", re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}(?!\d)")),
    ("long_numeric_id", re.compile(r"\b\d{12,}\b")),
    ("long_hex_id", re.compile(r"\b[0-9a-fA-F]{16,}\b")),
    ("local_user_path", re.compile(r"/Users/[^\s)>\"]+")),
    ("reddit_user_handle", re.compile(r"\bu/[A-Za-z0-9_-]+\b")),
]

ACTION_WORD_PATTERNS = [
    ("possible_external_action_word", re.compile(r"\b(send|submit|post|publish|reply|call)\b|发|提交|确认发送", re.IGNORECASE)),
]


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and child.suffix.lower() in TEXT_SUFFIXES:
                    files.append(child)
        elif path.is_file():
            files.append(path)
    return sorted(set(files))


def scan_file(path: Path, include_action_words: bool) -> list[tuple[str, int, str]]:
    if path.name == "scan_public_safety.py":
        return []

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")

    patterns = BASE_PATTERNS + (ACTION_WORD_PATTERNS if include_action_words else [])
    findings: list[tuple[str, int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for name, pattern in patterns:
            match = pattern.search(line)
            if not match:
                continue
            if name == "email_address" and match.group(1).lower() in SAFE_EXAMPLE_DOMAINS:
                continue
            else:
                snippet = line.strip()
                if len(snippet) > 180:
                    snippet = snippet[:177] + "..."
                findings.append((name, lineno, snippet))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan public customer-discovery artifacts for private details and external-action wording."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    parser.add_argument(
        "--include-action-words",
        action="store_true",
        help="Also flag generic action words such as send, submit, post, publish, reply, or call.",
    )
    args = parser.parse_args()

    paths = [Path(item).expanduser().resolve() for item in args.paths]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"missing: {path}", file=sys.stderr)
        return 2

    findings_count = 0
    for path in iter_files(paths):
        findings = scan_file(path, args.include_action_words)
        for name, lineno, snippet in findings:
            findings_count += 1
            print(f"{path}:{lineno}: {name}: {snippet}")

    if findings_count:
        print(f"\nFound {findings_count} item(s) to inspect before publication.")
        return 1

    print("No public-safety scan findings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
