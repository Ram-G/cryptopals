"""Shared challenge-corpus support for language-specific scaffolders."""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
import re


@dataclass(frozen=True)
class Challenge:
    """Metadata needed to initialize one challenge solution."""

    set_number: int
    challenge_number: int
    title: str

    @property
    def url(self) -> str:
        return (
            f"https://cryptopals.com/sets/{self.set_number}/"
            f"challenges/{self.challenge_number}"
        )


class ChallengeHeadingParser(HTMLParser):
    """Collect text from h3 headings in a Cryptopals challenge page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_heading = False
        self._parts: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag.lower() == "h3":
            self._in_heading = True
            self._parts = []

    def handle_data(self, data: str) -> None:
        if self._in_heading:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "h3" and self._in_heading:
            heading = " ".join("".join(self._parts).split())
            if heading:
                self.headings.append(heading)
            self._in_heading = False
            self._parts = []


def find_description(
    root: Path, set_number: int, challenge_number: int
) -> Path:
    challenge_dir = (
        root
        / "descriptions"
        / "cryptopals.com"
        / "sets"
        / str(set_number)
        / "challenges"
    )
    candidates = (
        challenge_dir / f"{challenge_number}.html",
        challenge_dir / f"{challenge_number}.txt",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise ValueError(
        f"challenge {challenge_number} is not present in set {set_number}"
    )


def title_from_html(description: Path) -> str:
    parser = ChallengeHeadingParser()
    parser.feed(description.read_text(encoding="utf-8"))
    site_heading = "the cryptopals crypto challenges"
    for heading in parser.headings:
        if heading.casefold() != site_heading:
            return heading
    raise ValueError(f"could not find a challenge title in {description}")


def title_from_text(description: Path, challenge_number: int) -> str:
    title_pattern = re.compile(rf"^{challenge_number}\.\s+(.+?)\s*$")
    for line in description.read_text(encoding="utf-8").splitlines():
        match = title_pattern.match(line)
        if match:
            return match.group(1)
    raise ValueError(f"could not find a challenge title in {description}")


def load_challenge(
    root: Path, set_number: int, challenge_number: int
) -> Challenge:
    """Load challenge metadata from the offline corpus."""
    description = find_description(root, set_number, challenge_number)
    if description.suffix == ".html":
        title = title_from_html(description)
    else:
        title = title_from_text(description, challenge_number)
    return Challenge(set_number, challenge_number, title)


def create_parent_directories(root: Path, destination: Path) -> None:
    """Create destination parents without traversing symbolic links."""
    current = root
    for part in destination.relative_to(root).parts[:-1]:
        current /= part
        if current.is_symlink():
            raise ValueError(f"refusing to use symbolic-link directory {current}")
        try:
            current.mkdir()
        except FileExistsError:
            if not current.is_dir():
                raise ValueError(f"parent path is not a directory: {current}")


def write_new_file(root: Path, destination: Path, contents: str) -> None:
    """Create a new file without overwriting or traversing symlink parents."""
    create_parent_directories(root, destination)
    with destination.open("x", encoding="utf-8") as output_file:
        output_file.write(contents)
