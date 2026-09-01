#!/usr/bin/env python3
"""Safely restore the current Collatz archive into a fresh working tree."""

from __future__ import annotations

from pathlib import Path
import argparse
import hashlib
import json
import shutil
import zipfile


REPO = Path(__file__).resolve().parents[1]
BUILD_PATH = REPO / "CURRENT_ARCHIVE_BUILD.json"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def safe_target(root: Path, member: str) -> Path:
    target = (root / member).resolve()
    target.relative_to(root.resolve())
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--destination",
        type=Path,
        default=REPO / "_restored_current",
        help="fresh destination; existing paths are refused",
    )
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination == REPO.resolve() or REPO.resolve() not in destination.parents:
        raise AssertionError("destination must be a child of the repository")
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite existing destination: {destination}")

    build = json.loads(BUILD_PATH.read_text(encoding="utf-8"))
    archive = REPO / build["archive"]
    if digest(archive) != build["archive_sha256"]:
        raise AssertionError("current archive hash mismatch")

    destination.mkdir(parents=True)
    try:
        with zipfile.ZipFile(archive) as zf:
            if zf.testzip() is not None:
                raise AssertionError("archive CRC failure")
            for info in zf.infolist():
                target = safe_target(destination, info.filename)
                if info.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(info) as source, target.open("xb") as sink:
                    shutil.copyfileobj(source, sink, 1 << 20)
    except Exception:
        raise

    print(f"restored_to={destination}")
    print(f"archive_sha256={build['archive_sha256']}")
    print(f"archive_members={build['member_count']}")
    print("CURRENT ARCHIVE RESTORE: PASS")


if __name__ == "__main__":
    main()
