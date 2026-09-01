#!/usr/bin/env python3
"""Build the deterministic current Collatz research archive for GitHub."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import hashlib
import json
import os
import zipfile


REPO = Path(__file__).resolve().parents[1]
EXTRACTED = REPO / "_extracted"
ARCHIVE_ROOT_NAME = "Collatz Problemi — Araştırma Arşivi"
ARCHIVE_ROOT = EXTRACTED / ARCHIVE_ROOT_NAME
RESEARCH_MANAGER = REPO / "research_manager"
AUDIT_ROOT = REPO / "audit_cp20_task8b3_e4_independent_20260831"
AUDIT_OUTPUTS = AUDIT_ROOT / "outputs"
AUDIT_ZIP = AUDIT_ROOT / "CP20_TASK8B3_E4_INDEPENDENT_AUDIT_OUTPUTS.zip"
OUTPUT = REPO / "Collatz_Research_Archive_CURRENT.zip"
TEMP = REPO / "Collatz_Research_Archive_CURRENT.zip.tmp"
BUILD_RECORD = REPO / "CURRENT_ARCHIVE_BUILD.json"
GITHUB_FILE_LIMIT = 100_000_000


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def iter_files(root: Path):
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        yield path


def arc_join(*parts: str) -> str:
    return str(PurePosixPath(*parts))


def add_tree(entries: list[tuple[Path, str]], root: Path, prefix: str) -> None:
    if not root.is_dir():
        raise FileNotFoundError(root)
    for path in iter_files(root):
        entries.append((path, arc_join(prefix, path.relative_to(root).as_posix())))


def zip_add(zf: zipfile.ZipFile, path: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(arcname, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zf.writestr(
        info,
        path.read_bytes(),
        compress_type=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    )


def main() -> None:
    if ARCHIVE_ROOT.resolve().parent != EXTRACTED.resolve():
        raise AssertionError("archive root escaped extracted directory")
    if OUTPUT.resolve().parent != REPO.resolve() or TEMP.resolve().parent != REPO.resolve():
        raise AssertionError("output path escaped repository")

    entries: list[tuple[Path, str]] = []
    add_tree(entries, ARCHIVE_ROOT, ARCHIVE_ROOT_NAME)
    add_tree(entries, RESEARCH_MANAGER, arc_join(ARCHIVE_ROOT_NAME, "RESEARCH_MANAGEMENT"))
    add_tree(
        entries,
        AUDIT_OUTPUTS,
        arc_join(ARCHIVE_ROOT_NAME, "INDEPENDENT_AUDITS", "CP20_TASK8B3_E4", "outputs"),
    )
    if not AUDIT_ZIP.is_file():
        raise FileNotFoundError(AUDIT_ZIP)
    entries.append(
        (
            AUDIT_ZIP,
            arc_join(
                ARCHIVE_ROOT_NAME,
                "INDEPENDENT_AUDITS",
                "CP20_TASK8B3_E4",
                AUDIT_ZIP.name,
            ),
        )
    )
    add_tree(entries, REPO / "tools", arc_join(ARCHIVE_ROOT_NAME, "REPOSITORY_TOOLING"))

    entries.sort(key=lambda item: item[1])
    arcnames = [arcname for _, arcname in entries]
    if len(arcnames) != len(set(arcnames)):
        raise AssertionError("duplicate archive member")

    oversized_members = [
        {"path": str(path), "bytes": path.stat().st_size}
        for path, _ in entries
        if path.stat().st_size >= GITHUB_FILE_LIMIT
    ]
    if oversized_members:
        raise AssertionError(f"source member exceeds limit: {oversized_members}")

    if TEMP.exists():
        TEMP.unlink()
    with zipfile.ZipFile(TEMP, "w", allowZip64=True) as zf:
        for path, arcname in entries:
            zip_add(zf, path, arcname)

    zip_bytes = TEMP.stat().st_size
    if zip_bytes >= GITHUB_FILE_LIMIT:
        raise AssertionError(f"generated ZIP exceeds GitHub file limit: {zip_bytes}")
    zip_sha256 = digest(TEMP)
    os.replace(TEMP, OUTPUT)

    record = {
        "archive": OUTPUT.name,
        "archive_sha256": zip_sha256,
        "built_utc": datetime.now(timezone.utc).isoformat(),
        "member_count": len(entries),
        "schema": "COLLATZ_CURRENT_ARCHIVE_BUILD_V1",
        "source_groups": [
            "full extracted research archive",
            "research_manager",
            "independent E4 audit outputs",
            "repository tooling",
        ],
        "total_uncompressed_bytes": sum(path.stat().st_size for path, _ in entries),
        "zip_bytes": zip_bytes,
    }
    BUILD_RECORD.write_text(
        json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
