# Engineering controls

**Version:** 0.1.0 · **Status:** proposed, not ratified · **Non-normative**

This file says how engineering work on this repository is controlled: when work is committed, pushed,
reviewed, ratified and released, and what evidence each of those acts leaves. It is about how the
standard is worked on. It changes nothing in the standard, and it authorises no normative change.

Its inclusion in the repository is not ratification, and neither is the merge of a pull request that
carries it. Every consequential decision about this standard's governance is recorded as a decision
record in [`decisions/`](decisions/), and the repository keeps no second way of deciding
([`GOVERNANCE.md`](GOVERNANCE.md)). These controls therefore become this repository's practice only
when a decision record adopts them. Until then this file is a proposal, and Part C says which of its
rows restate something the repository has already recorded and which are proposed here for the first
time.

- **Part A** reproduces the engineering-controls proposal submitted to the engineering work by the
  maintainer on 25 November 2026. It is reproduced as submitted, with three exceptions, each marked
  where it occurs: its headings sit one level lower; two passages that name a private system are left
  out; and in a third passage only the name of that system is left out. Nothing else is changed.
- **Part B** records three proposed amendments, which came from a review of that proposal. They are
  kept apart from Part A so that each can be accepted or dropped on its own.
- **Part C** says where this repository implements each control.

## Part A — The proposal, as submitted on 25 November 2026

**Git should be the continuous evidence base for engineering work, not simply the destination for completed and approved work.**

At present, I suspect we are allowing agents to undertake too much work before establishing a reviewable baseline. This increases the risk of semantic drift, lost rationale and expensive retrospective review.

We should distinguish **committing, pushing, reviewing, ratifying and releasing**. These are separate acts with different authorities.

### **Proposed Git controls**

| Control | Rule |
|---|---|
| Baseline | Commit the authorised plan, source references and acceptance criteria before implementation begins. |
| Frequent commits | Commit each coherent change, rather than waiting for a complete work package. |
| Remote visibility | Push working branches frequently so independent reviewers can access the latest state. |
| Review checkpoints | Review at each logical milestone against an exact commit SHA. |
| Evidence | Commit test results, conformance matrices, challenge findings and responses alongside implementation. |
| Rejected work | Preserve rejected approaches and the reasons for rejection. |
| History protection | No force-pushing or rewriting shared review history. |
| Ratification | Only authorised, independently reviewed changes enter the protected baseline. |
| Release | Tag releases with their applicable MTDR version and conformance evidence. |

### **Proposed agent engineering lifecycle**

**Authorised baseline**

Plan, scope, sources and acceptance criteria

**Incremental implementation**

Small commits pushed to the remote branch

**Independent challenge**

Review against pinned commit and authoritative sources

**Remediation**

Further commits responding to specific findings

**Human ratification**

Acceptance against an exact reviewed commit

**Merge and release**

Protected baseline with traceable evidence

### **Commit frequency**

I would establish the following defaults for Claude, Hermes and other engineering agents:

- Before starting an authorised work package.
- After each coherent specification, skill or implementation change.
- Before and after every independent review.
- Before starting an experiment and after recording its findings.
- At least every 30 minutes during substantive engineering work, where changes exist.
- Before handing work to another agent or ending a session.

The 30-minute threshold is a proposed starting point, not a substitute for logical commit boundaries.

### **Apply MTDR to our own engineering**

There is also an opportunity to make each consequential commit traceable to its governing transformation records:

| Artefact | Evidence relationship |
|---|---|
| TDR | Why the change was authorised |
| Git commit | What changed |
| Independent challenge | Whether the change conforms |
| Acceptance record | Who accepted the outcome and against which criteria |
| Release tag | Which approved implementation became available |
| *[One row is left out here: it names a private system.]* | |

*[One sentence is left out here: it names a private system.]*

**I would make this an immediate engineering control, rather than wait for MTDR closure.** It changes how we execute the existing programme, not the methodology itself.

I would also audit the existing Git histories of MTDR and *[the name of a private system is left out here]* against these proposed controls before ratifying them, to establish the actual commit frequency, review coverage and evidence gaps. I have not yet verified those histories.

## Part B — Proposed amendments (from a review; not part of the proposal)

1. The 30-minute threshold is an engineering checkpoint, not an approval or ratification mechanism.
2. Evidence must be reproducible, with exact commit SHAs, source versions, tests, fixture hashes and
   independent challenge. Confidential source material must not be committed without authorisation.
3. Not every commit requires a TDR. Consequential semantic changes require governing decisions;
   implementation commits link to those decisions or authorised work packages.

## Part C — How this repository implements each control, or would

Each row is marked **recorded** where it restates a rule that an accepted record of this repository
already states, and **proposed** where it is new here. A proposed row describes what would happen
once the controls are adopted. It does not describe what has happened so far: most of the commits on
`main` to date were made directly on it, not through a reviewed branch.

| Control | Here | Standing |
|---|---|---|
| Baseline | A work package would start with a statement of its scope, its sources and its acceptance criteria, given in the pull request that carries it and committed in its evidence record. | proposed |
| Frequent commits | One commit for each coherent change, on a working branch. A checkpoint commit may be marked work in progress; it conveys no review or approval. | proposed |
| Remote visibility | Working branches would be pushed, and work would no longer be committed directly to `main`. | proposed |
| Review checkpoints | A review would name the exact commit it reviewed. If the commit changes afterwards, the new commit would be reviewed again. | proposed |
| Evidence | Evidence would be committed under [`decisions/evidence/`](decisions/evidence/), in a commit of its own that follows the commit it verifies, recording the exact commit, the commands, the versions used, the exit codes and the output. That folder already holds ratification evidence and the release record. | proposed |
| Rejected work | A decision is never edited or deleted, only superseded ([`CONTRIBUTING.md`](CONTRIBUTING.md)). A candidate that fails admission keeps its record ([`specification/record-admission-test.md`](specification/record-admission-test.md)). An identifier published on a branch is never reused ([`decisions/ALLOCATION.md`](decisions/ALLOCATION.md)). | recorded |
| | A rejected approach in other work would also stay in the history, with the reason for its rejection. | proposed |
| History protection | No force-push to any shared branch, and no rewriting of history that has been reviewed. | proposed |
| Ratification | "Standing is conferred by an authorised human ratification of a defined candidate judgement. MTDR requires durable, attributable evidence sufficient to establish that ratification before a record may represent the judgement's standing as `accepted`." ([TDR-0027](decisions/TDR-0027-human-ratification-confers-standing.md)). No tool ratifies anything ([`GOVERNANCE.md`](GOVERNANCE.md)). A status changes in place; a change of meaning needs a superseding record ([`CONTRIBUTING.md`](CONTRIBUTING.md)). | recorded |
| Release | Eligibility computed from the obligations register ([TDR-0037](decisions/TDR-0037-release-eligibility-from-standing-governance.md)), an authorised human act, and then one tag, one release record and one changelog entry that says which commit and which generated catalogue it describes ([TDR-0042](decisions/TDR-0042-changelog-headings-are-not-releases.md)). | recorded |

**The five acts are separate, and each has its own authority:**

| Act | Who | What it establishes |
|---|---|---|
| Commit | whoever is doing the work | what changed |
| Push | whoever is doing the work, to a working branch | that others can see it |
| Review | someone who did not write the change | whether it conforms, at a named commit |
| Ratify | an authorised person; for this repository, the maintainer | standing. The record may be shown as `accepted` only once durable, attributable evidence of that act exists (TDR-0027). A commit, a merge, or a tool writing `accepted` establishes none of this |
| Release | an authorised human act, by the maintainer | that it is available as a version of the standard |

"MTDR closure", in Part A, refers to the completion of the current programme of work on the standard.

A clean local run of the suite is evidence of what was run and what it returned. It is not continuous
integration, and it is never reported as such.
