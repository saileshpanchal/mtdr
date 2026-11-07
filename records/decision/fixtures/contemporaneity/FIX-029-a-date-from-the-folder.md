# FIX-029 — a date from the folder: a time needs a basis

> **Fictional worked fixture.** Morrow Street Housing Association, its people and its numbers are invented.

**Proves** constraint 3 of DAC-0048: a time is the fragment's own statement or its source's recorded
metadata, or it is `unknown`.

## Sources

**A — Working note, `operations/2019-Q1/repairs-options.md`**, no date in the text and none in the
file's recorded metadata

> One line for repairs would cost less than four offices, if the evening rota changes.

**B — Board minute, 2019-03-14** — the single repairs line agreed.

## Expected

- **A's `capture_time` and `creation_time` are `unknown`.** The folder name `2019-Q1` is not a
  basis. A computes `indeterminate`.
- **A is `unlinked`**, classified by what it is; its unknown times make it `indeterminate`, and its
  contribution cannot be presented as context. Its kind says nothing about when it was written.

## Must not

- **Set A's capture time to `2019-01`, `2019-03`, or `2019` from the folder.** Each would make A
  contemporaneous, and each is a time with no basis.
- **Use a reviewer's knowledge of when the note was written** in place of the note or its metadata.

## What this fixture detects

Backdating by the well-intentioned route: a gap closed with the most likely date, after which the
computation is faithful to a time that was never evidenced.
