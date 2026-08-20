# VR-4 reconstruction protocol

**Version 1.0.0 · non-normative · pre-registered**

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

A capture that fails **MTDR** validation produced a non-conformant MTDR artefact — a finding about the
runtime. A capture that fails **benchmark** validation failed to *report* properly — a rejected run.
Collapsing the two would let a harness defect read as a conformance failure, or worse, the reverse.

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

The report is therefore a **divergence matrix per boundary** — categorical in, categorical out:

| Boundary | Claude C1↔C2 | Codex X1↔X2 | Copilot P1↔P2 | Cross-runtime |
|---|---|---|---|---|
| source selection | stable | stable | stable | none |
| fragment | differs | stable | differs | differs |
| … | | | | |

Each cross-runtime finding takes one label, assigned **mechanically from that matrix**:

| Label | Condition |
|---|---|
| `cross-runtime-only` | absent from both relevant runtimes' repeat pairs |
| `also-observed-within-runtime` | the same divergence class occurs between repeat executions |
| `indeterminate-at-current-sample` | two runs cannot separate a runtime effect from stochastic behaviour |

`indeterminate-at-current-sample` is a first-class outcome, not a hedge — the same discipline as
`indeterminate` in the validation result. Forcing a finding into `cross-runtime-only` when the sample
cannot support it is the benchmark's version of manufacturing standing.

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

## What this protocol may not do

- It may not modify MTDR. If a runtime struggles with MTDR, that is initially evidence about the
  runtime, the instructions or the proposition — **not permission to modify the standard until it
  passes.**
- It may not invent a metric to make a claim expressible. The comparator stays categorical.
- It may not admit a benchmark contract into the normative schema tree.
- It may not carry real material or any client name into a public repository.
