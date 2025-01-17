from typing import Any
from typing import Tuple
from typing import Generator


class CodepointSet:

    def __init__(self, table: str) -> None:
        ...

    def __contains__(self, cp: int) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def __eq__(self, rhs: Any) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def items(self) -> Generator[Tuple[int, int], None, None]:
        ...
