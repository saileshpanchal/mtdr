---
id: TDR-0014
title: Publish the Consequential Decision Grammar as a candidate authoring aid
status: accepted
template: minimal
decision_date: 2026-07-23
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0003, TDR-0013
confirmed_by_outcome: pending — review once the grammar has been tested across the full range of decision classes
---

# TDR-0014 — Publish the Consequential Decision Grammar as a candidate authoring aid

## Context — what was known at the time

The standard defined the record and the skills, but the on-ramp for a human — how to write a single
consequential decision well — was implicit in the capture skill rather than named. Given–When–Then and user
stories show what a shared authoring shape does for adoption: it makes the good questions obvious without
adding process. A six-line grammar (Under · Given · We decide · This means · Unless · Until) had emerged and
was ready to test in public, provided it added nothing to the record format and was offered as a candidate,
not settled doctrine.

## Decision

Publish the grammar as [`practice/decision-grammar.md`](../practice/decision-grammar.md): the six lines,
clause guidance, the mapping into the existing MTDR fields, anti-patterns, a consequentiality test, and
fictional worked examples — explicitly **non-normative and additive** (no field, template or schema change).
Reference it from the capture and identification skills. Mark it a working candidate (v0.1) and invite
testing across decision classes. The public face is always the spoken six-line form, never an initialism.

## Alternatives rejected

- **Put the grammar in the spec as normative** — rejected: it is an authoring aid over the existing fields,
  not a change to the format; making it normative would imply a new conformance obligation and could ossify a
  candidate still being tested.
- **Add fields for authority and exceptions** — rejected: *Under*'s authority and *Unless*'s exceptions live
  in the record's prose; the grammar deliberately needs no new field, so every existing record still validates.
- **Use the initialism publicly** — rejected: the mnemonic is unreadable; the spoken six-line form is the
  public face.
- **Wait until the grammar is proven across every decision class** — rejected: it is offered as a candidate
  precisely so that testing it in the open is how it gets proven or corrected, by superseding change.

## Options foreclosed

The grammar is now part of the repository's practice surface and its public identity is the six spoken lines.
Changing the clause set is a meaning change, made by a superseding record, not an edit.

## Review

`confirmed_by_outcome` tests whether the six separations stay conceptually distinct across strategy, policy,
architecture, risk acceptance, regulatory interpretation, investment, operating model, agent-mandate and
runtime decisions. Where a clause collapses for a whole class, that is the evidence for a superseding revision.
