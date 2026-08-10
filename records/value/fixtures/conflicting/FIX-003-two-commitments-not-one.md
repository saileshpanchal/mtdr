# FIX-003 — two commitments, not one

> **Fictional worked fixture.** Ashworth Building Society, its programme and its numbers are invented.

**Proves** the invariant: **proximity is never identity.** Two value commitments from one programme,
described in near-identical language in the same steering pack, must not merge.

This is the most important fixture of the four, and the only one whose **failure produces output that
looks better than a pass** — one tidy candidate instead of two. It must be run every time, and never
judged by appearance.

## Sources

Both extracts are from the same document, `arrears-programme-steering-2026-05-12.pdf`, two pages
apart, written to the same template by the same author.

**A — page 4**

> Workstream 1 will reduce cost-to-serve in collections by an estimated £600k annually. Baseline:
> £3.1m, measured FY25 from the Finance MI pack. Benefit accrues to the Society through reduced
> operational cost.

**B — page 6**

> Workstream 2 will reduce cost-to-serve in collections by an estimated £600k annually. Baseline:
> £3.1m, measured FY25 from the Finance MI pack. Benefit accrues to customers in arrears through
> earlier intervention and fewer possession proceedings.

The value, the baseline, the measurement source, the wording and the document are shared. The
**beneficiary differs**, and the workstream differs.

## Expected

- **2 SourceFragments.**
- **Contributions to two distinct commitments**, each with its own `beneficiary` — the Society in A,
  customers in arrears in B.
- **Exactly 2 CandidateAssemblies.** Both `status: candidate`.
- **Neither `grouping_basis` cites the other's fragment.** Each candidate groups only its own
  contributions.
- **`unresolved` on at least one candidate notes the question** — the shared baseline may mean these
  double-count one saving, or may mean two workstreams draw on one measured starting position. The
  evidence does not settle it, so it is recorded, not decided.
- Both candidates report the same substantial `missing_semantics` — among them `falsifying-signal`,
  `committed-by`, `authority`, `finance-countersignatory`, `due-point` and `linked-decision`.

Note that both candidates are **inadmissible** for want of a linked decision, and that is not a
defect in the fixture. This fixture tests **grouping**, and grouping happens before admission. A
skill that merges these two and only then discovers the admissibility failure has already made the
error this fixture exists to catch.

## Must not

- **Merge into one candidate**, on any basis. Same document, same page range, same programme, same
  author, same figure, same baseline, same wording — none is admissible, individually or together.
  Semantic similarity here is near-total and is worth nothing.
- **Resolve the double-count question.** Recording it is required; deciding it is not this skill's
  work.
- **Report the identical £600k as corroboration.** One claim written twice is one claim, not two
  pieces of evidence. Treating repetition as strength is confidence inflation.
- **Assign `assembly_confidence: high` to either candidate.** The shared baseline is real
  disconfirming evidence about how cleanly these separate.
- **Drop either candidate as a duplicate of the other.**

## What this fixture detects

Any grouping strategy driven by embedding distance, document proximity or figure matching. All three
merge here, and all three produce a single coherent, fully provenanced record of a £600k commitment
that does not exist — indistinguishable by inspection from a correct one.

The only signal that separates them is the beneficiary, one clause in each extract. A skill that
groups before reading the beneficiary role will fail, and will fail invisibly.
