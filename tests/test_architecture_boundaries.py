"""Architecture contract tests for the V0 project structure."""

import ast
import importlib
import sys
from pathlib import Path

import pytest

SOURCE_ROOT = Path(__file__).resolve().parents[1] / "src"
PACKAGE_ROOT = SOURCE_ROOT / "sim_origins"
DOMAIN_ROOT = PACKAGE_ROOT / "domain"
PYTHON_SOURCE_ROOTS = [SOURCE_ROOT, Path(__file__).resolve().parents[1] / "tools"]
FORBIDDEN_DOMAIN_IMPORT_PREFIXES = (
    "interactions",
    "objects",
    "services",
    "sim_origins.sims_integration",
    "sims4",
    "situations",
    "ui",
)


@pytest.mark.parametrize(
    "module_name",
    [
        "sim_origins",
        "sim_origins.application",
        "sim_origins.domain",
        "sim_origins.infrastructure",
        "sim_origins.sims_integration",
    ],
)
def test_architecture_packages_import_without_sims_runtime(module_name):
    importlib.import_module(module_name)


def test_domain_does_not_import_sims_runtime_or_integration_modules():
    violations = []

    for path in DOMAIN_ROOT.rglob("*.py"):
        tree = ast.parse(path.read_text(), filename=str(path))
        for import_name in imported_names(tree):
            if import_name.startswith(FORBIDDEN_DOMAIN_IMPORT_PREFIXES):
                violations.append(f"{path} imports {import_name}")

    assert violations == []


def test_python_sources_parse_as_python_37_compatible_syntax():
    parse_kwargs = {}
    if sys.version_info >= (3, 8):
        parse_kwargs["feature_version"] = (3, 7)

    for root in PYTHON_SOURCE_ROOTS:
        for path in root.rglob("*.py"):
            ast.parse(path.read_text(), filename=str(path), **parse_kwargs)


def imported_names(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                yield alias.name
        elif isinstance(node, ast.ImportFrom) and node.module:
            yield node.module
