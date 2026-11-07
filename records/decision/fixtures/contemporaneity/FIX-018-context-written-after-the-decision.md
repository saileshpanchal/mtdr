# FIX-018 — context written after the decision

> **Fictional worked fixture.** Ashgrove Rail, its people and its numbers are invented.

**Proves** that material created after a decision is never its context, however well it explains it.

## Sources

**A — Board minute, `board/2021-05-12-minute.md`**

> The board agreed to retire the paper ticket stock at all staffed stations from 1 September, as
> recommended in paper 21/14. Owner: Hana Brightwell, Director of Retail.

**B — Paper 21/14, `board/papers/21-14-paper-tickets.md`, dated 2021-04-28**

> Paper stock costs £0.6m a year to print and distribute. Smartcard use at staffed stations is 71%.

**C — Risk paper, `risk/2021-06-01-ticketing-risk.md`, dated 2021-06-01**

> The paper stock contract carried an unhedged exposure to a single printer, which the board was
> right to remove.

## Expected

- **One candidate**, decision date `2021-05-12`, owner Hana Brightwell, both evidenced by A.
- **B is context**: `cited-material`, `considered: evidenced` by A's citation, graded
  `contemporaneous`.
- **C computes `later`.** Its capture time, 2021-06-01, begins after the event. It is not context, and
  contributes at most `corroboration` that the decision was taken.

## Must not

- **Render C's printer exposure as part of what was known.** Nothing contemporaneous says it.
- **Grade C `indeterminate` to keep it.** Its time is evidenced and after the event; the grade is
  `later`.
- **Read the risk paper's verdict — "right to remove" — as the decision's rationale.**

## What this fixture detects

Hindsight entering context by the most ordinary route: a later document that explains the decision
better than the decision's own papers did.
