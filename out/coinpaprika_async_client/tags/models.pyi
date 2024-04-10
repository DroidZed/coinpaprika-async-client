from dataclasses import dataclass
from typing import List

@dataclass
class TagModel:
    id: str
    name: str
    coin_counter: int
    ico_counter: int
    description: str
    type: str
    coins: List[str]
    icos: List[str]
    def __init__(
        self,
        id,
        name,
        coin_counter,
        ico_counter,
        description,
        type,
        coins,
        icos,
    ) -> None: ...
