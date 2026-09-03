#!/usr/bin/env python3
"""Build the deterministic current Collatz research archive.

Primary mode uses the historical extracted tree when available. Recovery mode
rebuilds from the already committed current archive, preserving all static
historical members byte-for-byte after decompression while replacing canonical
management/tooling/continuity/audit overlays from the repository.
"""

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
ZERO_TRUST_ROOT = REPO / "bagimsiz-denetim"
START_HERE = REPO / "START_HERE_CURRENT_HANDOFF.md"
CURRENT_STATE = REPO / "CURRENT_RESEARCH_STATE.json"
OUTPUT = REPO / "Collatz_Research_Archive_CURRENT.zip"
TEMP = REPO / "Collatz_Research_Archive_CURRENT.zip.tmp"
BUILD_RECORD = REPO / "CURRENT_ARCHIVE_BUILD.json"
GITHUB_FILE_LIMIT = 100_000_000

DYNAMIC_PREFIXES = (
    f"{ARCHIVE_ROOT_NAME}/RESEARCH_MANAGEMENT/",
    f"{ARCHIVE_ROOT_NAME}/INDEPENDENT_AUDITS/CP20_TASK8B3_E4/",
    f"{ARCHIVE_ROOT_NAME}/INDEPENDENT_AUDITS/CANONICAL_ZERO_TRUST/",
    f"{ARCHIVE_ROOT_NAME}/REPOSITORY_TOOLING/",
    f"{ARCHIVE_ROOT_NAME}/CONTINUITY/",
)

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

def dynamic_entries() -> list[tuple[Path, str]]:
    entries: list[tuple[Path, str]] = []
    def add_tree(root: Path, prefix: str) -> None:
        if not root.is_dir():
            raise FileNotFoundError(root)
        for path in iter_files(root):
            entries.append((path, arc_join(prefix, path.relative_to(root).as_posix())))
    add_tree(RESEARCH_MANAGER, arc_join(ARCHIVE_ROOT_NAME, "RESEARCH_MANAGEMENT"))
    add_tree(AUDIT_OUTPUTS, arc_join(ARCHIVE_ROOT_NAME, "INDEPENDENT_AUDITS", "CP20_TASK8B3_E4", "outputs"))
    if not AUDIT_ZIP.is_file():
        raise FileNotFoundError(AUDIT_ZIP)
    entries.append((AUDIT_ZIP, arc_join(ARCHIVE_ROOT_NAME, "INDEPENDENT_AUDITS", "CP20_TASK8B3_E4", AUDIT_ZIP.name)))
    if ZERO_TRUST_ROOT.is_dir():
        add_tree(ZERO_TRUST_ROOT, arc_join(ARCHIVE_ROOT_NAME, "INDEPENDENT_AUDITS", "CANONICAL_ZERO_TRUST"))
    add_tree(REPO / "tools", arc_join(ARCHIVE_ROOT_NAME, "REPOSITORY_TOOLING"))
    for path in (START_HERE, CURRENT_STATE):
        if not path.is_file():
            raise FileNotFoundError(path)
        entries.append((path, arc_join(ARCHIVE_ROOT_NAME, "CONTINUITY", path.name)))
    return entries

def zipinfo(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.create_system = 0
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info

def write_bytes(zf: zipfile.ZipFile, name: str, data: bytes) -> None:
    zf.writestr(zipinfo(name), data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

def main() -> None:
    dynamic = dynamic_entries()
    dynamic_names = {name for _, name in dynamic}
    if len(dynamic_names) != len(dynamic):
        raise AssertionError("duplicate dynamic archive member")

    if TEMP.exists():
        TEMP.unlink()

    static_count = 0
    total_uncompressed = 0
    with zipfile.ZipFile(TEMP, "w", allowZip64=True) as out:
        if ARCHIVE_ROOT.is_dir():
            for path in iter_files(ARCHIVE_ROOT):
                name = arc_join(ARCHIVE_ROOT_NAME, path.relative_to(ARCHIVE_ROOT).as_posix())
                if any(name.startswith(prefix) for prefix in DYNAMIC_PREFIXES):
                    continue
                data = path.read_bytes()
                write_bytes(out, name, data)
                static_count += 1
                total_uncompressed += len(data)
        elif OUTPUT.is_file():
            with zipfile.ZipFile(OUTPUT) as old:
                if old.testzip() is not None:
                    raise AssertionError("existing current archive CRC failure")
                for item in sorted(old.infolist(), key=lambda x: x.filename):
                    name = item.filename
                    if item.is_dir() or any(name.startswith(prefix) for prefix in DYNAMIC_PREFIXES):
                        continue
                    data = old.read(name)
                    write_bytes(out, name, data)
                    static_count += 1
                    total_uncompressed += len(data)
        else:
            raise FileNotFoundError("neither extracted historical tree nor existing current archive is available")

        for path, name in sorted(dynamic, key=lambda row: row[1]):
            data = path.read_bytes()
            write_bytes(out, name, data)
            total_uncompressed += len(data)

    with zipfile.ZipFile(TEMP) as zf:
        names = [x.filename for x in zf.infolist()]
        if len(names) != len(set(names)):
            raise AssertionError("duplicate archive member")
        bad = zf.testzip()
        if bad is not None:
            raise AssertionError(f"archive CRC failure: {bad}")
        member_count = len(names)

    zip_bytes = TEMP.stat().st_size
    if zip_bytes >= GITHUB_FILE_LIMIT:
        raise AssertionError(f"generated ZIP exceeds GitHub file limit: {zip_bytes}")
    archive_sha256 = digest(TEMP)
    os.replace(TEMP, OUTPUT)

    record = {
        "archive": OUTPUT.name,
        "archive_sha256": archive_sha256,
        "built_utc": datetime.now(timezone.utc).isoformat(),
        "member_count": member_count,
        "schema": "COLLATZ_CURRENT_ARCHIVE_BUILD_V1",
        "source_groups": [
            "preserved historical current-archive static members (or full extracted research archive when available)",
            "research_manager",
            "independent E4 audit outputs",
            "canonical zero-trust audit records",
            "repository tooling",
            "continuity handoff snapshot",
        ],
        "static_member_count": static_count,
        "total_uncompressed_bytes": total_uncompressed,
        "zip_bytes": zip_bytes,
    }
    BUILD_RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
