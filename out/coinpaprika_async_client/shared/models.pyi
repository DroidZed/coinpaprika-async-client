from dataclasses import dataclass

@dataclass
class Fiat:
    name: str
    symbol: str
    def __init__(self, name, symbol) -> None: ...

@dataclass
class Tag:
    id: str
    name: str
    coin_counter: int
    ico_counter: int
    def __init__(self, id, name, coin_counter, ico_counter) -> None: ...
