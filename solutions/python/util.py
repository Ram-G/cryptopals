"""Shared helpers for Python challenge solutions."""

from __future__ import annotations

import sys
from collections.abc import Callable
from typing import TypeVar


Answer = TypeVar("Answer")


def verify(solve: Callable[[], Answer], expected: Answer | None) -> Answer:
    """Run a solution and return its answer after checking the expected value."""
    if expected is None:
        raise RuntimeError("set EXPECTED before verifying the solution")
    actual = solve()
    if actual != expected:
        raise AssertionError(f"expected {expected!r}, got {actual!r}")
    return actual


def run_and_verify(
    solve: Callable[[], Answer], expected: Answer | None
) -> int:
    """Run, verify, and print a solution with concise command-line errors."""
    try:
        answer = verify(solve, expected)
    except (AssertionError, NotImplementedError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(answer)
    print("✅ verified")
    return 0
