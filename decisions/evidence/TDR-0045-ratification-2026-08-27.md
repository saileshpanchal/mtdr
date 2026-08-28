# Ratification evidence — TDR-0045

This note preserves the attributable human act permitting TDR-0045 to represent its standing as
`accepted`, and DAC-0045 as `proceed-with-constraints`.

**This is the act that opens the release gate**, and it was taken separately from the release
authorisation that follows it, so a later reader can see the re-scoping was accepted on its merits
rather than as part of shipping.

## Attributable act

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal |
| Authority | Accountable owner of TDR-0045 and repository authority for MTDR's design decisions |
| Date | 2026-08-27 |
| Act | Ratified TDR-0045; accepted DAC-0045 as `proceed-with-constraints` |
| Subject | External validation follows publication and cannot gate it |
| Consequence | `DAC-0032#4` gates `externally-validated`; the release gate reaches `pass` |

## Decision-bearing ruling preserved

The reviewer accepted that:

1. An obligation satisfied only *after* publication cannot be a precondition *of* publication.
   Publication is what makes a participant unknown to the author possible.
2. The permitted re-scoping reason is **subject**: `DAC-0032#4`'s measure concerns a *participant*,
   and under TDR-0032 a claim about participant behaviour implies nothing about repository
   conformance.
3. `DAC-0032#4` is **retained entire** — measure, owner, note and `release-gated` verification
   state unchanged, carried in every validation result. MTDR claims no external validation while it
   stands.
4. **This move opens the gate**, unlike the first re-scoping, and that is recorded as the strongest
   reason to scrutinise it rather than as a footnote.
5. The permitted release claim is limited to TDR-0045's wording. Any claim of external validation,
   proven adoption, ease of installation or usability is false while #4 is outstanding.
6. **A third re-scoping reopens DAC-0045 before it lands.** Two is a judgement; three is a pattern.
7. The author's business architecture team will be the first external cohort. Their trial is
   **admissible evidence that does not by itself discharge #4** — they are independent of the
   authoring role but not unknown to the author, and recording their run as full discharge would be
   reinterpreting a measure to fit the participants available.

## Reviewed and accepted content

| Artefact | SHA-256 |
|---|---|
| Reviewed TDR-0045 as proposed | `cca15b002e51e26fd43c21e1d1b3fa19fb436586818e2a8e03e6a5da5b0f6c84 d79372fb068c8b50c08c59b6d6b97bc0bb8554a5c2ecd7e8ac006f91c7a79fdb 7c6e9e074e5954a6f3f69030af9635fec7c8a1efd0deebe85510d1fb76a1a7d8 4b50a872e75abfa500151dca0ba383a6dd38cd023728705c91cc77e87130d24f` |
| Accepted TDR-0045 representation | `` |
| Reviewed DAC-0045 as proposed | `` |
| Accepted DAC-0045 representation | `` |

The hashes differ only by the lifecycle transition and its banner. No substantive proposition changed
between review and acceptance.

## Source integrity

The ruling was supplied as a human instruction in the Claude Code session after the circularity
argument, the subject argument, the gate-opening consequence and DAC-0045's reopened adversarial
assessment were presented.
