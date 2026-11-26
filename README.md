# MTDR — Markdown Transformation Decision Record

Record the judgement behind a significant decision while the people who made it are still there to
ask: what was known at the time, who was accountable, how confident they were, what they rejected,
and what the decision closed off.

**TDR**, the Transformation Decision Record, is the standard. **MTDR** is its markdown reference
format, as MADR (Markdown Architectural Decision Records) is to the architecture decision record
(ADR). A TDR is one markdown file with a short YAML header.

MIT licensed. Tool-neutral. Regulator-neutral. Works alongside what you already run.

## What you can do with it

- **Decide what not to record.** If reversing a decision would cost less than writing the record, do
  not write the record.
- **Keep the reasoning when the judgement changes.** An accepted record is never edited; a changed
  judgement is a new record that supersedes it.
- **Let an assistant draft while a named person decides.** The skills are written for humans and
  structured so AI assistants can apply them directly.

## Write your first TDR

**Follow the [quick start](practice/quickstart.md).** It is the procedure for a first record: three
rules that never bend, and the loop you follow for each decision.

The loop has you draft at a template sized to the decision: the more it would cost to reverse, the
fuller the record. There are three, each with a record to copy from:

| The decision is | Template | A record to copy from |
|---|---|---|
| Irreversible, or costly to reverse | [Full](records/decision/templates/tdr-full.md) | [Retaining a servicing channel](records/decision/examples/example-full-consumer-duty-channel-decision.md) (fictional) |
| Significant, but revisable at tolerable cost | [Minimal](records/decision/templates/tdr-minimal.md) | [Migrating a data platform](records/decision/examples/example-minimal-data-platform-migration.md) (fictional) |
| Reversible and low-stakes | [Bare](records/decision/templates/tdr-bare.md), or no record at all | [TDR-0004](decisions/TDR-0004-markdown-yaml-serialisation.md), one of this standard's own |

The examples are accepted records. If you start from one, change its `id`, `title`, `decision_date`
and `accountable_owner`, set `status: proposed` until the named owner confirms it, and keep
`conforms_to` as it is.

The [TDR specification](records/decision/specification/tdr.md) is the authority; §4.1 defines the
fields in the templates, all but `conforms_to`, which [record identity](specification/record-identity.md)
defines.

### Two routes to the same record

A TDR can be written for a decision as it is made, or recovered for a decision made in the past. The
decision package names the two routes, and they follow different rules:

| | Authoring path | Interpretation path |
|---|---|---|
| Use it when | You are recording a decision at the time it is made | A decision was taken in the past and never recorded at the time |
| It works from | "A human who holds the reasoning" | "Reconstruction from material": the documents that survive the decision |
| Its rules | The quick start's three rules that never bend | One rule: "Recover what can be evidenced. Preserve what cannot. Never turn a contemporary interpretation into historical authority" |
| It produces | A TDR that its named owner confirms | "A retrospective candidate with no standing" |
| Status in this release | Part of the normative decision package | Proposed under TDR-0048 and TDR-0049 |
| Start at | The [quick start](practice/quickstart.md) | The [`recover-decision-records`](records/decision/skills/recover-decision-records/) skill and [historical recovery](specification/historical-recovery.md) |

Three terms recur throughout the repository. A **candidate** is a proposal: unratified, with no
organisational standing. **Ratification** is a named individual accepting accountability for a
record's content, and no skill or tool performs it ([candidacy and
ratification](specification/candidacy-and-ratification.md)). **Standing** is what ratification
confers ([TDR-0027](decisions/TDR-0027-human-ratification-confers-standing.md)), so a candidate has
none. A *retrospective* candidate's standing is always none: attesting that the organisation decided
something in the past says nothing about whether that decision governs today.

The quick start does not yet route someone holding minutes of a past decision to historical recovery
(see [Known limitations](#known-limitations)). [The decision package's
README](records/decision/README.md#skills) lists the skills on each route, and [Using MTDR with your
framework](practice/using-mtdr-with-your-framework.md) walks through reconstruction across a body of
existing documents.

### Installing, invoking and validating

A person can read a skill and follow it without any tool. To have an AI assistant apply the skills,
install one record type's package into your project and verify it where it sits. Run both commands
from the root of a clone of this repository, with [uv](https://docs.astral.sh/uv/) installed; uv
creates a `.venv` there on the first run.

```
uv run python -m mtdr_packaging.profiles install <record-type> --runtime <runtime> --project <your project>
uv run python -m mtdr_packaging.profiles verify <installed package folder>
```

`<runtime>` is `claude-code` or `hermes` (Hermes Agent). `install` prints the folder it created, which
is what `verify` takes: `<your project>/.mtdr/plugins/mtdr-<record-type>` for Claude Code, and
`<your project>/.agents/skills/mtdr-<record-type>` for Hermes.
[`skills/packaging/`](skills/packaging/) explains both commands and says how each runtime discovers and
invokes a skill.

Each package is built for recovering decisions from existing documents, the interpretation path
above. It leaves out the skill that writes a new record and the governance review. To have an
assistant write a new record, point it at
[`problem-framing-and-decision-capture`](records/decision/skills/problem-framing-and-decision-capture/SKILL.md)
in the repository.

Two further commands check two different things:

- `uv run python -m mtdr_validation <folder> [--sources <evidence-folder>]` assesses the output of a
  recovery: the historical candidates in `<folder>` and their review events, which record what a named
  individual did with a candidate. It does not assess a TDR you have authored, and it gives no overall
  result ([`mtdr_validation/`](mtdr_validation/README.md)).
- `uv run tests/verify.py` runs this repository's own suite. Contributors run it before opening a pull
  request ([`tests/`](tests/README.md)).

**No command yet checks a TDR you have written.** Work through the
[`validate-record`](skills/shared/validate-record/SKILL.md) checklist by hand, or have an assistant
apply it. The record's YAML header must also satisfy
[`tdr.schema.json`](records/decision/schema/tdr.schema.json), which any JSON Schema validator can check
once the header is converted to JSON. Run on a folder of TDRs, `mtdr_validation` reports
`0 artefact(s) assessed`: that is not a pass.

The installer and the folder validator belong to decision recovery, which is proposed and not yet
ratified (see [What this release contains](#what-this-release-contains)).

## Why

Organisations record the outcomes of decisions, rarely the judgement behind them. When the people
who held the context move on, the organisation re-makes decided questions at full cost. When a
board, auditor or supervisor asks a named individual to demonstrate the judgement that was
exercised, fragments in a shared drive do not answer the question.

A TDR preserves the judgement at the moment it is exercised: context as it stood, a named accountable owner, stated confidence, evidence assessed across seven dimensions, alternatives rejected, options foreclosed, and lineage connecting each decision to those before and after it.

## Beyond the decision record

The TDR has two sibling records:

- **Value Record (VR)** — the governed memory of an Operational Value Commitment: what the
  organisation committed to pursue or preserve, and how that commitment settled, held as one record.
  See [the VR specification](records/value/specification/vr.md).
- **Decision Assurance Case (DAC)** — a TDR preserves the judgement but does not prove that its
  consequences are acceptable. The DAC records the reasoning that challenges those consequences before
  execution. [The DAC specification](records/decision/specification/dac.md) sets out when one is
  required (§4).

## What this release contains

| Capability | Record | Status |
|---|---|---|
| Decision | TDR, with the DAC | Normative |
| Value | VR | Normative |
| Decision recovery | Retrospective candidates, the recovery skills, the installer and the folder validator | **Proposed** under TDR-0048, TDR-0049, TDR-0050 and DAC-0048. It is published only once those records are ratified |
| Inheritance | OIR, the Operational Inheritance Record | Experimental: published for review, not part of the standard ([TDR-0047](decisions/TDR-0047-experimental-packages.md)) |
| Authority | OAR, the Operational Authority Record | Candidate: scope only, not yet admitted |
| Evidence | OER, the Operational Evidence Record | Candidate: scope only, not yet admitted |

**Normative** means part of the standard. **Proposed** means the records that would govern the capability are not yet ratified. **Experimental** and **candidate** in this table describe packages, not records: an experimental package is published for review and is not part of the standard, and a candidate package holds a statement of scope only and has not passed the [record admission test](specification/record-admission-test.md).

This release does not claim external validation, proven adoption, ease of installation or usability.
Those claims wait for independent practitioners to test it ([DAC-0045](decisions/DAC-0045-external-validation-follows-publication.md)).

## Known limitations

- A proposed TDR that honestly leaves the owner's confidence unstated fails the TDR schema: the field
  has no value for "not yet stated" ([#14](https://github.com/saileshpanchal/mtdr/issues/14)).
- The quick start teaches writing a record at the time of a decision. It does not yet route someone
  holding minutes of a past decision to historical recovery, and the installed `decision` package
  leaves out the skill that writes a new record
  ([#15](https://github.com/saileshpanchal/mtdr/issues/15)).
- No command checks a TDR you have written; the `validate-record` checklist is applied by hand or by
  an assistant (see [Installing, invoking and validating](#installing-invoking-and-validating)).
- Four smaller questions are open: what `status: proposed` means for a decision already approved
  ([#16](https://github.com/saileshpanchal/mtdr/issues/16)); what `confirmed_by_outcome` holds when
  no review was set ([#17](https://github.com/saileshpanchal/mtdr/issues/17)); a manifest dependency
  on `specification/record-identity.md` ([#18](https://github.com/saileshpanchal/mtdr/issues/18));
  and whether an editorial change to a specification changes its version
  ([#19](https://github.com/saileshpanchal/mtdr/issues/19)).
- Copying the skills flat into an agent's skills folder breaks their links. Use the installer, which
  supports Claude Code and Hermes ([`skills/packaging/profiles/`](skills/packaging/profiles/)).
- If a specification's version is raised in a later release, records bound to the earlier version
  would fail the identity check. A fix was held out of this release for a governed decision.
- The tests that shipped with v1.30.0 report 13 failures against this release. All 13 come from the
  experimental package state, which v1.30.0 predates.

## Feedback

If you try MTDR without help from its authors, please tell us what happened:
[open an independent trial report](https://github.com/saileshpanchal/mtdr/issues/new?template=independent-trial-report.md).
Report a defect with the [defect template](https://github.com/saileshpanchal/mtdr/issues/new?template=defect.md),
and challenge a design decision with the [challenge template](https://github.com/saileshpanchal/mtdr/issues/new?template=challenge-a-decision.md).

## What's here

The repository is organised as **record packages**, one per organisational language: one class of
organisational meaning, such as decision or value, with one primary record type. The packages sit on
a shared, record-neutral layer that the repository calls the substrate
([TDR-0021](decisions/TDR-0021-record-package-architecture.md)):

| Path | Contents |
|---|---|
| [`specification/`](specification/) | The substrate: the [umbrella specification](specification/organisational-records.md), the [contribution model](specification/contribution-model.md) (fragments → contributions → candidates), provenance, identity, uncertainty, [candidacy and ratification](specification/candidacy-and-ratification.md), the [record admission test](specification/record-admission-test.md) and [what conformance means](specification/conformance.md), the [validation-result contract](specification/validation-result.md), the [derivation projection](specification/derivation-projection.md), the [obligation chain](specification/obligation-chain.md) and the [standards boundary](specification/standards-boundary.md) |
| [`records/decision/`](records/decision/) | **The decision language** — TDR spec, DAC spec, schemas, templates, examples, fixtures, validation, and its skills (authoring, drafting, assurance) |
| [`records/value/`](records/value/) | **The value language** — VR v2 spec (the Operational Value Commitment), schema, template, example, fixtures, validation, and its skills |
| [`records/`](records/) | The package index, the extraction and dependency rules, two **candidate** packages (authority · evidence) holding scope only, and one **experimental** package (work) published for open review and not part of the standard ([TDR-0047](decisions/TDR-0047-experimental-packages.md)) |
| [`skills/shared/`](skills/shared/) | The record-neutral skills: identify contributions · reconcile fragments · challenge · validate · [show me why](skills/shared/show-me/) |
| [`skills/packaging/`](skills/packaging/) | Distribution adapters — deploying the same files through specific runtimes ([TDR-0024](decisions/TDR-0024-packaging-independence.md)) |
| [`schemas/`](schemas/) | The [validation-result contract](schemas/validation-result.schema.json) and, in [`shared/`](schemas/shared/), the interchange schemas for the contribution model |
| [`mtdr_validation/`](mtdr_validation/) | A **non-normative** reference implementation of the result contract. The contract governs; this code does not |
| [`mtdr_packaging/`](mtdr_packaging/) | A **non-normative** generator that assembles distribution bundles from the manifests. It decides where files go and never what they mean |
| [`tests/`](tests/) | Cross-language fixtures, [validation-result](tests/validation/) and [inspectability](tests/inspectability/) fixtures, the [adoption case](tests/adoption/), deployed-agent probes, the corpus, and the interoperability horizon |
| [`practice/`](practice/) | Practice guides: quick start, **[applying MTDR to your own framework](practice/using-mtdr-with-your-framework.md)**, operating model, administration & assurance |
| [`spikes/`](spikes/) | **Non-normative** experiments whose findings are recorded — currently the [SHACL relational-validity spike](spikes/shacl-relational-validity/) |
| [`decisions/`](decisions/) | **This standard's own design decisions, recorded as TDRs**, and the [identifier allocation register](decisions/ALLOCATION.md) |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) · [`FAQ.md`](FAQ.md) · [`GOVERNANCE.md`](GOVERNANCE.md) · [`CONTRIBUTING.md`](CONTRIBUTING.md) | The layered architecture and where the standard ends · what a TDR is not · how the repository governs itself · how to challenge a decision |

Files at pre-restructure paths (`spec.md`, `templates/`, `shared/`, …) are pointer stubs preserving
old links; the canonical artefacts live in the packages.

## A standard that uses itself

Every significant decision about the TDR's design is recorded in [`/decisions`](decisions/) using
the format itself, so the proportionality ladder is demonstrated there too. Decisions there are
never edited or deleted, only superseded. If you disagree with the reasoning, [propose a superseding
TDR](CONTRIBUTING.md): what is now known that was not known at the time?

## Relationship to existing standards

TDRs extend the [ADR](https://adr.github.io/) lineage with gratitude: MADR generalised scope, and
the TDR adds accountability semantics. TDRs work alongside ADRs, MADR, SAP LeanIX, Confluence and
GRC platforms; they replace none of them. See spec §2 and
[TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

## Acknowledgement

This standard emerged from the *Decision Debt* article series. Its development was supported by Digital Transformation Advisory. The standard itself is neutral, open, and belongs to whoever finds it useful.

## Author

Sailesh Panchal · MIT License
