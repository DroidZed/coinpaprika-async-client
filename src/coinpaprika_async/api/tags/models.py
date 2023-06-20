from typing import List
from dataclasses import dataclass


@dataclass
class Tag:
    id: str
    name: str
    coin_counter: int
    ico_counter: int
    description: str
    type: str
    coins: List[str]
    icos: List[str]
