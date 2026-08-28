# Ratification evidence — TDR-0044

This note preserves the attributable human act permitting TDR-0044 to represent its standing as
`accepted`, and DAC-0044 as `proceed-with-constraints`.

**It authorises no release, and it makes no transition eligible.** It was ratified as its own act,
deliberately separate from any release authorisation, so that a later reader can see the gate
mechanism was accepted on its merits before the release it affects.

## Attributable act

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal |
| Authority | Accountable owner of TDR-0044 and repository authority for MTDR's design decisions |
| Date | 2026-08-27 |
| Act | Ratified TDR-0044; accepted DAC-0044 as `proceed-with-constraints` |
| Subject | An obligation gates a named transition, not every transition |
| Explicitly withheld | `assessed_state` is **not** altered by this act |

## Decision-bearing ruling preserved

The reviewer accepted that:

1. An obligation whose subject is a register cannot be a precondition of a standards repository
   publishing its specification. Re-scoping `DAC-0032#5` to `registered` is a judgement about
   **subject**, not about difficulty or timing.
2. **Re-scoping changes when an obligation blocks, never whether it exists.** `DAC-0032#5` is kept
   fully visible as carried debt: retained entire, measure and owner and note unchanged, and
   surfaced in every validation result under the code `carried-not-gating`.
3. **The anti-vacancy rule is preserved as ruled**: if no obligation gates a requested transition,
   the result is `indeterminate`, never `pass`. Eligibility may not be established by vacancy.
   This was a defect found by falsifying the record's own rule, and the ruling makes its preservation
   explicit rather than incidental.
4. Nothing here discharges `DAC-0032#5`. Any statement that MTDR has satisfied it is false.
5. `assessed_state` remains `pre-release`. This act does not move it, and the machinery continues
   to report the repository's actual state.

## Reviewed and accepted content

| Artefact | SHA-256 |
|---|---|
| Reviewed TDR-0044 as proposed | `01f97bf28a5110d02958b7df80e0bb4c32f2b50ccc1977ed0cb5246dd47fbb95 b36534602759c5bdee771fb8dfea11601db7b3bd3ad46f48cfaed00b4ae98e41 47deb8aa7c9a84c8718814bfebd8225d6b8c7ae53fe9c62cb266a0a07c3d444d f9566fcc22d0881420a86605d2041cf80c3fbcd076fa9715542c8e6a653b9bb8` |
| Accepted TDR-0044 representation | `` |
| Reviewed DAC-0044 as proposed | `` |
| Accepted DAC-0044 representation | `` |

The hashes differ only by the lifecycle transition and its banner. No substantive proposition changed
between review and acceptance.

## Source integrity

The ruling was supplied as a human instruction in the Claude Code session after the mechanism, its
three guard rails and the falsification that exposed the vacancy defect were presented. The source
instruction remains the authoritative evidence of the act.
