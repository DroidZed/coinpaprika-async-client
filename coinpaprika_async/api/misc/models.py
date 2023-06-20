from typing import List
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
class PeopleItem:
    id: str
    name: str
    description: str
    teams_count: int
    links: Links
    positions: List[Position]
