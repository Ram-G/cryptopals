"""Set 1, Challenge 1: Convert hex to base64."""

from base64 import b64encode


INPUT_HEX = (
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f"
    "69736f6e6f7573206d757368726f6f6d"
)
EXPECTED = (
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
)


def hex_to_base64(hex_text: str) -> str:
    """Convert a hex-encoded string to a base64-encoded string."""
    raw = bytes.fromhex(hex_text)
    return b64encode(raw).decode("ascii")


def solve() -> str:
    return hex_to_base64(INPUT_HEX)


def verify() -> str:
    """Return the solution after checking it against the expected answer."""
    actual = solve()
    if actual != EXPECTED:
        raise AssertionError(f"expected {EXPECTED!r}, got {actual!r}")
    return actual


if __name__ == "__main__":
    print(verify())
