# Independent confirmation of decision recovery — 26 November 2026

Evidence for the maintainer's decision on DAC-0048, TDR-0048 and TDR-0049, under the return of
7 November ("Run another independent confirmation before satisfying TDR-0049's gate"). **It is not
ratification evidence, it satisfies no gate by itself, and it makes no recommendation.** Whether it
meets the confirmation the return asks for is the maintainer's judgement.

## Who did what

| Role | Who | What they had |
|---|---|---|
| Corpus author | An AI agent, Claude Sonnet 5.5, launched for the purpose | No access to MTDR, its repository or any tool to be applied; no network. Wrote nine documents and an answer key from its own invention ([`corpus/key/authoring-note.md`](corpus/key/authoring-note.md)) |
| Adopter | An AI agent, Claude Fable 5.2, launched for the purpose. Not a person | A clean clone of MTDR at `57d68c00406f2260b832be0fc8c14a0ddbc9d692`, the nine documents, an empty project folder and an empty output folder |
| Comparison with the key | The maintainer's assistant (Claude Opus 5.5), after the adopter had finished | The adopter's outputs and the key |

Neither agent drafted DAC-0048, TDR-0048 or TDR-0049. All three are models from the same vendor as the
drafter. No person took part.

**Sealing.** The adopter never saw the key, and the key's author never saw MTDR. The corpus and key
were hashed as the run began, at 22:57 UTC, with the key held outside every folder the adopter was
given (aggregate
`aa866e4d84d1ce9bdda0bb48f84d7586ffe038a1c686a70250f803565afc62ca`). The hashes in
[`SHA256SUMS`](SHA256SUMS) still verify.

**What the adopter was told not to open.** Anything under `tests/`, `records/*/fixtures/` or
`decisions/evidence/`, so it saw neither the worked example nor the earlier trial. It was told not to
run `tests/verify.py`, not to change the clone, and not to read history or other branches. It reports
opening none of them, and the clone's `git status` was empty at the end. Nobody coached it.

**What it did read that weakens the evidence.** Before producing output it read the folder validator's
source (`mtdr_validation/fidelity.py` in full, `folder.py` lines 1–200), because the validator's input
format is not documented (its friction item 1). The validator's own README says such a run should come
"from a checkout the engine cannot read". The validator's pass is therefore weaker evidence than the
match against the key, which the adopter could not have tuned to.

## Results

- **Decisions.** The key names four decisions. The adopter recovered four candidates, one for each,
  and no others ([`comparison.md`](comparison.md)).
- **Look-alikes.** None of the eight look-alikes the key lists became a candidate. Seven were
  reported as findings; the eighth, the proposal of 1 October, is inside HC-003 as what the Chair
  agreed to.
- **Validator.** `python -m mtdr_validation out --sources sources` passed structural, semantic and
  relational (including source fidelity) for all four, on its first and only run.
- **Where it guessed.** It invented the form of every output except the candidate, and it settled
  three values by its own judgement: a date with no year, a decision log's evidence kind, and a joint
  owner.
- **Where the two readings of invocation diverge.** The adopter followed the specification's broad
  reading for one candidate (HC-003). Under the narrow reading, which TDR-0049 states, its authority
  would be missing and the instrument reported as applicability. See the comparison, and RR3 of the
  review of 26 November.

The adopter's own report is [`out/REPORT.md`](out/REPORT.md), verbatim except that local paths are
replaced by `<run>` and `<scratch>`. Its outputs are in [`out/`](out/), with the same replacement and
nothing else changed.

## What this does and does not establish

| The confirmation asked for | This run |
|---|---|
| An adopter who is not the drafter (DAC-0048 debt row 5) | Met in the letter. The adopter is an AI agent, not the drafter, and from the same vendor |
| Material the drafter did not write (debt row 5) | Met. The corpus was written by a third agent with no sight of MTDR |
| "A further independent confirmation" (the return) | For the maintainer to judge. No person took part, and the engine read the validator's source |
| TDR-0049's `confirmed_by_outcome`: "an implementation outside this repository loads the not-a-decision reasons and the recovery roles from the published vocabulary" | Not met. The adopter read the vocabulary and carried out the skills itself. It is not an implementation outside this repository |
| DAC-0045 constraint 5: provenance for uncoached evidence | Recorded above |

It ran at `57d68c0`, before the corrections that follow the review of 26 November. The one correction
that changes an output is RR3: under the narrow reading, HC-003's authority contribution would be a
wrong answer.
