"""Reference implementation of the MTDR validation-result contract — NON-NORMATIVE.

The contract is `specification/validation-result.md` plus `schemas/validation-result.schema.json`.
This module is one way to satisfy it. A conforming independent implementation is governed by those
documents, never by behavioural equivalence with this code; if they disagree, this code is wrong.
See `mtdr_validation/README.md`.

Required by TDR-0033; typed subjects per TDR-0032; the authority boundary per TDR-0027.
"""
from .result import (  # noqa: F401
    Dim,
    PASS,
    FAIL,
    INDETERMINATE,
    NOT_APPLICABLE,
    RESULTS,
    LEGAL_RESULTS,
    ValidationResult,
    IllegalResult,
    schema,
    validate_document,
)

__all__ = [
    "Dim", "PASS", "FAIL", "INDETERMINATE", "NOT_APPLICABLE", "RESULTS", "LEGAL_RESULTS",
    "ValidationResult", "IllegalResult", "schema", "validate_document",
]
