from typing import List
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Social:
    url: str
    followers: int


@dataclass
class Links:
    github: List[Social]
    linkedin: List[Social]
    medium: List[Social]
    twitter: List[Social]
    additional: List[Social]


@dataclass
class Position:
    coin_id: str
    coin_name: str
    position: str


@dataclass
class Person:
    id: str
    name: str
    teams_count: int


@dataclass
class PeopleItem(Person):
    description: str
    links: Links
    positions: List[Position]


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


@dataclass
class Currency:
    id: str
    name: str
    symbol: str
    rank: int
    is_new: bool
    is_active: bool
    type: str


@dataclass
class Exchange:
    id: str
    name: str
    rank: int


@dataclass
class Ico:
    id: str
    name: str
    symbol: str
    is_new: bool


@dataclass
class Tag:
    id: str
    name: str
    coin_counter: int
    ico_counter: int


@dataclass
class SearchResult:
    currencies: List[Currency]
    icos: List[Ico]
    exchanges: List[Exchange]
    people: List[Person]
    tags: List[Tag]
