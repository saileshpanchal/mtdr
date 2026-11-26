# MTDR — Markdown Transformation Decision Record

Record the judgement behind a significant decision while the people who made it are still there to
ask: what was known at the time, who was accountable, how confident they were, what they rejected,
and what the decision closed off.

**TDR**, the Transformation Decision Record, is the standard. **MTDR** is its markdown reference
format, as MADR is to ADR. A TDR is one markdown file with a short YAML header.

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

The loop has you draft at a proportional template. These are the three, each with a record to copy
from:

| The decision is | Template | A record to copy from |
|---|---|---|
| Irreversible, or costly to reverse | [Full](records/decision/templates/tdr-full.md) | [Retaining a servicing channel](records/decision/examples/example-full-consumer-duty-channel-decision.md) (fictional) |
| Significant, but revisable at tolerable cost | [Minimal](records/decision/templates/tdr-minimal.md) | [Migrating a data platform](records/decision/examples/example-minimal-data-platform-migration.md) (fictional) |
| Reversible and low-stakes | [Bare](records/decision/templates/tdr-bare.md), or no record at all | [TDR-0004](decisions/TDR-0004-markdown-yaml-serialisation.md), one of this standard's own |

The [TDR specification](records/decision/specification/tdr.md) is the authority; §4.1 defines the
fields in the templates, all but `conforms_to`, which [record identity](specification/record-identity.md)
defines.

### Two routes to the same record

The decision package names two: an **authoring path**, for a person who holds the reasoning, and an
**interpretation path**, for reconstruction from material. [Its README](records/decision/README.md#skills)
lists the skills on each. [Using MTDR with your framework](practice/using-mtdr-with-your-framework.md)
walks through reconstruction across a body of existing documents.

## Why

Organisations record the outcomes of decisions, rarely the judgement behind them. When the people who held the context move on, the organisation re-makes decided questions at full cost — and when a board, auditor or supervisor asks a named individual to demonstrate the judgement that was exercised, fragments in a shared drive do not answer the question.

A TDR preserves the judgement at the moment it is exercised: context as it stood, a named accountable owner, stated confidence, evidence assessed across seven dimensions, alternatives rejected, options foreclosed, and lineage connecting each decision to those before and after it.

## Beyond the decision record

The TDR has two sibling records:

- **Value Record (VR)** — the governed memory of an Operational Value Commitment, holding the
  commitment and its settlement as one record. See [the VR specification](records/value/specification/vr.md).
- **Decision Assurance Case (DAC)** — a TDR preserves the judgement, it does not prove the
  consequences are acceptable; the DAC records the reasoning that challenges them, before execution.
  [The DAC specification](records/decision/specification/dac.md) sets out when one is required (§4).

## What this release contains

| Capability | Record | Standing |
|---|---|---|
| Decision | TDR, with the DAC | Normative |
| Value | VR | Normative |
| Decision recovery | Retrospective candidates, the recovery skills, the installer and the folder validator | **Proposed** under TDR-0048, TDR-0049, TDR-0050 and DAC-0048. It is published only once those records are ratified |
| Inheritance | OIR | Experimental: published for review, not part of the standard ([TDR-0047](decisions/TDR-0047-experimental-packages.md)) |
| Authority | OAR | Candidate: scope only, not yet admitted |
| Evidence | OER | Candidate: scope only, not yet admitted |

This release does not claim external validation, proven adoption, ease of installation or usability.
Those claims wait for independent practitioners to test it ([DAC-0045](decisions/DAC-0045-external-validation-follows-publication.md)).

## Known limitations

- A proposed TDR that honestly leaves the owner's confidence unstated fails the TDR schema: the field
  has no value for "not yet stated" ([#14](https://github.com/saileshpanchal/mtdr/issues/14)).
- The quick start teaches writing a record at the time of a decision. It does not yet route someone
  holding minutes of a past decision to historical recovery, and the installer packages the recovery
  skills, not the authoring ones ([#15](https://github.com/saileshpanchal/mtdr/issues/15)).
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

The repository is organised as **record packages** — one per organisational language — over a
record-neutral substrate ([TDR-0021](decisions/TDR-0021-record-package-architecture.md)):

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

Every significant decision about the TDR's design is recorded in [`/decisions`](decisions/) using the format itself — including the proportionality ladder, demonstrated rather than asserted. Decisions there are never edited or deleted, only superseded. If you disagree with the reasoning, [propose a superseding TDR](CONTRIBUTING.md): what is now known that was not known at the time?

## Relationship to existing standards

TDRs extend the [ADR](https://adr.github.io/) lineage with gratitude — MADR generalised scope; the TDR adds accountability semantics. TDRs work alongside ADRs, MADR, SAP LeanIX, Confluence and GRC platforms; they replace none of them. See spec §2 and [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

## Acknowledgement

This standard emerged from the *Decision Debt* article series. Its development was supported by Digital Transformation Advisory. The standard itself is neutral, open, and belongs to whoever finds it useful.

## Author

Sailesh Panchal · MIT License
