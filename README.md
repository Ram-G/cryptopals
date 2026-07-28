# Cryptopals

An offline, multi-language workspace for working through the
[Cryptopals Crypto Challenges](https://cryptopals.com/).

> [!WARNING]
> This repository contains challenge solutions and therefore contains spoilers.

## Repository layout

```text
descriptions/                 Offline challenge pages and official input data
solutions/
  python/
    set01/                    Current Python solutions
    archive/                  Earlier Python 2 implementations
  rust/
    archive/                  Earlier Rust implementations
  csharp/
    archive/                  Earlier C# implementation
tools/new-solution            Solution-file scaffolder
```

Current work uses `solutions/<language>/setNN/chNN.*`. Directories under
`archive/` preserve earlier implementations from the original repository; they
are useful references but are not the active workflow.

## Run the current Python solution

The current solution uses only the Python standard library:

```sh
python3 solutions/python/set01/ch01.py
```

The file checks its result against the expected challenge answer before
printing it.

For challenges that need third-party packages, create a local environment and
install only what the implementation requires:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install PACKAGE
```

The `.venv/` directory and generated caches are ignored by Git.

## Start a solution

From the repository root, scaffold a Python solution from the offline corpus:

```sh
./tools/new-solution 1 2
```

This creates `solutions/python/set01/ch02.py`, includes the challenge title and
description path, and supplies `solve()` and `verify()` placeholders. Set
`EXPECTED`, implement `solve()`, then run the file directly.

Python is currently the only template. The explicit equivalent is:

```sh
./tools/new-solution --language python 1 2
```

The scaffolder validates set and challenge numbers and refuses to overwrite an
existing solution.

## Read challenges offline

Open `descriptions/cryptopals.com/index.html` directly, or serve the mirror
locally:

```sh
python3 -m http.server 8000 --directory descriptions/cryptopals.com
```

Then open <http://localhost:8000/>. Official challenge input files are under
`descriptions/cryptopals.com/static/challenge-data/`.

## Add another language

Use the same set-based shape under `solutions/<language>/`. Keep small
expected-answer verification beside the implementation and use separate data
files only when a challenge needs large vectors or fixtures. To scaffold the
language, add a renderer and file-extension mapping to `tools/new-solution`,
then document its idiomatic run command here.

See [solutions/README.md](solutions/README.md) for the detailed solution and
archive conventions.
