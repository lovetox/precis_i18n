
from typing import Any
from typing import Optional
from typing import Union

from precis_i18n.baseclass import BaseClass


class Profile:
    def __init__(self, base: BaseClass, name: str, casemap: Optional[str] = ...) -> None:
        ...
    
    @property
    def base(self) -> BaseClass:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    def enforce(self, value: Union[bytes, str]) -> str:
        ...
    
    def apply_five_rules(self, value: str) -> str:
        ...
    
    def width_mapping_rule(self, value: str) -> str:
        ...
    
    def additional_mapping_rule(self, value: str) -> str:
        ...
    
    def case_mapping_rule(self, value: str) -> str:
        ...
    
    def normalization_rule(self, value: str) -> str:
        ...
    
    def directionality_rule(self, value: str) -> str:
        ...
    
    def idempotence_check(self, value: str) -> str:
        ...
    


class Username(Profile):
    def __init__(self, ucd: Any, name: str, casemap: Optional[str] = ...) -> None:
        ...
    
    def width_mapping_rule(self, value: str) -> str:
        ...
    
    def directionality_rule(self, value: str) -> str:
        ...
    


class OpaqueString(Profile):
    def __init__(self, ucd: Any, name: str) -> None:
        ...
    
    def additional_mapping_rule(self, value: str) -> str:
        ...
    


class Nickname(Profile):
    def __init__(self, ucd: Any, name: str, casemap: Optional[str] = ...) -> None:
        ...
    
    def additional_mapping_rule(self, value: str) -> str:
        ...
    
    def normalization_rule(self, value: str) -> str:
        ...
    
    def idempotence_check(self, value: str) -> str:
        ...
    


