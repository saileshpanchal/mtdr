"""Source fidelity: does each fragment say what its source says, where it says it? NON-NORMATIVE.

`specification/source-fragment.md` makes a fragment verbatim and immutable, and gives two quality checks:
the locator resolves, and the content matches the span. A validator that never opens the source cannot
apply either: a hash that re-computes beside cleaned-up content, or a locator a line short, still passes.
This module re-reads the source material, when the evaluation context includes it.

It defines nothing. It applies the fragment contract's own rules, and reports what it could not check as
`indeterminate`, never as a pass: a source outside the context, a hash it cannot recompute, a locator
kind it does not know. Normalisation is limited to what the contract allows, character encoding: the
bytes are decoded as UTF-8 and line endings are read as one newline. Nothing else is tidied.
"""
import hashlib
import os
import re

FAIL, INDETERMINATE, PASS = 'fail', 'indeterminate', 'pass'


def _text(data):
    return data.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')


def find_source(ref, sources):
    """`source_ref` is opaque to the standard: try it as a path inside the sources folder, then by file name
    if exactly one file there has that name. Never outside the folder the caller declared."""
    root = os.path.realpath(sources)
    direct = os.path.realpath(os.path.join(root, ref))
    if direct.startswith(root + os.sep) and os.path.isfile(direct):
        return direct
    name = os.path.basename(ref)
    hits = [os.path.join(d, name) for d, _, files in os.walk(root) if name in files]
    return hits[0] if len(hits) == 1 else None


def _line_bounds(loc):
    if isinstance(loc.get('lines'), str):
        m = re.fullmatch(r'\s*(\d+)\s*(?:-\s*(\d+)\s*)?', loc['lines'])
        if m:
            return int(m.group(1)), int(m.group(2) or m.group(1))
    start, end = loc.get('line_start', loc.get('start')), loc.get('line_end', loc.get('end'))
    if isinstance(start, int) and isinstance(end, int):
        return start, end
    return None


def locate(text, loc):
    """The span a locator selects, or None when this checker cannot apply that locator."""
    kind = loc.get('kind')
    if kind == 'line-range':
        bounds = _line_bounds(loc)
        if bounds is None:
            return None
        lines = text.split('\n')
        a, b = bounds
        if a < 1 or b < a or b > len(lines):
            return ''                      # resolves to nothing: the locator points outside the source
        return '\n'.join(lines[a - 1:b])
    if kind == 'char-offset' and isinstance(loc.get('start'), int) and isinstance(loc.get('end'), int):
        return text[loc['start']:loc['end']]
    return None


def fragment_fidelity(fragment, sources):
    """One fragment against its source. Returns (result, [(code, detail)])."""
    fid = fragment.get('fragment_id', '?')
    src = find_source(fragment.get('source_ref', ''), sources)
    if src is None:
        return INDETERMINATE, [('source-not-in-context', f"{fid}: its source {fragment.get('source_ref')!r} is not "
                                                          f"in the source material supplied, so it was not re-read")]
    data = open(src, 'rb').read()
    out, reasons = PASS, []
    algorithm, _, given = str(fragment.get('source_hash', '')).rpartition(':')
    if algorithm not in ('', 'sha256'):
        out = INDETERMINATE
        reasons.append(('hash-not-recomputable', f"{fid}: source_hash uses {algorithm}, which this checker does not compute"))
    elif given != hashlib.sha256(data).hexdigest():
        return FAIL, [('source-hash-mismatch', f"{fid}: the source supplied does not hash to source_hash: it changed "
                                                f"after it was read, or the fragment names another source")]
    try:
        text = _text(data)
    except UnicodeDecodeError:
        return INDETERMINATE, reasons + [('source-not-text', f"{fid}: the source is not UTF-8 text, so the span "
                                                             f"cannot be compared")]
    content = _text(fragment.get('content', '').encode('utf-8'))
    if content not in text:
        squash = ' '.join(content.split())
        tidied = squash and squash in ' '.join(text.split())
        return FAIL, reasons + [('not-verbatim', f"{fid}: the content does not occur in the source as written"
                                 + (" (it does once whitespace is collapsed: the fragment was reflowed)" if tidied else
                                    ": it was summarised, cleaned, shortened or assembled"))]
    span = locate(text, fragment.get('locator') or {})
    if span is None:
        kind = (fragment.get('locator') or {}).get('kind')
        return INDETERMINATE, reasons + [('locator-not-applied', f"{fid}: the content is verbatim in the source, but a "
                                                                 f"`{kind}` locator is not one this checker applies")]
    if span != content:
        where = ('the locator selects nothing in the source' if span == '' else
                 'the located span is wider than the content' if content in span else
                 'the content is wider than the located span' if span in content else
                 'the locator selects other text')
        return FAIL, reasons + [('locator-mismatch', f"{fid}: {where}; the content must be exactly the span")]
    return out, reasons


def candidate_fidelity(candidate, sources):
    """Every fragment of a candidate. Returns (result, reasons): fail if any fragment fails; else indeterminate
    if any could not be checked; else pass."""
    results, reasons = [], []
    for f in candidate.get('fragments', []):
        r, why = fragment_fidelity(f, sources)
        results.append(r)
        reasons += why
    if FAIL in results:
        return FAIL, reasons
    if INDETERMINATE in results or not results:
        return INDETERMINATE, reasons or [('no-fragments', 'the candidate carries no fragment to re-read')]
    return PASS, reasons
