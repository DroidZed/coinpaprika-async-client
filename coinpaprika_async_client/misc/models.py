from typing import List
from datetime import datetime
from dataclasses import dataclass

from ..shared import Tag


@dataclass
class MiscSocial:
    url: str
    followers: int


@dataclass
class MiscLinks:
    github: List[MiscSocial]
    linkedin: List[MiscSocial]
    medium: List[MiscSocial]
    twitter: List[MiscSocial]
    additional: List[MiscSocial]


@dataclass
class MiscPosition:
    coin_id: str
    coin_name: str
    position: str


@dataclass
class Person:
    id: str
    name: str
    teams_count: int


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
class MiscExchange:
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
class SearchResult:
    currencies: List[Currency]
    icos: List[Ico]
    exchanges: List[MiscExchange]
    people: List[Person]
    tags: List[Tag]


@dataclass
class PeopleModel(Person):
    description: str
    links: MiscLinks
    positions: List[MiscPosition]
