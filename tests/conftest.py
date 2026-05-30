"""Shared pytest configuration for HC:// runtime and API contract tests."""

from __future__ import annotations

import pytest


@pytest.fixture()
def anyio_backend() -> str:
    """Run AnyIO-marked tests on asyncio without requiring optional Trio installs."""

    return "asyncio"
