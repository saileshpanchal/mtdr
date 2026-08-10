# SourceFragment

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

A span of organisational material, exactly as found. This is evidence, and it is the only structure in
this directory that is not an interpretation.

## The one rule

**A SourceFragment is immutable and verbatim.** It is not summarised, paraphrased, cleaned, translated
or normalised beyond character encoding. If the source says "circa £10m (TBC)", the fragment says
"circa £10m (TBC)" — the hedge and the uncertainty marker are evidence, and a skill that tidies them
away has destroyed the thing it was supposed to preserve.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `fragment_id` | Yes | Stable identifier for this span |
| `source_ref` | Yes | Identifier of the source artefact — path, URI, document id. **Opaque to this standard**; its meaning belongs to whatever supplied the material |
| `source_hash` | Yes | Hash of the source artefact as read, so a later reader can tell whether the source has since changed |
| `locator` | Yes | The exact span within the source. Structure depends on source type: page and character offsets, line range, sheet and cell range, timestamp range |
| `content` | Yes | The verbatim text of the span |
| `source_time` | No | When the source material was created or dated. Frequently unknown, and `unknown` is an honest value — see [`temporal-semantics.md`](temporal-semantics.md) |
| `observed_at` | Yes | When the fragment was read |
| `observed_by` | Yes | Identity and version of whatever read it |

## What it never holds

- **No record type.** A fragment does not know what it will contribute to.
- **No semantic role.** Naming the role is interpretation, and belongs to
  [`RecordContribution`](record-contribution.md).
- **No interpreted value.** The content is what the source says, not what it means.
- **No confidence.** There is nothing to be uncertain about yet; the source said what it said.

A fragment carrying a `record_type_hint` is not a fragment. It is an interpretation wearing evidence's
clothing, and it forces a one-to-one relationship between fragments and records that does not hold —
see the worked case in [`record-contribution.md`](record-contribution.md).

## Quality checks

- **The locator resolves.** Given `source_ref` and `locator`, a reader can find the span. A fragment
  whose locator cannot be resolved is not admissible evidence for anything.
- **The content matches the span.** Not a summary of it, not a longer passage containing it.
- **The span is large enough to carry its own meaning.** "£10m" alone is not a fragment; the sentence
  that gives it a subject and a tense is. Err towards the sentence, and towards the paragraph where a
  sentence depends on it.

## Anti-patterns

- **The tidied fragment** — hedges, qualifications and provisional markers removed because they made
  the extraction look weaker. They *are* the extraction.
- **The document-sized fragment** — the whole file recorded as one span, which makes the locator
  useless and every downstream provenance claim unfalsifiable.
- **The reconstructed fragment** — text assembled from two places and recorded as one span. Two spans
  are two fragments; a contribution may reference both.
- **The paraphrased fragment** — "the committee approved it" where the source said "the committee
  noted the paper and asked for a revised proposal". The difference is the whole point.
