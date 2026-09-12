"""Selection and recovery regression checks; never rebuild the real archive."""
import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec = importlib.util.spec_from_file_location("archive_builder", Path(__file__).with_name("build_current_archive.py"))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class ArchiveExtensionTests(unittest.TestCase):
    def test_selection_is_explicit_and_sorted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tracked = ["research_old/REPORT.md", "research_old/cache.pyc", "research_old/private.key",
                       "research_old/COMPLETE_PACKAGE.zip", "research_old/DRIVE_READBACK.json",
                       "research_manager/state.json", "RESEARCH_INDEX_20260908.md"]
            untracked = ["research_old/unreviewed.md", "research_integration_20260912/ARCHIVE_REVIEW.md",
                         "research_w_continuation_20260912/probe.py", "research_w_continuation_20260912/data.sqlite3"]
            for name in tracked + untracked:
                p = root / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(name, encoding="utf-8")
            result = subprocess.CompletedProcess([], 0, b"\0".join(s.encode() for s in tracked) + b"\0")
            with patch.object(builder, "REPO", root), patch.object(builder.subprocess, "run", return_value=result):
                first = builder.exploratory_entries()
                self.assertEqual(first, builder.exploratory_entries())
            self.assertEqual([p.relative_to(root).as_posix() for p, _ in first], [
                "RESEARCH_INDEX_20260908.md", "research_integration_20260912/ARCHIVE_REVIEW.md",
                "research_old/REPORT.md", "research_w_continuation_20260912/probe.py"])
            self.assertTrue(all("/EXPLORATORY_CONTINUATION/" in name for _, name in first))

    def test_recovery_preserves_static_and_replaces_exploratory_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "current.zip"
            static_name = builder.arc_join(builder.ARCHIVE_ROOT_NAME, "historic/source.bin")
            stale_name = builder.arc_join(builder.ARCHIVE_ROOT_NAME, "EXPLORATORY_CONTINUATION/research_old/stale.md")
            new_name = builder.arc_join(builder.ARCHIVE_ROOT_NAME, "EXPLORATORY_CONTINUATION/research_new/report.md")
            static_bytes = bytes(range(256)) + b"\x00\xff\r\n"
            with zipfile.ZipFile(output, "w") as zf:
                zf.writestr(static_name, static_bytes)
                zf.writestr(stale_name, b"obsolete overlay")
            source = root / "report.md"
            source.write_bytes(b"reviewed research\r\n")
            overrides = dict(OUTPUT=output, TEMP=root / "current.zip.tmp", ARCHIVE_ROOT=root / "absent",
                             BUILD_RECORD=root / "build.json", MEMBER_ROOT_RECORD=root / "members.json")
            with patch.multiple(builder, **overrides), patch.object(builder, "dynamic_entries", return_value=[(source, new_name)]), contextlib.redirect_stdout(io.StringIO()):
                builder.main()
                first_bytes = output.read_bytes()
                builder.main()
                self.assertEqual(first_bytes, output.read_bytes())
            with zipfile.ZipFile(output) as zf:
                self.assertEqual(zf.namelist(), [static_name, new_name])
                self.assertEqual(zf.read(static_name), static_bytes)
                self.assertEqual(zf.read(new_name), source.read_bytes())
                self.assertNotIn(stale_name, zf.namelist())
                self.assertIsNone(zf.testzip())


if __name__ == "__main__":
    unittest.main()
