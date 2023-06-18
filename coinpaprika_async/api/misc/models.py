from typing import List
from dataclasses import dataclass


@dataclass(repr=True)
class Social:
    url: str
    followers: int


@dataclass(repr=True)
class Links:
    github: List[Social]
    linkedin: List[Social]
    medium: List[Social]
    twitter: List[Social]
    additional: List[Social]


@dataclass(repr=True)
class Position:
    coin_id: str
    coin_name: str
    position: str


@dataclass(repr=True)
class PeopleItem:
    id: str
    name: str
    description: str
    teams_count: int
    links: Links
    positions: List[Position]
