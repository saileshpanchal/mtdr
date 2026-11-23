# `mtdr_validation` — reference implementation

**Non-normative.** This is one implementation of the validation-result contract. It is not the
contract.

A conforming independent implementation is governed by
[`specification/validation-result.md`](../specification/validation-result.md) and
[`schemas/validation-result.schema.json`](../schemas/validation-result.schema.json) — **never by
behavioural equivalence with this code**. If this module and those documents disagree, this module is
wrong. Nothing here may be cited as a normative requirement, and no conformance claim may be
expressed as "matches `mtdr_validation`".

The distinction is the one JSON Schema itself makes between a validation vocabulary and any
particular validator's console output, and it matters directly: the recovery experiment compares
independent runtimes, and a runtime is not being measured against this Python.

## What it does

Builds validation results, serialises them to JSON, validates them against the published schema, and
renders a summary that exposes every dimension.

```python
from mtdr_validation import ValidationResult, Dim, PASS, NOT_APPLICABLE

r = ValidationResult(
    subject_type="record", subject_id="TDR-0034",
    subject_ref="decisions/TDR-0034-public-allocation-authority.md",
    spec_id="records/decision/specification/tdr.md", spec_version="1.14.0",
    assessed_state="accepted",
)
r.report(Dim.STRUCTURAL, PASS)
r.report(Dim.SEMANTIC, PASS)
r.report(Dim.RELATIONAL, PASS)
r.report(Dim.TRANSITION, NOT_APPLICABLE, reasons=[("no-transition-requested", "...")])

errors = r.validate()      # [] when the result satisfies the published schema
print(r.summary())
```

## What it deliberately will not do

`summary()` renders four lines and no fifth. There is no `is_valid()`, no `ok`, no exit-code helper
and no truthiness on the result object, because DAC-0033 constraint 8 forbids a normative aggregate
green result — and a convenience property that could be read alone would be read alone.

`report()` will not accept an illegal result for a dimension, and `validate()` re-checks against the
schema rather than trusting the builder. The builder is convenience; the schema is the contract.

Results carry no standing, no repair and no inferred value. `validate()` never modifies the object
assessed, and the caller's inputs are never mutated.

## Validating a folder of recovery output

An adopter who has run a recovery — in any engine — checks what it produced with one command, from a
checkout of this repository:

```bash
uv run python -m mtdr_validation <folder> [--sources <evidence-folder>]
```

It finds every historical candidate and review event under `<folder>`, and writes to
`<folder>/validation/` (or `--out`) one validation result per artefact — each checked against the
published schema before it is written — and a `summary.md` a person can read:

| Dimension | What it reports for a candidate |
|---|---|
| structural | the candidate schema, and everything the candidate refers to it carries (`historical-candidate.md` integrity rules 1–5, 7, 8) |
| semantic | the recovery roles the object's package declares (rule 6) — `indeterminate` where the package declares none |
| relational | whether every review event naming the candidate was recorded against this exact content (its digest); with `--sources`, whether every fragment says what its source says, where it says it (below); and whether any Markdown rendering naming the candidate is a candidate view (`status: candidate`, `standing: none`, `retrospective: true`, `candidate_id`), never a record's frontmatter (`draft-tdr` §7) |
| transition-eligibility | always `not-applicable`: a candidate's standing is `none`, and attestation is a person's act |

The summary also gives the computed contemporaneity of every context contribution, and lists what it
did not assess. **There is no overall result**, and the exit status is operational — 0 when the folder
was assessed, 2 when it could not be — never a conformance verdict. `tests/verify.py` calls the same
functions (`mtdr_validation.recovery`) and checks that this command agrees with every published
candidate fixture.

### Source fidelity (`--sources`)

A fragment is verbatim and immutable, its locator resolves, and its content is exactly the span
([`source-fragment.md`](../specification/source-fragment.md)). A check that never opens the source
cannot test any of that: a hash that re-computes beside cleaned-up content still passes. Given the
folder of original material, the validator re-reads each fragment's source (`fidelity.py`):

- the source hashes to `source_hash`, or **fail**;
- the content occurs in the source as written, or **fail** (reflowed whitespace is named as such);
- the locator selects exactly the content: `line-range` and `char-offset` are applied, and a span that
  is wider, narrower or elsewhere is a **fail**.

What it cannot check is **indeterminate**, never a pass: a source not in the folder supplied, a hash
algorithm other than SHA-256, a locator kind it does not apply. The only normalisation is character
encoding (UTF-8, line endings). Without `--sources` the summary says that fidelity was not checked.
For an acceptance run, the harness should run this command after the engine has finished, from a
checkout the engine cannot read. A validator the engine can read becomes the engine's target.

## Requirements

`jsonschema` (with `referencing`, which it installs) for results; `pyyaml` as well for recovery output,
to read each package's declared vocabulary. Nothing else — no MTDR application, register or service.
