
from typing import Any

from precis_i18n.codepointset import CodepointSet

class UnicodeData:

    _halfwidth_chars = ...
    _space_chars = ...
    def __init__(self, ucd: Any = ...) -> None:
        ...
    
    @property
    def version(self) -> float:
        ...
    
    def category(self, char: str) -> str:
        ...
    
    def combining(self, char: str) -> int:
        ...
    
    def bidirectional(self, char: str) -> str:
        ...
    
    def normalize(self, form: str, value: str) -> str:
        ...
    
    def width_map(self, value: str) -> str:
        ...
    
    def map_nonascii_space_to_ascii(self, value: str) -> str:
        ...
    
    def default_ignorable(self, cp: int) -> bool:
        ...
    
    def has_compat(self, cp: int) -> bool:
        ...
    
    def control(self, cp: int) -> bool:
        ...
    
    def noncharacter(self, cp: int) -> bool:
        ...
    
    def old_hangul_jamo(self, cp: int) -> bool:
        ...
    
    def greek_script(self, cp: int) -> bool:
        ...
    
    def hebrew_script(self, cp: int) -> bool:
        ...
    
    def hiragana_katakana_han_script(self, cp: int) -> bool:
        ...
    
    def combining_virama(self, cp: int) -> bool:
        ...
    
    def arabic_indic(self, cp: int) -> bool:
        ...
    
    def extended_arabic_indic(self, cp: int) -> bool:
        ...
    
    def valid_jointype(self, value: str, offset: int) -> bool:
        ...
    


_DEFAULT_IGNORABLE: CodepointSet
_JOINTYPE_DUAL_JOINING: CodepointSet
_JOINTYPE_RIGHT_JOINING: CodepointSet
_JOINTYPE_LEFT_JOINING: CodepointSet
_JOINTYPE_TRANSPARENT: CodepointSet
_GREEK_SCRIPT: CodepointSet
_HEBREW_SCRIPT: CodepointSet
_HIRAGANA_KATAKANA_HAN: CodepointSet
_OLD_HANGUL_JAMO: CodepointSet
