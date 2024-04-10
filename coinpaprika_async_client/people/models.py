from typing import List
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Social:
    url: str
    followers: int


@dataclass
class PeopleLinks:
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
    teams_count: int
    description: str
    links: PeopleLinks
    positions: List[Position]
