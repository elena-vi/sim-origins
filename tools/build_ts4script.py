"""Build a Sims 4 .ts4script archive from the source package."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

DEFAULT_PACKAGE_NAME = "sim_origins"
DEFAULT_SOURCE_ROOT = Path("src")
DEFAULT_OUTPUT_PATH = Path("dist/sim-origins.ts4script")
BOOTSTRAP_MODULE_NAME = "sim_origins_bootstrap.py"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


@dataclass(frozen=True)
class ArchiveEntry:
    """A source file and the path it should have inside the archive."""

    source_path: Path
    archive_path: str


def collect_package_files(source_root: Path, package_name: str) -> List[ArchiveEntry]:
    """Collect Python files that should be included in the script archive."""

    package_dir = source_root / package_name
    if not package_dir.is_dir():
        raise FileNotFoundError(
            f"Could not find package directory for .ts4script build: {package_dir}"
        )

    bootstrap_path = source_root / BOOTSTRAP_MODULE_NAME
    if not bootstrap_path.is_file():
        raise FileNotFoundError(
            f"Could not find .ts4script bootstrap module: {bootstrap_path}"
        )

    entries = [
        ArchiveEntry(
            source_path=path,
            archive_path=path.relative_to(source_root).as_posix(),
        )
        for path in sorted(package_dir.rglob("*.py"))
        if "__pycache__" not in path.parts
    ]

    if not entries:
        raise ValueError(f"No Python files found for .ts4script build in {package_dir}")

    entries.append(
        ArchiveEntry(
            source_path=bootstrap_path,
            archive_path=bootstrap_path.name,
        )
    )
    return sorted(entries, key=lambda entry: entry.archive_path)


def write_archive(entries: Iterable[ArchiveEntry], output_path: Path) -> Path:
    """Write archive entries to a deterministic .ts4script zip file."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(str(output_path), "w") as archive:
        for entry in entries:
            zip_info = ZipInfo(entry.archive_path)
            zip_info.compress_type = ZIP_DEFLATED
            zip_info.date_time = ZIP_TIMESTAMP
            archive.writestr(zip_info, entry.source_path.read_bytes())

    return output_path


def build_ts4script(
    source_root: Path = DEFAULT_SOURCE_ROOT,
    package_name: str = DEFAULT_PACKAGE_NAME,
    output_path: Path = DEFAULT_OUTPUT_PATH,
) -> Path:
    """Build the Sims 4 script archive and return its path."""

    entries = collect_package_files(source_root=source_root, package_name=package_name)
    return write_archive(entries=entries, output_path=output_path)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Build the Sim Origins .ts4script archive."
    )
    parser.add_argument(
        "--source-root",
        default=str(DEFAULT_SOURCE_ROOT),
        help="Directory containing the package source tree.",
    )
    parser.add_argument(
        "--package",
        default=DEFAULT_PACKAGE_NAME,
        help="Package directory name to include in the archive.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT_PATH),
        help="Path to the .ts4script archive to write.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """CLI entry point."""

    args = parse_args(argv or [])
    output_path = build_ts4script(
        source_root=Path(args.source_root),
        package_name=args.package,
        output_path=Path(args.output),
    )
    print(f"Built {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
