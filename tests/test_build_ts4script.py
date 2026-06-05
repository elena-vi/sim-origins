"""Tests for the Sims 4 script archive builder."""

from zipfile import ZipFile

import pytest

from tools.build_ts4script import build_ts4script, collect_package_files


def test_build_ts4script_writes_package_python_files(tmp_path):
    source_root = tmp_path / "src"
    package_root = source_root / "sim_origins"
    package_root.mkdir(parents=True)
    (package_root / "__init__.py").write_text('"""Test package."""\n')
    (package_root / "module.py").write_text("VALUE = 1\n")
    cache_root = package_root / "__pycache__"
    cache_root.mkdir()
    (cache_root / "ignored.py").write_text("SHOULD_NOT_PACKAGE = True\n")

    output_path = tmp_path / "dist" / "sim-origins.ts4script"

    result = build_ts4script(
        source_root=source_root,
        package_name="sim_origins",
        output_path=output_path,
    )

    assert result == output_path
    assert output_path.is_file()

    with ZipFile(output_path) as archive:
        assert archive.namelist() == [
            "sim_origins/__init__.py",
            "sim_origins/module.py",
        ]
        assert archive.read("sim_origins/module.py") == b"VALUE = 1\n"


def test_collect_package_files_fails_when_package_directory_is_missing(tmp_path):
    with pytest.raises(FileNotFoundError, match="Could not find package directory"):
        collect_package_files(source_root=tmp_path / "src", package_name="sim_origins")


def test_build_ts4script_fails_when_package_has_no_python_files(tmp_path):
    source_root = tmp_path / "src"
    (source_root / "sim_origins").mkdir(parents=True)

    with pytest.raises(ValueError, match="No Python files found"):
        build_ts4script(
            source_root=source_root,
            package_name="sim_origins",
            output_path=tmp_path / "dist" / "sim-origins.ts4script",
        )
