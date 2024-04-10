from dataclasses import dataclass
from typing import Any

@dataclass(repr=True)
class ApiError:
    error: str
    def __init__(self, error) -> None: ...

@dataclass(repr=True)
class Result:
    Error: ApiError | None
    Data: Any
    def __init__(self, Error, Data) -> None: ...
