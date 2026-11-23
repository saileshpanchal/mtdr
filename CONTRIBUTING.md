# Contributing

Contributions are welcome — including, and especially, disagreement. Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).

## The mechanic

This repository's own design decisions live in [`/decisions`](decisions/) as TDRs. **Accepted decisions are never edited or deleted. They are superseded.**

To challenge a decision:

1. Copy the appropriate template from [`records/decision/templates/`](records/decision/templates/).
2. Write a superseding TDR: set `supersedes:` to the record you are challenging, and make the **Context** section state *what is now known that was not known at the time* of the original decision.
3. Open a pull request containing the new record. Discussion happens on the PR — in the standard's own format.
4. If accepted, the new record's status becomes `accepted`, the original's becomes `superseded`, and both remain in the folder permanently. The reasoning trail survives its own corrections.

Status transitions (`proposed → accepted`, `accepted → superseded`) and `confirmed_by_outcome` updates are made in place; they are lifecycle facts. Changes to decision *content* always require supersession.

## Editorial or normative?

Every other change follows one rule: **a change that alters meaning is accompanied by a superseding TDR
in [`decisions/`](decisions/); a change that does not needs no ceremony.** Proportionality applies to
contributions too.

Meaning lives in the specifications ([`specification/`](specification/) and each package's
`specification/` under [`records/`](records/)), the schemas, the templates, the skills, and each
package's `validation/` rules and fixtures. To tell which kind of change you have, ask whether a
record, a validation result or a skill's output could come out differently because of it. If it
could, the change is normative.

| Normative: bring a TDR | Editorial: a pull request is enough |
|---|---|
| Adding, removing or renaming a record field, or changing whether it is required | Typos, grammar, formatting and broken links |
| Changing a schema, an allowed value, a status or a lifecycle transition | Rewording for clarity that leaves every requirement as it was |
| Changing what a specification requires for conformance or validation | Navigation: READMEs, indexes and pointers to where something lives |
| Changing what a skill does, what it refuses, or what it hands to the next stage | Bringing a document level with a decision already accepted, citing that decision |

If you cannot tell which it is, say so in the pull request rather than guessing.

Three kinds of file are not edited in place, whichever kind of change it is:

- **Accepted records in [`decisions/`](decisions/).** They are superseded, as above.
- **Redirect stubs** (files headed `# Moved`, and the directories that hold only those). They exist
  so that old links keep resolving, and say only where something went. New material goes to the
  location the stub names.
- **Generated bundles** under [`skills/packaging/`](skills/packaging/): `canonical/` and the
  per-runtime directories. Edit the skill or the package manifest and regenerate, as that directory's
  README describes.

## Worked examples

Additional worked examples are welcome. They must be fictional and clearly marked as such: no real organisations, clients, employers or identifiable programmes.

## Scope boundary

This repository defines a format and its practice. Implementations — tooling, graph substrates, extraction pipelines, integrations — belong in their own projects, whoever builds them. Proposals that would bind the standard to particular software will be declined with thanks, per [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

The dividing line is direction, not subject matter, per [TDR-0018](decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md). **The standard ends at the artefact boundary.** A vendor-neutral skill that reads material and yields a conformant record *produces* the standard's own output, and belongs here. Storage, indexing, retrieval, orchestration, model selection, graph assembly and persistence *consume* records, and do not. Skills contributed here must make no assumption about storage, runtime, graph representation, orchestration or subsequent use.
