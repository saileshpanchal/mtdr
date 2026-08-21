# VR-4 reconstruction protocol

**Version 1.1.2 · non-normative · pre-registered**

This protocol is **frozen and published before any arm runs**. It is not part of the MTDR standard and
never becomes part of it. It describes a method for asking one question:

> Given the same closed evidence set, the same frozen MTDR specification and skills, and a
> pre-registered reconstruction protocol, do independent reasoning environments reconstruct materially
> equivalent governed organisational state — **while preserving uncertainty, and exposing rather than
> concealing divergence?**

Three clauses, and the last two are not decoration. A run that converges by resolving an uncertainty
the sources leave open has failed the proposition, not confirmed it.

**Failure is a valid result, and possibly the more valuable one.** If the proposition does not hold,
the boundary-level captures say *where* it stops holding.

## Why this document exists before the results do

A protocol published *after* the runs is a method written with the results already known, whatever the
intention. The sequence is therefore:

> develop privately → synthetic falsification → **freeze** → **publish the frozen protocol** →
> execute the arms → publish captures and comparison

The published commit hash of this document is recorded in every run as `protocol_commit`. A capture
whose `protocol_commit` does not match the published freeze is rejected rather than compared. That is
what makes the discipline checkable instead of self-reported.

## The eight boundaries

Comparison happens at **every** boundary, not at final-record similarity. Two runtimes can land on
similar candidates for different reasons, and final-record comparison misses exactly that. A
disagreement located at a boundary is diagnosable; a similarity score is not.

> source selection → fragment → contribution → assembly → candidate → derivation projection →
> validation → eligibility

## Two validation layers

Every capture is validated twice, against two separately named layers, and the report says which one
failed.

| Layer | Contracts | Status |
|---|---|---|
| **MTDR contract validation** | the seven public machine contracts | normative; frozen for the duration |
| **Benchmark protocol validation** | `source-selection.schema.json`, `capture.schema.json`, the run pins, `classification.schema.json`, the comparator's own requirements | non-normative; versioned by `protocol_version` |

A capture that fails **MTDR** validation produced a non-conformant MTDR artefact. That is a **finding
about the runtime** and a valid experimental outcome; the arm stays in the comparison so the
divergence can be located. A capture that fails **benchmark** validation failed to *report* properly
and is a **rejected run**; there is nothing to compare, and it says nothing about that runtime's
conformance.

The two are never collapsed into "failed". They appear under separate headings, the words *rejected*
and *failed* are not used interchangeably anywhere in the output, and the matrix states when an arm is
absent **through rejection rather than through failure**. Collapsing them would let a harness defect
read as a conformance failure, or worse, the reverse.

**VR-4 consumes and tests MTDR. It does not quietly expand MTDR's normative contract.**
`source-selection.schema.json` does not migrate into the normative schema tree after VR-4, however
useful it proves. Only a TDR admits a concept into MTDR, argued on its own merits — not a promotion
earned by a benchmark finding it handy.

## The pin

Every arm is mechanically identical in everything except runtime. `run.yaml` and the capture's `run`
block record:

```
mtdr_commit · mtdr_tag · corpus_id · corpus_version · corpus_inventory_digest
protocol_version · protocol_commit · adapter_version
runtime · runtime_version · model · model_version
environment (expanded) · environment_digest
capture_schema_version · timestamp · task_digest
```

`task_digest` is the sha256 of `task.md`, byte-identical for every arm:

```
74ee271ab268bc028ac3e6040410ba8d6b6a555b993bc8b178720060c02cad90
```

An arm whose digest differs did not run the same experiment.

### The environment is pinned, not just the runtime

"Claude version X + model Y" does not prove Claude saw the same *effective* environment as Codex. The
same canonical `SKILL.md` is reachable through five different discovery paths, so runtime identity and
effective instruction set are separate facts.

The environments are inherently not identical, and the aim is **not to make them identical — it is to
make their differences observable.** Each run records `instruction_files` (with digests),
`skill_discovery_roots`, `tools_enabled`, `runtime_settings`, `execution_mode`, `network_access` and
`tool_access`, and an `environment_digest` over them.

`network_access: false` is the expected state for every Brackwell arm: the corpus is closed and
complete, so an arm that reached the network consulted something outside `available_sources`, and that
fact appears in the capture rather than being inferred from a suspicious result.

**An arm whose `environment_digest` differs from its own repeat run has not repeated anything**, and
the comparator reports that before it reports any boundary divergence.

#### The digest has a published normalisation rule

Two semantically identical environments must not hash differently because of path ordering, a
timestamp or incidental config. Equally, an unbounded settings blob makes the digest differ for
reasons nobody can interpret. Both failures destroy the comparison the digest exists to support, in
opposite directions.

[`environment-keys.yaml`](environment-keys.yaml) is the rule, and `compare/validate.py` implements it
and nothing else:

```
normalise   lists sorted and deduplicated by canonical key
            paths reduced to their position under the corpus or MTDR checkout root
            runtime_settings reduced to the published key allowlist
            sha256 over JSON with sorted keys and no insignificant whitespace
include     instruction_files (path + sha256) · skill_discovery_roots (root + surface)
            tools_enabled · tool_access · execution_mode · network_access
            runtime_settings — only the six keys that can change what an arm reconstructs
exclude     absolute paths outside corpus and checkout · home directories · usernames
            hostnames, container ids, pids · wall-clock, timezone, locale
            terminal size · editor, shell, OS version · any unlisted setting key
```

The exclusions are **named rather than merely omitted**, for the same reason `excluded_sources`
carries reasons: a reader must be able to tell a deliberate exclusion from an oversight. Adding a key
to the settings allowlist is a `protocol_version` increment, because it changes every digest computed
after it.

## Repeatability and reproducibility are different questions

| | Holds constant | Varies | Measures |
|---|---|---|---|
| **Repeatability** | runtime, pin, evidence | nothing | how stable one runtime's reconstruction is |
| **Reproducibility** | pin, evidence | runtime | how equivalent reconstruction is across runtimes |

Repeatability is a **measured variable, not a sanity check**. Without it, a cross-runtime divergence is
indistinguishable from ordinary stochastic variance inside either runtime, and the experiment would
rest on an assumption it never tested. **Every arm runs at least twice.**

### No variance metric, because there is nothing to measure it with

The comparator is deliberately **categorical and boundary-based**, not a similarity score. "Smaller
than a runtime's own repeat variance" has no defined meaning here, and inventing a distance measure
purely to make that sentence true would put an unjustified number at the centre of the result. At
n=2 the honest claim is that repeatability is being **characterised**, not that a variance
distribution is being estimated.

The report is therefore a **divergence matrix per boundary** — categorical in, categorical out —
with **every pairing in its own column**. A single aggregate cross-runtime column hides the case where
two arms agree and one differs, which is the asymmetry most worth knowing:

| Boundary | C1↔C2 | X1↔X2 | P1↔P2 | C↔X | C↔P | X↔P |
|---|---|---|---|---|---|---|
| source selection | stable | stable | stable | none | none | none |
| fragment | differs | stable | stable | differs | differs | none |
| contribution | stable | stable | stable | differs | differs | none |

Row 3 names Claude as the outlier at `contribution` — runtime-specific, not shared, not stochastic.
Row 2 says the opposite: Claude's own repeats already differ there, so the cross-runtime differences
at that boundary are not a finding about runtimes. Neither reading needed a distance metric.

Each pairwise finding takes one label, assigned **mechanically from that matrix**:

| Label | Condition |
|---|---|
| `cross-runtime-only` | **both** arms' repeat pairs are demonstrably stable at this boundary |
| `also-observed-within-runtime` | the within-runtime difference is demonstrably **the same difference**, not merely some difference at the same boundary |
| `indeterminate-at-current-sample` | **the default** — everything else |

`indeterminate-at-current-sample` is the **default, not the fallback**, and a first-class outcome
rather than a hedge — the same discipline as `indeterminate` in the validation result. With two
repeats, over-classifying is the standing risk. Forcing a finding into `cross-runtime-only` when the
sample cannot support it is the benchmark's version of manufacturing standing.

### The outlier is named; the majority is never promoted

Where one arm stands alone and the others agree, that arm is **named**, because asymmetry is
diagnostic. It is not a verdict. **Agreement between runtimes is not evidence about the
organisation**, and the rule is applied mechanically, not merely asserted: there is no code path in
which the count of agreeing arms affects a classification, a label, or which side of a divergence is
rendered first. Two arms converging on an unsupported reading does not make the third one wrong.

## The comparison, and the rule that governs it

**It must never normalise away substantive divergence.** `canonicalisations.yaml` is an explicit
allowlist, each entry carrying its reason. The comparator applies *only* what that file permits, and
`compare/falsify.py` asserts it: a canonicalisation cannot be added silently, in code, to make two arms
agree.

The `never` list in that file is binding. It includes eligibility disagreement, a collapsed bounded
date, and a declared gap collapsed with an unaccounted-for value.

## Classification

Every divergence is classified into one of three, and **only the first justifies changing anything**:

| Class | Meaning | Response |
|---|---|---|
| `harness-defect` | one arm was not given materially equivalent inputs or capture requirements | fix, re-run **all** arms |
| `runtime-divergence` | the same protocol produces different reconstruction behaviour | record; this is the finding |
| `expected-ambiguity` | the source material admits more than one defensible reading | record as such |

**Agreement between runtimes is not evidence about the organisation.** Two runtimes converging on an
unsupported interpretation does not make it expected; three converging does not make it true. Every
classification therefore carries `basis` and `evidence`, and `basis` must point at the known-answer
fixture or at the source material — **never at the number of arms that agreed**. An
`expected-ambiguity` whose basis is "all three did it" is a `runtime-divergence` nobody wanted to write
down. The comparator rejects a basis that appeals to agreement.

## Calibration

The public calibration corpus is Brackwell, the **current known-answer calibration case** — a
published fixture already states what a good reconstruction must and must not do. Nothing makes it
uniquely privileged, and several calibration corpora exercising different failure modes would be
better than one; the harness takes the corpus as a parameter for exactly that reason.

**Calibration does not mean identical outputs.** It means every arm:

1. respects the same boundaries — nobody skips a stage or fuses two;
2. preserves the same uncertainty;
3. commits none of the known-answer fixture's forbidden moves.

**A shared gap is a correct answer. Convergence on a value where the fixture requires a gap is a
*worse* result than divergence.**

## Harness disciplines

The Claude arm is executed by the same environment that authored this harness. **The Claude capture is
therefore the one to distrust most, and a divergence where Claude is the odd arm out is *more*
interesting, not less.** Two disciplines follow:

1. A harness change is permitted **only** where it affects every arm identically.
2. Any harness change **re-runs every arm**. There is no partial re-run.

## A defect in this protocol increments it; the freeze is never overwritten

If a defect is found **after** execution, the frozen protocol is **not edited**. `protocol_version`
increments, a new protocol is pre-registered at a new commit, and **every arm re-runs under the new
pin**. There is no partial re-run.

**The earlier runs stay valid.** They are evidence of what the defective protocol produced, which is
itself a result — and discarding them would leave no record that the defect existed. This is
supersession rather than correction, the same discipline this standard applies to its own records: a
decision is superseded, never edited away.

The comparator enforces the mechanism rather than trusting it. `freeze_drift()` compares every
protocol file against the digests in `FREEZE.json` and **refuses to compare at all** if one has
changed. The remedy for that refusal is to increment and re-register, never to restore the file.

*This protocol is at 1.1.2 because that rule has already been applied three times, every one of them
before any arm ran: 1.0.0 was pre-registered; 1.1.0 added the canonical environment-digest rule and
the comparator pin; 1.1.1 and 1.1.2 corrected wording that had drifted from what the freeze actually
said. Rather than edit a freeze, each was incremented and re-registered — and because nothing had
executed, nothing needed re-running.*

## The comparator is pinned too

The protocol pin does not close one gap: a later run could use the same protocol and subtly different
comparison code, and no other pin would show it. So `comparator_commit` joins the run block, and every
run records the comparator it actually used.

`FREEZE.json` carries the comparator commit at the moment of the freeze, and that value is a
**starting** pin rather than a final one — it is false the next time the harness changes. **The
binding comparator pin for VR-4B is the comparator commit at the end of VR-4A**, recorded then, so the
private run cannot use the same protocol with subtly different comparison code.

## Publish the evidence, not only the report

Results publish **together**: the raw captures, the comparator output, every `classification` with its
`basis` and `evidence`, and the exact environment metadata. A polished report must never be the only
visible evidence — that is the same failure mode as an aggregate verdict, one step further out.

## What this protocol may not do

- It may not modify MTDR. If a runtime struggles with MTDR, that is initially evidence about the
  runtime, the instructions or the proposition — **not permission to modify the standard until it
  passes.**
- It may not invent a metric to make a claim expressible. The comparator stays categorical.
- It may not admit a benchmark contract into the normative schema tree.
- It may not carry real material or any client name into a public repository.
