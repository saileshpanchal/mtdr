# FIX-030 — a shared date is not an order

> **Fictional worked fixture.** Fenwick Harbour Trust, its people and its numbers are invented.

**Proves** that material dated the decision's own day is not thereby contemporaneous: the times order
material across days, never within one, and only evidence that it was before whoever acted closes the
order.

## Sources

**A — Board minute, `board/minutes-2024.md`**, document-management creation date 2024-06-21; the text
opens *Minutes of the Board, 17 June 2024*

> Members noted that the north pontoon had failed two load inspections this year. Having considered
> paper HB/24/31, tabled, the board agreed to close the north pontoon to commercial berthing from
> 1 August. Owner: Imogen Tate, Harbour Master.

**B — Paper HB/24/31, `board/papers/HB-24-31.md`**

> **HB/24/31, 17 June 2024 (tabled).** Repairing the north pontoon to commercial loading costs £1.3m.

**C — Email, `email/pontoon-insurer.md`**

> **17 June 2024.** Re HB/24/31: the insurer will not renew cover for the north pontoon at commercial
> loading after July.

## Expected

- **One candidate**, decision date `2024-06-17` from the minute's own heading, owner Imogen Tate.
- **The minute's own context** — two failed load inspections — is `considered: evidenced` by
  construction and grades `contemporaneous`. The minute was written up on 21 June; its capture is the
  meeting.
- **B is `cited-material`**, `considered: evidenced` by the minute's record of it as tabled, and grades
  `contemporaneous`: being before the board closes the order its date leaves open.
- **C joins on `entity-match`** — it names HB/24/31 — and is `unlinked`, `considered: unlinked`. It
  shares the meeting's date, which orders nothing, so it grades **`indeterminate`**. Whether the board
  knew of the insurer's position goes to `unresolved`.

## Must not

- **Grade C `contemporaneous` because it is dated the day of the meeting.** It may have been written
  that evening.
- **Grade C `later` because nothing shows it was before the board.** Unordered is not after.
- **Grade the minute's own context `indeterminate` because the minute was written up on 21 June.**
- **Present the insurer's position as part of what the board knew.**

## What this fixture detects

Two opposite errors on the decision's own day: a shared date read as an order — which lets material
written after the meeting become its context — and a late write-up read as a late capture.
