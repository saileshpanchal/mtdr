# Engineering controls

**Version:** 0.1.0 · **Status:** proposed, not ratified · **Non-normative**

This file says how engineering work on this repository is controlled: when work is committed, pushed,
reviewed, ratified and released, and what evidence each of those acts leaves. It is about how the
standard is worked on. It changes nothing in the standard, and it authorises no normative change.

Its inclusion in the repository is not ratification. Until the maintainer ratifies it, it is a proposal
that engineering work nevertheless follows.

- **Part A** reproduces the engineering-controls proposal submitted to the engineering work by the
  maintainer on 25 November 2026. It is reproduced as submitted. Three passages that name a private
  system are left out, and each omission is marked where it occurs; nothing else is changed.
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
| *[One row is omitted here: it names a private system.]* | |

*[One sentence is omitted here: it names a private system.]*

**I would make this an immediate engineering control, rather than wait for MTDR closure.** It changes how we execute the existing programme, not the methodology itself.

*[Two sentences are omitted here: the first names a private system and the second depends on it. They propose auditing existing Git histories against these controls before the controls are ratified.]*

## Part B — Proposed amendments (from a review; not part of the proposal)

1. The 30-minute threshold is an engineering checkpoint, not an approval or ratification mechanism.
2. Evidence must be reproducible, with exact commit SHAs, source versions, tests, fixture hashes and
   independent challenge. Confidential source material must not be committed without authorisation.
3. Not every commit requires a TDR. Consequential semantic changes require governing decisions;
   implementation commits link to those decisions or authorised work packages.

## Part C — How this repository implements the controls

| Control | Here |
|---|---|
| Baseline | A work package starts with a committed statement of its scope, its sources and its acceptance criteria, in the pull request that carries it. |
| Frequent commits | One commit for each coherent change, on a working branch. A checkpoint commit may be marked work in progress; it conveys no review or approval. |
| Remote visibility | Working branches are pushed. `main` is not a working branch. |
| Review checkpoints | A review names the exact commit it reviewed. If the commit changes afterwards, the new commit is reviewed again. |
| Evidence | Evidence is committed under [`decisions/evidence/`](decisions/evidence/), in a commit of its own that follows the commit it verifies. It records the exact commit, the commands, the versions used, the exit codes and the output. |
| Rejected work | A rejected approach stays in the history, with the reason for its rejection. A candidate that fails admission keeps its record ([`specification/record-admission-test.md`](specification/record-admission-test.md)). |
| History protection | No force-push to any shared branch, and no rewriting of history that has been reviewed. |
| Ratification | Ratification is the maintainer's act, against an exact reviewed commit. A status changes in place; a change of meaning needs a superseding record ([`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md)). A commit, a push, a review and a merge are none of them ratification. |
| Release | A release is one tag, one release record and one changelog entry that names the commit ([TDR-0042](decisions/TDR-0042-changelog-headings-are-not-releases.md)), with its eligibility computed from the obligations register ([TDR-0037](decisions/TDR-0037-release-eligibility-from-standing-governance.md)). |

**The five acts are separate, and each has its own authority:**

| Act | Who may do it | What it establishes |
|---|---|---|
| Commit | whoever is doing the work | what changed |
| Push | whoever is doing the work, to a working branch | that others can see it |
| Review | someone who did not write the change | whether it conforms, at a named commit |
| Ratify | the maintainer | that it is accepted |
| Release | the maintainer | that it is available as a version of the standard |

A clean local run of the suite is evidence of what was run and what it returned. It is not continuous
integration, and it is never reported as such.
