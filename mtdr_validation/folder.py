"""Assess a folder of recovery output — NON-NORMATIVE reference implementation.

Finds every historical candidate and review event in a folder, checks each against the published
contract, and reports each in TDR-0033's four dimensions, independently. There is no aggregate verdict:
a reader reads each line (DAC-0033 constraint 8). Nothing here confers standing — a candidate's standing
is `none` whatever this module says about it, and attesting an account is a named individual's act.
"""
import glob
import json
import os
import re

from .fidelity import candidate_fidelity
from .recovery import (ROOT, candidate_references, candidate_roles, contribution_grades, jcs_digest,
                       load_vocabulary, shared_registry)
from .result import FAIL, INDETERMINATE, NOT_APPLICABLE, PASS, Dim, ValidationResult

CANDIDATE_SCHEMA = 'schemas/shared/historical-candidate.schema.json'
EVENT_SCHEMA = 'schemas/shared/candidate-review-event.schema.json'
CANDIDATE_SPEC = 'specification/historical-candidate.md'
NO_TRANSITION = ('no-transition-requested', "A candidate's standing is none; attesting its account is a named "
                                            "individual's act, which no validator performs.")


def _spec_version(root, spec):
    m = re.search(r'\*\*Version:\*\*\s*([0-9]+\.[0-9]+\.[0-9]+)', open(os.path.join(root, spec), encoding='utf-8').read())
    return m.group(1) if m else 'unknown'


def _validator_version(root):
    """The release this code ships in, as the CHANGELOG states it — marked unreleased when it is."""
    text = open(os.path.join(root, 'CHANGELOG.md'), encoding='utf-8').read()
    release = re.search(r'^## \[([0-9]+\.[0-9]+\.[0-9]+)\]', text, re.M)
    unreleased = re.search(r'^## Unreleased', text, re.M)
    version = release.group(1) if release else '0.0.0'
    return version + ('+unreleased' if unreleased and (not release or unreleased.start() < release.start()) else '')


def _kind(doc):
    if isinstance(doc, dict) and 'candidate_id' in doc and 'retrospective' in doc:
        return 'candidate'
    if isinstance(doc, dict) and 'event_id' in doc and 'candidate_digest' in doc:
        return 'review-event'
    return None


def assess_folder(folder, root=ROOT, exclude=(), sources=None):
    """Assess every candidate and review event under `folder`. Returns (assessments, not_assessed): each
    assessment is a dict with the ValidationResult and what a reader needs beside it. With `sources`, the
    folder of original material, each fragment is re-read against its source (`fidelity.py`) and reported
    in the relational dimension; without it, the summary says that source fidelity was not checked."""
    from jsonschema import Draft202012Validator
    registry, vocabulary = shared_registry(root), load_vocabulary(root)
    check = {k: Draft202012Validator(json.load(open(os.path.join(root, p), encoding='utf-8')), registry=registry)
             for k, p in (('candidate', CANDIDATE_SCHEMA), ('review-event', EVENT_SCHEMA))}
    spec = (CANDIDATE_SPEC, _spec_version(root, CANDIDATE_SPEC))
    validator = {'name': 'mtdr_validation', 'version': _validator_version(root)}
    context = {'id': 'output-folder', 'description': 'the candidates and review events found in the folder assessed'}
    if sources:
        context = {'id': 'output-folder-and-sources', 'description': 'the candidates and review events found in the '
                   'folder assessed, and the source material supplied with it, which every fragment is re-read against'}
    exclude = [os.path.abspath(e) for e in exclude]

    found, not_assessed = {'candidate': [], 'review-event': []}, []
    for path in sorted(glob.glob(os.path.join(folder, '**', '*.json'), recursive=True)):
        if any(os.path.abspath(path).startswith(e + os.sep) for e in exclude):
            continue
        rel = os.path.relpath(path, folder)
        try:
            doc = json.load(open(path, encoding='utf-8'))
        except (OSError, ValueError) as e:
            not_assessed.append((rel, f'not readable as JSON: {e}'))
            continue
        kind = _kind(doc)
        if kind is None:
            not_assessed.append((rel, 'not a historical candidate or a review event'))
            continue
        found[kind].append((rel, doc, [e.message for e in check[kind].iter_errors(doc)]))

    digests = {}
    for rel, doc, errors in found['candidate']:
        if not errors:
            try:
                digests.setdefault(doc['candidate_id'], []).append(jcs_digest(doc))
            except ValueError:
                pass
    events_for = {}
    for rel, doc, errors in found['review-event']:
        if not errors:
            events_for.setdefault(doc['candidate_id'], []).append((rel, doc))

    assessments = []
    for rel, doc, errors in found['candidate']:
        cid = str(doc.get('candidate_id', rel))
        r = ValidationResult('interchange-structure', cid, *spec, subject_ref=rel, assessed_state='candidate',
                             validator=validator, context=context)
        refs = [] if errors else candidate_references(doc)
        if errors or refs:
            r.report(Dim.STRUCTURAL, FAIL, reasons=[('schema', e) for e in errors] + [('reference', e) for e in refs])
        else:
            r.report(Dim.STRUCTURAL, PASS)
        roles, grades = None, {}
        if errors or refs:
            r.report(Dim.SEMANTIC, INDETERMINATE, reasons=[(
                'structure-failed', "The recovery roles were not evaluated: the candidate does not have the contract's shape.")])
        else:
            roles = candidate_roles(doc, vocabulary)
            if roles is None:
                r.report(Dim.SEMANTIC, INDETERMINATE, reasons=[(
                    'no-recovery-vocabulary', f"The package recording {doc['assembly']['target_object']} declares no "
                    f"recovery vocabulary, so its roles were not checked.")])
            elif roles:
                r.report(Dim.SEMANTIC, FAIL, reasons=[('recovery-role', e) for e in roles])
            else:
                r.report(Dim.SEMANTIC, PASS)
            try:
                grades = contribution_grades(doc)
            except (KeyError, ValueError):
                grades = {}
        events = events_for.get(cid, [])
        if not events:
            rel_result, rel_reasons = NOT_APPLICABLE, [('no-review-event', 'No review event names this candidate.')]
        elif errors:
            rel_result, rel_reasons = INDETERMINATE, [('structure-failed', 'The candidate cannot be digested.')]
        else:
            mine = jcs_digest(doc)
            stale = [e_rel for e_rel, e in events if e['candidate_digest'] != mine]
            rel_result, rel_reasons = (FAIL, [(
                'digest-mismatch', f"{e_rel} was recorded against different content: the candidate changed after "
                f"review, or the event names another candidate") for e_rel in stale]) if stale else (PASS, [])
        fidelity = None
        if sources and not errors:
            fidelity, why = candidate_fidelity(doc, sources)
            rel_reasons = (rel_reasons if rel_result != NOT_APPLICABLE else []) + why
            rel_result = (FAIL if FAIL in (rel_result, fidelity) else
                          INDETERMINATE if INDETERMINATE in (rel_result, fidelity) else PASS)
        elif sources:
            rel_result, rel_reasons = INDETERMINATE, [('structure-failed', 'The candidate does not have the '
                                                      "contract's shape, so its fragments were not re-read.")]
        r.report(Dim.RELATIONAL, rel_result, reasons=rel_reasons)
        r.report(Dim.TRANSITION, NOT_APPLICABLE, reasons=[NO_TRANSITION])
        assessments.append({'kind': 'candidate', 'ref': rel, 'result': r, 'grades': grades, 'fidelity': fidelity})

    for rel, doc, errors in found['review-event']:
        eid = str(doc.get('event_id', rel))
        r = ValidationResult('interchange-structure', eid, *spec, subject_ref=rel, assessed_state='recorded',
                             validator=validator, context=context)
        if errors:
            r.report(Dim.STRUCTURAL, FAIL, reasons=[('schema', e) for e in errors])
        else:
            r.report(Dim.STRUCTURAL, PASS)
        r.report(Dim.SEMANTIC, NOT_APPLICABLE, reasons=[(
            'schema-only', 'A review event carries no semantic rule beyond its schema. Its existence is never '
            'evidence that a valid human act occurred (TDR-0027).')])
        if errors:
            r.report(Dim.RELATIONAL, INDETERMINATE, reasons=[('structure-failed', 'The event does not have the contract shape.')])
        elif doc['candidate_id'] not in digests:
            r.report(Dim.RELATIONAL, INDETERMINATE, reasons=[(
                'candidate-not-in-folder', f"The candidate it names, {doc['candidate_id']}, is not in the folder assessed.")])
        elif doc['candidate_digest'] in digests[doc['candidate_id']]:
            r.report(Dim.RELATIONAL, PASS)
        else:
            r.report(Dim.RELATIONAL, FAIL, reasons=[(
                'digest-mismatch', f"The digest matches no version of {doc['candidate_id']} in the folder.")])
        r.report(Dim.TRANSITION, NOT_APPLICABLE, reasons=[NO_TRANSITION])
        assessments.append({'kind': 'review-event', 'ref': rel, 'result': r, 'grades': {}})
    return assessments, not_assessed


def summary_markdown(folder, assessments, not_assessed, sources=None):
    """A human summary: every artefact, every dimension, no aggregate verdict."""
    lines = ['# Validation summary', '',
             f"Assessed by the MTDR reference validator (non-normative), over `{folder}`.", '',
             (f"Source fidelity: every fragment re-read against the material in `{sources}` (relational)." if sources
              else "**Source fidelity was not checked**: no source material was supplied (`--sources`), so no "
                   "fragment was compared with what its source says."), '',
             '**There is no overall result.** Each artefact is reported in four dimensions that are read '
             'independently (TDR-0033). Nothing here confers standing: a candidate stays a candidate.', '']
    for kind, title in (('candidate', 'Candidates'), ('review-event', 'Review events')):
        group = [a for a in assessments if a['kind'] == kind]
        lines += [f'## {title}', '']
        if not group:
            lines += ['None found.', '']
        for a in group:
            d = a['result'].to_dict()
            lines.append(f"### {d['subject']['id']} — `{a['ref']}`")
            lines.append('')
            for dim in d['dimensions']:
                reasons = dim.get('reasons', [])
                first = (' — ' + ' '.join(reasons[0]['detail'].split())) if reasons else ''
                more = f' (+{len(reasons) - 1} more)' if len(reasons) > 1 else ''
                lines.append(f"- **{dim['dimension']}**: {dim['result']}{first}{more}")
            if a['grades']:
                graded = ' · '.join(f'`{c}` {g}' for c, g in sorted(a['grades'].items()))
                lines.append(f'- **contemporaneity of context**: {graded}')
                if 'later' in a['grades'].values():
                    lines.append('  - A `later` contribution is not context, whatever it says.')
            lines.append('')
    lines += ['## Not assessed', '']
    lines += [f'- `{rel}` — {why}' for rel, why in not_assessed] or ['Nothing.']
    return '\n'.join(lines) + '\n'


def write_results(folder, out, assessments, not_assessed, sources=None):
    """One validation result per artefact, each checked against the published schema before it is
    written, and the summary beside them."""
    os.makedirs(out, exist_ok=True)
    for a in assessments:
        problems = a['result'].validate()
        if problems:
            raise ValueError(f"{a['ref']}: the result does not satisfy the published schema: {problems[0]}")
        name = re.sub(r'[^A-Za-z0-9._-]', '_', a['result'].subject_id)
        with open(os.path.join(out, f'{name}.validation.json'), 'w', encoding='utf-8') as fh:
            fh.write(a['result'].to_json(indent=2, ensure_ascii=False) + '\n')
    with open(os.path.join(out, 'summary.md'), 'w', encoding='utf-8') as fh:
        fh.write(summary_markdown(folder, assessments, not_assessed, sources))
