"""Checking historical candidates and their review events — NON-NORMATIVE reference implementation.

The contract is `specification/historical-candidate.md`, `specification/historical-recovery.md` and the
schemas under `schemas/shared/`; a package's recovery vocabulary is its own declaration, named in its
manifest. This module implements them and defines nothing. `tests/verify.py` calls these functions, so
the suite and an adopter running this module apply one implementation, not two that could drift.
"""
import datetime
import glob
import hashlib
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
EVENT_TIME = re.compile(r'[0-9]{4}(-(0[1-9]|1[0-2])(-(0[1-9]|[12][0-9]|3[01]))?)?')


def shared_registry(root=ROOT):
    """Every shared schema, by `$id`: they refer to their siblings, so a bare validator would fail at the
    first `$ref`, at run time rather than at authoring."""
    from referencing import Registry, Resource
    docs = (json.load(open(p, encoding='utf-8'))
            for p in sorted(glob.glob(os.path.join(root, 'schemas', 'shared', '*.schema.json'))))
    return Registry().with_resources((d['$id'], Resource.from_contents(d)) for d in docs)


def load_vocabulary(root=ROOT):
    """The recovery vocabulary each package declares, by the object it records — read from the
    package's own manifest and machine-readable form, never from a copy."""
    import yaml
    out = {}
    for m in sorted(glob.glob(os.path.join(root, 'records', '*', 'package.yaml'))):
        man = yaml.safe_load(open(m, encoding='utf-8')) or {}
        if man.get('vocabulary') and man.get('object'):
            path = os.path.join(root, 'records', man['name'], man['vocabulary'])
            out[man['object']] = json.load(open(path, encoding='utf-8'))['$defs']
    return out


def _values(d):
    return {d['const']} if 'const' in d else set(d.get('enum', []))


def candidate_references(c):
    """Integrity rules 1–5, 7 and 8 of `historical-candidate.md`: everything the candidate refers to,
    it carries. Structural — they hold or fail whatever the record type."""
    out = []
    frags = [x['fragment_id'] for x in c['fragments']]
    contribs = {k['contribution_id'] for k in c['contributions']}
    for k in c['contributions']:
        out += [f"contribution {k['contribution_id']} cites fragment {r}, which the candidate does not carry"
                for r in k['fragment_refs'] if r not in frags]
    out += [f"the assembly groups {r}, which the candidate does not carry"
            for r in c['assembly']['contribution_refs'] if r not in contribs]
    if sorted(a['fragment_ref'] for a in c['fragment_annotations']) != sorted(frags):
        out.append("fragment_annotations must name each fragment exactly once")
    named = [a['contribution_ref'] for a in c['contribution_annotations']]
    if len(named) != len(set(named)) or not set(named) <= contribs:
        out.append("contribution_annotations must name contributions the candidate carries, each at most once")
    for a in c['contribution_annotations']:
        out += [f"considered cites fragment {r}, which the candidate does not carry"
                for r in a['considered']['fragment_refs'] if r not in frags]
    if c['event_time_ref'] != 'unknown' and c['event_time_ref'] not in c['assembly']['contribution_refs']:
        out.append(f"event_time_ref {c['event_time_ref']} names no contribution in the assembly")
    out += [f"{a['fragment_ref']} restates itself" for a in c['fragment_annotations']
            if a.get('restates') == a['fragment_ref']]
    if any(b['basis'] == 'singleton' for b in c['assembly']['grouping_basis']):   # TDR-0050: the entry, never the container
        source = {x['fragment_id']: x['source_ref'] for x in c['fragments']}
        grouped = {r for k in c['contributions'] if k['contribution_id'] in c['assembly']['contribution_refs']
                   for r in k['fragment_refs']}
        if len({source[r] for r in grouped if r in source}) > 1:
            out.append("the assembly cites `singleton`, and its contributions rest on more than one source")
    return out


def candidate_roles(c, vocabulary):
    """Integrity rule 6: the recovery roles the object's package declares. Semantic. Returns None when
    the package declares no recovery vocabulary, so a caller can say so rather than pass silently."""
    vocab = vocabulary.get(c['assembly']['target_object'])
    if not vocab:
        return None
    out = []
    role = {k['contribution_id']: k['semantic_role'] for k in c['contributions']}
    never, context = _values(vocab['never_inferred_roles']), _values(vocab['context_roles'])
    for k in c['contributions']:
        if k.get('derivation') == 'inferred' and k['semantic_role'] in never:
            out.append(f"{k['contribution_id']} infers {k['semantic_role']}: who acted, under what "
                       f"authority, or instead of what, is never inferred")
    findings = _values(vocab.get('finding_classes', {}))
    invoked = _values(vocab.get('invocation_roles', {}))
    out += [f"{k['contribution_id']} carries the finding class {k['semantic_role']}: findings are reported by "
            f"fragment, never grouped into a candidate" for k in c['contributions'] if k['semantic_role'] in findings]
    kind = {a['fragment_ref']: a['evidence_kind'] for a in c['fragment_annotations']}
    for a in c['fragment_annotations']:            # a restatement supports what its source supports
        if a.get('restates') in kind:
            kind[a['fragment_ref']] = kind[a['restates']]
    for k in c['contributions']:
        if k['semantic_role'] in invoked:
            out += [f"{k['contribution_id']} ({k['semantic_role']}) rests on {f}, `{kind[f]}` material: authority is "
                    f"what the act invokes, and an instrument it does not cite supports applicability, a finding"
                    for f in k['fragment_refs'] if kind.get(f) in ('unlinked', 'retrospective')]
    if c['event_time_ref'] != 'unknown' and role.get(c['event_time_ref']) not in _values(vocab['event_role']):
        out.append(f"event_time_ref {c['event_time_ref']} is not a contribution to the event role")
    event = next((k for k in c['contributions'] if k['contribution_id'] == c['event_time_ref']), None)
    if event and not EVENT_TIME.fullmatch(str(event['interpreted_value'])):
        out.append(f"the event contribution's value {event['interpreted_value']!r} is not a time the "
                   f"grade can be computed from (YYYY, YYYY-MM or YYYY-MM-DD)")
    annotated = {a['contribution_ref'] for a in c['contribution_annotations']}
    for cid, r in role.items():
        if (r in context) != (cid in annotated):
            out.append(f"{cid} ({r}): `considered` belongs on every context contribution and on no other")
    return out


def candidate_integrity(c, vocabulary):
    """Every rule a schema cannot express, structural and semantic together, as the suite applies them."""
    return candidate_references(c) + (candidate_roles(c, vocabulary) or [])


def _interval(t):
    """The days a partial date can denote: `2019` is the whole year, `2019-03` the whole of March."""
    y = int(t[:4])
    if len(t) == 4:
        return datetime.date(y, 1, 1), datetime.date(y, 12, 31)
    m = int(t[5:7])
    if len(t) == 7:
        nxt = datetime.date(y + m // 12, m % 12 + 1, 1)
        return datetime.date(y, m, 1), nxt - datetime.timedelta(days=1)
    d = datetime.date.fromisoformat(t)
    return d, d


def contemporaneity(capture, creation, event, considered='unknown'):
    """`historical-recovery.md` §Contemporaneity — computed from the times, never asserted. The times
    order material across days, never within one; an order they leave open is closed only by
    `considered: evidenced`, which never lifts a time-less artefact and never overrides `later`."""
    if event == 'unknown':
        return 'indeterminate'                 # a missing event moment is never assumed
    ev = _interval(event)
    if capture != 'unknown':
        cap = _interval(capture)
        if cap[1] < ev[0]:
            return 'contemporaneous'
        if cap[0] > ev[1]:
            return 'later'
        left_open = True                       # the event's own day, or a span that includes it
    elif creation != 'unknown':
        cre = _interval(creation)
        if cre[1] < ev[0]:
            return 'contemporaneous'           # the content existed by then, so it was captured by then
        left_open = cre[0] <= ev[1]            # written up later says nothing about capture
    else:
        left_open = False                      # no time at all: nothing to order
    return 'contemporaneous' if left_open and considered == 'evidenced' else 'indeterminate'


def contribution_grades(c):
    """Contemporaneity per context contribution, computed: a contribution resting on several fragments
    takes the least contemporaneous grade among them."""
    times = {a['fragment_ref']: (a['capture_time'], a['creation_time']) for a in c['fragment_annotations']}
    for a in c['fragment_annotations']:            # a restatement adds no time of its own
        if a.get('restates') in times:
            times[a['fragment_ref']] = times[a['restates']]
    value = {k['contribution_id']: k for k in c['contributions']}
    event = 'unknown' if c['event_time_ref'] == 'unknown' else str(value[c['event_time_ref']]['interpreted_value'])
    rank = ('later', 'indeterminate', 'contemporaneous')
    return {a['contribution_ref']: min((contemporaneity(*times[f], event, a['considered']['state'])
                                        for f in value[a['contribution_ref']]['fragment_refs']), key=rank.index)
            for a in c['contribution_annotations']}


def jcs_digest(doc):
    """RFC 8785. For documents of strings, integers, booleans and nulls with ASCII keys, sorted compact
    UTF-8 JSON is byte-identical to JCS; a non-integer number is where they part, so one is refused
    rather than hashed wrongly. Implementations use a JCS library."""
    def numbers(o):
        if isinstance(o, float):
            return True
        return any(numbers(v) for v in (o.values() if isinstance(o, dict) else o if isinstance(o, list) else ()))
    if numbers(doc):
        raise ValueError("a non-integer number: hash it with a JCS library")
    canonical = json.dumps(doc, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return 'sha256:' + hashlib.sha256(canonical.encode('utf-8')).hexdigest()
