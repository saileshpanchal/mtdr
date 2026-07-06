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

## Challenging a decision

Disagree with any of this? Good — that is what the format is for.

Open a pull request proposing a **superseding TDR**: a new record with its `supersedes:` field pointing at the decision you are challenging, stating what is now known that was not known at the time, and what evidence supports the change. Discussion happens in the standard's own format.

Decisions here are never edited or deleted. They are superseded. That is the point.
