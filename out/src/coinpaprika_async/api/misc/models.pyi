from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Social:
    url: str
    followers: int
    def __init__(self, url, followers) -> None: ...

@dataclass
class Links:
    github: List[Social]
    linkedin: List[Social]
    medium: List[Social]
    twitter: List[Social]
    additional: List[Social]
    def __init__(
        self, github, linkedin, medium, twitter, additional
    ) -> None: ...

@dataclass
class Position:
    coin_id: str
    coin_name: str
    position: str
    def __init__(self, coin_id, coin_name, position) -> None: ...

@dataclass
class Person:
    id: str
    name: str
    teams_count: int
    def __init__(self, id, name, teams_count) -> None: ...

@dataclass
class PeopleItem(Person):
    description: str
    links: Links
    positions: List[Position]
    def __init__(
        self, id, name, teams_count, description, links, positions
    ) -> None: ...

@dataclass
class ConvertResult:
    base_currency_id: str
    base_currency_name: str
    base_price_last_updated: datetime
    quote_currency_id: str
    quote_currency_name: str
    quote_price_last_updated: datetime
    amount: int
    price: float
    def __init__(
        self,
        base_currency_id,
        base_currency_name,
        base_price_last_updated,
        quote_currency_id,
        quote_currency_name,
        quote_price_last_updated,
        amount,
        price,
    ) -> None: ...

@dataclass
class Currency:
    id: str
    name: str
    symbol: str
    rank: int
    is_new: bool
    is_active: bool
    type: str
    def __init__(
        self, id, name, symbol, rank, is_new, is_active, type
    ) -> None: ...

@dataclass
class Exchange:
    id: str
    name: str
    rank: int
    def __init__(self, id, name, rank) -> None: ...

@dataclass
class Ico:
    id: str
    name: str
    symbol: str
    is_new: bool
    def __init__(self, id, name, symbol, is_new) -> None: ...

@dataclass
class Tag:
    id: str
    name: str
    coin_counter: int
    ico_counter: int
    def __init__(self, id, name, coin_counter, ico_counter) -> None: ...

@dataclass
class SearchResult:
    currencies: List[Currency]
    icos: List[Ico]
    exchanges: List[Exchange]
    people: List[Person]
    tags: List[Tag]
    def __init__(self, currencies, icos, exchanges, people, tags) -> None: ...
