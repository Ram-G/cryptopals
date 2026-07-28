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
      Challenge01.cs
```

Create set directories only when they are needed. Use zero-padded set and
challenge numbers so paths sort in challenge order. Language-specific project
files and helpers should stay within that language directory.

## Verification

For a small exercise, keep the expected answer and verification logic in the
same source file as the solution. A directly executed solution should fail
clearly when its result differs and print the verified result when it succeeds.

Use separate fixture or data files when inputs are large, shared, or numerous.
Prefer the official files already available under
`descriptions/cryptopals.com/static/challenge-data/` when applicable. A
language-native test suite can be added later when an implementation develops
reusable components or more complex edge cases.

## Scaffolding

The current Python template can be created from the repository root:

```sh
./tools/new-solution 1 2
```

The command reads the local challenge corpus, creates the appropriate set
directory, and refuses to replace an existing file. Future language renderers
use the `--language` option.

## Archived implementations

Earlier repository content is retained at:

- `python/archive/` — Python 2-era Set 1 scripts.
- `rust/archive/` — the original Set 1 Cargo project.
- `csharp/archive/` — the original Visual Studio/.NET solution.

Archived code preserves historical work and may require its original toolchain
or dependencies. New work belongs in the set directories outside `archive/`.
