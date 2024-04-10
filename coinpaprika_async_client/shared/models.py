from typing import List
from dataclasses import dataclass


@dataclass
class Fiat:
    name: str
    symbol: str


@dataclass
class Tag:
    id: str
    name: str
    coin_counter: int
    ico_counter: int
