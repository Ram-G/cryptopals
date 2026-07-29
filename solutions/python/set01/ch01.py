"""Set 1, Challenge 1: Convert hex to base64.

Online: https://cryptopals.com/sets/1/challenges/1
"""

START = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
EXPECTED = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def solve():
    b = bytes.fromhex(START)
    import base64
    encoded_bytes = base64.b64encode(b)
    base64_string = encoded_bytes.decode('ascii')
    return base64_string


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from util import run_and_verify

    raise SystemExit(run_and_verify(solve, EXPECTED))
