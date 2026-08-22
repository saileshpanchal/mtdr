# Governance

**Licence:** MIT · **Maintainer:** Sailesh Panchal

This repository is an open organisational-records standards and skills repository
([TDR-0020](decisions/TDR-0020-open-organisational-record-repository-boundary.md)). This file states
how it governs itself. It is short because the mechanism is the repository's own subject matter.

## The standard uses itself

**Every consequential decision about this standard — its semantics, architecture, governance or
evolution — is recorded as a TDR in [`decisions/`](decisions/).** The repository does not introduce a
parallel decision mechanism for itself: architecture decisions are decisions, and the register at
`decisions/README.md` is the single, navigable account of why the repository is the way it is.

Decisions are never edited or deleted. They are **superseded** — a new record with `supersedes:` set,
stating what is now known that was not known at the time. To challenge any decision here, open a pull
request proposing a superseding TDR. Discussion happens in the standard's own format.

## The structural rules

Each is decided in a record; this list is the index, not the authority.

| Rule | Decided in |
|---|---|
| The repository has no knowledge of its consumers; the standard ends at the artefact boundary | [TDR-0020](decisions/TDR-0020-open-organisational-record-repository-boundary.md), [TDR-0018](decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md) |
| Packages follow organisational languages; dependent artefacts live with the language they serve; packages depend downward on the substrate, never sideways | [TDR-0021](decisions/TDR-0021-record-package-architecture.md) |
| Candidate packages hold metadata and scope only until their language passes admission | [TDR-0021](decisions/TDR-0021-record-package-architecture.md) |
| Records are reconstructed from fragments; documents are containers; interchange structures are not records | [TDR-0022](decisions/TDR-0022-fragment-contribution-interchange-architecture.md) |
| Skills live with record semantics; shared skills must be demonstrably record-neutral | [TDR-0023](decisions/TDR-0023-portable-skill-architecture.md) |
| Packagings are distribution adapters, never normative architecture | [TDR-0024](decisions/TDR-0024-packaging-independence.md) |
| Conformance is layered — schema, examples, counter-examples, fixtures, semantic equivalence | [TDR-0025](decisions/TDR-0025-conformance-architecture.md) |
| The skill proposes; the organisation ratifies | [TDR-0018](decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md) |
| Removal or weakening of the accountability core is a different standard, not a new version | [`spec` §9](records/decision/specification/tdr.md) |
| Governance reconstruction outputs are projections over existing records, never a sixth record family — **proposed** | [TDR-0034](decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md) |

## Roles

- **Maintainer** — accepts records into the register, cuts releases, and is the named accountable
  owner where no other individual is. Canonical promotion is human-gated; no tool ratifies anything.
- **Contributors** — anyone, per [`CONTRIBUTING.md`](CONTRIBUTING.md). Proposals that would bind the
  standard to particular software are declined with thanks (TDR-0002); proposals that change meaning
  arrive with their superseding TDR.

## Releases

Semantic versioning, recorded in [`CHANGELOG.md`](CHANGELOG.md). The repository versions as a whole;
record specifications may version independently where a decision says so (the Value Record, per
[TDR-0019](decisions/TDR-0019-value-record-v2-operational-value-commitment.md)). Every release states
its compatibility claim honestly — "every prior record still validates" appears only when verified,
and a breaking change is named as one.
