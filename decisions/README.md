# Design decisions

This standard uses itself.

Every significant decision about the shape of the Transformation Decision Record is recorded here as a TDR. If the format cannot carry the reasoning behind its own design, it has no business asking your organisation to trust it with theirs.

The records also demonstrate the proportionality rule in practice:

| Record | Decision | Template |
|---|---|---|
| [TDR-0001](TDR-0001-publish-as-neutral-open-standard.md) | Publish as a neutral open standard | Full — one-way door |
| [TDR-0002](TDR-0002-differentiate-on-accountability-semantics.md) | Differentiate on accountability semantics, not scope | Full — one-way door |
| [TDR-0003](TDR-0003-ship-skills-alongside-spec.md) | Ship practice skills alongside the specification | Minimal — significant but revisable |
| [TDR-0004](TDR-0004-markdown-yaml-serialisation.md) | Markdown with YAML frontmatter as the serialisation | Bare — reversible with tooling |
| [TDR-0005](TDR-0005-repo-name-mtdr.md) | Name the repository MTDR | Minimal |
| [TDR-0006](TDR-0006-json-schema-for-frontmatter.md) | Provide a JSON Schema for the frontmatter | Minimal — significant but revisable |
| [TDR-0007](TDR-0007-add-decision-identification-skill.md) | Add a decision-identification skill in front of the capture skill | Bare — cheap to reverse |
| [TDR-0008](TDR-0008-add-value-record-as-sibling-record.md) | Add the Value Record as the TDR's sibling record | Minimal — significant but revisable |
| [TDR-0009](TDR-0009-decision-assurance-case.md) | Add the Decision Assurance Case as the second sibling record | Minimal — significant but revisable |
| [TDR-0010](TDR-0010-temporal-risk-delta.md) | Make the risk delta temporal; sharpen DAC object semantics | Minimal — significant but revisable |
| [TDR-0011](TDR-0011-agent-deployment-pack.md) | Ship an agent deployment pack; a minor release, not a v2 | Minimal — significant but revisable |
| [TDR-0012](TDR-0012-architecture-overview.md) | Publish an architecture overview fixing the boundary at the register | Minimal — significant but revisable |
| [TDR-0013](TDR-0013-practice-guides.md) | Add practice guides for building decision memory | Minimal — significant but revisable |
| [TDR-0014](TDR-0014-consequential-decision-grammar.md) | Publish the Consequential Decision Grammar as a candidate authoring aid | Minimal — significant but revisable |
| [TDR-0015](TDR-0015-visibility-and-effectiveness.md) | Visibility stays out of the record; open an `x-` namespace; defer effectiveness fields | Full — a reserved prefix and a boundary commitment are one-way doors |
| [TDR-0016](TDR-0016-routing-and-disposition-refinements-from-field-application.md) | Refine DAC routing and disposition from the first at-scale field application | Minimal — significant but revisable |
| [TDR-0017](TDR-0017-language-admission-test.md) | Adopt a language admission test; defer this standard's language specification to evidence | Full — a published test and a boundary commitment are one-way doors |
| [TDR-0018](TDR-0018-interpretation-skills-and-the-artefact-boundary.md) | Admit vendor-neutral interpretation skills; fix the standard's boundary at the artefact | Full — a scope clarification is a one-way door |
| [TDR-0019](TDR-0019-value-record-v2-operational-value-commitment.md) | Value Record v2 — specify the Operational Value Commitment; separate epistemic state from value state | Full — new required fields and a changed enum are a one-way door |
| [TDR-0020](TDR-0020-open-organisational-record-repository-boundary.md) | State the repository boundary — an open organisational-records standard with no knowledge of its consumers | Full — a published identity commitment is a one-way door |
| [TDR-0021](TDR-0021-record-package-architecture.md) | Record-package architecture — packages follow organisational languages; dependent artefacts live with the language they serve | Full — the extraction promise and the classification test are one-way doors |
| [TDR-0022](TDR-0022-fragment-contribution-interchange-architecture.md) | Ratify the fragment-and-contribution interchange model as repository architecture | Minimal — ratifies shipped architecture at repository level |
| [TDR-0023](TDR-0023-portable-skill-architecture.md) | Portable skill architecture — skills live with record semantics; shared skills must be demonstrably record-neutral | Minimal — significant but revisable |
| [TDR-0024](TDR-0024-packaging-independence.md) | Packaging independence — packagings are distribution adapters, never normative architecture | Minimal — significant but revisable |
| [TDR-0025](TDR-0025-conformance-architecture.md) | Conformance architecture — schema validation alone is insufficient; the layered test surface | Minimal — significant but revisable |
| [TDR-0026](TDR-0026-value-recovery-vocabulary.md) | Value-recovery vocabulary — contribution classes, the completeness view, the derivation marker, composition skills | Minimal — significant but revisable |
| [TDR-0027](TDR-0027-human-ratification-confers-standing.md) | Human ratification confers standing; evidence permits MTDR to represent it as accepted | Full — the authority boundary is a one-way door |

## Decision assurance cases

| Case | Assures | Disposition |
|---|---|---|
| [DAC-0027](DAC-0027-human-ratification-confers-standing.md) | TDR-0027 standing and ratification evidence | Proceed with constraints |

## Challenging a decision

Disagree with any of this? Good — that is what the format is for.

Open a pull request proposing a **superseding TDR**: a new record with its `supersedes:` field pointing at the decision you are challenging, stating what is now known that was not known at the time, and what evidence supports the change. Discussion happens in the standard's own format.

Decisions here are never edited or deleted. They are superseded. That is the point.
