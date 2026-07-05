# Contributing

Contributions are welcome — including, and especially, disagreement.

## The mechanic

This repository's own design decisions live in [`/decisions`](decisions/) as TDRs. **Accepted decisions are never edited or deleted. They are superseded.**

To challenge a decision:

1. Copy the appropriate template from [`/templates`](templates/).
2. Write a superseding TDR: set `supersedes:` to the record you are challenging, and make the **Context** section state *what is now known that was not known at the time* of the original decision.
3. Open a pull request containing the new record. Discussion happens on the PR — in the standard's own format.
4. If accepted, the new record's status becomes `accepted`, the original's becomes `superseded`, and both remain in the folder permanently. The reasoning trail survives its own corrections.

Status transitions (`proposed → accepted`, `accepted → superseded`) and `confirmed_by_outcome` updates are made in place; they are lifecycle facts. Changes to decision *content* always require supersession.

## Spec and template changes

Improvements to `spec.md`, the templates, or the skills follow the same rule when they change meaning: a superseding TDR in `/decisions` accompanies the change. Typo and clarity fixes need no ceremony — proportionality applies to contributions too.

## Worked examples

Additional worked examples are welcome. They must be fictional and clearly marked as such: no real organisations, clients, employers or identifiable programmes.

## Scope boundary

This repository defines a format and its practice. Implementations — tooling, graph substrates, extraction pipelines, integrations — belong in their own projects, whoever builds them. Proposals that would bind the standard to particular software will be declined with thanks, per [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).
