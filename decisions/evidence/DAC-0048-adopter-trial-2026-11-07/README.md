# Adopter trial of decision recovery — 7 November 2026

Evidence for [DAC-0048](../../DAC-0048-historical-recovery-doctrine.md), preserved at the owner's
instruction ([the return](../TDR-0048-0049-owner-return-2026-11-07.md)): the friction log, the fixture
versions, the candidate outputs, the independent contract checks, and the limitations. **It is one run.
It does not satisfy TDR-0049's confirmation, and a further independent confirmation is required before
that gate is met.**

## What ran

An AI agent, launched for the purpose and of the same model as the drafter of the records, ran
[`recover-decision-records`](../../../records/decision/skills/recover-decision-records/) from the
published files alone, as an adopter would on first use. It was forbidden to open the decision fixtures,
`tests/` or the worked examples, or to run the suite, and it modified nothing in the checkout. It wrote
its own validator for the pipeline's validation stage.

| | |
|---|---|
| **Pin** | the standard at `665aa6e` when the run began, 09:29 UTC |
| **During the run** | `7b2fb20` landed at 09:31 and changed two specification files the agent read — `historical-recovery.md` (rule 5, the least grade) and `historical-candidate.md` (integrity rule 6). Which version of those two files the agent read is **not established**. The contract — schemas and suite — is identical at both commits |
| **Inputs** | twelve case files, [`sources/CASE-018.md`](sources/) to `CASE-029.md`, one organisation each; and the six Brackwell documents, [`sources/brackwell/`](sources/brackwell/), as one run |
| **Outputs** | [`out/`](out/): seventeen candidates, thirteen reports, and the friction log, [`out/friction.md`](out/friction.md) |

**Fixture versions.** Each case file is the *Sources* section of the decision fixture of the same number
at `665aa6e`, verbatim, with the title, expected answers and must-not sections removed — except
CASE-019 and CASE-024, whose fixtures referred to a source "as in FIX-018" and whose case files spell
that source out so each case stands alone. The Brackwell files are byte-identical to
[`tests/adoption/brackwell/`](../../../tests/adoption/brackwell/) at the pin, and unchanged since. The
agent did not see [FIX-301](../../../tests/adoption/FIX-301-brackwell-reconstruction.md), the expected
reconstruction.

## How many candidates: seventeen

**Seventeen, from one run.** Eleven of the twelve cases produced one candidate each — CASE-027 produced
none, and five not-a-decision findings, one per reason — and the Brackwell run produced six. The
seventeen files are in `out/`; the friction log's closing check says *all 17 candidates pass*.

The agent's report to the drafter opened *"I ran the recovery over all 13 runs and got 16 candidates"*.
The same report's own file list (eleven case candidates and six Brackwell) and its per-run counts both
total seventeen. The sixteen is an arithmetic slip in one sentence, not an earlier stage of the trial:
there was one run, one report and one set of files. The drafter repeated the sixteen in a first summary
before counting the files.

## The checks

| Check | By | Result |
|---|---|---|
| The agent's own validation stage — [`validate.py`](validate.py): schema, integrity rules, recovery roles, fragment hashes re-read from the sources, contemporaneity recomputed | the trial agent | all seventeen pass, by its report |
| **The suite's own candidate contract, at the pin** — [`check.py`](check.py), reading the schemas, the manifests and `tests/verify.py` from the pinned commit | the drafter, independently of the agent | **17 of 17** — [`check-output.txt`](check-output.txt); the same at `665aa6e` and `7b2fb20` |
| The same check against the amended contract (informative) | the drafter | 14 of 17. All three failures are the evidence kind renamed after the trial (`prior-unlinked` to `unlinked`) |

Contract conformance is not historical correctness. The check against the amended contract shows it
most plainly: the three candidates that split the Cabinet's single vote (`brackwell-2` to `-4`) still
pass, because whether a vote is one act is a judgement no schema can see. The owner's ruling on it
reaches them only through review.

## What the trial changed

1. **Corrections drafted on its findings** (`f128984`): rules the suite enforced and the specifications
   did not state; fixtures that took dates from filenames, against the doctrine they illustrate; a
   hindsight route through the `evidence-*` roles; grouping on subject; the evidence kind for undated
   material.
2. **Four escalations, ruled by the owner** in the return: authority traced by fit (FIX-301 had called
   the Cabinet's approval competent because it fits the scheme; the agent refused to record that as
   authority), the three resolutions, the scheme's adoption, and the temporary arrangement — together
   with a substrate gap, single-source grouping, which the agent had to describe with a basis it did not
   meet.
3. **One correction reversed.** The agent read the specification as making a minute's own same-day
   context indeterminate (friction §3.6). `f128984` answered by stating that same-day capture is contemporaneous —
   what the suite already computed; the owner's same-day correction replaced both: a shared date orders nothing, and only evidence that
   material was before whoever acted closes the order.

## Limitations

- **One run, by one agent**, of the same model as the drafter — not a human adopter, and not
  independent of the drafter in the way DAC-0032's external validation requires.
- **Material the drafter wrote.** Every case was written by the author of the records it tests.
- **The checkout moved during the run**, as above.
- **The independent check is the drafter's**, applying the standard's own code; it shows the outputs
  meet the contract, not that they are right.
- **Structural conformance needed conventions** the standard did not supply in several places — the
  friction log names each.

## Sanitisation

Two edits, and nothing else changed. In `out/friction.md`, the validator's location *"scratchpad
`tools/validate.py`"* reads *"`validate.py`, preserved beside this log"*. In `validate.py`, the two
hard-coded local paths are read from the environment (`MTDR_ROOT`, `TRIAL_ROOT`). Before the edits
the two files hashed to:

```
ea09ea7ade2b007634d2e667b5e110912e1fb7a57e32f93c092d347b4887dc7e  out/friction.md
57a2841b687150024f79dbe87b6546b8d70dbfa5895ce90c15125f9f2fe00a40  validate.py
```

Every preserved file's hash, as committed, is in [`SHA256SUMS`](SHA256SUMS).

## Reproducing

```bash
uv run python decisions/evidence/DAC-0048-adopter-trial-2026-11-07/check.py
```

To rerun the agent's own validator, check out the pin and run it with `MTDR_ROOT` at that checkout and
`TRIAL_ROOT` at this directory.
