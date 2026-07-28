"""Set 1, Challenge 1: Convert hex to base64.

Online: https://cryptopals.com/sets/1/challenges/1
"""

EXPECTED = None


def solve():
    """Return the challenge answer."""
    raise NotImplementedError("implement this challenge")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from util import run_and_verify

    raise SystemExit(run_and_verify(solve, EXPECTED))
