# Solution conventions

Current implementations are organized first by language and then by challenge
set:

```text
solutions/
  python/
    set01/
      ch01.py
    set02/
      ch09.py
  rust/
    set01/
      ch01.rs
  csharp/
    set01/
      ch01.cs
```

Create set directories only when they are needed. Use zero-padded set and
challenge numbers so paths sort in challenge order. Language-specific project
files and helpers should stay within that language directory.

## Verification

For a small exercise, keep the expected answer in the same source file as the
solution. The language runner owns shared verification behavior: it loads the
challenge, invokes `solve()`, and either reports a mismatch or prints the
verified result. Each Python challenge has a small `__main__` entry point that
delegates to the same utility, so direct execution behaves identically.

Run a Python solution by set and challenge number:

```sh
./solutions/python/run-solution 1 1  # from the repository root
./run-solution 1 1                   # from solutions/python/
../run-solution 1 1                  # from solutions/python/set01/
```

You can also run `python3 chNN.py` from its set directory or use VS Code's
top-right play button. Python 3.10 or newer is required.

Use separate fixture or data files when inputs are large, shared, or numerous.
Prefer the official files already available under
`descriptions/cryptopals.com/static/challenge-data/` when applicable. A
language-native test suite can be added later when an implementation develops
reusable components or more complex edge cases.

## Scaffolding

The current Python template can be created from the repository root:

```sh
./solutions/python/init-solution 1 2  # from the repository root
./init-solution 1 2                   # from solutions/python/
../init-solution 1 2                  # from solutions/python/set01/
```

The command reads the local challenge corpus, creates the appropriate set
directory, and refuses to replace an existing file. Other languages can add
equivalent commands within their language directory when needed.

## Archived implementations

Earlier repository content is retained at:

- `solutions/python/archive/` — Python 2-era Set 1 scripts.
- `solutions/rust/archive/` — the original Set 1 Cargo project.
- `solutions/csharp/archive/` — the original Visual Studio/.NET solution.

Archived code preserves historical work and may require its original toolchain
or dependencies. New work belongs in the set directories outside `archive/`.
