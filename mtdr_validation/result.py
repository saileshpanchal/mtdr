"""Building, serialising and checking validation results — NON-NORMATIVE reference implementation.

See `mtdr_validation/README.md`. The contract is `specification/validation-result.md` and
`schemas/validation-result.schema.json`; this module implements them and defines nothing.
"""
import copy
import json
import os

CONTRACT_VERSION = "1.0.0"

_HERE = os.path.dirname(os.path.abspath(__file__))
_SCHEMA_PATH = os.path.join(_HERE, os.pardir, "schemas", "validation-result.schema.json")


class Dim:
    """The four dimensions of TDR-0033. Reported independently — not a pass pipeline."""
    STRUCTURAL = "structural"
    SEMANTIC = "semantic"
    RELATIONAL = "relational"
    TRANSITION = "transition-eligibility"
    ALL = (STRUCTURAL, SEMANTIC, RELATIONAL, TRANSITION)


PASS = "pass"
FAIL = "fail"
INDETERMINATE = "indeterminate"
NOT_APPLICABLE = "not-applicable"
RESULTS = (PASS, FAIL, INDETERMINATE, NOT_APPLICABLE)

#: Which results are legal in which dimension (validation-result.md §5). Structural validity omits
#: not-applicable: TDR-0033 permits it only where no serialised representation forms part of the
#: typed assessment, and every subject this contract admits has one, so the case is unreachable.
LEGAL_RESULTS = {
    Dim.STRUCTURAL: (PASS, FAIL, INDETERMINATE),
    Dim.SEMANTIC: RESULTS,
    Dim.RELATIONAL: RESULTS,
    Dim.TRANSITION: RESULTS,
}

#: Results that must carry a reason. `fail` unexplained is an assertion rather than a finding; an
#: `indeterminate`'s reason is the whole of its content; and `not-applicable` is the result most
#: easily used to make an inconvenient dimension disappear.
REASON_REQUIRED = (FAIL, INDETERMINATE, NOT_APPLICABLE)

#: The subjects this contract admits. Two of TDR-0032's seven are absent: `collection` has no
#: governed contract (DAC-0032 constraint 6), and `participant` makes a behavioural claim rather than
#: a validation claim (DAC-0033 constraint 7). Every subject here has a serialised representation,
#: which is why structural validity is never not-applicable.
SUBJECT_TYPES = ("record", "interchange-structure", "package", "skill", "repository")


class IllegalResult(ValueError):
    """Raised when a caller reports a result the contract does not permit for that dimension."""


def schema():
    """The published machine contract, loaded fresh. The schema is authoritative; this module is not."""
    with open(_SCHEMA_PATH, encoding="utf-8") as fh:
        return json.load(fh)


class ValidationResult:
    """One typed, four-dimensional assessment of one subject.

    Deliberately absent: any aggregate verdict, truthiness, `ok`, `is_valid` or exit-code helper.
    DAC-0033 constraint 8 forbids a normative aggregate green result, and a convenience property that
    could be read alone would be read alone.
    """

    def __init__(self, subject_type, subject_id, spec_id, spec_version,
                 subject_ref=None, assessed_state=None, requested_transition=None,
                 context=None, validator=None):
        if subject_type not in SUBJECT_TYPES:
            # `collection` and `participant` land here by design — see SUBJECT_TYPES.
            raise IllegalResult(
                f"{subject_type!r} is not a conformance subject this contract admits; "
                f"legal subjects are {', '.join(SUBJECT_TYPES)}")
        self.subject_type = subject_type
        self.subject_id = subject_id
        self.subject_ref = subject_ref
        self.spec_id = spec_id
        self.spec_version = spec_version
        self.assessed_state = assessed_state
        self.requested_transition = copy.deepcopy(requested_transition)
        self.context = copy.deepcopy(context)
        self.validator = copy.deepcopy(validator)
        self._dimensions = {}

    def report(self, dimension, result, reasons=(), evidence=(), unevaluated_because=None):
        """Record one dimension's result. Rejects illegal dimension/result pairs at the point of use."""
        if dimension not in Dim.ALL:
            raise IllegalResult(f"unknown dimension {dimension!r}")
        if result not in LEGAL_RESULTS[dimension]:
            raise IllegalResult(
                f"{result!r} is not legal for {dimension!r}; "
                f"legal results are {', '.join(LEGAL_RESULTS[dimension])}")
        if result in REASON_REQUIRED and not reasons:
            raise IllegalResult(f"{dimension!r} reported {result!r} with no reason")
        entry = {"dimension": dimension, "result": result}
        if reasons:
            entry["reasons"] = [{"code": c, "detail": d} for c, d in reasons]
        if evidence:
            entry["evidence"] = [
                {"ref": e[0], **({"locus": e[1]} if len(e) > 1 and e[1] else {})} for e in evidence]
        if unevaluated_because:
            entry["unevaluated_because"] = unevaluated_because
        self._dimensions[dimension] = entry
        return self

    def to_dict(self):
        """Serialise. Dimensions always appear in full, in contract order."""
        missing = [d for d in Dim.ALL if d not in self._dimensions]
        if missing:
            raise IllegalResult(f"every dimension must be reported; missing {', '.join(missing)}")
        out = {
            "contract_version": CONTRACT_VERSION,
            "subject": {"type": self.subject_type, "id": self.subject_id},
            "specification": {"id": self.spec_id, "version": self.spec_version},
            "dimensions": [copy.deepcopy(self._dimensions[d]) for d in Dim.ALL],
        }
        if self.subject_ref:
            out["subject"]["ref"] = self.subject_ref
        if self.assessed_state:
            out["assessed_state"] = self.assessed_state
        if self.requested_transition:
            out["requested_transition"] = copy.deepcopy(self.requested_transition)
        if self.context:
            out["context"] = copy.deepcopy(self.context)
        if self.validator:
            out["validator"] = copy.deepcopy(self.validator)
        return out

    def to_json(self, **kwargs):
        return json.dumps(self.to_dict(), **kwargs)

    def validate(self):
        """Check the serialised result against the published schema. Returns a list of messages.

        The builder's own checks are convenience; this is the contract. Nothing here mutates the
        result or anything it was given.
        """
        return validate_document(self.to_dict())

    def summary(self):
        """A human summary that exposes every dimension and reaches no aggregate verdict."""
        head = (f"subject: {self.subject_type} {self.subject_id} · "
                f"specification: {self.spec_id} {self.spec_version}")
        lines = [head]
        for d in Dim.ALL:
            entry = self._dimensions.get(d)
            if entry is None:
                lines.append(f"  {d:<24} (not reported)")
                continue
            first = " ".join(entry.get("reasons", [{}])[0].get("detail", "").split())
            if len(first) > 96:
                first = first[:93] + "..."
            lines.append(f"  {d:<24} {entry['result']}" + (f" — {first}" if first else ""))
        return "\n".join(lines)


def validate_document(doc):
    """Validate an already-serialised result against the published schema.

    Used for results this module did not build — a result reloaded in a fresh process, or one
    produced by another implementation.
    """
    from jsonschema import Draft202012Validator
    return [e.message for e in Draft202012Validator(schema()).iter_errors(doc)]
