from typing import Any
from typing import Tuple
from typing import Dict


PVALID: str
FREE_PVAL: str
DISALLOWED: str
UNASSIGNED: str
CONTEXTJ: str
CONTEXTO: str

def derived_property(cp: int, ucd: Any) -> Tuple[str, str]:
    ...

def in_letter_digits(category: str) -> bool:
    ...

def in_exceptions(cp: int) -> bool:
    ...

def in_backward_compatible(cp: int) -> bool:
    ...

def in_join_control(cp: int) -> bool:
    ...

def in_old_hangul_jamo(cp: int, ucd: Any) -> bool:
    ...

def in_unassigned(cp: int, category: str, ucd: Any) -> bool:
    ...

def in_ascii7(cp: int) -> bool:
    ...

def in_controls(cp: int, ucd: Any) -> bool:
    ...

def in_precis_ignorable_properties(cp: int, ucd: Any) -> bool:
    ...

def in_spaces(category: str) -> bool:
    ...

def in_symbols(category: str) -> bool:
    ...

def in_punctuation(category: str) -> bool:
    ...

def in_has_compat(cp: int, ucd: Any) -> bool:
    ...

def in_other_letter_digits(category: str) -> bool:
    ...

def exceptions(cp: int) -> str:
    ...

def backward_compatible(cp: int) -> str:
    ...

_EXCEPTIONS_TABLE: Dict[bytes, str]

_BACKWARD_COMPATIBLE_TABLE = ...
