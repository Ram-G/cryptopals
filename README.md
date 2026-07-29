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
    init-solution             Python solution scaffolder
    run-solution              Python solution runner
  c/
    set01/                    Current C solutions
    init-solution             C solution scaffolder
  rust/
    archive/                  Earlier Rust implementations
  csharp/
    archive/                  Earlier C# implementation
```

Current work uses `solutions/<language>/setNN/chNN.*`. Directories under
`archive/` preserve earlier implementations from the original repository; they
are useful references but are not the active workflow.

## Work on the current Python scaffold

Python 3.10 or newer is required. Run a challenge directly:

```sh
python3 solutions/python/set01/ch01.py
```

Each file delegates to the shared utility, which checks the result against the
expected answer before confirming the match and printing it. An unfinished
scaffold instead reports that `EXPECTED` must be set. You can also select a
challenge by number with `./solutions/python/run-solution 1 1`. From
`solutions/python/`, use `./run-solution 1 1`; from a set directory, use
`../run-solution 1 1`.

For challenges that need third-party packages, create a local environment and
install only what the implementation requires:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install PACKAGE
```

The `.venv/` directory and generated caches are ignored by Git.

## Start a Python solution

From the repository root, scaffold a Python solution from the offline corpus:

```sh
./solutions/python/init-solution 1 2
```

This creates `solutions/python/set01/ch02.py`, includes the clickable official
URL, and supplies `EXPECTED` and `solve()` placeholders plus a small entry point
that delegates to the shared utility. The command also prints the official URL
in the terminal. Set the expected answer, implement the solution, then run the
file directly or use `run-solution`.

From `solutions/python/`, use the shorter `./init-solution 1 2`; from a set
directory, use `../init-solution 1 2`. The scaffolder validates set and
challenge numbers and refuses to overwrite an existing solution.

## Work on C solutions

GCC or another C17 compiler and GNU Make are required. Initialize a challenge:

```sh
./solutions/c/init-solution 1 1
```

Build every existing C challenge from the repository root:

```sh
make
```

`make c` is equivalent. Sources matching `solutions/c/set*/ch*.c` are
discovered automatically, and executables mirror their paths under `.build/c/`.
Run or debug one directly after building:

```sh
./.build/c/set01/ch01
gdb .build/c/set01/ch01
```

The scaffold represents its final answer as a heap-allocated, printable C
string. The shared utility verifies and frees that answer. Internal challenge
code can still work with binary data.

For Vim, open a source normally, such as
`vim solutions/c/set01/ch01.c`, and run Make from another terminal. No
repository-specific Vim configuration is required.

## Read challenges offline

Open `descriptions/cryptopals.com/index.html` directly or browse the corpus in
the VS Code explorer. Official challenge input files are under
`descriptions/cryptopals.com/static/challenge-data/`.

## VS Code

Install the recommended official Python extensions and open a challenge file.
The top-right play button runs it directly. For debugging, press F5 with **Run
current Python solution** selected; VS Code passes the active file to the
project runner, so breakpoints inside `solve()` work.

To create a challenge, run **Tasks: Run Task** from the Command Palette and
select **Initialize Python solution**. VS Code prompts for the set and challenge
numbers; the created path and official URL appear in the integrated terminal.

## Add another language

Use the same set-based shape under `solutions/<language>/`. Keep small
expected answers beside the implementation and place shared verification or
other reusable behavior in that language's utility module. Use separate data
files only when a challenge needs large vectors or fixtures. When useful, add
language-local `init-solution` and `run-solution` commands and document their
usage here.

See [solutions/README.md](solutions/README.md) for the detailed solution and
archive conventions.
