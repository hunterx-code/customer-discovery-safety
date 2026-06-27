from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APPROVAL_SCRIPT = REPO_ROOT / "customer-discovery-safety/scripts/build_approval_packet.py"
SCAN_SCRIPT = REPO_ROOT / "customer-discovery-safety/scripts/scan_public_safety.py"


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-B", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class ApprovalPacketTests(unittest.TestCase):
    def test_missing_body_is_rejected(self) -> None:
        result = run_script(
            str(APPROVAL_SCRIPT),
            "--action",
            "send one email",
            "--channel",
            "email",
            "--identity",
            "founder@example.com",
            "--target",
            "ops-lead@example.com",
            "--purpose",
            "Test one interview route",
            "--approval-phrase",
            "Send this exact email",
        )

        self.assertEqual(result.returncode, 2)
        self.assertIn("Missing required field(s): body", result.stderr)

    def test_body_and_body_file_conflict_is_rejected(self) -> None:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as body_file:
            body_file.write("Draft body")
            body_file.flush()

            result = run_script(
                str(APPROVAL_SCRIPT),
                "--action",
                "send one email",
                "--channel",
                "email",
                "--identity",
                "founder@example.com",
                "--target",
                "ops-lead@example.com",
                "--body",
                "Inline body",
                "--body-file",
                body_file.name,
                "--purpose",
                "Test one interview route",
                "--approval-phrase",
                "Send this exact email",
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Use either --body or --body-file", result.stderr)


class PublicSafetyScanTests(unittest.TestCase):
    def test_normal_scan_allows_example_domains(self) -> None:
        result = run_script(
            str(SCAN_SCRIPT),
            "examples/synthetic-draft-email.txt",
            "examples/safe-approval-packet.md",
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("No public-safety scan findings.", result.stdout)

    def test_normal_scan_flags_unsafe_email_and_uses_relative_path(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as tmpdir:
            sample = Path(tmpdir) / "sample.md"
            unsafe_email = "founder@" + "realcompany.dev"
            sample.write_text(
                f"Allowed founder@example.com, unsafe {unsafe_email}\n",
                encoding="utf-8",
            )

            result = run_script(str(SCAN_SCRIPT), str(sample))

        self.assertEqual(result.returncode, 1)
        self.assertIn("sample.md:1: email_address", result.stdout)
        self.assertNotIn(str(REPO_ROOT), result.stdout)

    def test_strict_scan_flags_action_words(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as tmpdir:
            sample = Path(tmpdir) / "sample.md"
            sample.write_text("Do not send, post, or publish this.\n", encoding="utf-8")

            result = run_script(str(SCAN_SCRIPT), "--include-action-words", str(sample))

        self.assertEqual(result.returncode, 1)
        self.assertIn("possible_external_action_word", result.stdout)


if __name__ == "__main__":
    unittest.main()
