# The record admission test

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

How something new gets into this standard — a new organisational language, or a new artefact inside
an existing one. Decided in [TDR-0021](../decisions/TDR-0021-record-package-architecture.md).

## Not to be confused with two neighbours

This repository already carries two other admissions, and the three never overlap:

- **The language admission test** ([TDR-0017](../decisions/TDR-0017-language-admission-test.md))
  asks whether a *specification* qualifies as a language in the formal sense — abstract syntax,
  evaluation semantics, seven criteria. A question about specifications.
- **Candidate-record admissibility** ([`candidacy-and-ratification.md`](candidacy-and-ratification.md))
  asks whether the *evidence* supports proposing one candidate record to a human. A question about
  individual candidates.
- **This test** asks whether a proposed *record family* deserves to exist in the standard at all.
  A question about the standard's own shape.

## The classification test

Four questions, asked in order, of any proposed record family or artefact type:

1. **Does it express a distinct class of organisational meaning?**
2. **Can it exist independently of another record family?**
3. **Can its package be extracted and remain semantically complete?**
4. **Does it have an independent lifecycle** — rather than merely assuring, qualifying or projecting
   another record?

- Passes all four → a **candidate language**, eligible for its own package.
- Passes 1 but fails any of 2–4 → a **dependent artefact**, living inside the language it depends on.
  The Decision Assurance Case is the worked precedent: its own spec and schema, but `tdr_id`
  mandatory, lifecycle coupled, purpose assurance-over — it fails 2–4 and lives in
  [`records/decision/`](../records/decision/).
- Fails 1 → not a record at all. The interchange structures fail here **by design**: fragments,
  contributions and assemblies carry interpretation, not organisational meaning, and a proposal to
  govern or persist them as records is answered by this test.

## Candidacy is not admission

A package may exist before its language is admitted — architectural reservation is cheap and keeps
the tree honest about intent. But **candidate packages contain metadata and scope only**: identity,
semantic scope, `status: candidate`, and a statement that this test has not been passed. No normative
specification, schema, template, examples, validation rules or skills until admission succeeds.

A directory confers no maturity. A package's actual maturity is measured by which
[conformance layers](conformance.md) it carries, not by existing.

## What admission requires

Admission is a decision, recorded as a TDR in [`decisions/`](../decisions/), carrying:

- the four answers, with the evidence for each — not assertions;
- the failing query: something an adopter needs to know that no existing record family can answer;
- the semantic scope, bounded against every existing language (what it does **not** cover);
- the accountable owner of the admission.

The admission decision then unlocks the package: specification, schema, template, examples,
validation, skills — arriving through the repository's normal release discipline, each layer named
in the changelog as it lands.

## Demotion and refusal

A candidate that fails admission keeps its record: the failed TDR is the useful artefact, because it
states what was looked for and not found — the same discipline as a written-off Value Record. The
package directory is then removed or kept per that decision; what never happens is a candidate
accumulating normative artefacts while the question stays open.
