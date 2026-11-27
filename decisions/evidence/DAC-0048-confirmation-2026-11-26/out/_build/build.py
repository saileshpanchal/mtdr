"""Builds the recovery outputs from data.py. Written by the agent for this run; not MTDR tooling.
Usage: python build.py <sources-folder> <out-folder> <installed-package-folder>"""
import hashlib, json, os, sys, calendar
sys.dont_write_bytecode = True
import data as D

SRC, OUT, PKG = sys.argv[1], sys.argv[2], sys.argv[3]
NOW = '2026-11-26'
AGENT = {'name': 'Claude (AI agent) executing mtdr-decision/recover-decision-records', 'version': 'claude-fable-5-2'}

texts, hashes = {}, {}
for f in sorted(os.listdir(SRC)):
    raw = open(os.path.join(SRC, f), 'rb').read()
    hashes[f] = 'sha256:' + hashlib.sha256(raw).hexdigest()
    texts[f] = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

def times(fid):
    src = D.FRAGMENTS[fid][0]
    if src == D.S6:
        d = D.EMAIL_TIMES[fid.split('-')[1]]
        return d, d, d
    cap, cre, st, _ = D.SOURCE_TIMES[src]
    return cap, cre, st

FR = {}
for fid, (src, text) in D.FRAGMENTS.items():
    n = texts[src].count(text)
    assert n == 1, f'{fid}: text occurs {n} times in {src}'
    a = texts[src].index(text)
    f = dict(fragment_id=fid, source_ref=src, source_hash=hashes[src],
             locator={'kind': 'char-offset', 'start': a, 'end': a + len(text)},
             content=text, source_time=times(fid)[2], observed_at=NOW, observed_by=AGENT)
    FR[fid] = f

def contribution(c):
    return dict(contribution_id=c['contribution_id'], fragment_refs=c['fragment_refs'], **D.TDR,
                semantic_role=c['semantic_role'], interpreted_value=c['interpreted_value'], interpreter=AGENT,
                interpreted_at=NOW, extraction_confidence=c['extraction_confidence'],
                epistemic_confidence=c['epistemic_confidence'], derivation=c['derivation'])

# ---- contemporaneity, recomputed from historical-recovery.md rules 1-6 (the agent's own implementation)
def days(t):
    p = [int(x) for x in t.split('-')]
    if len(p) == 1: return (p[0], 1, 1), (p[0], 12, 31)
    if len(p) == 2: return (p[0], p[1], 1), (p[0], p[1], calendar.monthrange(p[0], p[1])[1])
    return tuple(p), tuple(p)

def grade_fragment(cap, cre, event, considered):
    if event == 'unknown': return 'indeterminate'
    e0, e1 = days(event)
    if cap != 'unknown':
        c0, c1 = days(cap)
        if c1 < e0: return 'contemporaneous'
        if c0 > e1: return 'later'
        return 'contemporaneous' if considered == 'evidenced' else 'indeterminate'
    if cre != 'unknown':
        r0, r1 = days(cre)
        if r1 < e0: return 'contemporaneous'
        if r0 > e1: return 'indeterminate'
        return 'contemporaneous' if considered == 'evidenced' else 'indeterminate'
    return 'indeterminate'

ORDER = {'later': 0, 'indeterminate': 1, 'contemporaneous': 2}
CONTEXT_ROLES = {'context', 'evidence-business', 'evidence-architecture', 'evidence-regulatory', 'evidence-operations',
                 'evidence-customer', 'evidence-data', 'evidence-external'}

os.makedirs(OUT, exist_ok=True)
def write(rel, obj):
    path = os.path.join(OUT, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        if isinstance(obj, str): fh.write(obj)
        else: json.dump(obj, fh, ensure_ascii=False, indent=2); fh.write('\n')

built, grades_all = [], {}
for cand in D.CANDIDATES:
    cid = cand['candidate_id']
    used = []
    for c in cand['contributions']:
        for r in c['fragment_refs']:
            if r not in used: used.append(r)
    for state, refs in cand['considered'].values():
        for r in refs:
            if r not in used: used.append(r)
    assert set(used) == set(cand['kinds']), (cid, set(used) ^ set(cand['kinds']))
    fann = []
    for fid in used:
        k = cand['kinds'][fid]
        cap, cre, _ = times(fid)
        a = dict(fragment_ref=fid, capture_time=cap, creation_time=cre, evidence_kind=k if isinstance(k, str) else k[0])
        if not isinstance(k, str): a['restates'] = k[1]
        fann.append(a)
    ctx = [c['contribution_id'] for c in cand['contributions'] if c['semantic_role'] in CONTEXT_ROLES]
    assert set(ctx) == set(cand['considered']), (cid, set(ctx) ^ set(cand['considered']))
    cann = [dict(contribution_ref=k, considered=dict(state=cand['considered'][k][0], fragment_refs=cand['considered'][k][1])) for k in ctx]
    doc = dict(
        contract_version='1.0.0', candidate_id=cid, retrospective=True, standing='none', status='candidate',
        event_time_ref=cand['event'],
        fragments=[FR[f] for f in used],
        contributions=[contribution(c) for c in cand['contributions']],
        assembly=dict(assembly_id=cid + '-ASM', **D.TDR,
                      contribution_refs=[c['contribution_id'] for c in cand['contributions']],
                      grouping_basis=[dict(basis=b, evidence=e) for b, e in cand['grouping_basis']],
                      assembly_confidence=cand['assembly_confidence'], missing_semantics=cand['missing_semantics'],
                      conflicts=cand['conflicts'], supersessions=cand['supersessions'], unresolved=cand['unresolved'],
                      status='candidate'),
        fragment_annotations=fann, contribution_annotations=cann)
    write(f'candidates/{cid}.json', doc)
    # recompute grades
    event = next(c['interpreted_value'] for c in cand['contributions'] if c['contribution_id'] == cand['event'])
    ann = {a['fragment_ref']: a for a in fann}
    g = {}
    for c in cand['contributions']:
        if c['semantic_role'] not in CONTEXT_ROLES: continue
        state = cand['considered'][c['contribution_id']][0]
        gs = []
        for r in c['fragment_refs']:
            a = ann[r]
            if a['evidence_kind'] == 'restatement' and a.get('restates') in ann: a = ann[a['restates']]
            gs.append(grade_fragment(a['capture_time'], a['creation_time'], event, state))
        g[c['contribution_id']] = min(gs, key=ORDER.get)
    grades_all[cid] = dict(event_time=event, grades=g)
    built.append((cand, doc, g))

write('stage5-validate/contemporaneity-recomputed.json', grades_all)

# ---- stage 1 outputs
all_contribs = [contribution(c) for cand in D.CANDIDATES for c in cand['contributions']]
write('stage1-identify/fragments.json', list(FR.values()))
write('stage1-identify/contributions.json', all_contribs)
write('stage1-identify/fragment-annotations.json', [
    dict(fragment_ref=fid, capture_time=times(fid)[0], creation_time=times(fid)[1],
         basis=(D.SOURCE_TIMES[D.FRAGMENTS[fid][0]][3] if D.FRAGMENTS[fid][0] != D.S6 else "the email's own header, '**Date:**'"),
         evidence_kind_by_candidate={c['candidate_id']: (c['kinds'][fid] if isinstance(c['kinds'][fid], str) else {'kind': c['kinds'][fid][0], 'restates': c['kinds'][fid][1]})
                                     for c in D.CANDIDATES if fid in c['kinds']})
    for fid in FR])
write('stage1-identify/considered-annotations.json', [
    dict(contribution_ref=k, considered=dict(state=v[0], fragment_refs=v[1])) for c in D.CANDIDATES for k, v in c['considered'].items()])
findings = [dict(finding_id=i, fragments=[FR[f] for f in refs], classification=cl, reading=note) for i, refs, cl, note in D.FINDINGS]
write('stage1-identify/findings.json', findings)
write('stage1-identify/unclassified.json', [dict(outcome='unclassified', id=i, fragment_refs=refs, fragments=[FR[f] for f in refs],
                                                 recognised=rec, why_classification_failed=why) for i, refs, rec, why in D.UNCLASSIFIED])
write('stage2-reconcile/assemblies.json', [doc['assembly'] for _, doc, _ in built])

# ---- agent's own schema checks of the non-candidate outputs (validate-decision-record check 5)
try:
    from jsonschema import Draft202012Validator
    load = lambda p: json.load(open(os.path.join(PKG, p), encoding='utf-8'))
    vf = Draft202012Validator(load('schemas/shared/source-fragment.schema.json'))
    vc = Draft202012Validator(load('schemas/shared/record-contribution.schema.json'))
    va = Draft202012Validator(load('schemas/shared/candidate-assembly.schema.json'))
    vk = Draft202012Validator(load('records/decision/schema/decision-contribution.schema.json'))
    lines = []
    def run(name, v, items, key):
        bad = [(key(i), [e.message for e in v.iter_errors(i)]) for i in items]
        bad = [b for b in bad if b[1]]
        lines.append(f'{name}: {len(items)} checked, {len(bad)} with schema errors')
        for b in bad: lines.append(f'  FAIL {b[0]}: {b[1]}')
    run('stage1 fragments vs source-fragment.schema.json', vf, list(FR.values()), lambda i: i['fragment_id'])
    run('stage1 contributions vs record-contribution.schema.json', vc, all_contribs, lambda i: i['contribution_id'])
    run('stage2 assemblies vs candidate-assembly.schema.json', va, [d['assembly'] for _, d, _ in built], lambda i: i['assembly_id'])
    run('finding classifications vs decision-contribution.schema.json', vk, [f['classification'] for f in findings], lambda i: json.dumps(i))
    write('stage5-validate/agent-schema-checks.txt', '\n'.join(lines) + '\n')
    print('\n'.join(lines))
except ImportError as e:
    print('jsonschema not available:', e)

# ---- stage 3 candidate views
SECTIONS = [
    ('Decision', ['decision-statement']),
    ('Decision date', ['decision-date']),
    ('Accountable owner (historical, as the evidence shows)', ['accountable-owner']),
    ('Authority invoked', ['authority']),
    ('Context — what was known at the time', ['context']),
    ('Evidence considered', ['evidence-business', 'evidence-architecture', 'evidence-regulatory', 'evidence-operations',
                             'evidence-customer', 'evidence-data', 'evidence-external']),
    ('Alternatives rejected', ['alternative-rejected']),
    ('Options foreclosed', ['option-foreclosed']),
    ('Consequences', ['consequence', 'reversal-cost']),
    ('Lineage', ['lineage', 'lineage-supersedes', 'lineage-derived-from']),
    ('Challenge recorded in the material', ['challenge']),
    ('Corroboration (later material: that it occurred, nothing else)', ['corroboration']),
]
GAPS = {
    'Accountable owner (historical, as the evidence shows)': "**MISSING.** No contribution. The material names a forum; a forum is not an owner. What would close it: evidence from the time naming the individual who held the decision.",
    'Authority invoked': "**MISSING.** The act cites no delegation or instrument, and no material shown to have been before whoever acted names one. See the applicability findings beside this candidate.",
    'Alternatives rejected': "**MISSING.** No contribution: the material records no option considered and not taken.",
    'Options foreclosed': "**MISSING.** No contribution: no span states what the decision closes off.",
    'Lineage': "None evidenced.",
    'Challenge recorded in the material': "None recorded.",
    'Evidence considered': "**MISSING.** No contribution to any of the seven evidence dimensions.",
}
COMPLETENESS = {
    'HC-001': dict(rows=[('decision-statement', 'supported', 'explicit'), ('context', 'supported', 'explicit'),
                         ('decision-date', 'supported', 'explicit'), ('accountable-owner', 'missing', 'no contribution')],
                   reading="The evidence did not supply an individual who held the decision, an authority the act invoked, or what reversing it would cost."),
    'HC-002': dict(rows=[('decision-statement', 'supported', 'explicit'), ('context', 'supported', 'explicit'),
                         ('decision-date', 'supported', 'explicit'), ('accountable-owner', 'missing', 'no contribution')],
                   reading="The evidence did not supply an individual who held the decision, an authority the act invoked, any alternative considered, the paper the minute cites, or what reversing it would cost."),
    'HC-003': dict(rows=[('decision-statement', 'supported', 'explicit'), ('context', 'supported', 'explicit'),
                         ('decision-date', 'supported', 'explicit'), ('accountable-owner', 'conflicting', 'two explicit contributions')],
                   reading="The evidence did not supply which one of two named individuals held the decision, the name of the instrument whose paragraph 4.5 was relied on, or what reversing it would cost."),
    'HC-004': dict(rows=[('decision-statement', 'supported', 'explicit'), ('context', 'partial', 'explicit; every contribution from the note grades indeterminate'),
                         ('decision-date', 'partial', 'inferred'), ('accountable-owner', 'partial', 'explicit')],
                   reading="The evidence did not supply the year in the act-record, the written agreement, an instrument for the stated limit, a full name and post in the act-record, or what reversing it would cost."),
}
for cand, doc, g in built:
    cid = cand['candidate_id']
    L = ['---', f'candidate_id: {cid}', 'status: candidate', 'standing: none', 'retrospective: true', '---', '',
         f'# {cid} — {cand["title"]}', '',
         f'*A view of historical candidate `{cid}`; no standing; the owner is the historical owner as the evidence shows them; '
         'whether this decision governs now is not established.*', '',
         f'This is not a TDR and not a draft of one. It renders `candidates/{cid}.json`, assembled on {NOW} by an AI agent from '
         'documents that survive the event. Nobody has proposed, reviewed or attested it. Each line below ends with the contribution '
         'it renders and the fragments that contribution rests on.', '',
         '**Proportionality tier:** undetermined — the material holds no statement of what reversing this decision would cost '
         '(admission criterion 6). The body below uses the minimal template\'s section names as a neutral shape; that is not a routing.', '']
    for title, roles in SECTIONS:
        cs = [c for c in cand['contributions'] if c['semantic_role'] in roles]
        L += [f'## {title}', '']
        if not cs:
            L += [GAPS.get(title, '**MISSING.** No contribution.'), '']
            if title == 'Consequences': pass
            continue
        held = []
        for c in cs:
            tag = f"`{c['contribution_id']}` ← {', '.join('`'+r+'`' for r in c['fragment_refs'])}; {c['semantic_role']}; derivation {c['derivation']}; extraction {c['extraction_confidence']}, epistemic {c['epistemic_confidence']}"
            if c['contribution_id'] in g:
                st = cand['considered'][c['contribution_id']][0]
                tag += f"; considered {st}; contemporaneity (recomputed) {g[c['contribution_id']]}"
                if g[c['contribution_id']] != 'contemporaneous':
                    held.append((c, tag)); continue
            L.append(f"- {c['interpreted_value']}  \n  [{tag}]")
        if held:
            L += ['', '**Gap — held, not rendered as context.** These contributions exist, but their contemporaneity is not evidenced, so they may not be presented as what was known at the time:', '']
            for c, tag in held:
                L.append(f"- {c['interpreted_value']}  \n  [{tag}]")
        L.append('')
        if title == 'Accountable owner (historical, as the evidence shows)' and cand['conflicts']:
            L += ['**CONFLICTING.** ' + cand['conflicts'][0]['note'], '']
        if title == 'Consequences' and not any(c['semantic_role'] == 'reversal-cost' for c in cs):
            L += ['**Reversal cost: MISSING.** No contribution.', '']
    L += ['## Confidence', '', '**MISSING.** No confidence was stated at the time.', '',
          '## Missing semantics (from the assembly)', ''] + [f'- {m}' for m in cand['missing_semantics']] + ['']
    L += ['## Unresolved (from the assembly)', ''] + [f'- {u}' for u in cand['unresolved']] + ['']
    L += ['## Grouping basis', ''] + [f'- **{b}** — {e}' for b, e in cand['grouping_basis']] + ['', f'Assembly confidence: {cand["assembly_confidence"]}.', '']
    comp = COMPLETENESS[cid]
    L += ['## Completeness view', '', '| Mandatory role | State | Derivation of what is held |', '|---|---|---|']
    L += [f'| `{r}` | {s} | {d} |' for r, s, d in comp['rows']]
    L += ['', comp['reading'] + ' Failure to recover evidence is not evidence that the decision was not taken.', '']
    L += ['## Provenance', '', '| Fragment | Source | Locator (char-offset) | Evidence kind | Capture | Creation |', '|---|---|---|---|---|---|']
    for a in doc['fragment_annotations']:
        f = FR[a['fragment_ref']]
        kind = a['evidence_kind'] + (f" of `{a['restates']}`" if 'restates' in a else '')
        L.append(f"| `{f['fragment_id']}` | {f['source_ref']} | {f['locator']['start']}–{f['locator']['end']} | {kind} | {a['capture_time']} | {a['creation_time']} |")
    L += ['', f"Source hashes and verbatim content are in `candidates/{cid}.json`. Interpreter: {AGENT['name']} ({AGENT['version']}), {NOW}.", '']
    write(f'stage3-draft/{cid}.view.md', '\n'.join(L))
print('built', len(FR), 'fragments;', len(all_contribs), 'contributions;', len(findings), 'findings;', len(D.UNCLASSIFIED), 'unclassified')
print(json.dumps(grades_all, indent=1))
