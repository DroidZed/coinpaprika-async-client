from dataclasses import dataclass
from typing import Any, Optional


@dataclass(repr=True)
class ApiError:
    error: str


@dataclass(repr=True)
class Result:
    Error: Optional[ApiError]
    Data: Any
