# Stage 1 — identify-decision-contributions: plain summary

Run on 2026-11-26 by an AI agent (Claude, model claude-fable-5-2) following the installed `identify-decision-contributions` and `identify-record-contributions` skills. Nine sources examined, all of each read. No TDR and no candidate is produced at this stage.

Outputs in this folder: `fragments.json` (100 verbatim spans, char-offset locators, SHA-256 source hashes), `contributions.json` (64), `fragment-annotations.json` (capture time, creation time, the basis of each, evidence kind per candidate), `considered-annotations.json` (one per context contribution), `findings.json` (38), `unclassified.json` (4).

## What appears to be present

Four spans record a commitment of money or time, each made by a different body or person on a different day:

1. OIC minute, 9 April 2026, item 4 — "The Committee approved the award to Vantry Systems Ltd as recommended, subject to …".
2. Board minute, 21 May 2026, item 7 — "The Board **RESOLVED** that … be transferred to the Kestrel Customer Hub with effect from 1 September 2026, and that £120,000 be released …".
3. Email, Margaret Oyelaran, 22 July 2026 — "Agreed, go with 1 October, and keep the agency cover going until then", answering Duncan Faraday's "I think we should move it to 1 October".
4. File note, P. Nandakumar, "Tues, wk of 1 June" — "Verbally agreed. Letter to follow".

## What is conspicuously absent

- A named individual holding either committee decision (1, 2). The material names forums.
- An instrument cited by any act except by paragraph number ("4.5") in the email thread around act 3.
- A year in the file note (4) and in the chat transcript.
- Any statement of reversal cost, and any stated confidence, for any of the four.
- Any alternative considered for act 2. Paper 7, which the Board minute cites, was not supplied.
- The letter from Calder, the 17 September Board minute, and the signed Vantry contract.

## Times and their bases

| Source | Capture | Creation | Basis |
|---|---|---|---|
| SRC-01 | 2025-01 | unknown | "Version 3, adopted by the Board January 2025"; the extract's own date is not stated |
| SRC-02 | 2026-03-26 | 2026-03-26 | "Dated: 26 March 2026" |
| SRC-03 | 2026-04-09 | unknown | heading "Date: 9 April 2026"; write-up date not stated |
| SRC-04 | 2026-05-21 | unknown | heading "Date: 21 May 2026"; write-up date not stated |
| SRC-05 | unknown | unknown | "Tues, wk of 1 June" has no year; scan date not stated |
| SRC-06 | 2026-07-13 / 2026-07-13 / 2026-07-14 / 2026-07-22 | same | each email's own "Date:" header |
| SRC-07 | unknown | unknown | "Thu 23 July" has no year |
| SRC-08 | unknown | 2026-09-30 | "Position as at 30 September 2026"; row entry dates not stated |
| SRC-09 | unknown | unknown | "For: Project Board, 14 October 2026" dates the meeting, not the report |

No time was taken from a filename, a folder or another document.

## Fragments found and not used in any contribution or finding

`F01-4.1-A`, `F01-4.3`, `F01-6.1`, `F01-6.2`, `F01-6.3` (scheme paragraphs read and quoted in notes only), `F06-E1-HDR`, `F06-E3-HDR` (email headers; their dates are the basis of the email times), `F09-HEAD`.
